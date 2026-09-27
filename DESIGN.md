---
name: Mindful Discipline & Cadence
colors:
  surface: '#f9f9ff'
  surface-dim: '#d3daef'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f3ff'
  surface-container: '#e9edff'
  surface-container-high: '#e1e8fd'
  surface-container-highest: '#dce2f7'
  on-surface: '#141b2b'
  on-surface-variant: '#424847'
  inverse-surface: '#293040'
  inverse-on-surface: '#edf0ff'
  outline: '#727877'
  outline-variant: '#c2c8c6'
  surface-tint: '#4e625f'
  primary: '#051917'
  on-primary: '#ffffff'
  primary-container: '#1a2e2b'
  on-primary-container: '#809692'
  inverse-primary: '#b5cbc6'
  secondary: '#006c4a'
  on-secondary: '#ffffff'
  secondary-container: '#82f5c1'
  on-secondary-container: '#00714e'
  tertiary: '#261000'
  on-tertiary: '#ffffff'
  tertiary-container: '#442100'
  on-tertiary-container: '#da7808'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e7e2'
  primary-fixed-dim: '#b5cbc6'
  on-primary-fixed: '#0a1f1c'
  on-primary-fixed-variant: '#364b47'
  secondary-fixed: '#85f8c4'
  secondary-fixed-dim: '#68dba9'
  on-secondary-fixed: '#002114'
  on-secondary-fixed-variant: '#005137'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#f9f9ff'
  on-background: '#141b2b'
  surface-variant: '#dce2f7'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.025em
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 21px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.04em
  stat-counter:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  margin: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

The design system embodies the philosophy of steady, continuous momentum: calm discipline, mindful reflection, and quiet mastery over daily routines. It deliberately rejects the hyper-stimulating, neon-fueled aggressive energy of commercial workout apps, as well as the cold clinical feel of health dashboards. Instead, it positions the interface as a personal daily sanctuary—grounded, architectural, and tactile.

The visual style merges Warm Minimalism with Organic Softness. Generous breathing room, precise editorial typography, and muted earth-mineral accents create an aura of clarity and serenity. The experience focuses attention on meaningful progression and daily completion without instilling guilt or cognitive overload.

## Colors

The palette draws directly from quiet natural sanctuaries—porcelain stone, deep alpine juniper, vibrant spring moss, and warm amber resin:

- **Canvas & Surface Tiering**: The core base is a warm porcelain cream (`#FAF9F6`), transitioning to crisp floating card surfaces in pure white (`#FFFFFF`). Borders are feather-light and tactile using fine mist gray (`#EAECEF`).
- **Primary Anchor (`#1A2E2B`)**: Deep botanical slate-forest. Used for primary actions, header emphasis, active progress meters, and key structural framing. It grounds the UI with quiet authority.
- **Secondary & Achievement (`#059669`)**: Fresh, vibrant mint-emerald. Reserved for positive reinforcement, completed streaks, successful check-ins, and target achievements.
- **Tertiary & Context (`#D97706`)**: Warm sunlit ochre. Accents rest days, active reflection prompts, missed habits under grace periods, and important personal notations.
- **Neutral Typography**: Deep obsidian (`#111827`) provides decisive legibility for primary headings, deep slate (`#4B5563`) supports body copy and descriptions, while cool stone (`#9CA3AF`) frames metadata, timestamps, and metric units.

## Typography

Plus Jakarta Sans brings a contemporary geometric structure softened by organic curve terminals, evoking both disciplined precision and friendly human warmth.

- Numerical data, repetition tallies, streak counters, and duration timers must enable tabular figures (`font-variant-numeric: tabular-nums;`) to prevent layout shifts during live tracking or scrolling.
- Display scale is applied to morning greetings, daily affirmations, and milestone achievements.
- Labels and timestamps use deliberate tracking (0.01em to 0.04em) to maintain crisp optical separation at tiny scales on mobile OLED viewports.

## Layout & Spacing

The layout philosophy follows a rhythm-first mobile-optimized fluid grid built on an 8px vertical baseline and 4px micro-increment grid:

