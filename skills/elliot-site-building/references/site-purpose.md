# What Elliot's sites are for (read at the start of every session)

These are lead-generation template sites for UK trade and service businesses, built as Astro skins in the `static-sites`
repo. Use this to judge every suggestion and change: **does it help a visitor decide quickly that this business can do
the job, and then phone or fill in the form?** Facts below come from `skins/_kit/BRIEF.md`, `skins/_kit/CONTRACT.md`,
`skins/QUALITY_BAR.md`, `CLAUDE.md`, `docs/model/skin-directions.md` and `elliot-guide.md` (as of 24 Nov 2026). Where a
fact is not in those files it says "ask Adrian". Do not fill a gap with a guess.

## The goal

**Bring enquiries.** A visitor lands from a search result, decides within seconds whether this business can do the
job, and phones or fills in the form. The lead form is the main action of every page. One skin has to carry many
sites, each with its own brand colours, logo, services and locations, so a design that only works for one trade is
not good enough.

## What the sites are

- **Trades covered by the brief:** training providers, survey firms, equipment hire, resin driveway installers, vehicle
  tracking, gas detector hire "and similar" (`skins/_kit/BRIEF.md`). Plant hire is the trade of the practice site
  https://hiremilo.co.uk/ (its images are the only trade images in the repo).
- **Templates only.** Names, phone numbers, addresses, photos, reviews and logos are placeholders. Prices are never shown:
  where one is needed the text is `(min-offer-price) to (max-offer-price)` and it sits in body text only (rule H24: no
  price field, no pound signs).
- **Built from parts.** Every page is an ordered list of parts (header, hero, body text, contents list, lead form,
  coverage line, footer, quote bar, and others). The part list is in `references/replacements.md`.
- **Page types:** Home, Service, County, Town, HomeCounty, Post, Legal, BlogIndex, Contact and NotFound. Service and
  location pages are the entry points: visitors find the service, then the place.
- **Who the finished sites belong to, who the end clients are, and whether Elliot's sites join an existing fleet or
  style group:** ask Adrian. The brief says only that Adrian or Alden upload what Elliot saves to Drive.

## Who visits

Not researched in the repo beyond one line in the brief: a person searching for a trade service who wants to know
fast whether this firm can do it and how to reach it. Anything more detailed (ages, devices, the businesses' own
customers): ask Elliot, because his view of the visitor is part of his taste profile. Facts only Adrian can know stay
with Adrian.

## The path a visitor takes

Search result, then a Service or location page, then the lead form or the phone number. The pieces of that path that
the skins already carry:

- The phone number and a way to reach the form are visible without scrolling on a phone, on pages that have a footer.
  Tap targets are at least 44 px.
- The "other locations" menu and the "we cover" line are useful content, not clutter.
- The form is easy to complete on a phone, and every page that has a form shows it (H23).
- A fixed bar on small screens links to `/contact` ("Get a quote"). The Contact page carries the full form and a
  reduced shell: simple header, no footer, no quote bar.

## What "good" means (the standard every build is judged against)

1. **The checks pass** (`scripts/GATES.md`, `skins/_kit/CONTRACT.md`): same links and text as the data, the lead form
   exactly as specified, no third-party hosts, axe-core clean at 375 px and 1280 px, Lighthouse mobile performance 90
   or higher, stylesheet 12 KB gzipped or less, no class names shared with another skin.
2. **It looks human-made** (`skins/QUALITY_BAR.md`, rules QB1 to QB5): no generic AI-template patterns (purple or blue
   gradient heroes, glassmorphism, glowing blobs, emoji as icons, a centred block of three identical rounded cards);
   real type hierarchy; no decoration without meaning; consistent spacing, alignment and radius; a design that fits
   the trade. An independent reviewer judges this from screenshots, and one fail fails the skin.
3. **It works on a phone and for everyone** (accessibility and phone view before taste).
4. **It looks and feels like what Elliot picked.** Elliot's own idea of a good website is learned in the taste
   interview (`references/onboarding.md`, Mission 1). It is not written here: it lives in `summary.md` (taste notes)
   and in Claude's memory for the folder. Read memory first, then use it as the tie-breaker among options that pass 1
   to 3.

## What this means for changes and advice

- **H23 and H24 are the defaults for these template sites, and Elliot's choice is the final decision.** H23 is the
  lead form on every page that has one, H24 is no prices. If he asks to break one, tell him in one sentence what it
  costs, then do what he decides. Do not refuse.
- **Every form and call to action should serve an enquiry.** It should be clear what the visitor gets and what happens
  next. Quote buttons go to `/contact`.
- **Speak to the visitor in plain words.** Wording comes from Elliot's taste notes: his own sentences, never copied
  from the sites he likes.
- **Skins add no text of their own.** Every claim, rating, testimonial, logo and figure comes from the page data. A
  part that would need new text or new data is a decision for Adrian (see `references/replacements.md`).
- **Trust signals** (reviews, accreditations, years in business) are welcome when Elliot likes them. They are
  placeholders here. Show them near the asks.
- **Do not add rules nobody asked for.** Templates display whatever data a site is given. Design, structure,
  accessibility and markup are in scope. If something looks like a serious legal problem, tell Adrian once in chat and
  leave it out of the design.
