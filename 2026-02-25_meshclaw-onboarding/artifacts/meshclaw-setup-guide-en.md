# MeshClaw Setup Guide

Personal AI agent for Amazon builders. Wiki: https://w.amazon.com/bin/view/Users/bolichen/MeshClaw/

## Prerequisites

- Brazil CLI (`brazil`)
- `kiro-cli` in PATH
- Valid Midway session (`mwinit -o`)

---

## Option A: Cloud Desktop (Recommended)

### 1. SSH into your Cloud Desktop

```bash
ssh dev-dsk-<alias>-<id>.<region>.amazon.com
```

**Ghostty users**: If you see `tput: unknown terminal "xterm-ghostty"` errors:
```bash
export TERM=xterm-256color
```

### 2. Set bash as default shell (one-time)

Cloud Desktops may default to zsh, but `.bashrc` contains bash-only commands (`shopt`) that cause errors.

> **Note**: `sudo usermod -s /bin/bash` does NOT persist — Cloud Desktops use LDAP/NIS which resets `/etc/passwd` on each login. `chsh` is also unavailable on Amazon Linux 2.

Permanent fix — auto-switch to bash on login:

```bash
echo 'exec bash --login' >> ~/.zshrc
```

Also add Ghostty terminal compatibility to both shells (one-time):

```bash
echo 'export TERM=xterm-256color' >> ~/.bashrc
echo 'export TERM=xterm-256color' >> ~/.zshrc
source ~/.bashrc
```

Reconnect to verify bash is the active shell.

### 3. Ensure Midway + tooling

```bash
mwinit -o
```

If `brazil` is not found:
```bash
# Install Builder Toolbox
curl -s https://toolbox.corp.amazon.com/install.sh | bash
export PATH="$HOME/.toolbox/bin:$PATH"

# Install Brazil CLI
toolbox install brazilcli
```

If git clone fails with `Permission denied`:
```bash
# Generate SSH key (required for git.amazon.com)
ssh-keygen -t ecdsa -f ~/.ssh/id_ecdsa -N ""
mwinit -o
```

### 4. Setup & launch

```bash
brazil ws create -n MeshClaw && cd MeshClaw && brazil ws use -p MeshClaw -vs live && cd src/MeshClaw && source setup.sh && meshclaw gateway
```

`setup.sh` will interactively:
1. Check/refresh Midway auth
2. Install toolbox dependencies (kiro-cli, aim, node20)
3. Run kiro-cli SSO login (opens browser)
4. Install MCP servers (builder-mcp, ai-community-slack-mcp)
5. Run `brazil-build`
6. Add `bin/` to PATH
7. Configure agent settings

**kiro-cli login**: When prompted, select **"Use with Pro license"** (not Builder ID).
- Start URL: `https://amzn.awsapps.com/start`
- Region: `us-east-1`

If you accidentally chose Builder ID, fix it later:
```bash
kiro-cli logout && kiro-cli login
```

### 5. Access the dashboard

Gateway prints two URLs on startup:
- `http://localhost:7777` — from Cloud Desktop browser
- `http://<hostname>:7777` — may not be accessible directly

**For remote access from your laptop, use an SSH tunnel:**

Terminal 1 (gateway — already running from step 4)

Terminal 2 (tunnel — new tab on your local machine):
```bash
ssh -N -L 7778:localhost:7777 dev-dsk-<alias>-<id>.<region>.amazon.com
```

Then open in your local browser:
```
http://localhost:7778
```

> Use port 7778 (not 7777) to avoid conflicts if MeshClaw is also installed locally.

### 6. Subsequent launches

```bash
# Terminal 1: SSH + gateway (bash + TERM already configured)
ssh dev-dsk-<alias>-<id>.<region>.amazon.com
cd ~/MeshClaw/src/MeshClaw && meshclaw gateway

# Terminal 2: SSH tunnel (local machine)
ssh -N -L 7778:localhost:7777 dev-dsk-<alias>-<id>.<region>.amazon.com

# Browser
http://localhost:7778
```

### 7. Verify

```bash
meshclaw doctor    # check dependencies, config, connectivity
meshclaw status    # query running gateway stats
```

---

## Option B: macOS (Local)

### 1. Setup (bash required for setup.sh)

```bash
brazil ws create -n MeshClaw && cd MeshClaw && brazil ws use -p MeshClaw -vs live && cd src/MeshClaw && bash setup.sh
```

> **Note**: Use `bash setup.sh`, not `source setup.sh` — the script is not compatible with fish or other non-POSIX shells.

### 2. Add to PATH

**fish shell**:
```fish
fish_add_path /path/to/MeshClaw/src/MeshClaw/bin
```

**bash/zsh**: `setup.sh` offers to add to `.bashrc`/`.zshrc` automatically.

### 3. Configure workspace

When prompted for workspace path, use a **local** directory:
```
~/.meshclaw/workspace
```

> **Do NOT use cloud-synced directories** (OneDrive, Google Drive) — MeshClaw writes frequently to SQLite/JSONL/PID files, which can cause sync conflicts and data corruption.

### 4. kiro-cli login

Select **"Use with Pro license"** when prompted:
- Start URL: `https://amzn.awsapps.com/start`
- Region: `us-east-1`

### 5. Launch

```bash
meshclaw gateway
```

Dashboard: `http://localhost:7777` or `http://mesh.claw:7777` (after running `meshclaw setup`)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `source setup.sh` fails in fish | Use `bash setup.sh` instead |
| `tput: unknown terminal "xterm-ghostty"` | `export TERM=xterm-256color` |
| `brazil: command not found` | `export PATH="$HOME/.toolbox/bin:$PATH"` |
| git clone `Permission denied` | Generate SSH key: `ssh-keygen -t ecdsa -f ~/.ssh/id_ecdsa -N ""` then `mwinit -o` |
| `.bashrc` shopt errors in zsh | `echo 'exec bash --login' >> ~/.zshrc` then re-login. (`usermod` won't persist due to LDAP, `chsh` unavailable on AL2) |
| Remote dashboard URL not accessible | Use SSH tunnel: `ssh -N -L 7778:localhost:7777 <host>` then `http://localhost:7778` |
| `ACP init timed out` after kiro-cli re-login | Restart gateway: Ctrl+C then `meshclaw gateway` |
| Chose wrong kiro-cli license | `kiro-cli logout && kiro-cli login` → select "Use with Pro license" |
| Kernel update notification on Cloud Desktop | Safe to do after MeshClaw setup: `sudo reboot` |
| builder-mcp missing from MCP servers | `aim mcp install builder-mcp` then Auto-Sync or restart gateway |
| Delete key not working over SSH | `export TERM=xterm-256color` (add to `.bashrc` and `.zshrc` for persistence) |

---

## Self-update

MeshClaw auto-updates on gateway restart. Manual:

```bash
meshclaw update    # git pull + rebuild
```

## Useful commands

```bash
meshclaw chat              # interactive REPL
meshclaw chat -m "message" # one-shot
meshclaw doctor            # health check
meshclaw status            # runtime stats
meshclaw cron list         # scheduled jobs
meshclaw learn list        # learned preferences
```
