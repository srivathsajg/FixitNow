# Design System Strategy: The Digital Concierge

## 1. Overview & Creative North Star
The North Star for this design system is **"The Digital Concierge."** 

In the high-stakes world of emergency home services, the UI must act as a calm, authoritative guide. We move beyond the "utilitarian grid" of standard service apps to create an experience that feels editorial and curated. This is achieved through **Soft Minimalism**: a philosophy that prioritizes breathing room, intentional asymmetry, and tonal depth over rigid lines and cluttered interfaces. 

By overlapping elements—such as a service card subtly breaking the plane of a hero section—we create a sense of movement and modernity. We don't just "list" services; we present them as premium solutions, using high-contrast typography and sophisticated layering to build immediate trust and urgency without causing panic.

---

## 2. Colors & Surface Philosophy
This system utilizes a Material 3-inspired tonal palette to ensure the "Electric Blue" feels sophisticated rather than "default."

### The "No-Line" Rule
**Borders are prohibited for sectioning.** 1px solid lines create visual "noise" that cheapens a premium brand. Instead, boundaries are defined by background shifts. To separate a hero section from a service list, transition from `surface` to `surface-container-low`. 

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of premium materials.
- **Base Layer:** `surface` (#f7f9fb)
- **Secondary Sectioning:** `surface-container-low` (#f2f4f6)
- **Primary Action Cards:** `surface-container-lowest` (#ffffff)
- **Nested Detail Elements:** Use `surface-container` (#eceef0) inside a white card to define sub-information (e.g., pricing breakdowns).

### The "Glass & Gradient" Rule
To elevate the "Startup-Grade" vibe, use **Glassmorphism** for floating headers or sticky "Book Now" bars. Use `surface-container-lowest` at 80% opacity with a 20px backdrop blur. 
- **Signature Texture:** Apply a subtle linear gradient from `primary` (#004ac6) to `primary_container` (#2563eb) for high-conversion CTAs. This creates a "glow" effect that flat hex codes cannot replicate.

---

## 3. Typography
We use a dual-typeface system to balance editorial elegance with functional clarity.

*   **Headlines (Manrope):** Our "voice." The wide apertures and geometric forms of Manrope convey a modern, urban authority.
*   **Functional Text (Inter):** Our "engine." Inter handles the heavy lifting of service descriptions and technical data with maximum legibility.

### The Scale
- **Display-LG (3.5rem):** Reserved for hero value propositions.
- **Headline-SM (1.5rem):** Used for service categories. High weight (Bold) to establish a clear entry point.
- **Title-MD (1.125rem):** The "Sub-header" for card titles.
- **Body-MD (0.875rem):** The standard for all service descriptions.
- **Label-SM (0.6875rem):** Used for "Urgent" or "Verified" badges in All-Caps with 5% letter spacing.

---

## 4. Elevation & Depth
We eschew traditional "Drop Shadows" in favor of **Tonal Layering** and **Ambient Light.**

- **The Layering Principle:** Place a `surface-container-lowest` (pure white) card on top of a `surface-container-low` background. The contrast alone provides enough "lift" for a premium feel.
- **Ambient Shadows:** For floating elements (e.g., a "Current Request" tracker), use a shadow with a 32px blur, 0px offset, and 4% opacity using a tinted `on-surface` color. It should feel like a soft glow, not a dark smudge.
- **The "Ghost Border" Fallback:** If a border is required for accessibility on form inputs, use `outline_variant` at **15% opacity**. 
- **Glassmorphism:** Use `surface-tint` sparingly in the background of glass layers to give the "frosted" effect a hint of the brand’s Electric Blue.

---

## 5. Components

### Buttons (High-Conversion)
*   **Primary:** Linear gradient (`primary` to `primary_container`), `xl` (1.5rem) corner radius. No border. Text is `on_primary`.
*   **Secondary:** `surface-container-highest` background with `on_surface` text. Used for "Cancel" or "View Later."
*   **Tertiary:** No background. `primary` text weight 600. Used for "See all."

### Cards (The "Service Block")
*   **Style:** `surface-container-lowest` (White) background, `xl` corner radius.
*   **Restriction:** **Zero dividers.** Separate header from body using 16px of vertical whitespace or a `surface-container-low` inset for the footer area.

### Input Fields (Trust & Clarity)
*   **Style:** `surface-container-low` background. 
*   **State:** On focus, transition background to `surface-container-lowest` and apply a 2px `primary` "Ghost Border" at 30% opacity.

### Emergency Chips
*   **Urgent State:** Background `tertiary_container` (#bc4800) with `on_tertiary_container` text. This "Gold/Amber" tone signals urgency without the "Stop" signal of red.

---

## 6. Do's and Don'ts

### Do
*   **Do** use 24px padding (`xl` scale) for all major container gutters to ensure an "expensive" feel.
*   **Do** overlap images of service professionals over container edges to create a 3D, high-end editorial look.
*   **Do** use `secondary_container` (#fed01b) sparingly to highlight "Premium" or "Gold" member features.

### Don't
*   **Don't** use 100% black (#000000). Always use `on_surface` (#191c1e) for text to maintain a soft, modern contrast.
*   **Don't** use standard `md` (8px) corners for primary cards. Stick to `xl` (24px) to emphasize the "Soft" in Soft Minimalism.
*   **Don't** use dividers to separate list items. Increase the `surface_container_low` padding between items instead.