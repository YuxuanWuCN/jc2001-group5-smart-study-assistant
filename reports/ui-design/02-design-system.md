# StudyGraph UI Design System (设计规范)

**Owner:** 50105989 (UI/UX Designer)
**Document status:** v1.0
**Aligned requirements:** NFR-03, NFR-07, NFR-08

## 1. Design Principles
- Console-style tool aesthetic, efficiency-first
- 8px grid system for all spacing and dimensions
- Light + dark dual themes, accessible contrast
- Icon + text dual indication for all statuses (not colour alone)
- Complete state design: default / hover / disabled / loading / empty / error

## 2. Layout System
Global console layout: left fixed sidebar + top status bar + main content area

| Area | Width / Height | Padding | Description |
| :--- | :---: | :---: | :--- |
| Sidebar | 240px fixed width | 16px | Navigation menu, project logo |
| Top bar | 56px fixed height | 0 24px | Page title, theme toggle, status info |
| Main content | Adaptive width | 24px | Core page content |

## 3. Color System (CSS Variables Ready)
### Light Theme
| Variable Name | Hex Value | Usage |
| :--- | :---: | :--- |
| `--bg-primary` | `#FFFFFF` | Main page background |
| `--bg-secondary` | `#F5F7FA` | Card background, sidebar background |
| `--bg-tertiary` | `#E5E6EB` | Border, divider line |
| `--text-primary` | `#1D2129` | Headings, body text |
| `--text-secondary` | `#4E5969` | Secondary description, hint text |
| `--text-tertiary` | `#86909C` | Disabled text, auxiliary info |
| `--color-primary` | `#165DFF` | Brand colour, primary button, active state |
| `--color-success` | `#00B42A` | Correct answer, success status |
| `--color-warning` | `#FF7D00` | Warning, pending status |
| `--color-danger` | `#F53F3F` | Wrong answer, error status |

### Dark Theme
| Variable Name | Hex Value | Usage |
| :--- | :---: | :--- |
| `--bg-primary` | `#121212` | Main page background |
| `--bg-secondary` | `#1E1E1E` | Card background, sidebar background |
| `--bg-tertiary` | `#2F2F2F` | Border, divider line |
| `--text-primary` | `#E8E8E8` | Headings, body text |
| `--text-secondary` | `#A9A9A9` | Secondary description, hint text |
| `--text-tertiary` | `#6B6B6B` | Disabled text, auxiliary info |
| `--color-primary` | `#4080FF` | Brand colour, primary button |
| `--color-success` | `#0FC6C2` | Correct answer, success status |
| `--color-warning` | `#FF9A2E` | Warning, pending status |
| `--color-danger` | `#F76560` | Wrong answer, error status |

## 4. Typography
| Level | Font Size | Line Height | Font Family | Usage |
| :---: | :---: | :---: | :--- | :--- |
| H1 | 24px | 32px | System sans-serif | Page title |
| H2 | 18px | 24px | System sans-serif | Section title, card title |
| Body | 14px | 22px | System sans-serif | Main body text |
| Caption | 12px | 16px | System sans-serif | Auxiliary text, tags |
| Mono | 14px | 20px | JetBrains Mono / Consolas | Data display, code, evidence labels |

## 5. Spacing System (8px Grid)
All padding, margin and gaps use multiples of 8px:
`8px / 16px / 24px / 32px / 48px`

## 6. Component Specifications
### Buttons
| Type | Height | Padding | Radius | Default State | Hover State |
| :--- | :---: | :---: | :---: | :--- | :--- |
| Primary button | 32px | 0 16px | 6px | Primary colour background + white text | Darken primary by 10% |
| Secondary button | 32px | 0 16px | 6px | Transparent bg + border + primary text | Light primary background |
| Text button | 32px | 0 8px | 4px | Transparent bg + primary text | Light primary background |

### Cards
- Radius: 8px
- Padding: 24px
- Border: 1px solid `--bg-tertiary`
- Shadow: subtle soft shadow (dark theme: none)

### Tags
- Height: 20px
- Padding: 0 8px
- Radius: 4px
- Font: 12px caption

## 7. State Design Rules
1.  All status feedback uses icon + text (not colour only)
2.  Empty state: illustration + hint text + action button
3.  Error state: error message + retry button
4.  Loading state: skeleton screen or spinner