- **Mobile Viewports (<640px)**: 4 fluid columns, 16px gutters, and 20px screen margins. Content groups prioritize vertical scanning with finger-friendly card modules.
- **Tablet / Expanded Viewports (>=640px)**: 8 fluid columns, 20px gutters, max-width bounded to 680px for single-column journals or 840px for split calendar-and-detail views, preserving intimate diary ergonomics.
- **Rhythm Anchors**: Spacing tokens (`space-xs` through `space-xl`) define exact paddings within card containers and separation between habit rows, keeping visual clutter low while preventing accidental taps.

## Elevation & Depth

This design system avoids harsh drop shadows and artificial neon glows in favor of soft ambient diffuse daylighting paired with hairline borders:

- **Base Canvas**: Flat `#FAF9F6`, non-elevated.
- **Tier 1 (Surface Cards & Daily Rows)**: Solid `#FFFFFF`, bordered by 1px solid `#EAECEF`, with an ambient diffused shadow: `0 2px 8px -2px rgba(26, 46, 43, 0.04), 0 8px 24px -4px rgba(26, 46, 43, 0.06)`.
- **Tier 2 (Floating Action Triggers & Overlays)**: `0 12px 32px -6px rgba(26, 46, 43, 0.12)`.
- **Tier 3 (Bottom Sheets & Modals)**: Backed by a soft backdrop blur (`backdrop-filter: blur(12px); background-color: rgba(26, 46, 43, 0.25)`), using an elevated card structure with an edge-lit top boundary (`0 -1px 0 rgba(255, 255, 255, 0.8)`).

## Shapes

The interface embraces generous, organic contours that feel smooth and tactile in the palm:

- Standard input fields, cards, and modal sheets leverage generous corner rounding (16px to 24px).
- Streak indicators, habit check pills, and action chips adopt full circular capsule radii (`9999px`) to invite thumb interactions and evoke pebble-like physical tokens.
- Interactive tap surfaces must maintain a minimum physical bounding box of 48px × 48px, even when visually rendering as smaller pills or icons.

## Components

### Buttons
- **Primary**: Deep botanical slate (`#1A2E2B`) with crisp white text (`#FFFFFF`), 48px height, 16px corner radius, font weight 600. Subtle compression scale (`scale(0.98)`) on active touch.
- **Secondary**: Pure white background (`#FFFFFF`), 1px outline in `#EAECEF`, obsidian text (`#111827`).
- **Ghost/Tertiary**: Transparent background, text colored with `#1A2E2B` or `#059669`, with `space-sm` horizontal padding.

### Goal & Habit Cards
- Pure white container (`#FFFFFF`), 20px corner radius, hairline `#EAECEF` border, 16px internal padding.
- Left side: Pill-shaped status indicator or circular completion ring.
- Center: Bold habit title (`headline-md`) over small frequency descriptor (`label-sm`).
- Right side: Dynamic counter (e.g., "12/20 min" or "Streak: 14d") rendered in tabular figures.

### Checkboxes & Habit Completion Triggers
- 32px circular tap target enclosing a 24px interactive ring.
- Incomplete: 2px border in `#D1D5DB`, interior `#FFFFFF`.
- Completed: Smooth transition to emerald green (`#059669`) fill with a crisp white checkmark icon, accompanied by a soft haptic-style scale ping.

### Calendar & Rhythm Strip
- Horizontal swipeable 7-day strip showcasing current cadence.
- Day nodes: 44px × 64px rounded pills. Active selected day is filled with `#1A2E2B` with white typography; completed days show an accent dot in `#059669`; rest/grace days show an accent dot in `#D97706`.

### Chips & Metrics
- Full capsule pills (`9999px`), 32px height, 12px horizontal padding.
- Inactive state: `#F3F4F6` background, `#4B5563` text.
- Active filter state: `#E6F4EA` background, `#059669` text with bold font weight.

### Modal Sheets
- Bottom-sheet presentation with 28px top-left and top-right radii.
- Centered drag handle (36px width, 4px height, `#D1D5DB`, rounded-full) placed 12px from the top rim.
- Used for mindful reflection inputs, journaling notes, and routine configuration.