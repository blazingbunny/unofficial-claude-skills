---
name: layout-clone-versions
description: Use when asked to make versions of a fixture site that clone the layout of reference sites (named URLs, a Google top-10, "make it look like <site>") while the theme and the words stay the same. Also use when building the shared content pack those versions read from.
allowed-tools: Read Edit Write Bash
---

# Layout-clone versions: same words, same theme, one reference layout each

Proven on HireMilo (2026-11-23/24): v7 Mammoth, v8 Pivotal, v9 Diamond, v10 Allshaw, v11 Travis Perkins, all over the shared `harness/fixtures/site-8` content pack. Repo: `static-sites`. Details, brief templates and pitfalls: [`reference.md`](reference.md).

The invariant: **the words and the theme never change between versions; only the layout does.** Every step protects it.

## Step 1 — Study each reference and record the evidence level

For each reference URL, fetch it (curl with a browser User-Agent, then the browser pane).

  IF the page loads (HTTP 200 with real content):
    → record `read` (text and structure seen) or `headings` (outline only).
  ELSE IF the page shows a bot check, a 403 or a captcha:
    → record `blocked`. Never complete the check or work around it. Ask the user for a paste or screenshot if the site matters.
  ELSE IF only a search-result snippet exists:
    → record `snippet`.

Done when every reference has a level and a one-line list of layout parts seen (header, hero, card grid, steps, footer, schema).

## Step 2 — Write the two buckets

Table per bucket: `element | source site | evidence level | in the demos today?`.
  IF a row's level is `snippet` or `blocked`:
    → the row is a hint only; the plan never relies on it.

Done when every planned layout part names its source site and level, and the user has seen the table (when no user is present, the table is written into the final report).

## Step 3 — Build the shared content pack

  IF the user wants the text to follow a reference site (for example Mammoth):
    → write a pattern guide first (title formulas, heading and paragraph shapes, card shape; template in `reference.md`), then write our own sentences in those shapes. Never paste the reference's sentences.
  ELSE:
    → reuse the existing pack.

First make the pack's worktree: `git worktree add -b feat/<skin>-<site>-content-pack ~/projects/static-sites-<skin>-<site> <base-commit>` (the base is the commit that already holds the skin and the harness), with the symlinks from Step 4.
Put the pack in `harness/fixtures/site-N` and add `tests/unit/milo-siteN.test.mjs` (unique paths, every link resolves, form only on Contact, no `£`, unique titles, toc ids match h2 ids). `tests/unit/lead-form-flag.test.mjs` whitelists the sites that turn the form off (regex `site-[...]`): add `N` to it, or the new site fails. Prices are the literal `(min-offer-price) to (max-offer-price)` in body text only (H24). Commit and push the pack: that commit is the base for Step 4.
Done when the pack's tests pass, `gate5` passes on the pack, and its screenshots have been looked at.

## Step 4 — One worktree and branch per version

`git worktree add -b feat/<skin>-vN-<ref> ~/projects/static-sites-<skin>-vN-<ref> <content-pack-commit>`; symlink `node_modules`, `harness/node_modules` and `data/sites.db` from a working checkout (untracked: always `git add` explicit paths).
Before any skin edit, build the other skin once and keep its output as the "before" copy: in `harness`, `SKIN=ss-01 npx astro build`, then copy `harness/dist` to `<scratch>/ss01-before` (Step 6 diffs against it).
Done when each worktree builds the harness once with `SKIN=<skin>` and the "before" copy exists.

## Step 5 — Get modern web guidance, then brief one agent per version (or build the version yourself)

First list which of the reference's layout parts the skin already has (compare the reference against the skin's header, hero, cards, footer) and build only the new ones.

Before any layout is written, load the `modern-web-guidance` skill and run its `search` for each layout part in Step 2 (header navigation, card grid, accordion, responsive images, sticky bar, form) and `retrieve` the broad guides `html`, `accessibility`, `css-layout`, `responsive-design` and `forms`. The retrieved rules and ids go into every brief; each agent runs the same `search` for the parts it builds and discloses the guide ids it applied in its report.
Then use the `subagent-briefs` rules plus the brief template in `reference.md`. A brief names: the layout parts from Step 2, the guide ids, the words-identical rule, the checks, the report file.
  IF an agent's report names no guide id:
    → send it back to run the searches before its work is accepted.
