# Builds linking-words.html from content.py and template.html.  python build_page.py
import html, os, re
from content import GROUPS, TRAPS

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape

PLAY = ('<svg viewBox="0 0 12 12" class="ico-play" aria-hidden="true"><path d="M2 1l9 5-9 5z"/></svg>'
        '<svg viewBox="0 0 12 12" class="ico-stop" aria-hidden="true"><rect x="2" y="2" width="8" height="8" rx="1"/></svg>')
TYPE_LABEL = {"JOIN": "joins", "START": "starts", "NOUN": "+ noun", "END": "at the end"}

ICONS = {
    "add": '<rect class="f-teal st" x="6" y="22" width="22" height="22" rx="5"/><rect class="f-amber st" x="36" y="22" width="22" height="22" rx="5"/>'
           '<circle class="f-white st" cx="32" cy="33" r="9"/><path class="ln" d="M32 28v10M27 33h10"/>',
    "contrast": '<path class="ln wide" d="M10 46h24a12 12 0 0 0 0-24H20"/><path class="f-coral st" d="M22 13l-12 9 12 9z"/>'
                '<circle class="f-violet st" cx="50" cy="46" r="6"/>',
    "cause": '<rect class="f-sky st" x="8" y="18" width="10" height="30" rx="2" transform="rotate(-28 13 48)"/>'
             '<rect class="f-amber st" x="24" y="18" width="10" height="30" rx="2" transform="rotate(-14 29 48)"/>'
             '<rect class="f-coral st" x="42" y="18" width="10" height="30" rx="2"/><path class="ln" d="M6 54h52"/>',
    "time": '<circle class="f-white st" cx="32" cy="32" r="22"/><path class="ln" d="M32 18v14l10 6"/>'
            + "".join(f'<circle class="f-ink" cx="{32 + 17 * c}" cy="{32 + 17 * s}" r="1.8"/>' for c, s in [(0, -1), (1, 0), (0, 1), (-1, 0)]),
    "condition": '<path class="ln" d="M32 58V14"/><path class="f-teal st" d="M32 16h20l6 7-6 7H32z"/><path class="f-coral st" d="M32 32H12l-6 7 6 7h20z"/>',
    "examples": '<rect class="f-white st" x="8" y="8" width="34" height="44" rx="4"/><path class="ln thin" d="M15 18h20M15 26h20M15 34h14"/>'
                '<circle class="f-sky st" cx="42" cy="40" r="10"/><path class="ln wide" d="M49 47l8 8"/>',
    "traps": '<path class="f-amber st" d="M32 8l26 46H6z"/><path class="ln" d="M32 24v14"/><circle class="f-ink" cx="32" cy="46" r="2.6"/>',
}

def icon(key, size=56):
    return f'<svg class="ic" viewBox="0 0 64 64" width="{size}" height="{size}" aria-hidden="true">{ICONS[key]}</svg>'

def rich(text):
    return re.sub(r"\*\*(.+?)\*\*", r'<b class="lk">\1</b>', E(text, quote=False))

def tags(types, register):
    out = [f'<span class="tag t-{t.lower()}">{TYPE_LABEL[t]}</span>' for t in types]
    if register:
        out.append(f'<span class="tag t-reg">{E(register)}</span>')
    return "".join(out)

def groups():
    out = []
    for gid, title, zh, items in GROUPS:
        cards = []
        for wid, word, mean, types, register, pattern, note, examples in items:
            exs = "".join(
                f'<li><button class="ex playable" type="button" data-src="audio/ex/{wid}-{n}.mp3"><span class="pbtn">{PLAY}</span>'
                f'<span>{rich(ex)}</span></button><p class="zh">{E(exzh)}</p></li>'
                for n, (ex, exzh) in enumerate(examples, 1))
            cards.append(
                f'<article class="card" id="{wid}"><header class="card-h">'
                f'<button class="hw playable" type="button" data-src="audio/w/{wid}.mp3"><span>{E(word)}</span><span class="pbtn">{PLAY}</span></button>'
                f'<span class="mean">{E(mean)}</span><span class="tags">{tags(types, register)}</span></header>'
                f'<p class="pattern">{E(pattern)}</p><ol class="exs">{exs}</ol>'
                + (f'<p class="note">{E(note)}</p>' if note else "") + '</article>')
        out.append(
            f'<section class="group" id="{gid}" aria-labelledby="{gid}-h"><div class="group-h">{icon(gid)}<div>'
            f'<h2 id="{gid}-h">{E(title)}</h2><p class="sub">{len(items)} linking words · {len(items) * 6} examples</p></div></div>'
            f'<div class="cards">{"".join(cards)}</div></section>')
    return "".join(out)

def traps():
    out = []
    for i, (wrong, rights, note) in enumerate(TRAPS, 1):
        rs = "".join(
            f'<button class="ex right playable" type="button" data-src="audio/trap/{i}-{j}.mp3"><span class="pbtn">{PLAY}</span>'
            f'<span><span class="mark ok" aria-label="Correct">✓</span> {E(r)}</span></button>'
            for j, r in enumerate(rights, 1))
        out.append(f'<article class="trap"><p class="wrong"><span class="mark no" aria-label="Wrong">✗</span> <s>{E(wrong)}</s></p>{rs}<p class="note">{E(note)}</p></article>')
    return "".join(out)

NAV = {"add": "Adding", "contrast": "Contrast", "cause": "Reasons", "time": "Time", "condition": "Conditions", "examples": "Examples"}
nav = "".join(f'<a href="#{gid}">{NAV[gid]}</a>' for gid, _, _, _ in GROUPS) + '<a href="#traps">Traps</a>'
n_words = sum(len(g[3]) for g in GROUPS)
n_ex = sum(len(it[7]) for g in GROUPS for it in g[3])
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
page = (tpl.replace("{{GROUPS}}", groups()).replace("{{TRAPS}}", traps()).replace("{{NAV}}", nav)
        .replace("{{TRAP_ICON}}", icon("traps")).replace("{{N_WORDS}}", str(n_words)).replace("{{N_EX}}", str(n_ex))
        .replace("{{N_TRAPS}}", str(len(TRAPS))))
open(os.path.join(HERE, "linking-words.html"), "w", encoding="utf-8").write(page)
print("words", n_words, "examples", n_ex, "traps", len(TRAPS), "bytes", len(page.encode()))
