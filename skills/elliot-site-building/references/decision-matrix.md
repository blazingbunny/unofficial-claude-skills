# Decision matrix: should we make this change, and what could it cost?

The source of truth for every "is this a good idea?" question Elliot asks, and for every decision about taking a part
from one place and putting it in another. It rests on the rules in `skins/_kit/CONTRACT.md`, `skins/QUALITY_BAR.md`,
`scripts/GATES.md` and the hard rules H23 and H24 (`CLAUDE.md`). When those change, update this file.

Use it **before** offering or making a change, and put its result in the risk explanation in plain words. No change
that touches a rule below is ever made silently.

**H23 and H24 are the defaults for these template sites, and Elliot's choice is the final decision.** They are the
form on every page that has one (H23) and no prices, no pound signs (H24). If Elliot asks to break one, tell him in
one sentence what it costs, then do what he decides. Do not refuse. Note his decision in `summary.md`. Every other
"must keep" rule below still needs Adrian's yes.

## How to use it with Elliot

Elliot decides what his site looks like; you advise. He is not technical, so you do the analysis and give him a clear
recommendation with the trade-off in one or two sentences. Never make him read the tables.

**1. Before you answer "can you change X?", work it out silently:**
- What does he actually want (the visible result), and which part is it (point or ask: header, hero, form, and so on,
  see `references/replacements.md`)?
- Which rules does that part carry (G1)? Look at the built page in the browser panel and in its HTML: the `data-ss-*`
  hooks, heading tags, links, image `alt`, the form's fields, the head, the contents list ids.
- Which routes are possible? Usually: (a) change it within the skin (same data, same words), (b) take the part from
  another skin or a reference site and rebuild it in the target skin's own names, (c) don't do it, or ask Adrian.
- Run G2 for each route. Score close calls with G2a.

**2. Tell him in this order, in plain words:**
1. **What you recommend, in one sentence.** "I recommend a split hero with the photo on the right, like the second
   site you pointed at."
2. **The checks first**, always, even when nothing changes: "The form and the links stay exactly the same, so the
   automatic checks still pass." If a rule would be touched, say which, in his terms: "this would add a line of text
   that isn't in the page data, and the checks fail any page with extra text".
3. **Phone and accessibility next**: "On a phone the button stays big enough to tap, and the text stays readable."
4. **The benefit**: what he gains (it looks the way he asked, the form is easier to find, it is faster).
5. **The cost or risk**: what changes or could break (spacing shifts, a second page type needs the same treatment),
   and the risk level (low, medium or high, below).
6. **Reversing it**: he can ask for the change to be reversed by rebuilding or editing it back, and a folder already
   saved to Drive is never overwritten (a new version is a new folder). Say this in one line, never promise more.
7. **The question**: "Keep it as it is, or go ahead?" Then wait.

**3. Match the strength of your advice to the result:**
- **Clear yes** (rules kept, positive score): recommend it plainly.
- **Clear no** (a must-keep rule lost with no way to keep it, or a negative score): recommend against it, say why in
  one sentence, and offer the alternative that gets him most of what he wants.
- **Close call** (G2a within plus or minus 2, or the answer flips): say it is a close call, give both sides in one line
  each, and ask Elliot to decide: it is his design.
- **Must-keep at risk or high risk** (other than H23 and H24, see the top of this file): don't offer to do it.
  Explain, and point him to Adrian.

If he still wants something you advised against, and it is not a must-keep or high-risk case, it is his call: restate
the cost once, get an explicit yes, and do it. Note the decision in `summary.md`.

**Examples**
- *"Put the quote button in the header too."* The Contact link already exists in the page data, and repeating a link
  that is already there is allowed. Clear yes, low risk: "It is the same link in a second place."
- *"Add a green 'Call now' button to the footer."* The page has no such link in its data, and the checks fail any page
  with a link the data does not imply. Recommend against: offer a bigger phone link built from the data that is
  already there, or ask Adrian whether the page data should carry it.
