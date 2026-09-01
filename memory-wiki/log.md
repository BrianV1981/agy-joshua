# Memory Log

This is a chronological, append-only record of J.O.S.H.U.A. operations.

## [2026-08-27] ingest | Antigravity OS Architecture Overhaul
- **Scaffolded Wiki:** Created initial `index.md`, `log.md`, and `pages/`.
- **Architectural Shift:** Documented the migration away from the legacy Linux bash wrappers (`joshua_os/`) to the modern Windows Sovereign Node architecture.
- **Files Touched:** Created `pages/architecture_shift.md`.

## [2026-08-27] ingest | MCP Portability, Skill CLI Bugfix, & Zero-Exemption Policy
- **MCP Portability:** Fixed LanceDB MCP paths to resolve dynamically via `os.path.abspath(__file__)` rather than hardcoded CWDs.
- **Skill Bugfix:** Fixed `aim-projects` skill which incorrectly used `--text` for single select fields in GitHub Projects v2.
- **Zero-Exemption Policy:** Amended `GEMINI.md` to strictly forbid bypassing GitOps for meta-modifications.
- **Files Touched:** Created `pages/agent_meta_modifications.md`.

## [2026-08-27] ingest | End-to-End Audit & Configuration Drift
- **Audit Findings:** Discovered critical bootstrap flaws (Gitignore trap, obsolete MCP init script) and an ingestion blindspot (memory-wiki was not indexed).
- **Files Touched:** Created `pages/configuration_drift_audit.md`.

## [2026-08-27] ingest | Configuration Drift Resolution
- **Gitignore Trap Fixed:** Un-ignored `.agents/skills.json` so cloned workspaces correctly discover their skill maps.
- **MCP Init Updated:** `init-workspace.ps1` now uses the global Python interpreter instead of the obsolete `uv run`.
- **Ingestion Parameterized:** `ingest_docs.py` can now dynamically index target directories, fixing the blindspot where `memory-wiki/` was missing from the knowledge base.
- **Graceful MCP Fallback:** `lancedb_mcp.py` now returns robust JSON telemetry when no tables are present, rather than opaque string errors.
- **Files Touched:** `log.md`.

## [2026-08-27] ingest | Unified CLI & Testing Framework
- **Testing Framework:** Initialized `pytest` suite in `tests/`, mocking the local database to verify MCP fallback telemetry and testing the document chunking algorithm in `ingest_docs.py`.
- **Unified Task Runner:** Wrapped bootstrap (`init`, `install`), operational (`ingest`), and development (`test`) procedures into a single `joshua.ps1` CLI to streamline Operator experience.
- **Files Touched:** `log.md`.

## [2026-08-27] ingest | Memory System Architecture Documentation
- **Documentation:** Mapped out the three distinct tiers of the Antigravity memory ecosystem (Session Brain, Persistent Global KI, and Project Sovereign Node).
- **Files Touched:** Created `pages/memory_system_architecture.md`, updated `index.md`.

## [2026-08-27] ingest | Unified Tooling & Testing Architecture
- **Tooling Consolidation:** Documented the new unified Task Runner (`joshua.ps1`) CLI surface for bootstrapping and operations.
- **Testing Standard:** Documented the `pytest` standard and `unittest.mock` strategies required to satisfy TDD mandates without mutating the database pools.
- **Files Touched:** Created `pages/tooling_and_testing.md`, updated `index.md`.

## [2026-08-28] ingest | Remote Control Architecture
- **Remote Integration:** Codified instructions and operational guidelines for utilizing the Antigravity Remote Control daemon and PWA mobile interfaces to orchestrate detached execution workloads.
- **Files Touched:** Created `pages/remote_control.md`, updated `index.md`.

## [2026-09-01] ingest | Localized Mandates & WSL Multi-Agent Orchestration
- **Decentralized Local Mandates:** Documented the architectural shift to keep \GEMINI.md\ strictly isolated per Sovereign Node (zero-global-mandates).
- **WSL Multi-Agent Orchestration:** Formally logged the "Path 2a" protocol for spawning and directing Linux coagents via WSL using the Shared Scratchpad (\im-communicate.md\), and explicitly demoting terminal scraping (Path 2b) to telemetry-only.
- **Files Touched:** Updated \index.md\, created \pages/localized_mandates.md\ and \pages/wsl_orchestration.md\.
