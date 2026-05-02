---
name: MindEase
colors:
  surface: '#faf9fa'
  surface-dim: '#dadadb'
  surface-bright: '#faf9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f5'
  surface-container: '#eeedef'
  surface-container-high: '#e9e8e9'
  surface-container-highest: '#e3e2e3'
  on-surface: '#1a1c1d'
  on-surface-variant: '#42474c'
  inverse-surface: '#2f3032'
  inverse-on-surface: '#f1f0f2'
  outline: '#73787c'
  outline-variant: '#c2c7cc'
  surface-tint: '#466274'
  primary: '#466274'
  on-primary: '#ffffff'
  primary-container: '#a8c5da'
  on-primary-container: '#365264'
  inverse-primary: '#adcadf'
  secondary: '#376380'
  on-secondary: '#ffffff'
  secondary-container: '#b1ddff'
  on-secondary-container: '#36627f'
  tertiary: '#5a5f63'
  on-tertiary: '#ffffff'
  tertiary-container: '#bdc2c7'
  on-tertiary-container: '#4b5054'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6fc'
  primary-fixed-dim: '#adcadf'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#2e4a5b'
  secondary-fixed: '#c9e6ff'
  secondary-fixed-dim: '#a0cced'
  on-secondary-fixed: '#001e2f'
  on-secondary-fixed-variant: '#1b4b67'
  tertiary-fixed: '#dfe3e8'
  tertiary-fixed-dim: '#c3c7cc'
  on-tertiary-fixed: '#171c20'
  on-tertiary-fixed-variant: '#42474b'
  background: '#faf9fa'
  on-background: '#1a1c1d'
  surface-variant: '#e3e2e3'
typography:
  h1:
    fontFamily: Times New Roman
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Times New Roman
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  h3:
    fontFamily: Times New Roman
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
---

## Brand & Style
The design system is anchored in a disciplined minimalism that prioritizes mental clarity and professional reliability. It avoids all forms of skeuomorphism, depth simulation, and complex textures to eliminate visual noise, creating a "flat-first" environment. The aesthetic is defined by large areas of negative space, crisp structural lines, and a deliberate absence of decorative trends like glassmorphism or prismatic effects. The emotional response is one of immediate calm, achieved through a restricted palette and high-legibility typography.

## Colors
The palette is architectural and cool-toned. **Sky Blue** serves as the primary brand touchstone, used for emphasis and key interactions. **Deepwater** provides a grounding secondary tone for active states and secondary UI elements. **Mist** acts as the primary container background to differentiate surfaces from the **White** base without using shadows. **Ink** is reserved strictly for high-contrast text and structural borders, ensuring maximum readability and professional rigor.

## Typography
This design system employs a sophisticated typographic contrast between classic serif and modern sans-serif faces. **Times New Roman** is used for all headlines and brand markers to evoke an editorial, authoritative, and intellectual mood. **Inter** handles all functional UI elements, labels, and body text to ensure clarity and a systematic feel. 

- Use serif headings to establish narrative flow and "calm" focal points.
- Use sans-serif for interactive elements and data-heavy blocks.
- Maintain generous line-heights to support the minimalist layout.

## Layout & Spacing
The layout follows a strict 45/55 split for presentation views. This asymmetrical balance allows for a clear hierarchy between high-level brand messaging (left) and functional UI interaction (right). 

- **Left Column (45%):** Uses **Mist** or **Sky Blue** backgrounds to frame primary headings.
- **Right Column (55%):** Uses **White** backgrounds for core content and interactive components.
- The system follows an 8px grid. Margins and gutters should remain consistent to uphold the professional, systematic appearance.

## Elevation & Depth
Depth is conveyed exclusively through **Tonal Layering** and **Low-Contrast Outlines**. 
- No shadows or blurs are permitted. 
- Elements are "raised" by changing the background color (e.g., a **Mist** card on a **White** background).
- Boundaries are defined by 1px solid strokes in **Ink** (at 10-15% opacity) or **Deepwater**. 
- This approach ensures the UI remains purely flat while maintaining a clear information hierarchy.

## Shapes
The shape language is a mix of geometric precision and organic softness. 
- **Buttons:** Use a full pill shape (999px) to provide a soft, approachable counterpoint to the rigid grid.
- **Badges:** Use small rounded squares (4px radius) for annotations to maintain a structured, professional look.
- **Containers/Cards:** Utilize a standard 0.5rem (8px) radius for a "Soft" finish that remains grounded.

## Components
Consistent application of components reinforces the serene mood:

- **Buttons:** Rounded pill-shaped with solid **Deepwater** or **Sky Blue** backgrounds. Text inside is **White** or **Ink** depending on contrast. No borders on solid buttons.
- **Badges:** Small rounded squares in **Mist** with **Ink** text for subtle annotations.
- **Input Fields:** Flat **White** rectangles with a 1px **Ink** (15% opacity) border. Focus states use a solid 2px **Sky Blue** border.
- **Chips/Selection:** Small pill shapes with a 1px stroke for unselected states and solid **Sky Blue** for active states.
- **Lists:** Clean rows separated by 1px **Mist** dividers, with generous vertical padding (16px+).
- **Cards:** Flat containers using **Mist** backgrounds to sit subtly against the **White** canvas.