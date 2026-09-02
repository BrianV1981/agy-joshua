# Browser Orchestration & Stealth Architecture

This document tracks the tactical distinctions, hardware requirements, and orchestration strategies for automated browser control within the Antigravity Windows 11 ecosystem.

## 1. Tactical Distinction: Native `/browser` vs `aim-browser`

There are two primary methods for controlling a browser, each serving fundamentally different tactical objectives:

### The Native `/browser` Subagent (Antigravity MCP)
- **Role:** Interactive Co-Piloting & Pair Programming.
- **Mechanism:** Leverages native MCP (Model Context Protocol) to connect directly to the user's active Chromium instance via CDP.
- **Strengths:** Perfect for live UI testing, local dev environment navigation, and tasks where the Operator needs to see the browser navigate live on their screen.
- **Weaknesses:** Highly susceptible to bot-detection (Cloudflare, Datadome) because it lacks stealth evasion techniques and connects via raw CDP.

### The `aim-browser` Engine (Standalone Framework)
- **Role:** Autonomous, Hostile Extraction & Batch Scraping.
- **Mechanism:** A standalone Node.js orchestration engine wrapping Chromium. It manages its own persistent daemon, profiles, and injects custom stealth scripts (canvas spoofing, WebGL masking, User-Agent rotation).
- **Strengths:** Designed for stealth, heavy scraping (e.g. YouTube, social media), and detached background execution.
- **Weaknesses:** Requires CLI execution and JSON parsing by the agent; cannot be natively driven via direct MCP thought-loop tools.

## 2. The Windows 11 Hardware Acceleration Mandate

**Discovery:** Software rendering inside a WSL (Windows Subsystem for Linux) Linux VM triggers advanced bot detection (e.g., Sannysoft's WebGL vendor checks flag as RED due to software rendering pipelines like llvmpipe).

To pass strict headless bot detection, `aim-browser` MUST leverage physical GPU hardware acceleration.
- **Legacy State:** `aim-browser` relied on Linux-specific bash scripts (`start.sh`, `stop.sh`, `check.sh`) to manage its daemon, forcing execution inside WSL.
- **Modern State:** As of `aim-browser v1.3.1`, the daemon lifecycle has been entirely rewritten into **pure cross-platform Node.js** (`src/daemon.js`).
- **Execution Mandate:** To achieve maximum stealth on a Windows host, agents should execute `aim-browser` directly inside the native Windows PowerShell environment (`npm run skill`) rather than bridging through WSL. This allows the Chromium instance to attach directly to the Windows 11 GPU, securing a "Green" WebGL flag in bot heuristic checks.
