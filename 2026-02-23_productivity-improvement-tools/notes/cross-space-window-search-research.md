# Cross-Space Window Searching & Switching on macOS

Date: 2026-02-23

## Problem Statement

Raycast's built-in "Switch Windows" command cannot search windows on other Spaces by title. The user needs a way to search for a specific window (by title) across all Spaces and switch to it -- especially for apps like Chrome and Slack that may have windows on every Space.

---

## 1. Raycast Extensions

### 1.1 Raycast Built-in "Switch Windows"

- **Cross-Space support: NO** -- only shows windows on the current Space.
- No configuration option exists to enable cross-Space searching.
- No changelog entries indicate plans to add cross-Space support.
- The GitHub issues repository has related feature requests (e.g., Arc extension issues #17942 and #16412 about Space-aware tab searching) but they were all closed as "Not Planned" or "Stalled."

### 1.2 Raycast Built-in Window Management

- Provides window positioning/resizing commands (halves, thirds, quarters, maximize, etc.).
- Has "Previous Display" / "Next Display" for multi-monitor setups.
- **Does not include any cross-Space window search or switching.**

### 1.3 Raycast Yabai Extension (by krzysztoff1)

- **Cross-Space support: YES (with caveats)**
- Available in Raycast store. Requires yabai installed (`brew install koekeishiya/formulae/yabai`).
- **Key command: "Search Windows"** -- "Search and focus Yabai managed windows" by window title or application name.
- Also provides: Focus Space, Create/Destroy Space, Focus Window by direction, Layout switching, Move windows.
- **Critical caveat**: yabai's cross-Space window operations (focus/move/swap Space) **require SIP to be partially disabled** per the official yabai documentation (issue #1863). The scripting addition that injects into Dock.app is needed for Space manipulation.
- Window **querying** (`yabai -m query --windows`) appears to work with SIP enabled -- it lists all windows across all Spaces with app name, title, Space ID, and window ID in JSON format.
- Moving a window to another Space and following it (`yabai -m window --space 2 --focus`) is documented as working "with both SIP enabled and disabled."
- **Focusing** a window on another Space (which requires switching to that Space) likely requires the scripting addition (SIP disabled).
- **Verdict**: The "Search Windows" command in the Raycast Yabai extension is the closest to what the user wants within Raycast, but it depends on yabai and likely requires SIP changes for full cross-Space focusing.

### 1.4 Switch-Windows-Yabai (PR #22438 -- never merged)

- A community PR for a dedicated "Switch Windows via Yabai" extension with fuzzy search, recently-used sorting, and display filtering.
- Was closed due to inactivity and potential overlap with the existing Yabai extension.
- Would have provided essentially the same functionality as the existing Yabai extension's Search Windows command.

### 1.5 Raycast Google Chrome Extension (by Codely)

- 359K+ downloads. Provides "Search Tabs" across all Chrome windows.
- **Cross-Space support: Partial** -- it queries Chrome's internal tab list (not macOS window APIs), so it can see tabs in all Chrome windows regardless of Space. When you select a tab, Chrome activates that window, and macOS should switch to the Space containing it (if "When switching to an application, switch to a Space with open windows for the application" is enabled in Desktop & Dock settings).
- **Limitation**: Only works for Chrome tabs, not arbitrary window titles. Requires the Chrome extension/API integration.
- Useful as a complementary solution for the Chrome-specific part of the problem.

---

## 2. Dedicated macOS Window Switchers (Third-Party Apps)

### 2.1 Contexts ($9.99) -- STRONGEST RECOMMENDATION

- **Cross-Space support: YES** -- explicitly designed for it.
- **Search by title: YES** -- press Control-Space (configurable) to open search, type characters from app name or window title. Supports non-consecutive character matching and prioritizes acronym matches.
- **How it works**: Command-Tab replacement that lists individual windows (not just apps). Can filter by "All Spaces," "Visible Spaces," or "Current Space."
- **Additional features**:
  - Sidebar: auto-hiding panel showing windows grouped by Space.
  - Trackpad gestures for window switching.
  - Multi-display support (search appears on all displays).
  - Fn key for even faster switching.
- **Maintained**: Yes. Version 3.9 current. Works on macOS Ventura, Sonoma, and Sequoia.
- **Pricing**: $9.99 one-time purchase.
- **Verdict**: This is the most complete solution for the specific problem. It provides exactly what Raycast's Switch Windows lacks -- a searchable window list across all Spaces.

### 2.2 AltTab (Free, GPL-3.0)

- **Cross-Space support: YES** -- shows windows from all Spaces by default (configurable).
- **Search by title: IN DEVELOPMENT** -- fuzzy search feature (PR #4962) is being actively developed. Issue #590 was closed as "completed" in Feb 2026, but the PR is not yet merged into a release. Version 10.2.0 (Feb 2026) does NOT include search.
- **How it works**: Windows-style Alt-Tab switcher showing thumbnails of all windows. Can configure which Spaces/screens to show per shortcut.
- **Current workaround for "search"**: You can visually scan thumbnails and use arrow keys to navigate, but there is no text-based filtering yet.
- **Additional features**:
  - Space number labels on thumbnails.
  - Window actions (minimize, close, fullscreen) from the switcher.
  - CLI interface (`AltTab --list` returns JSON of all windows with titles).
  - Blacklisting by app or (new in v10.2.0) by window title.
  - 3 visual styles: thumbnails, app icons, titles.
- **Maintained**: Very actively. 14.9k stars, 6.9M downloads, v10.2.0 (Feb 2026).
- **Pricing**: Free, open source (GPL-3.0).
- **Key settings for cross-Space use**:
  - Controls > Shortcut 1 > "Show windows from: All Spaces" (or "Visible Spaces").
  - Appearance > "Hide Space number labels" -- toggle OFF to show Space numbers.
  - Appearance > Theme -- "Titles" mode shows window titles more prominently.
- **Verdict**: Excellent for visual cross-Space window switching TODAY. Text-based search is coming soon but not yet shipped. Once the search feature lands, this becomes a very strong free alternative to Contexts.

### 2.3 Witch ($14, Many Tricks)

- **Cross-Space support: YES** -- windows accessible regardless of Space.
- **Search by title: YES** -- real-time type-to-search filtering.
- **How it works**: Activatable via keyboard shortcut. Shows windows/tabs. Type to filter in real time.
- **Additional features**:
  - Multiple switcher panels with different configurations.
  - 3 layouts: horizontal, vertical, menu bar.
  - Spring-loaded drill-down to show app windows/tabs.
  - App/window exclusion.
  - Keyboard shortcuts for window actions.
- **Maintained**: Yes. Version 4.7 (Dec 2025). Updated for macOS 26 (Tahoe).
- **Pricing**: $14 new, $8 upgrade from Witch 3. License valid forever, 1 year updates.
- **Verdict**: Solid commercial option. Cross-Space search works well. Less modern UI than Contexts but more configuration options with multiple switcher panels.

### 2.4 rcmd (Free)

- **Cross-Space support: YES** -- automatically navigates to the Space containing the app.
- **Search by title: NO** -- switches by app name only (Right Command + first letter).
- **Limitation**: Cannot distinguish between multiple windows of the same app (e.g., multiple Chrome windows).
- **Verdict**: Useful complement but does not solve the core problem of searching by window title.

---

## 3. macOS Accessibility / Automation Approaches

### 3.1 Hammerspoon

**Can it query window titles across all Spaces?**

YES, with significant caveats:

- `hs.window.filter` can enumerate windows across all Spaces when `currentSpace` is set to `nil` (the default).
- `hs.spaces.windowsForSpace(spaceID)` returns window IDs for all windows on a specific Space.
- `hs.spaces` module provides: `allSpaces()`, `activeSpaces()`, `gotoSpace(spaceID)`, `moveWindowToSpace()`, `windowSpaces()`.

**Known issues:**

1. **Bug #3276 (open)**: `hs.window.filter.new(true)` only returns all windows on the current Space plus the *last focused window* from each app on other Spaces. It does NOT return all windows from all Spaces reliably.
   - **Workaround**: Create two separate filters (`setCurrentSpace(true)` and `setCurrentSpace(false)`) and merge results. Even this only works if you have previously visited all Spaces.

2. **Performance**: The docs warn of "sometimes significant delay after every Space switch" because macOS forces re-querying of all windows.

3. **Bug #3698 (open)**: `hs.spaces.moveWindowToSpace` does NOT work on macOS 15.0 Sequoia (returns true but does nothing). No complete workaround exists.

4. **Bug #3709 (open)**: Delays in `hs.window.filter` on recent macOS.

**Building a cross-Space window switcher with Hammerspoon:**

It IS possible to build a basic one using `hs.chooser` (a searchable list popup) + `hs.window.filter`, but:
- Window enumeration across Spaces is unreliable (bug #3276).
- Space switching (`gotoSpace`) uses private APIs with visual artifacts.
- `moveWindowToSpace` is broken on Sequoia (bug #3698).
- You would need to call `hs.window:focus()` after switching Space, which requires the window to be on the target Space.

**Verdict**: Hammerspoon CAN theoretically do this, but the implementation is fragile, buggy on recent macOS versions, and requires significant Lua scripting. Not recommended as a primary solution.

### 3.2 AppleScript / System Events

- AppleScript can list windows of running applications: `tell application "System Events" to get name of every window of every process`.
- **Cross-Space limitation**: AppleScript only reliably sees windows on the current Space. Windows on other Spaces may not be enumerable via System Events.
- You can activate a specific application with `tell application "AppName" to activate`, which will switch to the Space containing the app's frontmost window (if the macOS setting "When switching to an application, switch to a Space with open windows" is enabled).
- **Cannot target a specific window by title across Spaces** -- you can activate an app, but choosing which window of that app to bring forward is unreliable across Spaces.

**Verdict**: AppleScript is NOT a viable solution for cross-Space window searching by title.

### 3.3 Shortcuts.app

- macOS Shortcuts has limited window management actions.
- No actions for enumerating windows across Spaces or switching to specific windows.
- Can run AppleScript/shell scripts as actions, but subject to the same limitations.

**Verdict**: Not useful for this purpose.

### 3.4 macOS Core Graphics API (CGWindowListCopyWindowInfo)

- The `CGWindowListCopyWindowInfo` API with `kCGWindowListOptionAll` can list ALL windows system-wide, including those on other Spaces.
- Returns: window ID, owner name (app), window title (kCGWindowName), bounds, layer, Space ID.
- This is the underlying API that tools like AltTab and Contexts use.
- **Limitation**: This is a C/Objective-C/Swift API. Not directly scriptable without building a helper tool.
- **Using it**: You would need to build a small Swift/ObjC command-line tool that calls this API, outputs JSON, and then use it from a Raycast extension or script.

**Verdict**: The API capability exists. The tools that solve this problem (AltTab, Contexts, Witch) all use it. Building a custom solution is possible but non-trivial.

### 3.5 yabai (CLI approach without Raycast)

- `yabai -m query --windows` lists all windows across all Spaces (with SIP enabled) as JSON including: id, app, title, space, display.
- Can be piped through `jq` for filtering: `yabai -m query --windows | jq '.[] | select(.title | contains("keyword"))'`
- **Focusing a found window**: `yabai -m window --focus <window-id>` works for windows on the current Space. For windows on other Spaces, you need the scripting addition (SIP partially disabled) to first focus the Space.
- **Alternative**: `yabai -m window <id> --space mouse --focus` moves the window to the current Space and focuses it (works with SIP enabled).

**Verdict**: yabai's query capability is powerful and works with SIP enabled. The limitation is that focusing/switching to a window on another Space requires either (a) SIP partially disabled, or (b) pulling the window to your current Space instead.

---

## 4. AltTab Configuration for Cross-Space Use

### Key Settings

1. **Controls > Shortcut 1 (or 2-5)**:
   - Set "Show windows from" to **"All Spaces"** (critical setting).
   - Can set separate shortcuts with different Space filters.

2. **Appearance**:
   - **Theme**: "Windows 10" (thumbnails), "macOS" (app icons), or "Titles" (text list).
   - For title-based searching (once available), "Titles" mode will be most useful.
   - **"Hide Space number labels"**: Keep OFF to see which Space each window is on.
   - Thumbnail size: Adjustable for readability.

3. **Behavior**:
   - Window ordering: Chronological (most recent first), alphabetical, or by Space.

4. **Blacklist**:
   - Exclude apps that create many transient windows (e.g., Finder, Electron helper processes).

5. **CLI usage** (for scripting):
   - `AltTab --list` -- returns JSON list of all windows with IDs and titles.
   - `AltTab --focus <window-id>` -- focuses a specific window (switches Space if needed).

### Current Limitation

AltTab does NOT have text-based search yet. The fuzzy search PR (#4962) is in active development and the maintainer has stated intent to finish it, but it is not in any released version as of v10.2.0 (Feb 2026).

---

## 5. Browser Extensions for Tab Management

### 5.1 Raycast Google Chrome Extension

- Already covered above. Searches all Chrome tabs regardless of Space.

### 5.2 Workona (Chrome Extension)

- Organizes tabs into project-based "spaces" (their own concept, not macOS Spaces).
- Search across all tabs and workona-spaces via keyboard shortcut.
- Autosaves tabs, cross-device sync, tab suspension.
- **Does NOT directly interact with macOS Spaces** -- it organizes within Chrome only.
- **Useful for**: Reducing Chrome window proliferation. Instead of one Chrome window per macOS Space, you could use fewer Chrome windows with Workona workspaces inside them.

### 5.3 Chrome Profiles

- Chrome supports multiple profiles, each with separate bookmarks, history, and extensions.
- Can use a different profile per project/context.
- Each profile runs as a separate process and shows as a separate app in the window switcher.
- **Helps with identification**: "Chrome - Work Profile" vs "Chrome - Personal" in window titles.
- **Does not solve cross-Space searching** but makes windows more distinguishable.

### 5.4 Arc Browser (Alternative to Chrome)

- Built-in "Spaces" feature for organizing tabs by project/context.
- Each Arc Space has its own set of tabs and sidebar.
- Keyboard shortcut to switch between Arc Spaces.
- **Does not solve macOS Spaces switching** but reduces the need for multiple Chrome windows.
- Has a Raycast extension but with known Space-related issues (GitHub #17942, #16412).

---

## 6. Comparison Matrix

| Tool | Cross-Space | Title Search | Free | Maintained | SIP Required | Best For |
|------|------------|-------------|------|------------|--------------|----------|
| **Contexts** | YES | YES | No ($9.99) | Yes | No | Full cross-Space window search |
| **Witch** | YES | YES | No ($14) | Yes | No | Configurable multi-panel switcher |
| **AltTab** | YES | SOON | Yes | Yes | No | Visual cross-Space switching |
| **Raycast Yabai ext** | YES* | YES | Yes | Yes | Partial* | Raycast-native with yabai |
| **Hammerspoon** | Buggy | Custom | Yes | Yes | No | DIY scripting (fragile) |
| **rcmd** | YES | No (app only) | Yes | Yes | No | Quick app switching |
| **AppleScript** | NO | NO | Yes | N/A | No | Not viable |
| **Shortcuts.app** | NO | NO | Yes | N/A | No | Not viable |
| **Raycast built-in** | NO | YES | Yes | N/A | No | Current Space only |

*Raycast Yabai extension: Window querying works without SIP; focusing windows on other Spaces likely requires SIP partially disabled.

---

## 7. Recommendations

### Best Solution: Contexts ($9.99)

- Directly solves the problem: type to search window titles across all Spaces, press Return to switch.
- No SIP changes, no complex setup.
- Works alongside Raycast (use Raycast for everything else, Contexts for cross-Space window search via a dedicated hotkey like Control-Space).

### Best Free Solution: AltTab (now) + Wait for Search Feature

- Configure AltTab to show all Spaces.
- Use visual scanning for now.
- The fuzzy search feature is actively being developed and should ship in the near future.
- Supplement with Raycast's Chrome extension for tab-specific searching.

### Power User Solution: yabai + Raycast Yabai Extension

- Install yabai via Homebrew.
- If willing to partially disable SIP: full cross-Space window focus via "Search Windows" command.
- If SIP must stay enabled: can still query all windows and move target windows to the current Space instead of switching Spaces.

### Complementary Tools (use alongside any of the above)

- **Raycast Chrome Extension**: Search Chrome tabs across all windows/Spaces.
- **rcmd**: Quick Right-Cmd+letter app switching with auto-Space navigation.
- **Chrome Profiles or Workona**: Reduce Chrome window proliferation.
