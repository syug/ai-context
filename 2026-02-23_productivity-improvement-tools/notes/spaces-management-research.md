# macOS Spaces Management Research

Date: 2026-02-23

## Context
User has 13 Spaces on macOS and wants better management tools and strategies.

---

## 1. Third-Party Tools for Space Management

### 1.1 Tiling Window Managers (Full Space + Window Control)

#### yabai
- **What it does**: Tiling window manager using binary space partitioning. Controls windows, spaces, and displays via CLI. Disables space-switching animations. Can create/destroy/focus spaces programmatically.
- **Maintained**: Yes, actively. 28.2k stars, 1,662 commits, latest release Feb 2026.
- **macOS support**: Intel: Big Sur 11.0+ through Sequoia 15.0+. Apple Silicon: Monterey 12.0+ through Tahoe 26.0+.
- **Pricing**: Free, MIT license.
- **Key limitations**:
  - Requires Accessibility API access.
  - Advanced features (like space management) require partially disabling SIP.
  - "Displays have separate Spaces" must be enabled in System Settings.
  - Apps using native macOS tabs may misbehave.
- **Best for**: Power users comfortable with CLI and SIP modification.

#### AeroSpace
- **What it does**: i3-inspired tiling window manager. Uses its own virtual workspace system instead of native macOS Spaces. Tree-based window tiling, CLI-first, plain text TOML config.
- **Maintained**: Yes, actively. 19k stars, public beta, latest releases in 2025-2026.
- **macOS support**: Ventura 13 through Tahoe 26.
- **Pricing**: Free, MIT license.
- **Key limitations**:
  - Does NOT use native macOS Spaces at all -- it emulates its own workspace system.
  - No GUI configuration (text-only).
  - Still pre-1.0, so breaking changes possible.
  - No sticky windows yet.
- **Advantage over yabai**: Does NOT require SIP disabling. Avoids private APIs.
- **Best for**: Users who want to abandon native Spaces entirely in favor of i3-style workspaces.

#### Amethyst
- **What it does**: Automatic tiling window manager inspired by xmonad. Multiple layout modes (tall, wide, column, BSP, fullscreen). Keyboard-driven. Can move windows between spaces 1-16.
- **Maintained**: Yes, actively. Latest release v0.24.1 (Dec 2025). 310 open issues with active development.
- **macOS support**: macOS 10.15 Catalina+.
- **Pricing**: Free, MIT license.
- **Key limitations**:
  - Strongly recommends disabling "Automatically rearrange Spaces based on most recent use."
  - Less control over Spaces themselves vs. yabai (more focused on window tiling within spaces).
  - Requires learning keyboard shortcuts.
- **Best for**: Users wanting automatic tiling without CLI complexity or SIP changes.

### 1.2 Window Management (Non-Tiling)

#### Rectangle (Free)
- **What it does**: Move and resize windows via keyboard shortcuts and snap areas. Half/quarter/third positioning, maximize, move between displays.
- **Maintained**: Yes, actively. Latest v0.93 (Jan 2026).
- **macOS support**: macOS 10.15+.
- **Pricing**: Free, MIT license.
- **Key limitations**: No Space management features. Window positioning only.

#### Rectangle Pro
- **What it does**: Premium version with workspace arrangements, custom snap targets, window stashing, app pinning.
- **Key feature for Spaces**: Workspace arrangements that auto-activate when displays connect/disconnect.
- **Maintained**: Yes, actively.
- **macOS support**: macOS 11+, Intel and Apple Silicon.
- **Pricing**: One-time purchase (~$10 USD estimated, 10-day free trial). License for 3 devices.
- **Key limitations**: Space management is limited to saving/restoring window arrangements per display configuration, not per-Space layouts.

#### Moom
- **What it does**: Window management via pop-up palette, saved layouts, snap zones, drop zones, keyboard control.
- **Key feature**: Saved layouts (app-specific or "any N windows"). Can chain actions together. Exportable settings.
- **Maintained**: Yes. Moom 4.4.2 current version.
- **macOS support**: macOS 10.13+.
- **Pricing**: $15 one-time (upgrade from Moom 3: $8). License valid forever, includes 1 year updates.
- **Key limitations**: Focuses on window arrangements within a screen, not Space-specific layout persistence.

### 1.3 Automation Tools

