$sourceSkills = Join-Path $PSScriptRoot "skills"

$targetConfig = Join-Path $env:USERPROFILE ".gemini\config"
$targetSkills = Join-Path $targetConfig "skills"

Write-Host "Installing J.O.S.H.U.A. universal skills into $targetConfig"

if (-not (Test-Path $targetConfig)) {
    New-Item -ItemType Directory -Force -Path $targetConfig | Out-Null
}

if (-not (Test-Path $targetSkills)) {
    New-Item -ItemType Directory -Force -Path $targetSkills | Out-Null
}

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
