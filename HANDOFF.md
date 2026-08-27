# J.O.S.H.U.A. - Engineering Handoff

> **Updated:** 2026-08-27T01:52:00-04:00
> **Updated by:** Antigravity Desktop Session (Standard App 2.0)
> **Priority Mission:** Resolve Configuration Drift & Bootstrapping Blindspots
> **Operator:** Brian Vasquez

---

## 0. COMPLETED WORK (DO NOT REVISIT)
| Session | Work | Status |
|---------|------|--------|
| Previous | Eradicated Linux `joshua_os/` directory | ✅ RESOLVED |
| Previous | Re-wrote `mcp_servers/lancedb_mcp.py` | ✅ RESOLVED |
| Previous | Built `scripts/ingest_docs.py` using Length-Constrained Accumulator & Ollama | ✅ RESOLVED |
| Previous | Scaffolded `memory-wiki/` and logged the architectural shift | ✅ RESOLVED |
| Current | Restored MCP Portability (dynamic paths, global `ollama`, no `uv`) | ✅ RESOLVED |
| Current | Fixed `aim-projects` GitHub CLI flag bug (`--single-select-option-id`) | ✅ RESOLVED |
| Current | Enforced Zero-Exemption GitOps policy in `GEMINI.md` | ✅ RESOLVED |
| Current | Performed End-to-End Repository Audit & Documented Drift | ✅ RESOLVED |
| Current | Logged Audit findings into `memory-wiki/` & Opened GitHub Issues | ✅ RESOLVED |

---

## 1. PROJECT IDENTITY
J.O.S.H.U.A. is a universal OS framework for autonomous agents natively operating within Antigravity. It mandates Sovereign Nodes (air-gapped local LanceDB instances via MCP), Test-Driven GitOps, and Epistemic Certainty. The repository is a highly curated template now fully migrated and functional on Windows.

### Your Knowledge Base
- `C:\agy-joshua\GEMINI.md` (Core Mandates)
- `C:\agy-joshua\memory-wiki\index.md` (Persistent Subconscious Memory)
- `C:\agy-joshua\memory-wiki\pages\configuration_drift_audit.md` (Recent Audit Findings)

---

## 2. YOUR MISSION: RESOLVE CONFIGURATION DRIFT
The recent End-to-End Audit discovered 3 critical bugs and 3 architectural enhancements that need to be resolved to ensure the OS framework is portable and fully functional out-of-the-box when cloned. 

### Execution Queue (in order)
#### 1️⃣ Resolve Gitignore & Skills Discovery Trap
**Problem:** `.agents/` is gitignored, meaning `skills.json` is missing on fresh clones.
**Fix:** Exclude `.agents/skills.json` from gitignore or have `init-workspace.ps1` generate it. (See GitHub Board)

#### 2️⃣ Update Obsolete MCP Configuration
**Problem:** `init-workspace.ps1` still generates an `mcp_config.json` that invokes LanceDB server using `uv run`.
**Fix:** Update `init-workspace.ps1` to write `"command": "python"`.

#### 3️⃣ Fix Ingestion Engine's Blindspot
**Problem:** `scripts/ingest_docs.py` has a hardcoded `DOCS_DIR = "./docs"`.
**Fix:** Parameterize it to accept target directories so it can index `memory-wiki/` as well.

#### 4️⃣ Architectural Enhancements (Optional but Recommended)
- Setup a Testing Framework (e.g., `pytest`) for Python scripts.
- Wrap scripts into a Unified Task Runner CLI (`joshua` CLI).
- Graceful DB Fallback in `lancedb_mcp.py`.

---

## 3. DETAILED ANALYSIS / BREAKDOWN
- **The Skills Trap:** The `agy-customizations` guide states that if skills are stored in a non-standard location like `skills/`, they MUST be registered in `skills.json`. Because `.agents/` is ignored, that mapping is lost on git clones.
- **The Ingestion Target:** The wiki update script specifically requires `sys.argv` or `argparse` to allow dynamic targets. The agent should test this by successfully ingesting `memory-wiki/` using the updated script.

---

## 4. IMPLEMENTATION STRATEGY
1. Claim an issue from the GitHub project board using `aim-projects`.
2. Spawn a GitOps worktree using `aim-gitops` (e.g. `git worktree add -b fix/issue-1 workspace/issue-1`).
3. Make the surgical fix.
4. Promote back to main and mark the issue as Done.
5. Repeat for the remaining issues in the queue.

---

## 5. THE CRITICAL TRAPS & WARNINGS
> **⚠️ EPISTEMIC / OPERATIONAL WARNINGS**
> - **META-MODIFICATIONS BLINDSPOT:** You are explicitly forbidden from modifying your own `.agents/`, `mcp_servers/`, or `skills/` files without spawning a GitOps worktree. There are zero exemptions.
> - **TEST-DRIVEN DEVELOPMENT:** When making changes to `ingest_docs.py` or the initializer scripts, empirically verify they work by running them in your worktree before promoting.

---

## 6. KEY PATHS
- **Gitignore:** `C:\agy-joshua\.gitignore`
- **Skills Mapping:** `C:\agy-joshua\.agents\skills.json`
- **Initializer:** `C:\agy-joshua\init-workspace.ps1`
- **Ingestion Script:** `C:\agy-joshua\scripts\ingest_docs.py`

---

## 7. THE FULL PICTURE / WHAT COMES AFTER
Once these bootstrapping flaws are resolved, the Sovereign Node architecture will be truly portable. The Operator can safely clone this repo anywhere and immediately have a functional agentic operating system with fully discovered skills and active memory pools.

---

## 8. OPERATOR PREFERENCES
- **Name:** Brian Vasquez
- **Environment:** Windows 11 / Antigravity Desktop App / PowerShell
- **Mandates:** Test-Driven Development (TDD) reflex, strict GitOps, strict reliance on empirical proof and documentation, and strict Kanban board tracking for every issue.

---

## 9. IMMEDIATE NEXT STEPS
1. Read this `HANDOFF.md` document entirely.
2. Query the GitHub Project board using `aim-projects` (`gh project item-list 9 --owner BrianV1981`).
3. Claim the first open BUG ticket and spawn a GitOps sandbox to fix it.