#### Bunch
- **What it does**: Plain-text automation for context switching. Launch apps, load files, open websites, change system settings (wallpaper, DND, audio), run scripts, hide/show Dock.
- **Maintained**: Yes, active development.
- **macOS support**: macOS (specific versions not listed).
- **Pricing**: Free.
- **Key features for Spaces**: Can set up "contexts" for different work modes. Switch wallpapers, launch app combinations, start servers, open folders.
- **Key limitations**: Does not directly manage Spaces (cannot create/switch/assign apps to specific Spaces natively). Works at the app/settings level.

#### Hammerspoon
- **What it does**: macOS automation via Lua scripting. Bridges OS APIs to Lua. Extensive extension system.
- **Key feature for Spaces**: `hs.spaces` module provides:
  - List all spaces, active spaces, focused space
  - Get space type (user/fullscreen)
  - Create/remove spaces
  - Switch to specific space (`gotoSpace`)
  - Move windows between spaces (`moveWindowToSpace`)
  - Get windows for a space, spaces for a window
  - Mission Control space names
- **Maintained**: Yes, actively. v1.1.0 (Dec 2025). 14.5k stars.
- **macOS support**: macOS (recent versions supported).
- **Pricing**: Free, MIT license.
- **Key limitations**: Requires Lua scripting knowledge. No GUI for configuration. Some space operations produce visual artifacts. Uses private APIs for space functions.
- **Best for**: Users who want full programmatic control over Spaces and are comfortable writing Lua scripts.

### 1.4 App/Window Switching

#### AltTab
- **What it does**: Windows-style alt-tab with window thumbnails. Shows all windows across apps. Can filter by Space.
- **Key features for Spaces**: Shows Space number labels on thumbnails. Can configure which Spaces/screens to show per shortcut.
- **Maintained**: Yes, actively. v10.2.0 (Feb 2026). 14.9k stars, 6.9M downloads.
- **macOS support**: macOS 10.12 to latest. Universal binary.
- **Pricing**: Free, GPL-3.0.
- **Key limitations**: Primarily a window switcher, not a Space manager. Stage Manager can cause thumbnail rendering issues.

#### rcmd
- **What it does**: App switcher using Right Command + first letter of app name. Automatically switches to correct Space.
- **Maintained**: Yes.
- **macOS support**: macOS 13.0+.
- **Pricing**: Free on Mac App Store.
- **Key advantage for Spaces**: When switching to an app, it automatically navigates to the Space containing that app's window.
- **Key limitations**: App-switching only, no Space management or layout features.

---

## 2. Space Naming / Identification

### 2.1 Menu Bar Space Indicators

#### Spaceman
- **What it does**: Menu bar app showing which Space you're on. 4 display styles: rectangles, numbers, rectangles+numbers, named spaces (up to 3 chars). Multi-display support.
- **Maintained**: Last release v1.0 (Dec 2021). Not actively maintained.
- **macOS support**: Requires macOS 15 Sequoia+ (per current README).
- **Pricing**: Free, MIT license.
- **Limitation**: Stale project, 3+ years without release. May have compatibility issues.

#### SpaceId
- **What it does**: Menu bar indicator showing current space number.
- **Maintained**: No. Last release v1.4 (Apr 2021).
- **macOS support**: Uncertain for Sonoma/Sequoia.
- **Pricing**: Free.
- **Limitation**: Likely broken on recent macOS. Inspired WhichSpace successor projects.

#### WhichSpace
- **What it does**: Original menu bar space indicator by Sindre Sorhus.
- **Maintained**: Repository returns 404 / appears discontinued.
- **Status**: Abandoned. Successors: SpaceId, Spaceman.

### 2.2 Custom Status Bars

#### SketchyBar
- **What it does**: Highly customizable status bar replacement for macOS. Can show Space indicators with numbers, icons, names, dot indicators. Integrates with yabai or AeroSpace.
- **Maintained**: Yes, actively. v2.23.0 (Nov 2025). 11.2k stars.
- **macOS support**: Recent macOS versions.
- **Pricing**: Free, GPL-3.0.
- **Space features**: Dynamic space indicators, click-to-focus, highlight active space, show window count per space. Requires yabai or AeroSpace for space queries.
- **Key limitations**: Requires significant configuration (shell scripts). Best paired with yabai or AeroSpace.

