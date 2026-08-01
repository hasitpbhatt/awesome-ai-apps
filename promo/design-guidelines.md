# Design Guidelines — awesome-ai-apps

A small, opinionated design system for the `awesome-ai-apps` repo's visual
assets: the logo (`assets/logo.svg`), the GitHub social preview
(`assets/social-preview.svg`), and any derived banners or badges.

## 1. Colors

Palette is a dark, indigo-first scheme with cyan→violet "AI spark" accents.
Works on both light and dark surfaces, but is optimized for dark backgrounds.

| Token            | Hex       | Usage                                                              |
| ---------------- | --------- | ------------------------------------------------------------------ |
| `bg-900`         | `#0F172A` | Deepest background (social preview base)                            |
| `bg-800`         | `#1E1B4B` | Primary panel / gradient start                                      |
| `bg-700`         | `#312E81` | Panel gradient mid / badge color                                    |
| `bg-600`         | `#164E63` | Gradient end (teal-tinted)                                          |
| `primary-600`    | `#4F46E5` | Buttons, links, badge color                                         |
| `primary-500`    | `#6366F1` | Hover / secondary interactive, glow center                          |
| `accent-cyan`    | `#22D3EE` | Spark gradient start, highlight numbers, dots                       |
| `accent-violet`  | `#A78BFA` | Spark gradient end, secondary highlight                             |
| `accent-green`   | `#34D399` | Success / "MIT" stat                                                |
| `text-strong`    | `#FFFFFF` | Headlines                                                            |
| `text-body`      | `#F8FAFC` | Body copy on dark                                                    |
| `text-soft`      | `#C7D2FE` | Subheads / taglines                                                  |
| `text-muted`     | `#94A3B8` | Labels, captions, footers                                            |
| `surface-glass`  | white @ 6–8% | Pill / chip fill (with 12–16% white stroke)                        |

### Category accent dots
When listing categories, assign each a distinct dot color:
Chatbots `#22D3EE` · Coding `#A78BFA` · Search & Research `#34D399` ·
Writing `#F472B6` · Image `#FB923C` · Video `#F87171` ·
Audio & Voice `#60A5FA` · Productivity `#FACC15` ·
Automation & Agents `#2DD4BF` · Local & Open Source `#E879F9`

### Gradient recipes
- **Brand spark**: linear `#22D3EE` → `#A78BFA`, top-left to bottom-right.
- **Panel background**: linear `#1E1B4B` → `#312E81` → `#164E63`.
- **Social preview**: linear `#0F172A` → `#1E1B4B` → `#312E81` with radial
  indigo glow top-left and cyan glow bottom-right.

## 2. Typography

System-first stack so assets render identically everywhere without font assets:

```
font-family: 'Segoe UI', system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif;
```

| Role        | Weight | Size (px)      | Case / letter-spacing       |
| ----------- | ------ | -------------- | --------------------------- |
| Display     | 800    | 76 (preview)   | tight `-1.5`                |
| Logo mark   | 700    | 42 (banner)    | `-0.5`                      |
| Headline    | 700    | 28 – 58        | `-0.4` to `-0.5`            |
| Tagline     | 400    | 25 (preview)   | normal                      |
| Chip label  | 600    | 18             | normal                      |
| Caption     | 400–600| 12 – 20        | `+0.2` to `+0.3` (small)    |

Rules:
- Display text is `#FFFFFF`, body is `#F8FAFC`, muted text `#94A3B8`.
- Never letter-space body copy; only headlines and small caps-style labels.
- Bold weights (700/800) only for emphasis — repo names, stats, headlines.

## 3. Spacing & layout

Base unit is **4 px**; use multiples of 4 everywhere.

| Scale | Value | Use                                    |
| ----- | ----- | -------------------------------------- |
| 1     | 4 px  | Icon stroke / dot gaps                 |
| 2     | 8 px  | Tight padding inside chips             |
| 3     | 12 px | Chip-to-chip vertical gap              |
| 4     | 16 px | Card padding minimum                   |
| 6     | 24 px | Pill gutter, section gutters           |
| 12    | 48 px | Major section rhythm                   |

- **Page margins**: 80 px on the social preview (left/right), 64 px top.
- **Chips/pills**: height 48–50 px, corner radius 24–25 px (fully rounded),
  12–16 px horizontal padding for text, 20 px from dot to text.
- **Stat blocks**: number baseline sits ~38 px above its label.
- **Footer bar**: 8 px tall accent strip pinned to the top edge of the preview.
- Keep whitespace generous; never let text touch panel edges or strokes.

## 4. Components

- **Spark mark**: 4-point curved star built from one `<path>`; gradient
  `#22D3EE` → `#A78BFA` with a small dark core circle (`#0F172A`, r ≈ 18% of
  the star) for the "neural node" feel. Center it in a soft radial glow.
- **Stat block**: big weight-800 number in an accent color, plain label below.
- **Category chip**: glassy pill (white @ 6–8% fill, 12–16% stroke), accent
  dot, weight-600 label.
- **Badge colors** (shields.io `color=`): stars `312E81`, forks `4F46E5`,
  contributors `6366F1`, license `34D399`, last-commit `0EA5E9`.

## 5. Do / don't

- **Do** keep the spark motif consistent across logo, preview, and favicons.
- **Do** export SVGs at exact pixel dimensions (`1280×640` for the preview).
- **Don't** add photo backgrounds or raster textures to the assets.
- **Don't** introduce brand colors outside the palette above.
- **Don't** mix font families — always use the system stack.