Done when every version has pushed commits and a report that lists the guide ids it applied.

## Step 6 — Check each version yourself before deploying

Run, per version, from the version's worktree:
1. Unit files: `timeout 400 node --test tests/unit/fixtures.test.mjs tests/unit/responsive-images.test.mjs tests/unit/lead-form-flag.test.mjs tests/unit/milo-siteN.test.mjs`. The full `npm run test:unit` takes over 5 minutes: run it in the background and never together with `gate5`.
2. `gate5` on the version's pages only: in `harness`, `SKIN=<skin> npx astro build`, then `SKIN=<skin> node gates/gate5_axe.mjs dist --pages "$(ls dist/site-N | sed 's#^#/site-N/#' | paste -sd,)"`. Run the full `gate5` (all fixture pages, about 6 minutes) once, on the content pack.
3. `gate4` and `gate3` need a whole harness `dist` per skin (the CSS sits in `_astro` and `hmstatic` at the root), not `dist/site-N`. For each skin `k` in `ss-01 ss-02 ss-03 serverscale <skin>`: `SKIN=$k npx astro build` in `harness`, then copy `harness/dist` to `<scratch>/dist-$k`. Then `npm run gate:4 -- --dist ss-01=<scratch>/dist-ss-01 --dist ss-02=<scratch>/dist-ss-02 --dist ss-03=<scratch>/dist-ss-03 --dist serverscale=<scratch>/dist-serverscale --dist <skin>=<scratch>/dist-<skin>` and `npm run gate:3 -- <scratch>/dist-<skin>`.
4. `diff -rq` of `harness/dist` after rebuilding ss-01 against `<scratch>/ss01-before` (must be empty).
View the home and one inner page screenshot.
  IF a check fails for a reason that also fails on the base commit (the "demo fixtures" test can fail with "locations must be a JSON object" in some worktrees):
    → record it as unrelated in the report, with the base-commit result.
  ELSE:
    → send the failure back to the version's agent.
Done when every version's report lists real gate output lines and you have seen its screenshots.

## Step 7 — Deploy each version as its own Pages project

  IF a Cloudflare token with Pages or Workers write exists for the account:
    → deploy with wrangler from a scratch folder that has no `wrangler.jsonc`.
  ELSE:
    → build the zip with `python3 -I scripts/prep_version.py --label vN --worktree <version worktree> --site site-N --name <project prefix> --canonical-to https://<demo domain> --out-root <scratch> --bridge-dir <scratch>/bridge`, then upload through the dashboard: a temporary CORS bridge Worker serves it, and the dashboard page fetches it into the "Drag and drop" input (`reference.md`, "Dashboard upload").
Then delete the bridge Worker and check live: key pages return 200, an unknown path returns 404, the noindex header is set, forms only on Contact, no `£`, canonical on the demo domain.
Done when each version's links are listed and the bridge returns 404.

## Step 8 — Learning review

| Question | Action |
|---|---|
| A reference needed a step not here? | Add it to the step |
| A check failed for a new environment reason? | Add it to `reference.md` pitfalls |
| Anything duplicated, stale or already obvious? | Prune it now |

If anything changed, edit `SKILL.md`, then `cp SKILL.md SKILL.v<N+1>.md` and add a row to `VERSIONING.md`.

## Checklist

- [ ] Evidence level per reference (Step 1)
- [ ] Two buckets shown to the user (Step 2)
- [ ] Content pack with its own tests (Step 3)
- [ ] One worktree and branch per version (Step 4)
- [ ] Modern web guidance searched and retrieved, ids in every brief and report (Step 5)
- [ ] Briefs sent, reports in (Step 5)
- [ ] Own checks and screenshots per version (Step 6)
- [ ] Each version deployed and verified live, bridge removed (Step 7)
- [ ] Learning review done (Step 8)
