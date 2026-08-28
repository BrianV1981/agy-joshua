# Antigravity Remote Control

Antigravity Remote Control allows you to securely connect to and drive your Antigravity 2.0 desktop sessions running across your machines from any web browser.

As AI agents take on larger-scope tasks—such as full-subsystem refactorings, extensive test suite runs, and complex dependency migrations—operations can run for extended periods. Remote Control untethers you from your physical desk while preserving your entire local development environment.

## 1. Enabling Remote Control in Antigravity 2.0

You can enable Remote Control directly from the Antigravity 2.0 Settings:

1. Open the **Settings** panel by pressing `Cmd + ,` (or `Ctrl + ,` on Linux/Windows), or click **Settings** at the bottom of the left sidebar.
2. Navigate to the **App** section.
3. Toggle **Enable Remote Control** to **On**.
4. *(Optional)* Set a custom **Nickname** (e.g., `workstation-primary` or `server-machine`) to easily identify this machine in your instance list.

## 2. Install Remote Control Headless Daemon

For background servers or headless nodes where the UI is not actively running, you can install the daemon directly.

### Linux and macOS
Run the installer script in your terminal:
```bash
curl -fsSL https://antigravity.google/cli/agy-daemon.sh | bash
```

To pass optional flags (such as setting an instance name or update interval), append `bash -s --`:
```bash
curl -fsSL https://antigravity.google/cli/agy-daemon.sh | bash -s -- install --name "my-box"
```

### Windows (requires Administrator)
Open Command Prompt as Administrator (**"Run as administrator"**) and run:
```cmd
curl -fsSL https://antigravity.google/cli/agy-daemon.cmd -o agy-daemon.cmd && agy-daemon.cmd install
```

> **Important:** On Windows, `install` and `uninstall` need an Administrator prompt, and the script must be run from Command Prompt, not PowerShell. `status` and `restart` work from a normal prompt.

## 3. Connecting from a Web Browser (Android / iOS / PC)

To access your remote Antigravity instance:

1. Open your web browser on any device and navigate to the [Antigravity Remote Control Dashboard](https://antigravity.google.com).
2. Sign in with the **same Google Account** that you used on your desktop application.
3. In the instance switcher, select the machine you want to control.
4. You now have full access to view active conversations, start new agent tasks, review implementation plans, and inspect artifacts.

> **💡 Mobile Pro-Tip:** On Android or iOS, tap your browser's menu (e.g., "Add to Home screen") to install it as a Progressive Web App (PWA). This gives you full-screen access and native **push notifications** when your agents complete tasks or request input!

## Troubleshooting

- **Machine doesn't show up:** Ensure "Enable Remote Control" is toggled on, your host machine isn't asleep, and you are signed in with the identical Google account on both ends.
- **Headless rename didn't take effect:** The name is read when the service starts; run `agy-daemon restart`.
- **Two similar entries in the Hub:** One is the desktop editor, one is the headless service. Rename one to differentiate.
