# layout-clone-versions: Versioning

## Active skill

`SKILL.md` is the live version. Snapshots are read-only history.

## Version history

| File | Date | What changed |
|---|---|---|
| SKILL.v1.md | 2026-11-24 | Initial release, from the HireMilo v7 to v11 runs (Mammoth, Pivotal, Diamond, Allshaw, Travis Perkins). `scripts/prep_version.py` tested by rebuilding v11 and diffing against the deployed folder: no differences. |
| SKILL.v2.md | 2026-11-24 | Step 5 now requires `modern-web-guidance` (search per layout part, retrieve html, accessibility, css-layout, responsive-design, forms) before any layout is written; guide ids go in every brief and report (Adrian's request). |
| SKILL.v3.md | 2026-11-24 | From the end-to-end test on a new site (DrainMilo, one fresh agent, blockeddrains-luton.uk layout): pack worktree and the `lead-form-flag` test edit in Step 3, a before-copy of ss-01 in Step 4, `modern-web-guidance` wording, runnable gate 3, gate 4 and gate 5 `--pages` commands in Step 6, the full prep command in Step 7, `prep_version.py` now requires `--site`, `--name` and `--canonical-to`, plus images, generator and evidence-level notes in `reference.md`. Commands re-run from the extracted text. |

## How to update

Edit `SKILL.md` (it becomes v`N+1`), then `cp SKILL.md SKILL.v<N+1>.md`, then add a row above. Rollback: `cp SKILL.v<N>.md SKILL.md`.

Bump for: new steps or branches, corrected commands, new pitfalls. Do not bump for typos or link fixes.
