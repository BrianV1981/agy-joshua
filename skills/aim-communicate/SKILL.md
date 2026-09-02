---
name: aim-communicate
description: >
  Inter-agent communication for messaging parallel WSL Linux coagents via tmux and polling their workspace for responses.
---

# `aim-communicate`

> **MANDATE:** Communicate directly with active WSL Linux coagents by injecting commands into their `tmux` session, and poll their workspace for their final output.

## 1. Finding the Target Agent
Before communicating, verify the agent is active by listing `tmux` sessions:
```powershell
wsl tmux ls
```
Identify the session name corresponding to the target agent (e.g., `aim-youtube`).

## 2. Sending a Message
Use `tmux send-keys` to inject your prompt directly into the agent's terminal. 
You **MUST** append the Path 2a Bridging Instruction to ensure they return data to you rather than leaving it in their terminal buffer:

```powershell
wsl tmux send-keys -t <session_name> "<your_message> CRITICAL: When you have finished your task, you must use your write_to_file tool to output your final report to aim-communicate.md in the root of your workspace, and then halt. Do not wait for a reply." C-m
```

## 3. Receiving a Message (Polling)
Once the task is dispatched, you must monitor the target agent's workspace for the `aim-communicate.md` file.
1. Use the `schedule` tool to create a recurring cron job (e.g., `* * * * *`) that checks for the file.
2. Ensure you check the correct WSL path for their workspace (e.g., `/home/kingb/<session_name>/aim-communicate.md`).
3. Example Schedule `Prompt`: `Check for the existence and content of /home/kingb/<session_name>/aim-communicate.md via wsl cat`
4. Once you read the response, you may cancel the cron job.

## 4. Loop Prevention
Do not engage in open-ended chat loops. Extract the final artifact, process it, and move on.