#### simple-bar (Ubersicht widget)
- **What it does**: Status bar widget showing apps/windows per workspace. Runs via Ubersicht. Integrates with yabai or AeroSpace.
- **Maintained**: Yes. 1.5k stars, 1,243 commits.
- **Key limitations**: Requires yabai or AeroSpace. Ubersicht dependency.

### 2.3 Space Naming

#### Spaces Renamer
- **What it does**: Adds custom names to macOS Spaces visible in Mission Control.
- **Maintained**: Somewhat. v1.11.1 (Aug 2024).
- **macOS support**:
  - Intel: Works on macOS up to 14.3. May not work on 14.4+.
  - Apple Silicon: Requires special beta MacForge version for macOS 14.4+.
- **Pricing**: Free, MIT license.
- **Key limitations**: Requires partially disabling SIP. Uses MacForge/SIMBL injection. Fragile on Apple Silicon and recent macOS. Likely to break with each major macOS update.

### 2.4 Per-Space Wallpapers (Built-in)
- macOS natively supports setting different wallpapers per Space.
- Navigate to each Space -> System Settings -> Wallpaper -> Set wallpaper. Each Space remembers its own wallpaper.
- This is the simplest and most reliable way to visually distinguish Spaces.

---

## 3. Window Layout Persistence

### Tools That Save/Restore Window Positions

| Tool | Save/Restore | Display Change Events | Notes |
|------|-------------|----------------------|-------|
| Rectangle Pro | Yes (Workspace Arrangements) | Yes (auto-activate on display connect/disconnect) | Best for multi-display setups |
| Moom | Yes (Saved Layouts) | No auto-trigger | Manual trigger via shortcut/menu |
| Hammerspoon | Yes (via scripting) | Yes (via `hs.screen.watcher`) | Requires custom Lua code |
| yabai | Partial (via scripting) | Partial | Can script layout restoration |
| Bunch | App-level (launch sets) | No direct support | Can trigger scripts on context switch |

**Recommendation**: Rectangle Pro is the most polished solution for layout persistence across display changes. Hammerspoon is the most flexible but requires coding.

---

## 4. Keyboard Shortcut Strategies for 13 Spaces

### 4.1 Native macOS Shortcuts
- **Ctrl + Left/Right Arrow**: Move to adjacent Space (sequential only -- slow for 13 spaces).
- **Ctrl + Number (1-9)**: Jump to Space 1-9 directly. Must be enabled in System Settings -> Keyboard -> Shortcuts -> Mission Control.
- **Limitation**: Native shortcuts only cover Spaces 1-9. Spaces 10-13 have no direct native shortcut.

### 4.2 Extending Shortcuts Beyond 9 Spaces

#### Karabiner-Elements
- **What it does**: Powerful keyboard remapper for macOS.
- **Maintained**: Yes, actively. v15.9.0 (Jan 2026). 21.6k stars.
- **macOS support**: Ventura 13 through Tahoe 26. Intel + Apple Silicon.
- **Pricing**: Free, public domain (Unlicense).
- **Use for Spaces**: Can remap arbitrary key combinations to trigger Space switching for Spaces 10-13. Example: Ctrl+0, Ctrl+-, Ctrl+=, Ctrl+\ for Spaces 10-13.

#### skhd (with yabai)
- **What it does**: Simple hotkey daemon. Text-based config, modal shortcuts, application-specific bindings.
- **Maintained**: Maintenance mode only (critical fixes). Consider Zig port for new features.
- **Use for Spaces**: Define shortcuts like `ctrl - 0 : yabai -m space --focus 10`.

#### Hammerspoon
- Can bind any key combo to `hs.spaces.gotoSpace(spaceID)`.

### 4.3 Recommended Keyboard Strategy for 13 Spaces

**Option A: Direct Jump (requires Karabiner-Elements or skhd)**
```
Ctrl+1 through Ctrl+9  -> Spaces 1-9 (native or remapped)
Ctrl+0                  -> Space 10
Ctrl+-                  -> Space 11
Ctrl+=                  -> Space 12
Ctrl+\                  -> Space 13
```

**Option B: Hyper Key Approach (requires Karabiner-Elements)**
- Remap Caps Lock to "Hyper" (Cmd+Ctrl+Alt+Shift)
- Hyper+1 through Hyper+= for all 13 Spaces
- Leaves Ctrl+number free for other uses

