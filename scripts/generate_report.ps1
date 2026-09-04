param(
    [string]$InputFile = "reports\test-report.xml",
    [string]$OutputFile = "reports\test-report.html"
)

[xml]$report = Get-Content -Raw $InputFile
$suite = $report.testsuites.testsuite
$testCases = @($suite.testcase)
$passed = @($testCases | Where-Object { -not $_.failure -and -not $_.error -and -not $_.skipped }).Count
$failed = @($testCases | Where-Object { $_.failure }).Count
$errors = @($testCases | Where-Object { $_.error }).Count
$skipped = @($testCases | Where-Object { $_.skipped }).Count
$total = $testCases.Count
$duration = [math]::Round([double]$suite.time, 2)
$durations = @($testCases | ForEach-Object { [double]$_.time })
$maxTime = [math]::Max(0.01, ($durations | Measure-Object -Maximum).Maximum)
$screenshots = @(Get-ChildItem -Path (Join-Path (Split-Path $OutputFile) "screenshots") -Filter *.png -ErrorAction SilentlyContinue)

$rows = foreach ($test in $testCases) {
    if ($test.failure) {
        $status = "Failed"
        $class = "failed"
    } elseif ($test.error) {
        $status = "Error"
        $class = "failed"
    } elseif ($test.skipped) {
        $status = "Skipped"
        $class = "skipped"
    } else {
        $status = "Passed"
        $class = "passed"
    }
    $barWidth = [math]::Round(([double]$test.time / $maxTime) * 100, 1)
    "<tr><td>$($test.classname)</td><td>$($test.name)</td><td><div class='duration'><span style='width:${barWidth}%'></span></div>$($test.time)s</td><td class='$class'>$status</td></tr>"
}

$screenshotRows = foreach ($screenshot in $screenshots) {
    "<li><a href='screenshots/$($screenshot.Name)'>$($screenshot.Name)</a></li>"
}

$html = @"
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Testometer Test Report</title>
<style>
body{font-family:Segoe UI,Arial,sans-serif;background:#f4f7fb;color:#172033;margin:0}
.container{max-width:1200px;margin:40px auto;padding:0 24px}
header{background:linear-gradient(135deg,#193b72,#2878b5);color:#fff;padding:28px;border-radius:16px;box-shadow:0 8px 24px #193b7233}
h1{margin:0 0 8px;font-size:30px}.muted{opacity:.8}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:22px 0}
.card{background:#fff;border-radius:12px;padding:20px;box-shadow:0 3px 12px #17203314}.value{font-size:28px;font-weight:700}.label{color:#64748b}
.passed{color:#14804a;font-weight:700}.failed{color:#c0392b;font-weight:700}.skipped{color:#b7791f;font-weight:700}
.table-wrap{background:#fff;border-radius:12px;overflow:auto;box-shadow:0 3px 12px #17203314}
table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:14px 16px;border-bottom:1px solid #e8edf3}th{background:#eef4fa;color:#334155}
tr:hover{background:#f8fbff}
.duration{display:inline-block;width:110px;height:7px;background:#e7edf5;border-radius:8px;margin-right:8px;vertical-align:middle}.duration span{display:block;height:100%;background:#2878b5;border-radius:8px}
.meta{display:flex;gap:24px;flex-wrap:wrap;color:#526174;margin:18px 0}.attachments{background:#fff;border-radius:12px;padding:18px 24px;margin-top:22px;box-shadow:0 3px 12px #17203314}.attachments a{color:#1d65a6}
@media(max-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
</style>
</head>
<body><main class="container">
<header><h1>Testometer Execution Report</h1><div class="muted">Generated $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")</div></header>
<div class="meta"><span><strong>Suite duration:</strong> ${duration}s</span><span><strong>Host:</strong> $env:COMPUTERNAME</span><span><strong>OS:</strong> $([System.Environment]::OSVersion.VersionString)</span><span><strong>PowerShell:</strong> $($PSVersionTable.PSVersion)</span></div>
<section class="cards">
<div class="card"><div class="value">$total</div><div class="label">Total tests</div></div>
<div class="card"><div class="value passed">$passed</div><div class="label">Passed</div></div>
<div class="card"><div class="value failed">$($failed + $errors)</div><div class="label">Failed / Errors</div></div>
<div class="card"><div class="value skipped">$skipped</div><div class="label">Skipped</div></div>
</section>
<section class="table-wrap"><table><thead><tr><th>Class</th><th>Test</th><th>Duration</th><th>Status</th></tr></thead><tbody>
$($rows -join "`n")
</tbody></table></section>
$(if ($screenshots.Count -gt 0) { "<section class='attachments'><h2>Failure screenshots</h2><ul>$($screenshotRows -join "`n")</ul></section>" })
</main></body></html>
"@

Set-Content -Path $OutputFile -Value $html -Encoding UTF8
Write-Host "Generated $OutputFile"
