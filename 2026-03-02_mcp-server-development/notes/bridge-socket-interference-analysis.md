# Slack->cmux Bridge: Socket Interference Analysis

## Problem Statement

After spawning a Slack MCP server as a child process via Node.js `StdioClientTransport`, all subsequent Unix domain socket connections to cmux (`/private/tmp/cmux.sock`) return a non-JSON error `"ERROR: Acc..."` instead of valid JSON-RPC responses.

This is a blocking issue for building a bridge that relays Slack messages to cmux (Claude desktop app) via its Unix domain socket API.

## Environment

- macOS Darwin 25.3.0 (arm64, Apple Silicon)
- Node.js v22.21.1
- cmux desktop app with Unix domain socket at `/private/tmp/cmux.sock`
- Slack MCP server: `/Users/saitshug/.aim/mcp-servers/ai-community-slack-mcp` (spawned via `StdioClientTransport`)
- The bridge process runs as a regular user process (not LaunchAgent, not sandboxed app)

## Reproduction Steps

1. Start a Node.js process.
2. Connect to the cmux socket, send a JSON-RPC request (e.g., `listWorkspaces`) -> **SUCCESS** (16 workspaces returned).
3. Spawn the Slack MCP server child process via `StdioClientTransport` (uses stdin/stdout pipes, not the socket).
4. Connect to the cmux socket again, send the same JSON-RPC request -> **FAIL** (receives `"ERROR: Acc..."` instead of JSON).
5. Kill the Node.js process entirely, run the socket test in a new standalone process -> **SUCCESS**.

The failure is deterministic: it occurs every time after step 3, and recovers every time after step 5.

## Confirmed Working

- cmux socket works 6/6 times in a standalone Node.js script (no child processes spawned).
- cmux socket works from terminal (`socat` or direct Node.js).
- cmux CLI (`cmux --help`, etc.) works from terminal.
- The Slack MCP server itself starts and operates correctly via stdio pipes.

## Confirmed Failing

- cmux socket fails **after** `StdioClientTransport` spawns the child process, even though the child uses stdio pipes (not the socket).
- cmux CLI fails from LaunchAgent context (SIGPIPE -- macOS session isolation issue, separate but possibly related).
- The error `"ERROR: Acc..."` is sent **by the cmux socket server**, not by the Slack MCP server. The socket connection itself succeeds; the server responds with this error string.

## Key Code

```typescript
// StdioClientTransport spawns child process like this internally:
// child_process.spawn(command, args, { stdio: ['pipe', 'pipe', 'pipe'], env })
const transport = new StdioClientTransport({
  command: "/Users/saitshug/.aim/mcp-servers/ai-community-slack-mcp",
  args: [],
  env: { PATH: "...", ...process.env },
});
await transport.start(); // After this call, cmux socket starts failing

// cmux RPC via Unix domain socket (separate connection each time)
function cmuxRpc(method: string, params: object): Promise<any> {
  return new Promise((resolve, reject) => {
    const sock = net.createConnection("/private/tmp/cmux.sock");
    const payload = JSON.stringify({ jsonrpc: "2.0", id: 1, method, params });
    sock.write(payload + "\n");
    // ... accumulate data, parse JSON response
  });
}
```

Important: the child process communicates with the parent via stdio pipes only. It does NOT connect to `/private/tmp/cmux.sock`. Yet its mere existence causes cmux to reject the parent's socket connections.

## Observed Error Detail

The cmux socket server responds with a plain-text string starting with `"ERROR: Acc"`. The response is truncated in logs, but the prefix strongly suggests one of:

- `"ERROR: Access denied"`
- `"ERROR: Account ..."`
- `"ERROR: Accepting ..."`

This is NOT a connection refusal (ECONNREFUSED) or a timeout. The TCP-level connection to the Unix socket succeeds, and the server actively sends back this error string.

## Hypotheses to Investigate

### H1: Process-group or session-level authentication
cmux may authenticate connections based on process-level attributes obtained via `getpeereid()`, `SO_PEERCRED`, or macOS-specific audit tokens (`audit_token_to_pid`, etc.). Spawning a child process could change the parent process's process group, session ID, or other kernel-level attribute that cmux checks.

**Test:** Before and after spawning the child, log `process.pid`, `process.ppid`, and run `ps -o pid,pgid,sess,tty -p <pid>` to see if any attributes change.

### H2: File descriptor table pollution
`StdioClientTransport` creates pipes for the child's stdio. This changes the parent's file descriptor table. If cmux uses `SCM_RIGHTS` or inspects the connecting process's open file descriptors as a security check, this could cause rejection.

**Test:** Spawn a minimal child process (`/bin/cat`) instead of the Slack MCP server. If cmux still fails, the issue is about child process spawning in general, not specific to the Slack MCP binary.

### H3: Environment variable or signal handler side effects
The `StdioClientTransport` constructor merges `process.env` with custom env vars. If a library loaded during this process modifies environment variables (e.g., `HOME`, `USER`, `XDG_RUNTIME_DIR`, or Apple-specific vars like `__CF_USER_TEXT_ENCODING`), cmux might detect a mismatch.

