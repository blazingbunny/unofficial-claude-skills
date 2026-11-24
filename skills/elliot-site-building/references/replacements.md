# The parts library: what each page part can be

Used in Mission 3 (build) and whenever Elliot says "I want the header like that one". Sources: `skins/_kit/CONTRACT.md`
(what every skin must do), `docs/model/parts.md` (the part list, P1 to P22), `docs/model/skin-directions.md` (fifteen
proposed whole-page looks, SD1 to SD15), and the four skins in `skins/` (read their `parts/` and `theme.css`). When
those change, update this file. Whether a swap is a good idea is decided with `references/decision-matrix.md`; this
file records what exists and what is fixed.

## The skins today

| Folder | Name | Character | Status (Adrian, 20 Nov 2026; ask Adrian if it has moved) |
|---|---|---|---|
| `skins/ss-01` | Ledger and Bearing (A) | Split hero (text left, job photo right), sticky enquiry card beside the content, numbered contents list, Services dropdown in the header | Kept |
| `skins/serverscale` | Classic (D) | A white 64rem column on the site colour, full-width photo hero with the business name, "Skip to" box, two icon buttons in the header (other locations, menu) | Kept |
| `skins/ss-02` | Folio Press | Editorial and print-led: serif headings, square corners, thin rules and numbers (01, 02, 03), plain text navigation, a form that reads like a printed form | Rejected ("feels off, not premium") |
| `skins/ss-03` | Kerbside | Friendly and rounded: sticky call strip on phones, bottom-sheet menu, icon-led services, full-bleed photo hero with a scrim | Rejected ("not premium, wrong for the trade") |

Whether parts of a rejected skin may still be cherry-picked: ask Adrian. Each skin has its own class prefix, and the
cross-skin check fails on any shared name, so a part taken from another skin is rebuilt in the target skin's own names,
never copied across.

## Fixed rules (the contract; H23 and H24 are defaults)

**H23 and H24 are the defaults for these template sites, and Elliot's choice is the final decision.** If he asks to
break one, tell him in one sentence what it costs, then do what he decides. Do not refuse. All the other rows below
need Adrian's yes to change.

| Rule | What it says | Where |
|---|---|---|
| H23 | Every page shows a visible lead form, except Legal and NotFound. A button that opens a form does not count. Quote buttons link to `/contact`, which carries the full form. The Contact page uses the reduced shell (simple header, no footer, no quote bar). | `CLAUDE.md`, `docs/model/skin-directions.md` |
| H24 | No prices. Where one is needed the text is `(min-offer-price) to (max-offer-price)`, in body text only. No pound signs. | `CLAUDE.md`, `skills/layout-clone-versions/SKILL.md` |
| No added text | A skin renders every piece of text and every link the page data carries, in order, and adds none: no extra labels, "read more", "call now" links or titles inside inline SVG. | CONTRACT sections 1 and 2 |
| Hooks | `data-ss-nav` on the header, `data-ss-content` around the body, `data-ss-footer` on the footer, `data-ss-sent` on the thank-you message. The checks find regions only through these. | CONTRACT section 2 |
| Links | The set of links on a page equals the set the data implies. Repeating a link that is already there is fine. `tel:` is the phone with spaces removed; `mailto:` is the email as given. | CONTRACT section 2 |
| First `<h1>` | On content pages it is the hero title plus " in <location>". The skin adds none on Legal, Contact or NotFound. | CONTRACT section 2 |
| Lead form | `method="post"`, `action` from the data, one field per data field, one submit button, hidden inputs exactly as given, a hidden spam-trap field (off screen, not `display: none`), the `?sent=1` thank-you message when the data asks for it. | CONTRACT section 3 |
| Head | charset, viewport, title, description (always), canonical, robots when set, favicon, JSON-LD injected as given. `lang="en"`. | CONTRACT section 5 |
| No third parties | No CDN fonts, icon fonts or outside scripts. The only exception is Google Tag Manager, and only when the data has an id. Icons are hand-drawn inline SVG. Fonts are system fonts or at most two self-hosted `woff2` files. | CONTRACT section 5, BRIEF |
| Budgets | Stylesheet 12 KB gzipped or less. Lighthouse mobile performance 90 or higher. Hero image uses the given `src`, `srcset`, `width` and `height` (`<picture>` when `sources` is set), eager and high priority; every other image lazy. | CONTRACT sections 4 and 6, BRIEF |
| Colours | Brand colours can be low contrast: the skin derives its own text colours so every text and button reaches WCAG AA (4.5:1). | CONTRACT section 1 |
| Own names | A skin has its own Tailwind prefix, class prefix, token names and asset folder. Never reuse another skin's names. | CONTRACT section 6, BRIEF |

## The parts, and the options for each

"In repo" means a skin renders it today from the page data. "No" means a skin cannot show it until Adrian approves new
page data (the Model doc named in the last column holds the open questions). Two routes still work without new data:
write it into the page body (the body is stored HTML with headings, lists, tables and images, styled by the skin
through element selectors, CONTRACT section 4), or tell Elliot it is a decision for Adrian.

