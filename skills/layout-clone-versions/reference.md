# layout-clone-versions: reference

## Pattern guide template (Step 3)
One file in the scratchpad, written in our own words from the pages you read. Sections: page title formulas (product, category, home); heading patterns per page type with their order; paragraph shapes (3-sentence category intro, 2-sentence product description, FAQ answer: direct answer, rule of thumb, pointer to the quote button); card shape (title, 4 to 6 spec bullets starting with the number, price line, badges, button); "things the reference has that we do not copy" (exact prices, basket, search, chat, cookie banner, the reference's font, generator leaks such as internal notes, real reviewer names). Header line: "formulas, not sentences: never paste the reference's text".

## Brief template (Step 5)
Rules block first (from `subagent-briefs`: B1 no `sleep N; cmd`, never `pgrep -f` with a pattern in your own command line, no pkill, one simple command per Bash call, own worktree only, explicit `git add <paths>`, report file, no deploy, no browsing). Then the guide ids (from `npx -y modern-web-guidance@latest search "<2 to 5 words>"` and `retrieve "html,accessibility,css-layout,responsive-design,forms"`) with the instruction "run the same search for each part you build before you write it, and list the ids you applied in your report". Then: context (repo, skin, content pack path, the invariant), the version's layout description in the reference's own parts and order, process (read, implement in `skins/<skin>` with the the skin's own class prefix (milo uses `mh-`), optional contract fields documented in `skins/_kit/CONTRACT.md`, fixtures edited in place without changing words), checks, screenshots at 1280 and 375 px with a scroll before capture so lazy images load, commit steps, report under 35 lines.

## Checks that protect the invariant
- Text parity: a test compares tag-stripped text of every changed body or part with the old one, or a digest file (`tests/unit/fixtures/<name>-digest.json`) shows everything else is byte-identical to the content-pack commit.
- Other skins unchanged: `diff -rq` of the other skin's harness `dist` before and after.
- `gate4` (no shared classes, custom properties or file names between skins), `gate3`, `gate5` (axe, 2 viewports).
- Prices: no `£` anywhere; the literal placeholder only in body text. A schema block may repeat it only when the visible FAQ shows it.

## Pitfalls seen
- `pgrep -f "<pattern>"` in a wait loop matches its own command line and hangs forever. Run the command in the foreground with `timeout` and read the log.
- `wrangler pages project create` run in a folder that contains a `wrangler.jsonc` deploys that Worker. Run wrangler from a scratch folder with no config.
- The fixture guard accepts only `example.test` and a short host list: keep `site-N.example.test` in fixtures and rewrite the canonical host in the built pages (`prep_version.py` does this).
- The "demo fixtures" test can fail with "locations must be a JSON object" when `build/locations.json` is missing. It failed in the v7 to v11 worktrees and passed in a later fresh worktree (0 failures); confirm on the base commit before calling it unrelated.
- Fixture JSON rewrites: keep the file's indent style and rewrite only the files you change, or the diff fills with noise.
- Full-page screenshots show lazy images blank: scroll the page before capture.
- Dashboard pane size changes between navigations, so coordinate clicks miss. Drive the page with `javascript_tool`.
- Cloudflare bot checks and 403s are a stop, not an obstacle (Step 1).

## Dashboard upload (no token with Pages or Workers write)
1. `prep_version.py` writes `<bridge-dir>/<name>-<label>.zip`. Add `index.html` and a `_headers` file (`/*` then `Access-Control-Allow-Origin: *`) to the bridge folder and a wrangler config `{ "name": "<name>-bridge", "assets": { "directory": "<bridge-dir>" } }`; run `wrangler deploy -c <config>` twice from the scratch folder and wait until `<name>-bridge.<account>.workers.dev/<zip>` returns 200.
2. In the Pages dashboard, open `.../pages/new/upload`, set the project name, create it, then in page script: fetch the zip from the bridge, put it into `input[type=file][accept=".zip"]` through a `DataTransfer`, wait for "All files were successfully uploaded", click "Deploy site".
3. `wrangler delete --name <name>-bridge --force`; confirm the zip URL returns 404.
The deployed URL is `<project>.pages.dev`. Add noindex through the folder's `_headers` and `robots.txt` (the script does).

## Images and the logo for a different trade
Only the plant-hire banners in `harness/public/assets/site-1` exist. A new trade has no photos yet: say so in the report, use the nearest existing images as stand-ins, and never change the shared logo glyph or another site's look without a per-site flag (the DrainMilo test replaced the excavator glyph in the skin and changed site-8 by accident).

## Fixture text generator
If a script generates the fixture JSON (for example from a Python dict), commit it next to the fixtures or in `scripts/` so the pack can be regenerated; an uncommitted generator in the scratchpad is lost.

## Evidence level `skimmed`
A page that loaded but was only read as an outline is `headings`. A page read in full is `read`. Do not write more than the level supports.
