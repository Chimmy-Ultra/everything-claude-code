---
name: verify
description: Build The Workbook (toeic.html) and drive it in headless Chromium through real clicks to verify a change.
---
# Verify The Workbook

Build (from `english-reading/toeic/`): `python3 build_page.py` — refuses to build if any hand-written item is unreviewed or any chapter lacks a lesson; `--draft` builds anyway (don't commit a draft toeic.html; `git checkout -- toeic.html`).

Drive: `SP=<scratch dir> node .claude/skills/verify/drive.js` (needs `$SP/verify/` to exist; writes screenshots there).
It uses the global Playwright (`require(npm root -g + '/playwright')`, Chromium preinstalled) at 390×844 and clicks through:
contents → chapter → lesson → Skip → answer a wrong option → dock (Lesson sheet, Esc, 中, Star, Ask Claude with a mocked
`window.claude.use('sample')`) → tap-to-gloss → Next → reload + Continue → review shelf → word chapter (search, card, Practise)
→ listening playback (`--autoplay-policy=no-user-gesture-required`; checks `au.paused`/`currentTime`) → text-size limits.

Gotchas
- `ERR_CERT_AUTHORITY_INVALID` console errors are Google Fonts blocked by the sandbox proxy, not the page.
- The gloss tip can cover the next dotted word; click elsewhere (`page.mouse.click(5,5)`) before tapping another.
- Size buttons disable at the ends; click while enabled, not a fixed count.
- `db`/`user` capabilities only exist inside claude.ai; locally the page uses localStorage.
