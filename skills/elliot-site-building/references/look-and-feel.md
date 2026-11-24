# Look and feel check (priority 3 of the decision matrix)

Read this when you check a built page or a part change, or when Elliot asks whether something "looks right", is
readable, or is spaced evenly. It is the "looks and feels" line of `decision-matrix.md`, checked on the real page.
The gates and quality bar come first (`skins/QUALITY_BAR.md`, `scripts/GATES.md`), then accessibility and phone,
then this. Page speed and rankings are not part of this check.

The rules below are hand-edited from the *impeccable* design skill's typography, layout, audit and polish guides
(MIT licence), cut down to what matters for Astro template pages. Only the guidance is borrowed: do not run
impeccable's own detector or tools on these pages unless Adrian approves it.

## The reference

- What Elliot picked: the sites and parts he pointed at in the taste interview. A part built from his choice should
  look and feel like what he chose, not like a generic version.
- Neighbours: the other parts on the same page, and the same part on the other pages of the site.
- Polish is refinement, not a hidden redesign. Keep the chosen fonts, colors and spacing; change only what was asked.

## When and how

1. For every built page or part change, at **desktop width (1280px)** and **phone width** (`resize_window` mobile
   preset; reset with the desktop preset afterwards). If the panel cannot get narrower than about 550px, say the
   phone check was at that width.
2. **Measure** with `scripts/look-check.js`: paste the file into the browser's JavaScript tool, with `SCOPE` set to
   the part's parent box (for example `'#main'`, or `'.vk-panel'` for one part in the ss-01 skin) so the
   neighbours are included. It reads the page and changes nothing. The header and footer are skipped. If a sticky
   header covers the page in a narrow panel, hide it for the check only.
3. **Look** at screenshots of the part and what is around it, at both widths, against the list below.
4. **Tell Elliot in one line**, then details only if something is off: "Looks: same spacing as the sections
   around it; text 19px on computer and 16px on phone; nothing scrolls sideways."

## What the script measures

| What | Good | Why |
|---|---|---|
| Body text size | 16px or more (headings may be larger, never smaller than body) | smaller is hard to read on a phone |
| Line height | 1.4 × the text size or more for body text | tight lines are hard to follow |
| Line length | about 45 to 75 characters per line | long lines lose the reader's place |
| Contrast | 4.5:1, or 3:1 for large text (24px, or 19px bold) | WCAG AA; pale text on white fails it |
| Touch targets | 24px or more (WCAG AA); 44px is comfortable on a phone. Links inside a sentence are exempt | small buttons get missed |
| Sideways scroll | none at phone width | content wider than the screen |
| Gaps between blocks | equal between blocks of the same kind | uneven spacing looks unfinished |

The script cannot measure text over a background image (it skips it): check that contrast by eye. Axe-core in the
gates covers accessibility properly; this script is the quick look while building.

## What to look at

**Hierarchy (the squint test).** With the detail blurred, you can still tell the most important thing, the next,
and the groups, in the right order. Headings, body text, labels and small print are recognisable without reading
them. Two sizes or weights that are almost the same cannot carry different jobs.

**Matches its neighbours.** Text in the same role (all section headings, all body paragraphs, all buttons) uses the
same font, size, weight, color and spacing across the page. One heading in a different font while the others stay
is a mismatch: say so and offer to change them all. Use the skin's theme values (`theme.css` variables and the
fonts and colors it defines), not one-off values.

**Grouping and rhythm.** Related things sit close; separate groups have more space between them. Spacing follows the
skin's existing steps rather than new one-off values. One spacing value repeated everywhere makes everything look
equally important; a deliberate mix of tight and generous gaps reads better, but match what the skin already does.

**Lines and wrapping.** At both widths: no text cut off or overlapping, no heading that wraps with one lonely word on
its last line (a short last line of body text is fine), nothing pushed off the side of the screen. Long words, long
headings and buttons with long labels are where it breaks first. Template text is placeholder text, so try a long
placeholder business name or town name too.

**Images.** Right shape (not stretched or squashed), no jump in the layout as they load, alt text kept.

**Behaviour ("feels").** Links and buttons go where they should. Hover and keyboard focus show (press Tab through
the part). The enquiry form is on the page and its fields are easy to tap. Menus, accordions and tabs open and
close. Nothing animates unless Elliot asked for it.

**Phone.** Content reflows rather than shrinking; tap targets are big enough and not crowded together; nothing
needs sideways scrolling; a sticky header or the quote bar does not cover the content.

## What to do with a finding

- **Breaks reading or use** (overlap, sideways scroll, unreadable on a phone, a control that does not work): fix it
  before the build counts as done.
- **A mismatch** (spacing, size, font or color differs from the neighbours): show it, offer the fix, and let
  Elliot decide.
- **Does not match what Elliot picked** (he pointed at a tight, dense header and the build is airy): say what
  differs, show both, and ask which he wants.
- **Comes from the skin itself** (for example a skin color that measures 2.4:1 on its background): report it
  separately as "in the skin, not caused by this change", for Adrian. Do not fix it in passing: it is a skin-wide
  color or font.

Verify with what you measured or saw, not with a bare "looks fine". A clean script result is the floor, not proof the
design is good.