| Part | In repo | Options in the skins and the directions | Elliot-specific notes and where it is documented |
|---|---|---|---|
| P1 Header | Yes | Services dropdown plus a Menu button on phones (ss-01). Logo with two icon buttons, one for other locations and one for the menu, folding down a panel (serverscale). Plain numbered text navigation (ss-02). Call strip stuck to the top on phones with the phone number and a quote button, menu as a bottom sheet (ss-03). Proposed: utility bar with phone, hours and quote button above a main bar (SD1, SD2). Contact page: brand link and Home link only | `docs/model/parts/header.md`. Every header link sits inside `data-ss-nav`. The other-locations menu is content, keep it |
| P2 Footer | Yes | Link groups, contact details, company record, small print. Dense dark footer with address and map link (SD2), four link groups on dark ink (SD1) | `docs/model/parts/footer.md`. Every footer link inside `data-ss-footer`. None on Contact |
| P3 Quote bar | Yes | Fixed bar on small screens with a "Get a quote" link to `/contact`; ss-03 turns it into the top call strip | `docs/model/parts/quote-bar.md`. The phone number appears only where the data has one |
| P4 Announcement | No | One line above the header (emergency, hours) | Needs new data: `docs/model/parts/announcement.md` |
| P5 Hero | Yes | Split: text left, photo right (ss-01, SD1). Full-width photo with the business name (serverscale, SD2). Full-bleed photo under a scrim (ss-03). Editorial, photo used sparingly (ss-02). Proposed: photo with a quote form card on it (SD3), headline only with trust points and no photo (SD4), founding year with a yard photo (SD12), big call button on a dark hero (SD13) | `docs/model/parts/hero.md`. Text stays readable on any photo and brand colour. With no hero image the part still works. A hero that carries the form counts as the form (H23) |
| P6 Content | Yes | The page text. Headings, paragraphs, lists, tables, images; call-to-action links style as the primary button | `docs/model/parts/content.md`. Reviews, steps and FAQ can live here as plain headings and lists |
| P7 Contents list | Yes | Numbered list (ss-01, ss-02). "Skip to" box (serverscale) | `docs/model/parts/contents-list.md`. One link per body heading, ids exactly as given |
| P8 Lead form | Yes | Sticky card beside the content (ss-01). Form at the side (serverscale). Ruled-line printed-form look (ss-02). Roomy fields with a large button (ss-03). Proposed: in the hero (SD3), full width mid-page (SD4), step by step (SD7), one-row form under the hero (SD9) | `docs/model/parts/lead-form.md`. Fixed by H23 and the form contract. Easy to complete on a phone |
| P9 Gallery | Yes (photo only) | Grid of project photos. Proposed: before and after pairs, cards with captions | `docs/model/parts/gallery.md`. Captions and before photos need new data |
| P10 Coverage | Yes | "We cover <place>" line plus the other-locations menu | `docs/model/parts/coverage.md`. Extra places, groups and a map need new data |
| P11 Post cards | Yes | Blog list cards on the blog page | `docs/model/parts/post-cards.md` |
| P12 Services | No | Icon-led list (ss-03 has a Services part), ruled list (SD1), photo tiles in two sizes (SD2), machine category tiles (SD5) | A full service list needs new data: `docs/model/parts/services.md` |
| P13 Benefits | No | "Why choose us" points, with or without icons | `docs/model/parts/benefits.md` |
| P14 Trust | No | Accreditation and partner logos, short badges, short points. One row of accreditations (SD1) | `docs/model/parts/trust.md`. Placeholders only here |
| P15 Reviews | No | Two large quotes side by side (SD1), three signed quotes (SD2), review score on the hero (SD10) | `docs/model/parts/reviews.md`. Names, towns and quotes are placeholders |
| P16 Stats | No | A row of 3 to 4 facts under the hero (SD2) | `docs/model/parts/stats.md` |
| P17 Process | No | Numbered steps ("how it works") | `docs/model/parts/process.md` |
| P18 CTA band | No | Full-width call to action with phone and button, closing the page (SD2) | `docs/model/parts/cta-band.md` |
| P19 FAQ | No | Questions and answers, open and close | `docs/model/parts/faq.md` |
| P20 Contact block | Partly | Phone, email, address, hours, directions, used on the Contact page | `docs/model/parts/contact-block.md` |
| P21 About and team | No | Company story, timeline, team photos | `docs/model/parts/about-team.md` |
| P22 Pricing | Not used | Sites never show prices (H24) | If Elliot likes a pricing part on another site, take the layout idea (a table or a range line) and fill it with the literal `(min-offer-price) to (max-offer-price)` in body text |

## What Elliot tends to pick

Not known yet, and it must not be guessed here. His picks are recorded per session in `summary.md` (the cherry-pick
table and taste notes) and in Claude's memory for the folder. Read memory first. When he returns, open with what he
liked before and check whether it still holds. The part library supplies the options, his taste profile chooses.

## Cherry-pick list: how a pick becomes a build step

For each pick on Elliot's list, record: the part (P-number), the site it comes from, why he liked it (his words),
the evidence level of what Claude saw (`read`, `headings`, `blocked` or `snippet`, see `layout-clone-versions`), and
the route below. A `blocked` or `snippet` pick is a hint only, never a spec.

## Routes when a pick does not exist as a part

1. **Use the part as it is** in the skin being built. Usually the right answer.
2. **Re-style or re-arrange within the contract:** new layout, same data, same hooks, same words. Done in the skin's
   own `parts/` and `theme.css`.
3. **Bring the pick in through the body:** reviews, steps or a FAQ written as headings and lists in the page body
   (placeholder text, own sentences), styled by the skin.
4. **Adopt a proposed direction:** one of SD1 to SD15 supplies a whole-page look. Whole-page choices are Elliot's
   call; Adrian and Alden upload the result.
5. **Needs new page data** (a "No" part, extra gallery fields, an announcement line, a company record): a decision for
   Adrian. Say what Elliot would gain and what the data would cost.

Recommend one, and tell Elliot what he would notice change.
