param(
    [string]$Command,
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$ArgsList
)

switch ($Command) {
    "init" {
        if ($ArgsList.Length -eq 0) {
            Write-Error "Usage: .\joshua.ps1 init <TargetWorkspace>"
            exit 1
        }
        $target = $ArgsList[0]
        .\init-workspace.ps1 -TargetWorkspace $target
    }
    "install" {
        .\install.ps1
    }
    "ingest" {
        if ($ArgsList.Length -gt 0) {
            python scripts/ingest_docs.py $ArgsList[0]
        } else {
            python scripts/ingest_docs.py
        }
    }
    "test" {
        python -m pytest tests/
    }
    default {
        Write-Host "J.O.S.H.U.A. - Universal Operating System CLI" -ForegroundColor Cyan
        Write-Host "==============================================="
        Write-Host "Available commands:"
        Write-Host "  init <dir>    Initialize a new Sovereign Node in the target directory"
        Write-Host "  install       Install prerequisites and setup the host machine"
        Write-Host "  ingest [dir]  Run the ingestion engine on the target directory (default: ./docs)"
        Write-Host "  test          Run the automated test suite"
    }
}
