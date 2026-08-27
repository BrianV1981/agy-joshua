param(
    [Parameter(Mandatory=$true)]
    [string]$TargetWorkspace
)

if (-not (Test-Path $TargetWorkspace)) {
    Write-Error "Target workspace '$TargetWorkspace' does not exist."
    exit 1
}

$pluginsDir = Join-Path $TargetWorkspace ".agents\plugins\lancedb"
$mcpDir = Join-Path $TargetWorkspace "mcp_servers"
$lanceDir = Join-Path $TargetWorkspace "memory_lance"

Write-Host "Infecting target repository '$TargetWorkspace' with Sovereign Node Architecture..."

# 1. Create the plugin directories
if (-not (Test-Path $pluginsDir)) {
    New-Item -ItemType Directory -Force -Path $pluginsDir | Out-Null
}
if (-not (Test-Path $mcpDir)) {
    New-Item -ItemType Directory -Force -Path $mcpDir | Out-Null
}

# 2. Copy the MCP Server script
$sourceMcp = Join-Path $PSScriptRoot "mcp_servers\lancedb_mcp.py"
Copy-Item -Path $sourceMcp -Destination $mcpDir -Force
Write-Host "- Injected lancedb_mcp.py"

# 3. Create the mcp_config.json
$mcpConfig = @"
{
  "mcpServers": {
    "lancedb": {
      "command": "python",
      "args": [
        "mcp_servers/lancedb_mcp.py"
      ]
    }
  }
}
"@
Set-Content -Path (Join-Path $pluginsDir "mcp_config.json") -Value $mcpConfig
Write-Host "- Injected mcp_config.json"

# 4. Create the empty local database folder
if (-not (Test-Path $lanceDir)) {
    New-Item -ItemType Directory -Force -Path $lanceDir | Out-Null
    Write-Host "- Initialized isolated ./memory_lance Datajack pool"
}

Write-Host "`nSuccess! '$TargetWorkspace' is now an air-gapped Sovereign Node."
Write-Host "The Antigravity IDE will automatically boot the local LanceDB MCP server using 'python' whenever you open this workspace."
