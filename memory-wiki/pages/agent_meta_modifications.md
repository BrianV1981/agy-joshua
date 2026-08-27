# Agent Meta-Modifications (The Zero-Exemption Policy)

## Overview
A common cognitive blindspot for AI agents is treating their own environmental setup—such as .agents/ configurations, MCP server definitions, and custom skills—as "meta-tasks" exempt from standard project workflows.

## The Policy
To ensure airtight operational stability on the gy-joshua Sovereign Node, the **Zero-Exemption Mandate** explicitly bans this behavior.
Absolutely all file modifications on the host, including agent configs and skills, must flow through the exact same GitOps worktree pipeline as standard repository code:
1. Open an issue
2. Claim it on the board
3. Spawn a sandbox worktree
4. Stage, commit, and promote
5. Close the issue

## Case Study: LanceDB MCP & aim-projects Skill
On 2026-08-27, an agent bypassed GitOps to hardcode absolute paths into mcp_servers/lancedb_mcp.py while troubleshooting environment variables (uv missing on host). The agent was corrected, the paths were made dynamic, and the im-projects skill was simultaneously patched via the correct GitOps workflow (Issue #2) after discovering it was passing invalid --text arguments to GitHub Projects v2 single-select fields. The Zero-Exemption policy was then formally added to GEMINI.md.
