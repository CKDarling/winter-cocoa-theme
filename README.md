# Winter Cocoa — VS Code Theme

A warm, dark theme built from the **Manly Winter — Winter Cocoa** color palette.

## Palette

| Swatch | Hex | Role |
|--------|---------|------|
| ![#1a1210](images/swatches/1a1210.png) | `#1a1210` | Editor, sidebar and panel background (deep espresso) |
| ![#3b2f2f](images/swatches/3b2f2f.png) | `#3b2f2f` | Current line, word highlights, indent guides (espresso) |
| ![#d9d6cf](images/swatches/d9d6cf.png) | `#d9d6cf` | Foreground text, variables (cream) |
| ![#5c4033](images/swatches/5c4033.png) | `#5c4033` | Selection, button hover (walnut) |
| ![#708090](images/swatches/708090.png) | `#708090` | Comments, active borders, badges, muted UI (slate) |
| ![#4b3621](images/swatches/4b3621.png) | `#4b3621` | Source palette (umber) |

## Derived Syntax Colors

| Swatch | Color | Hex | Used for |
|--------|-------|---------|----------|
| ![#a3b08a](images/swatches/a3b08a.png) | Sage | `#a3b08a` | Strings, docstrings |
| ![#c4978c](images/swatches/c4978c.png) | Dusty rose | `#c4978c` | Keywords, control flow, `global` / `nonlocal`, exceptions, CSS at-rules |
| ![#8aaec2](images/swatches/8aaec2.png) | Pale blue | `#8aaec2` | Functions, HTML tags, links |
| ![#84aeb8](images/swatches/84aeb8.png) | Teal grey | `#84aeb8` | Builtins, builtin types (`int`, `str`, `list`), type hints, `__name__`, CSS properties |
| ![#d4b99a](images/swatches/d4b99a.png) | Warm sand | `#d4b99a` | Classes, headings, HTML attribute values |
| ![#c09878](images/swatches/c09878.png) | Caramel | `#c09878` | Decorators, f-string braces, escape sequences, HTML attributes |
| ![#b094a4](images/swatches/b094a4.png) | Mauve | `#b094a4` | Numbers, enum members, CSS colors and units |
| ![#a07850](images/swatches/a07850.png) | Bronze | `#a07850` | `True` / `False` / `None`, `ALL_CAPS` constants, read-only values |
| ![#a08da0](images/swatches/a08da0.png) | Plum grey | `#a08da0` | `self` / `cls`, CSS pseudo-classes |
| ![#8a9eb2](images/swatches/8a9eb2.png) | Bright slate | `#8a9eb2` | CSS / SCSS variables |

## Git Colors

| Swatch | Hex | Used for |
|--------|---------|----------|
| ![#7a907a](images/swatches/7a907a.png) | `#7a907a` | Added / untracked |
| ![#8a9eb2](images/swatches/8a9eb2.png) | `#8a9eb2` | Modified |
| ![#a07070](images/swatches/a07070.png) | `#a07070` | Deleted |
| ![#9a8090](images/swatches/9a8090.png) | `#9a8090` | Conflicts |

## Install

```bash
# From the extension directory:
code --install-extension winter-cocoa-0.1.0.vsix

# Or during development — open this folder in VS Code, press F5,
# then Cmd+K Cmd+T → select "Winter Cocoa".
# examples/orders.py exercises most of the Python colors.
```

## Build .vsix

```bash
npm install -g @vscode/vsce
cd winter-cocoa-theme
vsce package
```

## Source

Palette: [Manly Winter — Winter Cocoa](https://www.color-hex.com/color-palette/1075024)
