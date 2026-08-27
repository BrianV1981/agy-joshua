$sourceSkills = Join-Path $PSScriptRoot "skills"
$sourceRules = Join-Path $PSScriptRoot "GEMINI.md"

$targetConfig = Join-Path $env:USERPROFILE ".gemini\config"
$targetSkills = Join-Path $targetConfig "skills"

Write-Host "Installing J.O.S.H.U.A. rules and skills into $targetConfig"

if (-not (Test-Path $targetConfig)) {
    New-Item -ItemType Directory -Force -Path $targetConfig | Out-Null
}

if (-not (Test-Path $targetSkills)) {
    New-Item -ItemType Directory -Force -Path $targetSkills | Out-Null
}

# Copy GEMINI.md to rules (global rules)
$targetRulesDir = Join-Path $targetConfig "rules"
if (-not (Test-Path $targetRulesDir)) {
    New-Item -ItemType Directory -Force -Path $targetRulesDir | Out-Null
}
Copy-Item -Path $sourceRules -Destination (Join-Path $targetRulesDir "joshua_mandates.md") -Force

# Copy skills
Get-ChildItem -Path $sourceSkills -Directory | ForEach-Object {
    $targetDir = Join-Path $targetSkills $_.Name
    if (Test-Path $targetDir) {
        Write-Host "Updating skill: $($_.Name)"
        Copy-Item -Path $_.FullName -Destination $targetSkills -Recurse -Force
    } else {
        Write-Host "Installing skill: $($_.Name)"
        Copy-Item -Path $_.FullName -Destination $targetSkills -Recurse
    }
}

Write-Host "Installation complete! J.O.S.H.U.A. is now active in your Antigravity IDE."
