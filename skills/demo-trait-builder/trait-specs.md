# Trait specs for the demos still missing their named trait

Source of truth: `docs/model/skin-directions.md`. Content: live Pro Construction Equipment text only, marked sample otherwise.
Built already (copy their shape): SD8 postcode hero (`Hero.astro`, `.pc*` roles, `initPostcode` in `form.js.tpl`), SD1 and SD2 sticky side form (`stickyForm` flag, `place()` in `Page.astro`), SD15 comparison (`Compare.astro`, `V-compare`).

| Demo | Trait | Flag | DOM to render | Data | DOM check |
|---|---|---|---|---|---|
| SD7 | Step by step form: step 1 (job type and timing) always visible, later steps in the same place | `stepForm` | Same `<form>` with the fields grouped in `<fieldset data-sd-step>`; Next and Back buttons; the form still posts once, by the existing script | Existing form fields grouped: step 1 first_name and last_name, step 2 postcode, step 3 email, phone, message | 3 fieldsets, only the first visible at load, the last has the submit button, form still validates |
| SD9 | Before and after hero: one job split in two labelled photos, form as one row directly under it | `beforeAfter`, `formRow` | Hero media holds two `<img>` side by side with labels Before and After; a gallery of pairs; LeadForm variant with all fields and the button in one row | Two live service photos stand in, labelled as sample pair (no live before and after exists) | Two hero images with labels, the form fields share one row at 1280, stack at 375 |
| SD11 | Two doors: Homes and Businesses panels side by side, each with photo, short list and a button that sets the customer type | `doors` | Services variant with two equal panels; the form gets a first field Customer type (Home or Business); the door button scrolls to the form and sets it | Panels' service lists split from the five live services, marked sample copy for the audience text | Two panels of equal width and height, button sets the field value |
| SD12 | Established firm: founding year large in the hero, a timeline of dated points beside the form | `founded`, `timeline` | Hero shows the year in a large `<p>`; About part becomes a `<ol>` timeline; form beside it on desktop | No founding year on the live site: render `Est. Sample year` and sample timeline points, marked sample | Year element present in the hero, timeline has 3 to 5 items, form beside it at 1280 |

Rules for every trait: one flag, one commit, content never invented, layout lint clean, trait test added.
Header settings from the config (width, radius, opacity, logo slot) and direction fonts are a separate gap and are not part of a trait.
