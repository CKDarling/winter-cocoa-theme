# Winter Cocoa — VS Code Theme

A warm, dark theme built from the **Manly Winter — Winter Cocoa** color palette.

## Palette

| Swatch | Hex | Role |
|--------|---------|------|
| ██ | `#3b2f2f` | Editor background (espresso) |
| ██ | `#d9d6cf` | Foreground text (warm grey) |
| ██ | `#5c4033` | Borders, accents (walnut) |
| ██ | `#708090` | Comments, muted UI (slate) |
| ██ | `#4b3621` | Sidebar/panels (dark umber) |

## Derived Syntax Colors

| Color | Hex | Used for |
|-------|---------|----------|
| Dusty rose | `#cf6a6a` | Keywords, control flow, exceptions |
| Blue spruce | `#7aa2c4` | Functions, links |
| Sage green | `#8fb07e` | Strings |
| Forest green | `#7a9a6b` | Docstrings, git added |
| Warm amber | `#c4965a` | Decorators, numbers, constants, git modified |
| Golden honey | `#d1aa74` | Classes, headings |
| Teal | `#6a9a9a` | Builtins, type hints, regex |
| Plum | `#b07aa2` | `self`/`cls`, git conflicts |

## Install

```bash
# From the extension directory:
code --install-extension winter-cocoa-0.1.0.vsix

# Or during development — open this folder in VS Code, press F5,
# then Cmd+K Cmd+T → select "Winter Cocoa"
```

## Build .vsix

```bash
npm install -g @vscode/vsce
cd winter-cocoa-theme
vsce package
```

## Source

Palette: [Manly Winter — Winter Cocoa](https://www.color-hex.com/color-palette/1075024)
