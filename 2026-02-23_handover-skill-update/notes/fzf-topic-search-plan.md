# fzf Topic Search — Implementation Plan

## Goal
Fish shell function `ho` that uses fzf with preview to fuzzy-search and navigate handover topics.
GHQ-like experience for ai-context topics.

## Design

### Input
- `.index.json` parsed with `jq`
- Each topic formatted as: `{date}  {dir} — {title} [{tag1, tag2, ...}]`
- Aliases also included as searchable text

### fzf Configuration
- `--reverse` — top-aligned
- `--height=50%` — half screen
- `--preview` — show `head -40` of handover.md for selected topic
- `--preview-window=right:50%:wrap` — right panel with wrapping
- Search targets: date, dir (slug), title, tags — all visible in the line

### Preview Command
```
head -40 $AI_BASE/{dir}/handover.md 2>/dev/null || echo '(no handover.md)'
```

### Action on Selection
- Default: `cd $AI_BASE/{dir}` — navigate to topic directory
- Future: optional flag for editor open, Claude Code load, etc.

### Function Name
- `ho` — short, memorable, doesn't conflict with existing commands

## Dependencies
- fish shell
- fzf (homebrew) — verify installed
- jq (homebrew) — verify installed

## Implementation Steps
1. Create fish function `~/.config/fish/functions/ho.fish`
2. Parse .index.json with jq to build display lines
3. Pipe to fzf with preview
4. Extract dir from selected line
5. cd to topic directory
6. Test with various search terms (date, slug, tag, title keyword)

## Edge Cases
- No .index.json -> fallback to `ls` directory names
- No selection (Ctrl+C) -> no action
- Selected topic has no handover.md -> preview shows "(no handover.md)"
- Empty .index.json topics array -> show "No topics found"
