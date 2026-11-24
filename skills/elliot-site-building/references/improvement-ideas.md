# Improvement ideas: reviewing a page when Elliot asks

Read this only when Elliot asks for an opinion, in his own words: "what would make this better?", "does this page
work?", "why would anyone call?", "make this better", or when he points at a page and says it feels off. These are
lenses for advice, **not rules**: nothing here is checked on every build, and nothing is changed without the usual
preview, the decision matrix and his yes.

Hand-edited from the *impeccable* design skill's critique, clarify, distill, harden, colorize, animate, delight,
onboard, quieter and bolder guides (MIT licence), cut down to what fits Astro template pages for local businesses.
Only the guidance is borrowed: do not run impeccable's own tools on these pages unless Adrian approves it.

## How to give a review

1. **Look as a visitor** at desktop and phone width. First answer: what is this page for, and what is the one
   action a visitor should take (call, send the enquiry form, ask for a quote)? Every suggestion serves that.
2. **Say what works first** (two or three things, specifically).
3. **Give three to five suggestions, most important first.** More buries the ones that matter. For each:
   - **What:** the problem, in plain words ("the enquiry form is below three screens of text on a phone").
   - **Why it matters to visitors.**
   - **The fix**, concretely, as a part or option from `references/replacements.md` where one fits.
   - **What it takes:** a change to one page, a change to a part used on every page, or a skin-wide change
     (colors, fonts, header, menus) that needs Adrian. Say whether it still passes the gates and the quality bar.
   Rank them: **blocks the visitor** (cannot find or use the action), **major** (hard to use, unreadable, fails
   accessibility), **minor** (annoying, there is a workaround), **polish**.
4. **Ask which to do first**, or whether he wants only the top ones. Anything he picks goes through the normal
   flow: preview, decision matrix, yes. Keep his answer: it tells you what he thinks a good site is.

## Lenses

**Local-business landing pages.** The first screen says what the business does and where, shows the main action
plainly (phone number, enquiry form, quote button), and shows the proof a visitor looks for: reviews, areas
covered, photos of the work. Real-looking structure beats filler. A claim with nothing near it to back it reads as
marketing. Template text stays placeholder text (names, phones, photos, reviews) and prices stay as the fixed
placeholder range; the lens is about where things sit, not about inventing facts.

**Mental effort.** Can a visitor do the main task without distractions competing for attention? Is information in
small groups (about four items per group)? Is there one clear decision at a time, with no more than about four
choices visible at once (five to seven is pushing it; eight or more and people skip, misclick or leave)? Is detail
revealed when needed (an accordion, a "more" link) rather than all at once? Does a visitor have to remember
something from another page to act on this one?

**The ten usability checks** (Nielsen's heuristics), website edition:
1. Visitors can tell what is happening (a form says it was sent; a button shows it is working).
2. It uses visitors' words, not internal ones ("roof repair", not a trade code).
3. There is a way back (close a menu, a clear back link).
4. Same things look and work the same across pages.
5. Mistakes are prevented (required fields marked, examples in fields, sensible defaults).
6. Options are visible rather than remembered (labels on icons, the current page marked in the menu).
7. Returning visitors have shortcuts (a phone link that dials, links straight to the services) where it matters.
8. Nothing on the page competes with the main message without a reason.
9. Errors say what went wrong and how to fix it, next to the problem, and keep what was typed.
10. Help is findable where people get stuck (questions and answers near the form, contact near the quote).

**Walk it as different visitors.** Pick the two or three that fit the page and name what breaks for each:
- a **first-timer** who reads everything literally and will not guess (is the first action clear in five seconds?
  are icons labelled? is jargon explained?);
- an **impatient visitor** who skims and leaves (can they reach the action in seconds? are there unskippable
  popups or slow animations?);
- someone using a **keyboard or screen reader** (can they tab to everything, see where focus is, and hear
  sensible names for buttons, links and images?);
- a **phone visitor** on the move (big enough buttons, short sections, nothing that needs sideways scrolling, the
  phone number one tap away);
- a **sceptical buyer** comparing three local firms (what they do, where, proof and next step easy to find).

**Words.** Each spot says the one thing the visitor needs now, then the next action. Buttons name what they do
("Get a quote", not "Submit"). Errors say what failed and how to recover. Plain language, consistent terms and
capitalisation, no repeated intros. Alt text says what the image shows (empty for decoration). Never rely on
color or an icon alone to carry a message. Do not add claims, prices or facts to a template.

**Simpler.** One main action per section; secondary actions quieter. Cut what is said elsewhere. One or two brand
colors plus neutrals; one font family in three or four sizes and two or three weights. No boxes inside boxes;
spacing and alignment do the grouping. Pick left or centred alignment and stick to it. Shorter copy, active voice
("Send your enquiry", not "Your enquiry will be sent").

**Robust.** Long names and headings do not break the layout; it still works at 200% zoom; form fields are at
least 16px on phones (smaller makes iPhones zoom in and jumbles the form); errors keep what was typed; every
button and form has its hover, focus, sending, success and error states.

**Color.** Brand colors have jobs (main action, links, highlights) rather than being sprinkled everywhere; the main
action's color is not spent on decoration. No grey text on a colored background (use a darker or lighter shade of
that color). Contrast as in `look-and-feel.md`.

**Motion.** Movement should explain something (a response to a click, where something went, one featured moment),
not decorate. The same fade-in on every section is noise. Nothing should make visitors wait, and people who turn
motion down in their device settings should still get the information.

**Delight.** Personality belongs at moments that matter (form sent, an empty or first-time state, an error) and
must never slow the task or joke about money, privacy or a problem the visitor has.

**Too loud or too flat.** If a page feels loud: fewer colors, lighter weights, more space, fewer effects, but keep
the hierarchy. If it feels flat: make one decisive move with what the skin already has (its type scale, its
motif, its colors), then quiet everything around it. Do not add new colors or fonts unasked. If Elliot says "too
busy" or "boring", use this lens and show him the quieter or bolder version next to the current one.

**Small details.** Text selection color, focus outlines, link underlines and scrollbars still show browser
defaults on many pages; theming them to the skin is cheap polish. These are usually skin-wide: raise it with
Adrian.