- *"Show the price on the cards like that site does."* H24 is the default: no prices. Offer the placeholder wording
  `(min-offer-price) to (max-offer-price)` in the body text. If he still wants an exact price, say once what it costs
  (an exact price on a template goes stale and every client's price differs), then do it his way.
- *"Remove the form from the home page, it looks cleaner."* H23 is the default: a visible form on every page except
  Legal and NotFound. Say what it costs (this page can no longer turn a visitor into an enquiry) and offer a quieter
  form layout instead (a one-row form, or a form lower on the page). If he still wants it gone, do it.
- *"Change the menu."* The header is on every page and holds the site's main links: high risk for a site-wide change.
  Preview the new look in the panel first and explain what moves.

## Order of priorities

1. **The gates and the quality bar pass.** Always first. A pick that fails a gate or a quality rule does not ship.
2. **Accessibility and the phone view.** AA contrast, keyboard and focus, tap targets, nothing overflowing at 375 px.
3. **It looks and feels like what Elliot picked.** "Feels" covers behaviour too: hover, menu opening, sticky bars,
   scroll. Where his picks conflict with 1 or 2, find the nearest version that passes and say what changed.

A redesign Elliot asks for (new layout, new part) is a design decision, not a rule violation, as long as every
part that stays keeps its rules.

## G1. The rules a part carries, by weight

| Weight | Signals | Rule |
|---|---|---|
| **Must keep** | the `data-ss-nav`, `data-ss-content`, `data-ss-footer`, `data-ss-sent` hooks; every link and every piece of text the page data carries, in order, and none added; `tel:` and `mailto:` exactly as given; the first `<h1>` rule; the lead form contract (method, action, field names, hidden inputs, hidden spam-trap field, thank-you message); the head (title, description, canonical, robots, JSON-LD as given); `lang="en"`; H23 (form on every page but Legal and NotFound); H24 (no prices, no pound signs); no third-party hosts; the skin's own class, token and file names (no overlap with another skin) | Never change without Adrian's yes. Tell Elliot, stop, and point him to Adrian. The exception is H23 and H24: they are defaults, and Elliot's choice is final (see the top of this file). |
| **Keep if possible** | contents list links and the heading ids they point to; `<picture>` sources, `width` and `height` on images; image `alt` text; lists stay lists, tables stay tables; the skip link; the stylesheet size; the Lighthouse score | Keep it, or tell Elliot exactly what changes and get his yes. |
| **No rule weight** | decorative shapes, spacing, dividers, wrappers, hover motion, corner radius (while consistent) | Change freely (still preview first, and still subject to QB1 to QB5). |

## G2. The matrix (one question per step; stop at the first that applies)

1. **Does the page type exist?** The ten page types are Home, Service, County, Town, HomeCounty, Post, Legal, BlogIndex,
   Contact and NotFound. A request for a page type that does not exist (a shop, a login, a pricing page) is out of
   scope: tell him, and offer the nearest part inside an existing page.
2. **Does the change lose a must-keep rule?**
   - Yes, but a different arrangement keeps it (for example the form in the hero instead of beside the content, the
     phone link built from the data already there) → offer that rebuild and prove nothing was lost (compare the
     built HTML before and after, `scripts/seoscan.py diff`).
   - Yes, and nothing keeps it → don't do it. Tell him why in one sentence, and point him to Adrian if he still wants
     it. (If the rule is H23 or H24, tell him the cost in one sentence and do what Elliot decides.)
3. **Would anything visible, functional or "keep if possible" change?** → score it with G2a. Decide when the answer is
   clear. When it is a close call, say so and ask Elliot to decide.
4. **Otherwise** → go ahead (preview, risk explanation, yes, build, checks).

## G2a. Scoring a close call

1. **Musts (pass/fail; an option that fails one is out):** every must-keep rule in G1 holds; function intact (the
   form submits, the menu opens by keyboard); accessibility not worse (contrast AA, focus visible, labels, landmarks,
   skip link); the page text is still the page data's text.
2. **Wants, scored -1 / 0 / +1 against keeping the part as it is now (baseline 0):**

   | Want | Weight | What it covers |
   |---|---|---|
   | Visitor on a phone | **5** | how the part works at 375 px: what they can reach, tap size, thumb reach, the phone number and form without scrolling |
   | Matches Elliot's pick | **4** | how closely it looks and feels like what he pointed at and said |
   | Quality bar | **3** | QB1 to QB5: human-made look, hierarchy, meaning in every decoration, consistency, fits the trade |
   | Page speed | **3** | Lighthouse mobile, layout shift, stylesheet weight, scripts added |
   | Cost | **2** | effort, a new mechanism or dependency, reversibility, how much of the shared code it touches |

3. **Total = sum of weight x score.** Positive → recommend it. Zero or negative → recommend keeping what is there.
4. **Close call:** if swapping two neighbouring weights flips the answer, or the total is within plus or minus 2 →
   say so and ask Elliot to decide.
5. **Risk check:** can it be reversed by editing or rebuilding, and does it need a change outside this site's skin?

Tell Elliot the result in plain words, not the table: "This keeps the form and the links the same and makes the header
feel like the site you liked. The only change is that the menu opens from the bottom on a phone. I recommend it."
Show the table only if he asks.

## G3. Facts that shape decisions now

- **Skins add no text.** Everything shown comes from the page data. A part that needs new words or numbers (reviews,
  stats, announcement, extra gallery captions) is not a skin change. It is either body content (placeholder text,
  our own sentences) or a decision for Adrian about new page data.
- **A copied layout is not a copied site.** Take layout, look and phrasing patterns from the sites Elliot likes. Write
  our own sentences. A page that blocks the browser panel (bot check, 403, captcha) is a stop, never a hurdle.
- **Names must not overlap.** Gate 4 fails any class, custom property, file name or asset folder shared between skins.
  A part taken from another skin is rebuilt in the target skin's own names.
- **Which checks run on Elliot's laptop:** the accessibility check (gate 5) needs Chrome installed. Lighthouse (gate 6)
  runs only on lobster, not on a laptop. Gate 3 is for the orchestrator. Whether Elliot's project folder has the
  repo's scripts and the build command: look in the folder (`scripts/`, `harness/`); if they are missing, tell Adrian
  the starting files are incomplete. List in `summary.md` every check that could not run, never write
  "passed" for one that did not run.
- **The practice and demo sites are noindex** (the layout-clone-versions deploy writes `_headers` and `robots.txt` for
  that). Nothing Elliot builds goes online by itself: Adrian or Alden upload it.
- **How to check:** look at the built page (HTML in the browser panel), not only the settings. Pages with lazy images
  look blank in a full-page screenshot until scrolled.

## Checking tools (measure, don't eyeball)

| Tool | Use it for | Here |
|---|---|---|
| **`seoscan.py`** (ours, Python standard library only) | every SEO and structure signal on a built page, tagged by the page part that produced it; `diff` before vs after | bundled: `<skill dir>/scripts/seoscan.py` |
| **`look-check.js`** (ours, read-only) | measured text size, line height, contrast, spacing and phone overflow in the browser panel | bundled: `<skill dir>/scripts/look-check.js` |
| **The gates** (`scripts/GATES.md`) | link and text parity, accessibility, cross-skin names, Lighthouse, quality bar screenshots | only where the repo and Chrome are present, see G3 |
| **`modern-web-guidance`** | guides before building, `legacy-scan` after (the lint step) | see `SKILL.md` |

**For a change that touches a built page, use `seoscan.py` before and after:**
1. **Before** anything changes, save the built page's HTML (from the site folder, or from the browser panel) to a
   scratch file such as `before.html`.
2. `python3 -I seoscan.py scan before.html` lists the page's signals: headings, links (`rel`, `target`), images
   (`alt`), ids, lists, the head. Use it to fill in G1 for the part.
3. **After** the change, save the page again as `after.html`, then run `python3 -I seoscan.py diff before.html
   after.html`.
   - **Exit code 0** means no difference.
   - Otherwise every line is a difference. Each one must be a change Elliot already accepted. Anything else is a
     failure: tell him and offer to fix it or edit it back.
4. Say the result in the change note: "Structure check: no differences" or "Structure check: one accepted change (...)".

Notes:
- Run it with `python3 -I` from the scratch folder, never from inside a downloaded folder. If `python3` is not
  installed, read the same signals in the browser panel with JavaScript (headings, links, image `alt`, the form's
  fields, hidden inputs, ids, JSON-LD) and compare by hand. Say the bundled check could not run.
- Report what was already there separately from what the change did, so the change is not blamed for it.
- A change across the whole site (header, footer, global colours or fonts) needs the diff on the home page and on one
  inner page of each type that uses the part.

## Look and feel check (priority 2 and 3)

After the structure check, check that the change looks, reads and behaves right at desktop and phone width: readable
text size, line height and contrast, even spacing, matching its neighbours, nothing broken on a phone, links and the
form still working. The checklist, thresholds and what to do with each finding are in `references/look-and-feel.md`
(with `scripts/look-check.js` to measure). Read it before the check.

## Risk level for the risk explanation

- Rate the change **as if it were on a real client site**, so Elliot learns the real stakes even though everything
  here is a template.
- **Low:** no must-keep or keep-if-possible rule touched, look and behaviour the same or only decorative, one part on
  one page type.
- **Medium:** a keep-if-possible rule or the look changes, a part is rebuilt from another skin or a reference site,
  the same part changes on several page types, or a new script is added (menu, sticky bar).
- **High:** a must-keep rule, anything site-wide that every page shares (header, footer, menu, colours, fonts, the
  form), new page data, a new third-party host, a new dependency, or anything outside this site's skin and content.
  High means stop and point him to Adrian unless Adrian has already approved it.
