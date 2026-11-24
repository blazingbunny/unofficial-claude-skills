---
name: demo-trait-builder
description: Use when a demo (SD1..SD15 in demos/) is missing the named trait its direction promises in docs/model/skin-directions.md, such as a step form, before and after pair, two doors, founding year timeline, postcode hero, sticky side form or comparison table. Also use when a visual review reports a spec MISMATCH for a demo, or when adding any new part or hero or form variant to the demo generator.
allowed-tools: Read Edit Write Bash
---

# Build one named trait of a demo direction

A trait is the thing a direction is known for. The demos share one component set, so a trait is a small, flagged variant: it changes only the demos whose design-policy flag is set. Three traits were built by hand first (SD8 postcode hero, SD1 and SD2 sticky side form, SD15 comparison), then SD7, SD9, SD11 and SD12 by an agent using this skill. Copy their shape.

Repo: the `static-sites` checkout (worktree `~/projects/static-sites-sdlc`, branch `sdlc/demo-sites`). Work on that branch. One trait per commit.

## Step 1 — Read the spec for the trait

Read the direction in `docs/model/skin-directions.md` (Skeleton and Look lists), then `trait-specs.md` in this folder for the wanted DOM, the data source and the done check of the trait.
Done when you can name: the flag, the DOM you will render, the data source, and the one DOM check that proves it.

## Step 2 — Decide the content source

  IF the live Pro Construction Equipment site has the fact (services, areas, steps, FAQ, phone, address):
    → read it from the fixture props (`props.services`, `props.process`, ...), never copy it into a component.
  ELSE IF the trait needs a fact the live site lacks (a founding year, ratings, before and after photos, audience split, timeline dates):
    → render the structure with marked sample content: `data-sd-sample` on the container and the word `Sample` as the value (see `Compare.astro`). Invent nothing.
Done when no component contains an invented number, date, rating, name or claim.

## Step 3 — Touch the six places, in this order

1. `demos/src/lib/design-policy.mjs`: add the flag to the direction line in `DIRECTION_DESIGN` (for example `heroPostcode: true`). Only the target demo gets it.
2. `demos/src/lib/roles.mjs`: register every new class role in `ROLE_BASE` with layout-only declarations. `cls()` throws on an unregistered role.
3. `demos/src/lib/ui-text.mjs`: add any new interface wording (labels, button text, headings the live site lacks).
4. The component: edit the existing one (`Hero.astro`, `LeadForm.astro`, `Services.astro`, `Process.astro`, ...) or add one. A new non-part block is a view id `V-name`: add its import and branch in `Part.astro`, and insert it in the `order` list in `Page.astro`.
5. `Page.astro`: pass the flag down (`postcode={!!D.heroPostcode}`) or change `place()` for placement. Placement rules live only in `place()`. A component reads a flag one of two ways: a prop from `Page.astro`, or `import { DIRECTION_DESIGN }` and `DIRECTION_DESIGN[p.toUpperCase()]`. `Part.astro` passes no flags.
6. `demos/src/lib/design-css.mjs`: add the rules guarded by the flag, `if (D.flag) { add(...); mq(...) }`. Use `P`, `X(role)`, `R`, `LINE`, `W`. In `mq` text, `§` stands for the page prefix.
   The generated CSS is sorted, so a plain `ROLE_BASE` rule can lose to an equal-specificity rule that sorts later (`.sd9-ba-media{display:grid}` lost to `.sd9-hero-media{display:block}`). To override another role's property, declare it in `design-css.mjs` under `${P} ${X(role)}` and use a longer selector such as `.P .main .colmain>.band`.
   A role `display` beats the `hidden` attribute: add `[hidden]{display:none}` for every toggled element.
   Whitespace between inline spans is trimmed by JSX: insert `{' '}` or the text reads "Est.Sample year".
If the trait needs a script (a multi-step form, a field that fills another), edit `demos/templates/form.js.tpl`: one new function, called from the existing DOMContentLoaded line. No storage, no cookies, no third-party host.
form.js.tpl ships in all 15 demos' scripts, so check the 12 KB gzip limit after editing it.
`demos:build` fails with "class role has no base rule" until every class used in any component is in `ROLE_BASE`.
Done when all six places for this trait are edited and `npm run demos:build` prints `demos:build ok`.

## Step 4 — Obey the generator grammar

- No `style=` attribute in any component. Counts and sizes go in CSS.
- CSS: no quotes, no `!important`, no `url()`, no animation. Classes are `sdN-role` only.
- Never emit two CSS rules with the same selector in different forms (base plus media): the css-gen tests compare rules by selector. Use `clamp()` instead of a media override when a value only scales.
- A coloured side border over 1px fails the unit test "no thick side border" (a 3px timeline line failed). Use a 1px line or a dot.
- Absolutely positioned labels sit at least 12px inside a painted container, and a painted main-column band needs side padding, or the lint flags a flush panel.
- Padding on any panel with a background, border or shadow is added automatically (css-gen post-pass). Do not remove it.
- A form control or button must stay at least 4.5:1 contrast. Gradients and background images count.
- The stylesheet stays under 12 KB gzip per demo.
Done when `npm run demos:build` passes, which runs these guards.

## Step 5 — Look at it, then measure it

  0. Iterate with `npm run demos:build -- --demos SDn` (about 15 s). The full build (about 95 s) must still run before each commit and before any trait test, because a single-demo build leaves stale dist for the others and tests can pass or skip wrongly.
  1. `node scripts/demos_shot.mjs SDn out.png 1280 <scrollY> 900` and again at width 375. Read both images. Look for the trait, empty areas, flush text, a hidden subject.
  2. `node scripts/demos_layout_lint.mjs --only SDn` must print `clean` for flush panels, overflow, button contrast and logo size.
  3. Prove the trait with one DOM assertion (see `trait-specs.md`), and put it in `tests/unit/demo-design.test.mjs` as a browser test that skips when `dist/demos` is missing.
Done when the screenshot shows the trait, the lint has no hard flag for this demo, and the new test passes.

## Step 6 — Test and commit

  1. `node --test tests/unit/demo-css-gen.test.mjs tests/unit/demo-form-script.test.mjs tests/unit/demo-design.test.mjs tests/unit/demos-layout-lint.test.mjs`.
  2. IF the change touched `Page.astro`, `roles.mjs` or the form script: run `npm run test:unit` (serial, about 8 minutes) before the commit.
  3. `git add` only the files you changed, commit, `git push origin sdlc/demo-sites`.
  4. Never touch the user's preview servers on ports 4400 to 4415. Start your own on ports 5500 and up, and stop only those.
Done when the tests pass and the commit is pushed.

## Step 7 — Learning review

  IF the trait needed a file or step not listed in Step 3: add it there.
  IF a guard or test message was unclear: add the message and its fix to Step 4.
  IF anything changed: snapshot `SKILL.v<N+1>.md` and add a row to `VERSIONING.md`.

## Checklist

- [ ] Spec read, flag named, DOM check named
- [ ] Content from fixtures or marked sample, nothing invented
- [ ] Six places edited, build ok
- [ ] Screenshot viewed at 1280 and 375
- [ ] Layout lint clean for this demo
- [ ] Trait test added and passing, suite green
- [ ] Committed and pushed
- [ ] Learning review done
