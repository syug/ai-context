# MCP OAuth Token Expiry Research Findings

Date: 2026-02-20
Claude Code Version: 2.1.47

## 1. Where Claude Code Stores OAuth Tokens for SSE MCP Servers

**Primary storage: macOS Keychain**

- Keychain entry: `Claude Code-credentials` (service name), account = `$USER`
- Data format: JSON object with top-level key `mcpOAuth`
- Each MCP server has a key in the format `{serverName}|{hash}` (e.g., `notion|414bd617b9ad5ae9`)

**Current Notion entry structure (from keychain):**
```json
{
  "mcpOAuth": {
    "notion|414bd617b9ad5ae9": {
      "serverName": "notion",
      "serverUrl": "https://mcp.notion.com/sse",
      "clientId": "Di61H7KHe6A4YllD",
      "accessToken": "...",
      "expiresAt": 0,
      "scope": ""
    }
  }
}
```

**Fallback storage (when Keychain unavailable):**
- File: `~/.claude/.credentials.json` (plaintext JSON, chmod 600)
- Same JSON structure as Keychain

**Key observation:** No `refreshToken` field is stored for Notion. The `expiresAt` is `0`.

**Also stored (separately):** `mcpOAuthClientConfig` for servers with custom client credentials (client_id/client_secret specified via `--client-id`/`--client-secret`).

## 2. Can You Refresh the Token Without Removing/Re-adding?

### Current state: NO automatic refresh works

This is a **confirmed, known bug** in Claude Code. Multiple GitHub issues document this:

- **#5706** (Aug 2025, STILL OPEN): "Missing Token Refresh Mechanism for MCP Server Integrations" - the oldest tracking issue
- **#21333** (Jan 2026): "MCP OAuth refresh tokens stored but never used"
- **#25245** (Feb 2026): "Token expired without refresh token despite refresh token being stored"
- **#19481** (Jan 2026): "`/mcp reconnect` doesn't refresh expired OAuth access tokens"

**Root cause:** Claude Code stores refresh tokens when available but **never uses them** to obtain new access tokens. In Notion's case, no refresh token is even stored (only access token with expiresAt=0).

### Workaround: Use `/mcp` to Clear and Re-authenticate

1. Inside Claude Code, type `/mcp`
2. Select the Notion server
3. Choose **"Clear authentication"**
4. Then choose **"Authenticate"** to re-do the OAuth browser flow

This is the only reliable workaround. It clears the stored token and re-initiates the full OAuth flow.

### Alternative workaround: Remove and re-add

```bash
claude mcp remove notion
claude mcp add --transport sse notion https://mcp.notion.com/sse
```
Then use `/mcp` to authenticate.

## 3. CLI Commands for Re-authorization

There is **no dedicated CLI command** for re-authorization. Available commands:

| Command | Purpose | Handles Re-auth? |
|---------|---------|-------------------|
| `/mcp` (in-session) | Server management UI with "Clear authentication" and "Authenticate" options | YES (manual) |
| `/mcp reconnect` | Reconnects transport | NO (bug #19481: reports success but doesn't refresh token) |
| `claude mcp remove` + `claude mcp add` | Remove and re-add server | YES (nuclear option) |
| `claude mcp add --client-id --client-secret` | Add with custom OAuth credentials | For initial setup only |

**The `/mcp` in-session command is the best option:**
- Type `/mcp` in Claude Code
- Select the Notion server
- Use "Clear authentication" to wipe the expired token
- Then "Authenticate" to get a new one

## 4. Documentation and Community Status

### Official Documentation (code.claude.com/docs/en/mcp)
- States: "Authentication tokens are stored securely and refreshed automatically"
- States: Use "Clear authentication" in the `/mcp` menu to revoke access
- **The "refreshed automatically" claim is not working as documented**

### GitHub Issues Summary
- **20+ duplicate issues** filed about this problem
- **No official Anthropic engineering response** on any of the issues
- **No timeline for a fix** has been communicated
- Issue #5706 has been open for 6+ months with 37+ upvotes
- The MCP Authorization spec requires clients to implement refresh token handling

### Affected Services (from community reports)
- Notion, Asana, Linear, Sentry, Supabase, Atlassian, Microsoft OAuth, Buildkite, Circleback, and custom OAuth servers

## Summary of Actionable Steps

### Immediate fix when token expires:

1. In Claude Code, type `/mcp`
2. Select "notion"
3. Select "Clear authentication"
4. Select "Authenticate"
5. Complete browser OAuth flow

### Longer-term options:

- **Watch GitHub issue #5706** for a fix
- **Consider Notion API key approach instead:** If Notion supports static API tokens, you could use a header-based auth approach instead of OAuth:
  ```bash
  claude mcp add --transport sse notion https://mcp.notion.com/sse \
    --header "Authorization: Bearer ntn_YOUR_NOTION_INTEGRATION_TOKEN"
  ```
  (Note: This may not work with Notion's MCP server depending on whether it accepts integration tokens vs OAuth tokens)

### If you want to inspect your stored tokens:

```bash
security find-generic-password -s "Claude Code-credentials" -a "$USER" -w | python3 -m json.tool
```