**Option C: Reduce to 10 Spaces and use Ctrl+0-9**

**Critical Setting**: Disable "Automatically rearrange Spaces based on most recent use" in System Settings -> Desktop & Dock. Otherwise Space numbers shift and shortcuts become unpredictable.

---

## 5. Alternative Approaches

### 5.1 Reduce Space Count + Use AeroSpace Virtual Workspaces
- AeroSpace emulates unlimited workspaces without using native Spaces at all.
- Can have named workspaces (e.g., "web", "code", "comms") without the 16-space native limit.
- No animation delays when switching.
- Trade-off: Lose native macOS Spaces features (Mission Control visual overview, per-Space wallpaper).

### 5.2 Stage Manager (macOS Ventura+)
- Groups windows into "stages" on the side of the screen.
- Can work alongside Spaces (use fewer Spaces, more Stage Manager groups within each).
- Trade-off: Not everyone finds Stage Manager intuitive. Limited to showing ~4 recent groups.

### 5.3 App-Based Organization
- Use app features instead of Spaces:
  - **Browser**: Tab groups / profiles for different contexts
  - **VS Code / editors**: Workspaces/projects
  - **Terminal**: tmux sessions or tabs
  - **Finder**: Tab groups
- Combine with fewer Spaces (e.g., 4-5 purpose-based Spaces) + AltTab for window switching.

### 5.4 Bunch for Context Switching
- Instead of keeping 13 Spaces permanently, use Bunch to define "contexts" that launch/quit apps, set wallpapers, run scripts.
- Switch between contexts as needed rather than maintaining all Spaces simultaneously.

---

## 6. Tool Combination Recommendations

### Tier 1: Minimal Setup (Low Complexity)
- **Per-Space wallpapers** (native) for visual identification
- **Karabiner-Elements** for keyboard shortcuts to all 13 Spaces
- **AltTab** for cross-Space window switching
- **rcmd** for instant app-focused Space switching
- Disable "Automatically rearrange Spaces" in System Settings

### Tier 2: Medium Setup
- Everything in Tier 1, plus:
- **Rectangle Pro** ($10) for window layout persistence and display-change handling
- **Bunch** (free) for context switching / workspace setup automation

### Tier 3: Power User Setup (High Complexity)
- **yabai** + **skhd** for full tiling + Space control + keyboard shortcuts
- **SketchyBar** or **simple-bar** for custom Space indicators
- **Hammerspoon** for Space automation scripts
- OR: **AeroSpace** (replaces yabai, no SIP changes needed) + **SketchyBar**

### Tier 4: Alternative -- Fewer Spaces
- Reduce to 4-6 purpose-based Spaces
- **AeroSpace** for virtual workspaces within Spaces (unlimited)
- **Bunch** for context switching
- **AltTab** + **rcmd** for navigation
- Browser tab groups + editor workspaces for app-level organization

---

## Summary Table

| Tool | Type | Price | Maintained | macOS 14/15 | SIP Required | Space Features |
|------|------|-------|------------|-------------|--------------|----------------|
| yabai | Tiling WM | Free | Yes | Yes | Partial (for space mgmt) | Full control |
| AeroSpace | Tiling WM | Free | Yes (beta) | Yes | No | Own workspace system |
| Amethyst | Tiling WM | Free | Yes | Yes | No | Move windows between spaces |
| Rectangle Pro | Window Mgmt | ~$10 | Yes | Yes | No | Layout save/restore |
| Moom | Window Mgmt | $15 | Yes | Yes | No | Layout save/restore |
| Hammerspoon | Automation | Free | Yes | Yes | No | Full hs.spaces API |
| Bunch | Automation | Free | Yes | Yes | No | Context switching |
| AltTab | Switcher | Free | Yes | Yes | No | Space-aware switching |
| rcmd | Switcher | Free | Yes | Yes | No | Auto-navigate to app Space |
| Karabiner-Elements | Key Remap | Free | Yes | Yes | No | Custom Space shortcuts |
| SketchyBar | Status Bar | Free | Yes | Yes | No | Space indicators |
| Spaceman | Indicator | Free | No (2021) | Uncertain | No | Space number display |
| Spaces Renamer | Naming | Free | Partial | Fragile | Yes | Name Spaces in MC |
