#!/bin/bash
# Enable keyboard shortcuts for switching to Desktops 1-16
#
# === HOW MACOS SYMBOLIC HOTKEYS WORK ===
# Domain: com.apple.symbolichotkeys
# Key: AppleSymbolicHotKeys
# Each entry: { enabled = 1; value = { parameters = (ascii, keycode, modifiers); type = standard; }; }
#
# Modifier flags:
#   262144   = Control
#   393216   = Control + Shift
#   786432   = Control + Option
#   917504   = Control + Option + Shift
#
# Symbolic hotkey IDs for "Switch to Desktop N":
#   118 = Desktop 1,  119 = Desktop 2, ..., 126 = Desktop 9
#   127 = Desktop 10, 128 = Desktop 11, ..., 133 = Desktop 16
#
# macOS virtual keycodes for number keys:
#   0=29, 1=18, 2=19, 3=20, 4=21, 5=23, 6=22, 7=26, 8=28, 9=25
#
# === SHORTCUT SCHEME ===
# Desktops 1-10:  Ctrl + Option + Shift + 1-9,0 (modifier 917504)
# Desktops 11-16: Ctrl + Option + 1-6           (modifier 786432)
# These are backend-only shortcuts for Raycast Spaces Manager Extension.
# Not intended for direct human use.
#
# === TECHNICAL NOTES ===
# - `defaults write -dict-add` does NOT overwrite existing keys (silently skips)
# - PlistBuddy writes bypass cfprefsd cache (system won't see changes)
# - Correct approach: defaults export → PlistBuddy on temp file → defaults import
# - killall Dock forces Mission Control to reload shortcut bindings
#
# Usage:
#   bash enable-space-shortcuts.sh

set -e

DOMAIN="com.apple.symbolichotkeys"
TMPFILE=$(mktemp /tmp/symhotkeys.XXXXXX.plist)

echo "=== Enabling Space Switching Shortcuts ==="
echo ""

# Export current prefs (reads from cfprefsd — live values)
defaults export "$DOMAIN" "$TMPFILE"
echo "Exported current preferences."

# --- Helper function ---
set_shortcut() {
    local id="$1" ascii="$2" keycode="$3" modifier="$4"
    /usr/libexec/PlistBuddy \
        -c "Set :AppleSymbolicHotKeys:${id}:enabled true" \
        -c "Set :AppleSymbolicHotKeys:${id}:value:parameters:0 ${ascii}" \
        -c "Set :AppleSymbolicHotKeys:${id}:value:parameters:1 ${keycode}" \
        -c "Set :AppleSymbolicHotKeys:${id}:value:parameters:2 ${modifier}" \
        "$TMPFILE"
}

# --- Desktops 1-9: Ctrl+Option+Shift (917504) ---
echo "Setting Ctrl+Opt+Shift+1-9 for Desktops 1-9..."
set_shortcut 118 49 18 917504  # 1
set_shortcut 119 50 19 917504  # 2
set_shortcut 120 51 20 917504  # 3
set_shortcut 121 52 21 917504  # 4
set_shortcut 122 53 23 917504  # 5
set_shortcut 123 54 22 917504  # 6
set_shortcut 124 55 26 917504  # 7
set_shortcut 125 56 28 917504  # 8
set_shortcut 126 57 25 917504  # 9
echo "  Done."

# --- Desktop 10: Ctrl+Option+Shift+0 (917504) ---
echo "Setting Ctrl+Opt+Shift+0 for Desktop 10..."
set_shortcut 127 48 29 917504  # 0
echo "  Done."

# --- Desktops 11-16: Ctrl+Option (786432) ---
echo "Setting Ctrl+Opt+1-6 for Desktops 11-16..."
set_shortcut 128 49 18 786432  # 1
set_shortcut 129 50 19 786432  # 2
set_shortcut 130 51 20 786432  # 3
set_shortcut 131 52 21 786432  # 4
set_shortcut 132 53 23 786432  # 5
set_shortcut 133 54 22 786432  # 6
echo "  Done."

# Import back through cfprefsd (updates both cache AND file)
echo ""
echo "Importing via cfprefsd..."
defaults import "$DOMAIN" "$TMPFILE"
rm -f "$TMPFILE"
echo "  Done."

# Activate settings
echo ""
echo "=== Activating Settings ==="
/System/Library/PrivateFrameworks/SystemAdministration.framework/Resources/activateSettings -u

# Restart Dock to force Mission Control to reload
echo "Restarting Dock..."
killall Dock 2>/dev/null || true

echo ""
echo "=== Summary ==="
echo "  Ctrl+Opt+Shift+1-9   → Desktops 1-9   (917504)"
echo "  Ctrl+Opt+Shift+0     → Desktop 10      (917504)"
echo "  Ctrl+Opt+1-6         → Desktops 11-16  (786432)"
echo ""
echo "Verify in: System Settings > Keyboard > Keyboard Shortcuts > Mission Control"
