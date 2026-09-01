# WSL Multi-Agent Orchestration (Windows 11)

Antigravity operates on Windows 11 as the master Orchestrator. When it needs to spawn specialized CLI agents (like Grok or OpenCode) for parallel processing, it leverages the Windows Subsystem for Linux (WSL) and `tmux`.

## The Challenge
Linux CLI coagents running inside a WSL terminal cannot access the native Antigravity message API. Historically, this was solved via complex, brittle `tmux send-keys` procedures.

## The Solution: The Shared Scratchpad (Path 2a)
Because Windows and WSL share the local file system seamlessly, the file system itself is the API bridge.

1. **Spawning & Directing (`aim-coagents` skill):**
   Antigravity spawns the Linux agent using:
   `wsl tmux new-session -d -s <session-name> ...`
   Crucially, Antigravity injects a directive into the prompt telling the agent to write its final output to `aim-communicate.md` in the root of the workspace.

2. **Data Handoff (`aim-communicate` skill):**
   The Linux agent completes its work and uses its file-writing tools to dump a clean, structured markdown report into `aim-communicate.md`.
   Antigravity does not wait synchronously; instead, it uses the native `/schedule` tool to run a background cron job that polls the file.

3. **Telemetry & Health (Path 2b):**
   Terminal scraping (`wsl tmux capture-pane`) is extremely brittle due to ANSI codes and pagination. Therefore, terminal capture is strictly demoted to a health-check role (to ensure the agent hasn't crashed) and is NEVER used to extract the final data payload.
