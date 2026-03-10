# Space Keyboard Shortcuts Research
**Date:** 2026-02-26

## Current State

### Ctrl+1-9 (Desktops 1-9)
- **Status: NOT enabled**
- Symbolic hotkey IDs 118-126 are completely absent from `com.apple.symbolichotkeys`
- These need to be enabled either via System Settings GUI or `defaults write`

### Ctrl+Arrow (Space Left/Right)
- **Status: Enabled** (IDs 79-82)

### Desktop 10-16 shortcuts
- **Status: No native shortcut exists**
- macOS System Settings shows "Switch to Desktop N" entries for each existing desktop
- However, the system only assigns Ctrl+1-9 by default

## Approaches Investigated

### 1. System Settings GUI (Recommended for Desktops 1-9)
**Path:** System Settings > Keyboard > Keyboard Shortcuts > Mission Control
- Scroll down to see "Switch to Desktop 1" through "Switch to Desktop 16"
- Check each checkbox and assign Ctrl+1, Ctrl+2, etc.
- This is the most reliable method
- For Desktop 10+, you can assign any modifier+key combo here

### 2. `defaults write` (Script-based, for all desktops)
**Symbolic Hotkey IDs:**
| ID | Action | Default Key |
|----|--------|-------------|
| 118 | Switch to Desktop 1 | Ctrl+1 |
| 119 | Switch to Desktop 2 | Ctrl+2 |
| 120 | Switch to Desktop 3 | Ctrl+3 |
| 121 | Switch to Desktop 4 | Ctrl+4 |
| 122 | Switch to Desktop 5 | Ctrl+5 |
| 123 | Switch to Desktop 6 | Ctrl+6 |
| 124 | Switch to Desktop 7 | Ctrl+7 |
| 125 | Switch to Desktop 8 | Ctrl+8 |
| 126 | Switch to Desktop 9 | Ctrl+9 |
| 127* | Switch to Desktop 10 | (none) |
| 128* | Switch to Desktop 11 | (none) |
| 129* | Switch to Desktop 12 | (none) |
| 130* | Switch to Desktop 13 | (none) |
| 131* | Switch to Desktop 14 | (none) |
| 132* | Switch to Desktop 15 | (none) |
| 133* | Switch to Desktop 16 | (none) |

*IDs 127-133 are extrapolated from the sequential pattern. Not officially documented by Apple. Need to test.

**Parameter format:** `(ASCII_code, virtual_keycode, modifier_flags)`

**Modifier flags:**
- 262144 = Control
- 131072 = Shift
- 393216 = Control + Shift (262144 + 131072)
- 524288 = Option
- 786432 = Control + Option (262144 + 524288)

**macOS virtual keycodes for number keys:**
| Key | Virtual Keycode | ASCII |
|-----|----------------|-------|
| 0 | 29 | 48 |
| 1 | 18 | 49 |
| 2 | 19 | 50 |
| 3 | 20 | 51 |
| 4 | 21 | 52 |
| 5 | 23 | 53 |
| 6 | 22 | 54 |
| 7 | 26 | 55 |
| 8 | 28 | 56 |
| 9 | 25 | 57 |

**Apply changes without logout:**
```bash
/System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings -u
```

### 3. Karabiner-Elements + shell_command (Fallback for Desktops 10-16)
If the `defaults write` approach with IDs 127-133 does not work, use Karabiner-Elements to intercept key combos and run a script that navigates via Ctrl+Arrow.

**Approach:**
- Karabiner catches Ctrl+0 / Ctrl+Shift+1-6
- Executes `switch-to-space.sh N` which:
  1. Detects current space number via `com.apple.spaces.plist`
  2. Calculates direction and distance
  3. Sends minimal Ctrl+Left/Right arrow presses via AppleScript

**Pros:** Works regardless of macOS version, no undocumented IDs
**Cons:** Visible transition animation (each arrow key press shows a space slide), slight delay (~0.12s per space), requires Accessibility permission

### 4. yabai (Not recommended)
- Can switch spaces directly: `yabai -m space --focus 10`
- Full functionality requires SIP partial disable
- Overkill for just space switching

## Recommended Setup

### Phase 1: Enable Ctrl+1-9 (Do this NOW)
**Option A (GUI, safest):**
1. Open System Settings > Keyboard > Keyboard Shortcuts > Mission Control
2. Check boxes and assign Ctrl+1 through Ctrl+9

**Option B (Script):**
```bash
bash ~/Library/CloudStorage/GoogleDrive-syugo3hz@gmail.com/My\ Drive/.ai/2026-02-23_macos-spaces-management/artifacts/enable-space-shortcuts.sh
```

### Phase 2: Test Desktops 10-16 via defaults write
Run the script (includes IDs 127-133). Then check System Settings to verify they appear.

If they DO work: Done. No Karabiner needed for this.
If they DON'T work: Proceed to Phase 3.

### Phase 3: Karabiner Fallback (Only if Phase 2 fails)
1. Import `karabiner-spaces-10-16.json` into Karabiner-Elements
2. The rules use `switch-to-space.sh` at `~/scripts/switch-to-space.sh`

## Shortcut Scheme Summary

| Shortcut | Target | Method |
|----------|--------|--------|
| Ctrl+1 | Desktop 1 | Native (symbolic hotkey 118) |
| Ctrl+2 | Desktop 2 | Native (symbolic hotkey 119) |
| Ctrl+3 | Desktop 3 | Native (symbolic hotkey 120) |
| Ctrl+4 | Desktop 4 | Native (symbolic hotkey 121) |
| Ctrl+5 | Desktop 5 | Native (symbolic hotkey 122) |
| Ctrl+6 | Desktop 6 | Native (symbolic hotkey 123) |
| Ctrl+7 | Desktop 7 | Native (symbolic hotkey 124) |
| Ctrl+8 | Desktop 8 | Native (symbolic hotkey 125) |
| Ctrl+9 | Desktop 9 | Native (symbolic hotkey 126) |
| Ctrl+0 | Desktop 10 | defaults write (ID 127) or Karabiner |
| Ctrl+Shift+1 | Desktop 11 | defaults write (ID 128) or Karabiner |
| Ctrl+Shift+2 | Desktop 12 | defaults write (ID 129) or Karabiner |
| Ctrl+Shift+3 | Desktop 13 | defaults write (ID 130) or Karabiner |
| Ctrl+Shift+4 | Desktop 14 | defaults write (ID 131) or Karabiner |
| Ctrl+Shift+5 | Desktop 15 | defaults write (ID 132) or Karabiner |
| Ctrl+Shift+6 | Desktop 16 | defaults write (ID 133) or Karabiner |

## Does Raycast-based switching make Karabiner unnecessary?

**Short answer: Partially, but not fully.**

- **Raycast Space Dashboard** (already built) shows current space + project name
- **Raycast extension for space search** (planned) would allow searching by project name
- These are great for **discovery** ("which space has X?") but slow for **habitual switching** (Ctrl+5 is faster than "open Raycast, type project name, select, press Enter")

**Recommendation:** Use BOTH:
- Ctrl+1-9 for frequently used spaces (muscle memory)
- Raycast search for infrequently used or forgotten spaces
- Karabiner for 10-16 only as a fallback if `defaults write` fails
