# Configuration Drift & Bootstrapping Blindspots

During the end-to-end repository audit on 2026-08-27, several structural issues were discovered regarding how J.O.S.H.U.A. handles onboarding and initialization for new Sovereign Nodes. 

## The Gitignore & Skills Discovery Trap
While the OS skills are stored in `skills/`, they are dynamically mapped via `.agents/skills.json`. Because the `.agents/` folder was explicitly ignored in `.gitignore`, cloning the template repository resulted in the complete omission of the skills mapping file. Out of the box, the Antigravity IDE could not discover `aim-gitops`, `aim-projects`, etc. This violates the portability mandate of the Sovereign Node.

## Obsolete MCP Initialization
When the repository migrated from the `uv run` standard to the global `python` execution for the LanceDB MCP server (to resolve IDE pathing scopes), the bootstrap script (`init-workspace.ps1`) was not updated. It still generated legacy `mcp_config.json` payloads relying on `uv`.

## Ingestion Blindspots
The Datajack ingestion script (`scripts/ingest_docs.py`) strictly hardcoded `./docs` as the target corpus. The `memory-wiki/` folder, which serves as the persistent architectural brain of the OS, was completely ignored by the Vector DB. 

**Resolution Plan:** These structural flaws have been tracked in GitHub Issues (Bug Tickets #6, #7, #8) and are queued for execution in the next session block.
