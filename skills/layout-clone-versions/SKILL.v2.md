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

Done when every planned layout part names its source site and level, and the user has seen the table.

## Step 3 — Build the shared content pack

  IF the user wants the text to follow a reference site (for example Mammoth):
    → write a pattern guide first (title formulas, heading and paragraph shapes, card shape; template in `reference.md`), then write our own sentences in those shapes. Never paste the reference's sentences.
  ELSE:
    → reuse the existing pack.

Put the pack in `harness/fixtures/site-N` and add `tests/unit/milo-siteN.test.mjs` (unique paths, every link resolves, form only on Contact, no `£`, unique titles, toc ids match h2 ids). Prices are the literal `(min-offer-price) to (max-offer-price)` in body text only (H24).
Done when the pack's tests and `gate5` pass and its screenshots have been looked at.

## Step 4 — One worktree and branch per version

`git worktree add -b feat/<skin>-vN-<ref> ~/projects/static-sites-<skin>-vN-<ref> <content-pack-commit>`; symlink `node_modules`, `harness/node_modules` and `data/sites.db` from a working checkout (untracked: always `git add` explicit paths).
Done when each worktree builds the harness once with `SKIN=<skin>`.

## Step 5 — Get modern web guidance, then brief one agent per version

Before any layout is written, load the `modern-web-guidance` skill and run its `search` for each layout part in Step 2 (header navigation, card grid, accordion, responsive images, sticky bar, form) and `retrieve` the broad guides `html`, `accessibility`, `css-layout`, `responsive-design` and `forms`. The retrieved rules and ids go into every brief; each agent runs the same `search` for the parts it builds and discloses the guide ids it applied in its report.
Then use the `subagent-briefs` rules plus the brief template in `reference.md`. A brief names: the layout parts from Step 2, the guide ids, the words-identical rule, the checks, the report file.
  IF an agent's report names no guide id:
    → send it back to run the searches before its work is accepted.
Done when every version has pushed commits and a report that lists the guide ids it applied.

## Step 6 — Check each version yourself before deploying

Run, per version: the unit files, the harness build + `gate5`, `gate4` and `gate3` (cross-skin class sharing), and `diff -rq` of the other skin's harness `dist` before and after (must be empty). View the home and one inner page screenshot.
  IF a check fails for a reason that also fails on the base commit (for example `build/locations.json` missing in a worktree):
    → record it as unrelated in the report, with the base-commit result.
  ELSE:
    → send the failure back to the version's agent.
Done when every version's report lists real gate output lines and you have seen its screenshots.

## Step 7 — Deploy each version as its own Pages project

  IF a Cloudflare token with Pages or Workers write exists for the account:
    → deploy with wrangler from a scratch folder that has no `wrangler.jsonc`.
  ELSE:
    → upload through the dashboard: `scripts/prep_version.py` builds the zip, a temporary CORS bridge Worker serves it, and the dashboard page fetches it into the "Drag and drop" input (`reference.md`, "Dashboard upload").
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
