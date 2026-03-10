# Rectangle Pro - Workspace Arrangements (Layouts) Setup Guide

Date: 2026-02-24

## Overview

Rectangle Pro's marketing page calls this feature "Workspace Arrangements," but within the app and community, the feature is called **Layouts**. It allows you to save the positions and sizes of all your application windows and restore them with a keyboard shortcut or automatically when displays connect/disconnect.

---

## 1. Accessing Layouts in Rectangle Pro

- Open Rectangle Pro's preferences/settings (click the menu bar icon, then Settings)
- Navigate to the **Layouts** tab (may also appear under the main settings area)
- This is where you create, edit, and manage saved workspace arrangements

---

## 2. Creating and Saving a Layout

### Quick Method (Recommended)

1. **Arrange all your windows** exactly how you want them on your current display setup
2. From the Rectangle Pro **menu bar menu**, select **"Save Current Layout..."**
3. Give the layout a descriptive name (e.g., "Desk - External Monitor" or "Laptop Only")
4. Rectangle Pro captures the coordinates and sizes of all open application windows into an "Applications group"

### Configuration Options After Saving

- **Keyboard shortcut**: Record a shortcut to trigger the layout instantly
- **"Launch closed/minimized apps" checkbox**: Enable this to auto-launch apps that are part of the layout but currently closed
- **Menu bar visibility**: Add saved layouts to the menu bar menu via Settings > Menu & Icon tab
- **Drag and drop**: Reorganize window configurations between app groups by dragging items

### Size and Position Values

- Values **less than 1**: Interpreted as percentage of screen (e.g., 0.5 = 50% of screen width/height)
- Values **1 or greater**: Interpreted as absolute pixel dimensions

---

## 3. Auto-Triggering on Display Connect/Disconnect

### Available Trigger Types

Each layout has trigger options that can be enabled:

1. **Trigger on display connected** - Activates when an external monitor is plugged in
2. **Trigger on display disconnected** - Activates when an external monitor is removed
3. **Trigger on wake** - Activates when the system wakes from sleep

### How to Configure

1. Open the layout you want to auto-trigger
2. Look for the trigger options/checkboxes in the layout settings
3. For your **multi-monitor layout**: Enable "Trigger on display connected"
4. For your **laptop-only layout**: Enable "Trigger on display disconnected"

### Recommended Setup Pattern

Create **two layouts**:

| Layout Name | Trigger Setting | Description |
|---|---|---|
| "External Monitor" | Trigger on display connected | Windows arranged for external + laptop |
| "Laptop Only" | Trigger on display disconnected | Windows arranged for laptop screen only |

### Known Limitations and Issues

- **Timing problems**: The layout may trigger before macOS fully recognizes the display. The developer has noted: "the timing for the layout being applied vs when the display becomes reachable is not lining up." If windows don't position correctly, try adding a "Trigger on wake" as well, since connecting a display often involves waking the system.
- **No specific display identification (as of mid-2024)**: Rectangle Pro triggers on *any* display connect/disconnect event. It does not yet distinguish between specific monitors (e.g., home monitor vs. office monitor). The developer has stated plans to add "more configuration to layouts so that you can specify more details about when to apply layouts, like when specific displays are added" but this was not yet implemented as of the latest community discussions.
- **No desktop/space targeting**: There is no Apple API for targeting specific macOS Spaces/desktops, so layouts cannot specify which Space a window should go to.
- **Conflict potential**: Enabling triggers on multiple layouts can cause conflicts. Be careful to only enable "connected" on your multi-monitor layout and "disconnected" on your single-monitor layout -- not both triggers on both layouts.

---

## 4. Key Settings and Tips

### Best Practices

1. **Name layouts clearly**: Use descriptive names like "Home-2Monitor", "Office-UltraWide", "Laptop-Only" for easy identification
2. **Enable "Launch closed/minimized apps"**: Ensures your full workspace is restored even if apps were closed
3. **Test after saving**: Trigger the layout manually first (via shortcut) before relying on auto-trigger
4. **Update layouts by re-saving**: To update a layout, rearrange your windows and save a new layout with the same name (or delete and recreate -- updating in-place may not be straightforward)
5. **Use URL schemes for scripting**: Integrate with macOS Shortcuts or shell scripts:
   ```
   open -g "rectangle-pro://execute-layout?name=YourLayoutName"
   ```
6. **iCloud sync**: Enable Configuration Sync in settings to sync layouts across Macs

### Troubleshooting

- If layouts don't restore correctly after display connect, try also enabling "Trigger on wake"
- If windows end up on the wrong monitor, check the per-window display assignment in the layout editor
- CleanShot X has been reported to interfere with "Save Current Layout" -- quit it temporarily if you have issues saving

---

## 5. Step-by-Step Setup Instructions

### Initial Setup

1. **Install Rectangle Pro** from rectangleapp.com/pro (paid app, one-time purchase)
2. **Grant Accessibility permissions** when prompted (System Settings > Privacy & Security > Accessibility)
3. Open Rectangle Pro settings from the menu bar icon

### Creating Your Multi-Monitor Layout

1. Connect your external monitor(s)
2. Arrange all application windows exactly how you want them across all displays
3. Click the Rectangle Pro menu bar icon
4. Select **"Save Current Layout..."**
5. Name it (e.g., "Desk Setup")
6. In the layout settings:
   - Record a keyboard shortcut (e.g., Ctrl+Option+Cmd+1)
   - Check **"Launch closed/minimized apps"** if desired
   - Enable **"Trigger on display connected"**
7. Save

### Creating Your Laptop-Only Layout

1. Disconnect your external monitor(s)
2. Arrange all application windows how you want them on the laptop screen
3. Click the Rectangle Pro menu bar icon
4. Select **"Save Current Layout..."**
5. Name it (e.g., "Laptop Only")
6. In the layout settings:
   - Record a keyboard shortcut (e.g., Ctrl+Option+Cmd+2)
   - Check **"Launch closed/minimized apps"** if desired
   - Enable **"Trigger on display disconnected"**
7. Save

### Testing

1. Manually trigger each layout using the keyboard shortcuts to verify window positions
2. Disconnect your external monitor and verify the "Laptop Only" layout activates
3. Reconnect the external monitor and verify the "Desk Setup" layout activates
4. If timing issues occur, also enable "Trigger on wake" on the relevant layout

### Programmatic / Script Access

```bash
# Execute a layout from Terminal or scripts
open -g "rectangle-pro://execute-layout?name=Desk%20Setup"

# Execute a window action
open -g "rectangle-pro://execute-action?name=tile2x2"
```

---

## Sources

- Rectangle Pro official page: https://rectangleapp.com/pro
- Developer guide (Discussion #111): https://github.com/rxhanson/RectanglePro-Community/discussions/111
- Display trigger discussion (#611): https://github.com/rxhanson/RectanglePro-Community/discussions/611
- Stay replacement discussion (#825): https://github.com/rxhanson/RectanglePro-Community/discussions/825
- Feature request for display-specific layouts (#745): https://github.com/rxhanson/RectanglePro-Community/discussions/745
- Multi-display presets request (#521): https://github.com/rxhanson/RectanglePro-Community/issues/521
