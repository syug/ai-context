# Handover: MCP OAuth Token Expiry Research

## Background
Investigated how Claude Code handles OAuth token expiry for SSE MCP servers (specifically Notion at `https://mcp.notion.com/sse`). User was getting "MCP server requires re-authorization (token expired)" errors.

## Current Situation
- **Known bug in Claude Code** (v2.1.47 and prior): OAuth refresh tokens are stored but never used to obtain new access tokens
- **GitHub issue #5706** (open since Aug 2025, 6+ months) is the main tracking issue; 20+ duplicates filed
- **No official Anthropic response or fix timeline**

## Key Findings
1. **Token storage location:** macOS Keychain, entry `Claude Code-credentials`, JSON with `mcpOAuth` key
2. **Notion's token:** Has `expiresAt: 0` and no `refreshToken` stored
3. **`/mcp reconnect` is broken** for token refresh (issue #19481)
4. **Only working workaround:** `/mcp` -> select server -> "Clear authentication" -> "Authenticate"

## Deliverables
- `notes/research-findings.md` -- Full research with token storage details, CLI commands, and actionable steps

## Unresolved
- No automated token refresh exists; requires manual re-auth each time
- Unclear if Notion's MCP server supports refresh tokens at all (expiresAt=0 suggests non-expiring token OR missing metadata)
- Monitor #5706 for upstream fix
