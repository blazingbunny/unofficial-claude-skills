# Tool test and guided demo (mode 3)

Two parts, both on the practice page **https://hiremilo.co.uk/** in the browser panel, both preview only:
1. **The tool test** (about 5 minutes): Elliot clicks every tool himself and you say back what reached you. It is
   the first step of Mission 2 in `references/onboarding.md`, and he can ask for it again any time.
2. **The guided demo** (about 15 minutes): a short walk through the same site, changing it in preview, so he sees
   the whole loop of point, say and preview.

Run it when he says "start the demo", "tool test" or asks how this works. Use plain English, one step at a time, and
wait for "done" (or a question) before each next step. Keep each message short. He should use the microphone to
talk; website addresses are the one thing to paste.

Rules for both parts, on top of the skill's ground rules:
- Preview only. Change the page only inside the browser panel; never save anything, never write to the Drive folder,
  and never touch the project's site files. Nothing he does changes hiremilo.co.uk itself.
- While chatting, describe changes in plain words; keep exact colours and sizes for the summary at the end.
- You can't see the app's own buttons. Describe what to look for, then check the result from what he sends.
- A site that blocks you (bot check) is a stop: tell him and ask for a screenshot. Never get past a check. Never
  ask for a password.

## Part 1: The tool test

Open https://hiremilo.co.uk/ in the browser panel: `preview_start` with `url: "https://hiremilo.co.uk/"` (no server
is needed for an outside site), or `navigate` if the panel is already open. If he cannot see the panel: Ctrl+Shift+B
(Cmd+Shift+B on a Mac). A site asks permission the first time: he clicks **Allow**. If the panel is narrow, he drags
its left edge to widen it. The full steps for opening his own site (a local preview server through
`.claude/launch.json`) are in `SKILL.md`, "Opening the site in the browser panel": use them for the build, not for
this practice page.

Ask for one tool at a time, wait, and check what reached you:

| Tool | Ask him to | What should reach you |
|---|---|---|
| Pointer | Click the orange "Get a quote" button and say what he thinks of it | The button with his next message: its tag, classes, position on the page, styles, its HTML and neighbours, and a cropped picture. No "Add to chat" needed. |
| Pen, arrow, box | Draw around the logo or the main heading, then click **Add to chat**, then send | The drawing, only after "Add to chat" |
| Text | Type a short note next to something he likes, then **Add to chat** | The note, only after "Add to chat" |
| Screenshot or image | Add one with the plus button next to the message box | The image |
| Microphone | Click it and say a sentence about the page | The words he spoke |

After each tool, say back what you received in one line ("I got the button: orange, a link to /contact"). If nothing
arrives, say: "I can't see your drawing yet. Click **Add to chat** next to it, then send." If he drew, forgot Add to
chat and then recovered, that is the hidden badge **Lost Signal**. When every tool has worked, say "Tool test
complete".

If the "Get a quote" button or the logo is not where this table says (the practice page may have changed), pick the
nearest equivalent on the page and tell him which one you chose.

## Part 2: The guided demo (about 15 minutes)

1. **Welcome** in two sentences. Explain that nothing done today is saved, and that he can talk to you by clicking
   the microphone in the chat box. Keep the practice page open from the tool test, or open it again.
2. **Point:** ask him to use the Pointer to click the page's main heading and say "make this heading smaller and
   gold". Preview it, then ask how it looks.
3. **Adjust:** ask him to tweak it in his own words ("bigger", "a different colour"). Preview each change. If he
   asks what a colour code means, explain it simply.
4. **Draw:** ask him to use the box or pen to draw around one card or section and say "add a thin glowing border to
   parts like this". Remind him to click **Add to chat** before he sends. Preview it.
5. **Show:** ask him to paste a link or a screenshot from a website he likes and say what he likes about it. Apply
   one idea as a preview. Be honest about limits (for example, if the idea needs a photo or data the page does not
   have).
6. **Phone:** show the page at phone size and point out anything that looks broken. Say which problems were already
   there and which come from the preview.
7. **Start over:** ask him to refresh the page. Explain that everything went back to the original because previews
   are never saved, so nothing here needs reversing. If he worries he broke something, reassure him.
8. **Redo and explain building:** quickly redo his favourite change, then write a summary (page address; each change
   as "before -> after" with exact colours, sizes and wording; which section) and take a screenshot. Save the
   screenshot in a folder called `screenshots` inside the project folder with a clear file name, check the file is
   really there, and tell him its name. Then explain in plain words what building a real site from his picks
   involves: the spec sheet he approves, the build with Astro, the web-quality check, and the save to his Drive
   folder where Adrian or Alden pick it up. Don't build anything during the demo. If he asks you to build it anyway,
   say no kindly: building starts after the spec sheet in the onboarding (modes 1 and 2 in `SKILL.md`).
9. **Wrap up** in a few bullets:
   - what he learned (point, say, preview);
   - that previews are safe and a build only starts after he says yes to the spec sheet;
   - the phrases to remember: "show me...", "I need help", "I'm stuck", "what else did we miss?".

   Then ask if he has any questions. If he came here from the onboarding, return him to Mission 2 with one line:
   "Tool test done. Next: the versus rounds."