**Test:** Snapshot `process.env` before and after `transport.start()`, diff them.

### H4: macOS Mach port or XPC session changes
On macOS, spawning a child process can interact with the Mach bootstrap namespace. If cmux uses XPC or Mach-based service discovery, spawning a child might alter the parent's bootstrap context or session attributes.

**Test:** Run `launchctl print user/$(id -u)` before and after spawning the child to see if any session properties change.

### H5: The child process is connecting to cmux
Despite being configured for stdio-only communication, the Slack MCP server binary might independently attempt to connect to `/private/tmp/cmux.sock` during its initialization. If cmux has a per-process connection limit or stateful session tracking, this could poison the parent's subsequent connections.

**Test:** Use `lsof -U -p <child_pid>` to check if the child has any Unix socket connections. Also, `lsof -U | grep cmux` to see all processes connected to the cmux socket.

### H6: Node.js `child_process.spawn` inherits or modifies the parent's stdio
If `spawn()` is called without proper `detached` or `stdio` configuration, it might interfere with the parent's own stdio or file descriptor inheritance in ways that affect socket operations.

**Test:** Try spawning with `{ detached: true, stdio: ['pipe', 'pipe', 'pipe'] }` and `child.unref()` to fully detach the child.

## Diagnostic Steps (Priority Order)

1. **Minimal reproduction with `/bin/cat`:**
   Replace the Slack MCP server with `/bin/cat` as the child process. If cmux still fails, the issue is spawn-related, not Slack-MCP-related.

2. **Check process attributes before/after spawn:**
   ```javascript
   console.log("Before:", process.pid, process.ppid);
   // spawn child
   console.log("After:", process.pid, process.ppid);
   ```
   Also run from the Node.js process:
   ```javascript
   const { execSync } = require("child_process");
   console.log(execSync(`ps -o pid,pgid,sess,tty -p ${process.pid}`).toString());
   console.log(execSync(`lsof -U -p ${process.pid}`).toString());
   ```

3. **Capture the full error string:**
   Ensure the socket reader captures the complete response from cmux, not just the first chunk. Log the raw buffer as hex to catch any non-printable characters.

4. **Check if the child connects to cmux:**
   ```bash
   lsof -U | grep cmux.sock
   ```

5. **Try `detached: true` spawn:**
   ```javascript
   const child = spawn(command, args, {
     stdio: ['pipe', 'pipe', 'pipe'],
     detached: true,
     env: { ...process.env },
   });
   child.unref();
   ```

6. **Try spawning from a separate worker thread:**
   Use Node.js `worker_threads` to spawn the child process in an isolated thread, keeping the main thread's process context clean.

7. **Examine cmux logs:**
   If cmux writes logs to `~/Library/Logs/`, `~/Library/Application Support/`, or stdout of the cmux app, check for authentication rejection details.

## Architectural Considerations

### Option A: Process Separation (Recommended if root cause is process-level)
Run the Slack MCP client and the cmux sender in separate OS processes. Use IPC (Unix socket, named pipe, or localhost TCP) between them.

```
[Slack MCP Server] <--stdio--> [Bridge Worker Process] <--IPC--> [Main Process] <--socket--> [cmux]
```

### Option B: Deferred Spawn
Connect to cmux first, keep the connection alive, then spawn the child process. If cmux only checks credentials at connection time (not per-message), an already-established connection might continue working.

### Option C: Use cmux CLI Instead of Socket
If cmux provides a CLI that accepts JSON-RPC, pipe through that instead of the raw socket. This adds process overhead but avoids socket-level authentication issues.

### Option D: Worker Thread Isolation
Spawn the Slack MCP child process inside a Node.js `worker_thread`. This keeps the main thread's process context unmodified while still allowing stdio pipe communication with the child.

## Questions for Review

1. **Root cause:** What mechanism could cause a Unix domain socket server (cmux) to reject connections from a process **after** that process spawns an unrelated child? The child does not use the socket. The parent's PID does not change.

2. **macOS specifics:** Is there a macOS-specific security mechanism (App Sandbox, TCC, Gatekeeper, `SecTask`, audit session) that tracks whether a process has spawned children and modifies its trust level?

3. **cmux internals:** What authentication does cmux perform on incoming Unix socket connections? Does it use `getpeereid()`, `xpc_connection_get_audit_token()`, or something else? Where are cmux logs stored?

4. **Architecture:** What is the recommended architecture for a Node.js process that needs to:
   - Maintain a long-lived child process (Slack MCP) via stdio pipes
   - Make periodic, short-lived Unix domain socket connections (cmux)
   without interference between the two?

5. **Workaround viability:** Would keeping a persistent cmux socket connection (opened before the child spawn) avoid the issue? Or does cmux re-authenticate on each message?

## Please Provide

- Your root cause hypothesis with confidence level
- Suggested diagnostic steps (if different from or in addition to the above)
- Architectural recommendation for the bridge design
- Any macOS-specific knowledge about process attribute changes during `fork()`/`exec()`

---

*Document created for cross-LLM analysis. Written in English for compatibility with Kiro CLI, Gemini CLI, and other AI assistants. Be precise and technical in your response.*
