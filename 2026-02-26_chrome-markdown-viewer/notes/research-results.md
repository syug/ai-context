# Chrome Markdown Viewer Extensions - Research Results

Date: 2026-02-26

## Top Recommendations

### 1. Markdown Viewer (by simov) -- BEST OVERALL

- **GitHub**: https://github.com/simov/markdown-viewer (1,421 stars, MIT License)
- **Chrome Web Store**: Search "Markdown Viewer" by simov
- **Extension ID**: `ckkdlimhmcjmikdlpkmbgfkaikojcbjk`

**Features:**
- 30+ built-in themes (including GitHub light/dark)
- 3 parser engines: markdown-it, marked, remark
- Full GitHub Flavored Markdown (GFM): tables, strikethrough, task lists, fenced code blocks
- Syntax highlighting via Prism.js
- Table of Contents (ToC) generation
- MathJax formula rendering ($math$, $$math$$)
- Mermaid diagram support
- Emoji conversion (:shortnames:)
- Auto-reload on file save (for local dev workflow)
- Raw/rendered view toggle
- Custom theme upload (up to 8KB CSS)
- Settings sync across devices
- Width options: auto, full, wide (1400px), large (1200px), medium (992px), small (768px), tiny (576px)

**Local file:// support:** YES -- enable at chrome://extensions > Details > "Allow access to file URLs"

**Browser support:** Chrome, Firefox, Edge, Opera, Brave, Chromium, Vivaldi

**Permissions:** Optional host permissions (granular per-origin), storage, webRequest. Security-first design.

**Dark mode:** YES (via theme selection, includes dark GitHub theme)

**Verdict:** The most feature-rich and popular option. Highly configurable, actively maintained, open source.

---

### 2. Markdown Preview Plus (by volca)

- **GitHub**: https://github.com/volca/markdown-preview (250 stars, MIT License)
- **Chrome Web Store**: Search "Markdown Preview Plus"
- **Extension ID**: `febilkbfcbhebfnokafefeacimjdckgl`

**Features:**
- GitHub Flavored Markdown: tables, task lists, strikethrough, fenced code blocks
- Syntax highlighting for code blocks
- KaTeX and MathJax for mathematical expressions
- Mermaid.js diagram support (flowcharts, sequence diagrams, Gantt charts)
- Auto-reload on file save
- Multiple built-in themes + custom CSS support
- Export rendered markdown as HTML
- Bootstrap-based styling
- Table of Contents generation from headers

**Local file:// support:** YES -- enable "Allow access to file URLs" in chrome://extensions

**Permissions:** File URL access, active tab

**Dark mode:** Available via theme selection

**Verdict:** Solid option with good math/diagram support. Slightly fewer themes than Markdown Viewer but well-maintained (last updated Feb 2026). Good choice if you need strong KaTeX math rendering.

---

### 3. Chrome MD Preview Extension (by lpolish) -- MINIMALIST OPTION

- **GitHub**: https://github.com/lpolish/chrome-md-preview-extension (new, MIT License)
- **Install**: Manual install only (not on Chrome Web Store)

**Features:**
- Split-pane view: raw Markdown (left) + rendered preview (right)
- Synchronized scrolling between panes
- VS Code-style theme aesthetics
- Automatic dark/light mode (follows system preference)
- GitHub Flavored Markdown via marked.js
- Table rendering with alignment
- Zero configuration -- works immediately

**Local file:// support:** YES -- requires enabling "Allow access to file URLs"

**Permissions:** Content script on all URLs, file:// protocol access

**Dark mode:** YES (automatic, follows system prefers-color-scheme)

**Limitations:**
- No table of contents generation
- No math/diagram support
- No custom themes or settings UI
- Manual installation only (not on Chrome Web Store)
- No adjustable split-pane ratio

**Verdict:** Best for users who want a simple, no-config split-pane view with VS Code aesthetics. The raw+preview side-by-side is unique. However, requires manual installation and lacks advanced features.

---

### 4. Markdown Here (by adam-p) -- FOR EMAIL, NOT FILE VIEWING

- **GitHub**: https://github.com/adam-p/markdown-here (60,150 stars)
- **Note:** This is NOT a file viewer -- it's for writing emails in Markdown and rendering them before sending. Included here for completeness since it appears in many "best markdown extensions" lists, but it does NOT solve the .md file viewing use case.

---

## Comparison Table

| Feature | Markdown Viewer (simov) | Markdown Preview Plus | Chrome MD Preview |
|---|---|---|---|
| Chrome Web Store | Yes | Yes | No (manual) |
| GitHub Stars | 1,421 | 250 | 0 |
| GFM Support | Full | Full | Full |
| Local file:// | Yes | Yes | Yes |
| Dark Mode | Yes (themes) | Yes (themes) | Yes (auto) |
| ToC Generation | Yes | Yes | No |
| Math Rendering | MathJax | KaTeX + MathJax | No |
| Diagrams | Mermaid | Mermaid | No |
| Themes | 30+ | Multiple + custom CSS | 1 (VS Code) |
| Code Highlighting | Prism.js | Yes | marked.js |
| Auto-reload | Yes | Yes | No |
| Split Pane View | No | No | Yes |
| Export HTML | No | Yes | No |
| Custom CSS | Yes (8KB) | Yes | No |
| Parsers | 3 options | marked.js | marked.js |
| Active Maintenance | Yes | Yes (Feb 2026) | New project |
| License | MIT | MIT | MIT |

## Recommendation

**Install "Markdown Viewer" by simov.** It is the clear winner:
- Most popular (1,421 GitHub stars)
- Most feature-rich (30+ themes, 3 parsers, ToC, math, diagrams, emoji)
- Available on Chrome Web Store (easy install)
- Actively maintained
- Security-first design with granular permissions
- Works across all Chromium browsers + Firefox

After installing:
1. Go to `chrome://extensions`
2. Find "Markdown Viewer" and click "Details"
3. Toggle ON "Allow access to file URLs"
4. Open any local .md file -- it will render beautifully

Optional setup:
- Click the extension icon > Advanced Options to configure themes, ToC, etc.
- Enable ToC for document navigation
- Choose a GitHub-style theme for familiar rendering
