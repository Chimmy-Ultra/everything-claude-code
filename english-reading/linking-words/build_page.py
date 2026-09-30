# Builds linking-words.html from content.py, tiers.py and template.html.  python build_page.py
import html, os, re
from content import GROUPS, TRAPS
from tiers import NEW, EXTRA, TRICKY, MEDIUM, BASICS, MORE_TRAPS

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape

PLAY = ('<svg viewBox="0 0 12 12" class="ico-play" aria-hidden="true"><path d="M2 1l9 5-9 5z"/></svg>'
        '<svg viewBox="0 0 12 12" class="ico-stop" aria-hidden="true"><rect x="2" y="2" width="8" height="8" rx="1"/></svg>')
TYPE_LABEL = {"JOIN": "joins", "START": "starts", "NOUN": "+ noun", "END": "at the end"}

ICONS = {
    "tricky": '<path class="f-amber st" d="M32 8l26 46H6z"/><path class="ln" d="M32 24v14"/><circle class="f-ink" cx="32" cy="46" r="2.6"/>',
    "useful": '<rect class="f-teal st" x="6" y="22" width="22" height="22" rx="5"/><rect class="f-amber st" x="36" y="22" width="22" height="22" rx="5"/>'
              '<circle class="f-white st" cx="32" cy="33" r="9"/><path class="ln" d="M32 28v10M27 33h10"/>',
    "basics": '<rect class="f-white st" x="10" y="10" width="44" height="44" rx="8"/><path class="ln" d="M20 33l8 8 16-18"/>',
    "traps": '<circle class="f-coral st" cx="32" cy="32" r="22"/><path class="ln white" d="M24 24l16 16M40 24L24 40"/>',
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

# id -> (word, 中文, types, register, pattern, note, [(n, example, 中文)])
ENTRY = {}
for _, _, _, items in GROUPS:
    for wid, word, mean, types, register, pattern, note, examples in items:
        exs = [(n, ex, zh) for n, (ex, zh) in enumerate(examples, 1)]
        exs += [(n, ex, zh) for n, (ex, zh) in enumerate(EXTRA.get(wid, []), 7)]
        ENTRY[wid] = (word, mean, types, register, pattern, note, exs)
for wid, (word, mean, types, register, pattern, examples) in NEW.items():
    ENTRY[wid] = (word, mean, types, register, pattern, None, [(n, ex, zh) for n, (ex, zh) in enumerate(examples, 1)])

def ex_item(wid, n, ex, zh):
    return (f'<li><button class="ex playable" type="button" data-src="audio/ex/{wid}-{n}.mp3"><span class="pbtn">{PLAY}</span>'
            f'<span>{rich(ex)}</span></button><p class="zh">{E(zh)}</p></li>')

def card_head(wid):
    word, mean, types, register, _, _, _ = ENTRY[wid]
    return (f'<header class="card-h"><button class="hw playable" type="button" data-src="audio/w/{wid}.mp3"><span>{E(word)}</span>'
            f'<span class="pbtn">{PLAY}</span></button><span class="mean">{E(mean)}</span><span class="tags">{tags(types, register)}</span></header>')

def tricky():
    out, current = [], None
    for wid, section, why, compare, dont in TRICKY:
        if section != current:
            if current:
                out.append('</div>')
            out.append(f'<h3 class="sec">{E(section)}</h3><div class="big-cards">')
            current = section
        _, _, _, _, pattern, _, exs = ENTRY[wid]
        cmp = "".join(
            f'<div class="cmp-item"><button class="cmp-btn playable" type="button" data-src="audio/cmp/{wid}-{n}.mp3">'
            f'<span class="cmp-label">{E(label)}</span><span class="cmp-en"><span class="pbtn">{PLAY}</span><span>{rich(en)}</span></span></button>'
            f'<p class="zh">{E(zh)}</p></div>'
            for n, (label, en, zh) in enumerate(compare, 1))
        donts = "".join(
            f'<p class="dont"><span class="mark no" aria-label="Wrong">✗</span> <s>{E(w)}</s> <span class="arrow" aria-hidden="true">→</span> '
            f'<span class="mark ok" aria-label="Correct">✓</span> {E(r)}</p>' for w, r in dont)
        out.append(
            f'<article class="card big" id="{wid}">{card_head(wid)}<p class="pattern">{E(pattern)}</p>'
            f'<div class="why"><p class="why-h">Why it\'s tricky</p><p>{E(why)}</p></div>'
            f'<div class="cmp cols-{len(compare)}">{cmp}</div>'
            f'<p class="ex-h">{len(exs)} examples</p><ol class="exs two">{"".join(ex_item(wid, n, ex, zh) for n, ex, zh in exs)}</ol>'
            + (f'<div class="donts"><p class="why-h">Don\'t say</p>{donts}</div>' if dont else "") + '</article>')
    out.append('</div>')
    return "".join(out)

def useful():
    cards = []
    for wid, keep in MEDIUM:
        _, _, _, _, pattern, note, exs = ENTRY[wid]
        items = "".join(ex_item(wid, n, ex, zh) for n, ex, zh in exs if n in keep)
        cards.append(f'<article class="card" id="{wid}">{card_head(wid)}<p class="pattern">{E(pattern)}</p><ol class="exs">{items}</ol>'
                     + (f'<p class="note">{E(note)}</p>' if note else "") + '</article>')
    return "".join(cards)

def basics():
    rows = []
    for wid, keep in BASICS:
        word, mean, types, register, _, note, exs = ENTRY[wid]
        items = "".join(ex_item(wid, n, ex, zh) for n, ex, zh in exs if n in keep)
        rows.append(
            f'<article class="brow" id="{wid}"><div class="brow-h"><button class="hw small playable" type="button" data-src="audio/w/{wid}.mp3">'
            f'<span>{E(word)}</span><span class="pbtn">{PLAY}</span></button><span class="mean">{E(mean)}</span></div>'
            f'<ol class="exs">{items}</ol>' + (f'<p class="note">{E(note)}</p>' if note else "") + '</article>')
    return "".join(rows)

def traps():
    out = []
    for i, (wrong, rights, note) in enumerate(TRAPS + MORE_TRAPS, 1):
        rs = "".join(
            f'<button class="ex right playable" type="button" data-src="audio/trap/{i}-{j}.mp3"><span class="pbtn">{PLAY}</span>'
            f'<span><span class="mark ok" aria-label="Correct">✓</span> {E(r)}</span></button>'
            for j, r in enumerate(rights, 1))
        out.append(f'<article class="trap"><p class="wrong"><span class="mark no" aria-label="Wrong">✗</span> <s>{E(wrong)}</s></p>{rs}<p class="note">{E(note)}</p></article>')
    return "".join(out)

n_tricky, n_useful, n_basic = len(TRICKY), len(MEDIUM), len(BASICS)
n_ex = (sum(len(ENTRY[w][6]) for w, *_ in TRICKY) + sum(len(k) for _, k in MEDIUM) + sum(len(k) for _, k in BASICS))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
fill = {
    "TRICKY": tricky(), "USEFUL": useful(), "BASICS": basics(), "TRAPS": traps(),
    "ICON_TRICKY": icon("tricky"), "ICON_USEFUL": icon("useful"), "ICON_BASICS": icon("basics"), "ICON_TRAPS": icon("traps"),
    "N_WORDS": str(n_tricky + n_useful + n_basic), "N_TRICKY": str(n_tricky), "N_USEFUL": str(n_useful), "N_BASIC": str(n_basic),
    "N_EX": str(n_ex), "N_TRAPS": str(len(TRAPS) + len(MORE_TRAPS)),
}
page = tpl
for k, v in fill.items():
    page = page.replace("{{" + k + "}}", v)
assert "{{" not in page
open(os.path.join(HERE, "linking-words.html"), "w", encoding="utf-8").write(page)
print("tricky", n_tricky, "useful", n_useful, "basics", n_basic, "examples", n_ex, "traps", len(TRAPS) + len(MORE_TRAPS), "bytes", len(page.encode()))
