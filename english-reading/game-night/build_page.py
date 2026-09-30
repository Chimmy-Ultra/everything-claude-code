# Builds game-night.html from content.py.  python build_page.py
import html, json, os, re
from content import GROUPS, SCENES, READINGS, SOURCES, READ_SOURCES, NAMES, BIOS

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape
AV_PATH = os.path.join(HERE, "..", "avatars", "avatars.json")
AVATARS = json.load(open(AV_PATH, encoding="utf-8")) if os.path.exists(AV_PATH) else {}

def avatar(who):
    return AVATARS.get(who) or NAMES[who][0]

ITEMS = {wid: (word, zh, var) for _, _, _, items in GROUPS for wid, word, zh, _, _, var, _ in items}

# ---------- icons (64×64) ----------
def disc(cx, cy, r, top, side, ry=None):
    ry = ry or r * .45
    return (f'<path class="{side} st" d="M{cx-r} {cy} v6 a{r} {ry} 0 0 0 {2*r} 0 v-6"/>'
            f'<ellipse class="{top} st" cx="{cx}" cy="{cy}" rx="{r}" ry="{ry}"/>')

def card(x, y, w, h, fill, rot=0, cx=None, cy=None):
    t = f' transform="rotate({rot} {cx if cx is not None else x + w/2} {cy if cy is not None else y + h/2})"' if rot else ""
    return f'<rect class="{fill} st" x="{x}" y="{y}" width="{w}" height="{h}" rx="3.5"{t}/>'

def pips(pts, cls="f-dark"):
    return "".join(f'<circle class="{cls}" cx="{x}" cy="{y}" r="2.7"/>' for x, y in pts)

def arrow(d, head, cls="f-ink"):
    return f'<path class="ln" d="{d}"/><path class="{cls}" d="{head}"/>'

def border_squares(x0, y0, n, size, gap):
    cols = ["f-teal", "f-coral", "f-amber", "f-sky"]
    out, k = [], 0
    step = size + gap
    for i in range(n):
        for (x, y) in [(x0 + i * step, y0), (x0 + i * step, y0 + (n - 1) * step)]:
            out.append(f'<rect class="{cols[k % 4]}" x="{x}" y="{y}" width="{size}" height="{size}" rx="1.5"/>'); k += 1
    for j in range(1, n - 1):
        for (x, y) in [(x0, y0 + j * step), (x0 + (n - 1) * step, y0 + j * step)]:
            out.append(f'<rect class="{cols[k % 4]}" x="{x}" y="{y}" width="{size}" height="{size}" rx="1.5"/>'); k += 1
    return "".join(out)

HEART = "M32 38C22 31 22 23 27 22C30 21 32 24 32 25C32 24 34 21 37 22C42 23 42 31 32 38Z"
ICONS = {
    "a1": '<rect class="f-violet st" x="8" y="18" width="48" height="36" rx="4"/><rect class="f-amber st" x="8" y="18" width="48" height="12" rx="4"/>'
          + disc(22, 40, 6, "f-coral", "f-coral2") + card(33, 35, 14, 12, "f-white"),
    "a2": '<rect class="f-beige st" x="8" y="8" width="48" height="48" rx="4"/>' + border_squares(12, 12, 5, 7, 2)
          + disc(32, 30, 5, "f-sky", "f-sky2"),
    "a3": '<rect class="f-white st" x="7" y="26" width="27" height="27" rx="6"/>' + pips([(14, 33), (20.5, 39.5), (27, 46)])
          + '<g transform="rotate(14 44 26)"><rect class="f-coral st" x="31" y="13" width="26" height="26" rx="6"/>'
          + pips([(38, 20), (50, 20), (38, 32), (50, 32)], "f-white") + '</g>',
    "a4": disc(23, 38, 13, "f-sky", "f-sky2") + disc(42, 28, 13, "f-coral", "f-coral2"),
    "a5": card(19, 14, 28, 38, "f-violet", 9) + card(17, 12, 28, 38, "f-violet", -5) + card(18, 10, 28, 38, "f-white")
          + f'<path class="f-coral" transform="translate(0 -2)" d="{HEART}"/>',
    "a6": "".join(card(23, 12, 18, 30, f, a, 32, 58) for f, a in [("f-sky", -36), ("f-amber", -12), ("f-leaf", 12), ("f-coral", 36)]),
    "a7": "".join(f'<rect class="{"f-amber" if (i, j) == (1, 1) else "f-beige"} st" x="{10 + i*15}" y="{10 + j*15}" width="14" height="14" rx="2"/>'
                  for i in range(3) for j in range(3)) + disc(32, 30, 5, "f-sky", "f-sky2"),
    "a8": '<rect class="f-white st" x="14" y="8" width="36" height="48" rx="4"/><rect class="f-coral st" x="14" y="8" width="36" height="9" rx="4"/>'
          + '<path class="ln" d="M21 25v14M26 25v14M31 25v14M36 25v14M18 36l22-8"/>'
          + '<path class="f-amber st" d="M42 41l2.4 4.8 5.3.8-3.8 3.7.9 5.3-4.8-2.5-4.8 2.5.9-5.3-3.8-3.7 5.3-.8z"/>',
    "b1": '<rect class="f-beige st" x="7" y="32" width="50" height="24" rx="3"/>' + disc(20, 42, 5, "f-coral", "f-coral2")
          + card(36, 37, 12, 14, "f-violet") + arrow("M44 6v16", "M38 20h12l-6 8z")
          + '<path class="f-amber" d="M16 10l2 5 5 2-5 2-2 5-2-5-5-2 5-2z"/>',
    "b2": '<path class="ln" d="M6 22h12M4 32h14M8 42h10"/>'
          + '<g transform="rotate(-18 38 32)"><rect class="f-white st" x="22" y="16" width="32" height="32" rx="7"/>'
          + pips([(30, 24), (46, 24), (38, 32), (30, 40), (46, 40)]) + '</g>',
    "b3": card(10, 22, 20, 30, "f-sky", -14) + card(34, 22, 20, 30, "f-coral", 14)
          + '<path class="ln" d="M18 16c6-9 22-9 28 0"/><path class="f-ink" d="M42 10l7 7-9 2z"/>',
    "b4": card(24, 38, 16, 20, "f-violet") + card(6, 12, 14, 19, "f-white", -24) + card(25, 5, 14, 19, "f-white")
          + card(44, 12, 14, 19, "f-white", 24) + '<path class="ln dash" d="M28 36l-12-6M32 35V26M36 36l12-6"/>',
    "b5": card(16, 34, 30, 22, "f-violet") + card(14, 30, 30, 22, "f-violet") + card(18, 8, 26, 20, "f-white", -8)
          + arrow("M52 36V14", "M46 17h12l-6-8z"),
    "b6": card(6, 20, 20, 28, "f-sky") + card(38, 20, 20, 28, "f-coral")
          + '<path class="ln" d="M22 14c6-6 14-6 20 0"/><path class="f-ink" d="M38 8l7 8-10 1z"/>'
          + '<path class="ln" d="M42 54c-6 6-14 6-20 0"/><path class="f-ink" d="M26 60l-7-8 10-1z"/>',
    "b7": '<path class="f-amber st" d="M12 50l8-12h32l-8 12z"/>' + '<path class="ln dash" d="M32 14v16"/>'
          + '<path class="f-ink" d="M26 28h12l-6 7z"/>' + disc(32, 9, 8, "f-sky", "f-sky2"),
    "b8": '<path class="f-box st" d="M12 30h40v24H12z"/><path class="f-box2 st" d="M12 30l-6-8h40l6 8z"/>'
          + card(22, 8, 14, 18, "f-white", -10) + arrow("M46 6v14", "M40 18h12l-6 8z"),
    "c1": disc(32, 34, 10, "f-sky", "f-sky2")
          + '<path class="ln" d="M14 30a18 18 0 1 1 6 16"/><path class="f-ink" d="M10 42l12 2-4 10z"/>',
    "c2": disc(26, 38, 14, "f-sky", "f-sky2") + '<circle class="f-coral st" cx="44" cy="20" r="13"/>'
          + '<rect class="f-white" x="38.5" y="13" width="4" height="14" rx="1"/><rect class="f-white" x="45.5" y="13" width="4" height="14" rx="1"/>',
    "c3": '<path class="f-teal st" d="M6 16h52v36H6z"/><path class="f-white st" d="M9 14c8-3 16-3 23 2v34c-7-5-15-5-23-2z"/>'
          + '<path class="f-white st" d="M55 14c-8-3-16-3-23 2v34c7-5 15-5 23-2z"/>'
          + '<path class="ln thin" d="M14 22h13M14 28h13M14 34h10M37 22h13M37 28h13M37 34h10"/>',
    "c4": '<path class="f-amber st" d="M20 8h24v14a12 12 0 0 1-24 0z"/><path class="ln" d="M20 12h-7c0 9 3 12 8 13M44 12h7c0 9-3 12-8 13"/>'
          + '<rect class="f-amber st" x="28" y="34" width="8" height="10"/><rect class="f-violet st" x="18" y="44" width="28" height="10" rx="2"/>',
    "c5": '<path class="ln" d="M32 10v38M12 18h40"/><path class="f-violet st" d="M22 52h20v6H22z"/>'
          + '<path class="f-sky st" d="M4 34h16a8 5 0 0 1-16 0z"/><path class="f-coral st" d="M44 34h16a8 5 0 0 1-16 0z"/>'
          + '<path class="ln thin" d="M12 18l-8 16M12 18l8 16M52 18l-8 16M52 18l8 16"/>',
    "c6": card(20, 26, 26, 32, "f-white", 6) + f'<path class="f-coral" transform="translate(1 12) scale(.8) translate(8 8)" d="{HEART}"/>'
          + '<path class="f-white st" d="M14 16c8-10 26-10 34 0c-8 10-26 10-34 0z"/><circle class="f-dark" cx="38" cy="16" r="4.5"/>',
    "c7": '<path class="f-grey st" d="M14 22a8 8 0 0 1 8-10a10 10 0 0 1 19 1a7 7 0 0 1 9 9z"/><path class="f-amber st" d="M34 22l-4 7h5l-3 7"/>'
          + '<circle class="f-yellow st" cx="32" cy="44" r="15"/><circle class="f-dark" cx="26" cy="43" r="2"/><circle class="f-dark" cx="38" cy="43" r="2"/>'
          + '<path class="ln thin" d="M22 37l7 3M42 37l-7 3M26 53c4-4 8-4 12 0"/>',
    "c8": '<path class="ln" d="M32 34c2 10 6 16 12 22"/>'
          + "".join(f'<circle class="f-leaf st" cx="{x}" cy="{y}" r="10"/>' for x, y in [(24, 22), (40, 22), (24, 38), (40, 38)])
          + '<circle class="f-leaf2" cx="32" cy="30" r="5"/>',
    "c9": '<path class="ln" d="M14 30a18 18 0 0 1 32-11"/><path class="f-ink" d="M50 10l-1 13-11-4z"/>'
          + '<path class="ln" d="M50 34a18 18 0 0 1-32 11"/><path class="f-ink" d="M14 54l1-13 11 4z"/>'
          + '<rect class="f-white st" x="23" y="23" width="18" height="18" rx="4"/>' + pips([(28, 28), (36, 36)]),
}

def icon(wid, size=56, label=""):
    return (f'<svg class="ic" viewBox="0 0 64 64" width="{size}" height="{size}" aria-hidden="true">{ICONS[wid]}</svg>')

PLAY = '<svg viewBox="0 0 12 12" class="ico-play" aria-hidden="true"><path d="M2 1l9 5-9 5z"/></svg><svg viewBox="0 0 12 12" class="ico-stop" aria-hidden="true"><rect x="2" y="2" width="8" height="8" rx="1"/></svg>'

def var_attr(var):
    return E(";".join(f"{p}|{w}" for p, w in var), quote=True)

def var_rows(var):
    others = [(p, w) for p, w in var if p.split(",")[0] != "UK"]
    return "".join(f'<div class="var"><span class="pl-tag">{E(p)}</span>{E(w)}</div>' for p, w in others)

# ---------- word bank ----------
def word_cards():
    out = []
    for gid, zh, en, items in GROUPS:
        cards = []
        for wid, word, mean, ex, exzh, var, note in items:
            tag = '<span class="uk">UK</span>' if var else ""
            if gid == "talk":
                cards.append(
                    f'<article class="card say" id="{wid}"><button class="hw playable" type="button" data-src="audio/w/{wid}.mp3">'
                    f'<span class="pbtn">{PLAY}</span><span>{E(word)}{tag}</span></button>'
                    f'<p class="mean">{E(mean)}</p>{var_rows(var) if var else ""}</article>')
                continue
            cards.append(
                f'<article class="card" id="{wid}"><div class="head">{icon(wid)}<div>'
                f'<button class="hw playable" type="button" data-src="audio/w/{wid}.mp3"><span>{E(word)}{tag}</span><span class="pbtn">{PLAY}</span></button>'
                f'<p class="mean">{E(mean)}</p>{var_rows(var) if var else ""}</div></div>'
                f'<button class="ex playable" type="button" data-src="audio/w/{wid}e.mp3"><span class="pbtn">{PLAY}</span><span>{E(ex)}</span></button>'
                f'<p class="exzh zh">{E(exzh)}</p>'
                + (f'<p class="note">{E(note)}</p>' if note else "") + '</article>')
        out.append(f'<div class="group" id="g-{gid}"><h3><span>{E(en)}</span> <small>{len(items)}</small></h3>'
                   f'<div class="cards {"sayings" if gid == "talk" else ""}">{"".join(cards)}</div></div>')
    return "".join(out)

# ---------- dialogues ----------
def render_line(markup):
    out, pos = [], 0
    pat = re.compile(r"\[([a-d]\d):([^\]]+)\]|\{([^|}]+)\|([^|}]*)\|([^}]*)\}")
    for m in pat.finditer(markup):
        out.append(E(markup[pos:m.start()]))
        if m.group(1):
            wid, text = m.group(1), m.group(2)
            word, zh, var = ITEMS[wid]
            cls = "wb v" if var else "wb"
            extra = f' data-var="{var_attr(var)}" data-here="UK"' if var else ""
            out.append(f'<span class="{cls}" tabindex="0" data-en="{E(word, quote=True)}" data-zh="{E(zh, quote=True)}"{extra}>{E(text)}</span>')
        else:
            note = f' data-note="{E(m.group(5), quote=True)}"' if m.group(5) else ""
            out.append(f'<span class="g" tabindex="0" data-zh="{E(m.group(4), quote=True)}"{note}>{E(m.group(3))}</span>')
        pos = m.end()
    out.append(E(markup[pos:]))
    return "".join(out)

def scenes():
    out = []
    for n, (sid, title, intro, ic, lines) in enumerate(SCENES, 1):
        lis = []
        for i, (who, markup, zh) in enumerate(lines, 1):
            side = "me" if who == "W" else "them"
            lis.append(
                f'<li class="line seq {side} p-{who}" data-src="audio/{sid}/{i:02d}.mp3"><span class="av" aria-hidden="true">{avatar(who)}</span>'
                f'<div class="bub"><span class="who">{NAMES[who]}</span><p class="en">{render_line(markup)}</p><p class="zh">{E(zh)}</p></div>'
                f'<button class="pl" type="button" aria-label="Play line {i}">{PLAY}</button></li>')
        out.append(
            f'<section class="scene" id="{sid}" aria-labelledby="{sid}-h"><div class="scene-head">{icon(ic, 52)}<div>'
            f'<p class="kicker">Part {n} of {len(SCENES)}</p><h2 id="{sid}-h">{E(title)}</h2><p class="intro">{E(intro)}</p></div></div>'
            f'<div class="bar"><button class="btn play-all" type="button" data-scene="{sid}">{PLAY}<span class="lbl">Play all</span></button></div>'
            f'<ol class="dlg">{"".join(lis)}</ol></section>')
    return "".join(out)


# ---------- readings ----------
def plain_words(markup):
    t = re.sub(r"\[[a-d]\d:([^\]]+)\]", r"\1", markup)
    return re.sub(r"\{([^|}]+)\|[^|}]*\|[^}]*\}", r"\1", t)

def readings():
    out = []
    for rid, kicker, title, who, ic, paras in READINGS:
        words = sum(len(plain_words(" ".join(s)).split()) for s, _ in paras)
        body, i = [], 0
        for sentences, zh in paras:
            spans = []
            for sentence in sentences:
                i += 1
                spans.append(f'<span class="s seq" data-src="audio/{rid}/{i:02d}.mp3">{render_line(sentence)}</span>')
            body.append(f'<p class="para">{" ".join(spans)}</p><p class="zh pzh">{E(zh)}</p>')
        out.append(
            f'<article class="read" id="{rid}" aria-labelledby="{rid}-h"><div class="scene-head">{icon(ic, 52)}<div>'
            f'<p class="kicker">{E(kicker)}</p><h2 id="{rid}-h">{E(title)}</h2>'
            f'<p class="intro">{words} words · about {round(words / 150)} min · read by {NAMES[who]}</p></div></div>'
            f'<div class="bar"><button class="btn play-all" type="button" data-scene="{rid}">{PLAY}<span class="lbl">Play all</span></button>'
            f'<span class="hint">Click any sentence to hear it.</span></div>'
            f'<div class="read-body">{"".join(body)}</div></article>')
    return "".join(out)

def cast():
    return "".join(f'<div class="person p-{w}"><span class="av av-lg" aria-hidden="true">{avatar(w)}</span>'
                   f'<div><b>{NAMES[w]}</b><p>{E(bio)}</p></div></div>' for w, bio in BIOS.items())

n_words = sum(len(g[3]) for g in GROUPS)
n_lines = sum(len(s[4]) for s in SCENES)
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
page = (tpl.replace("{{WORDS}}", word_cards()).replace("{{SCENES}}", scenes()).replace("{{CAST}}", cast()).replace("{{READINGS}}", readings())
        .replace("{{N_WORDS}}", str(n_words)).replace("{{N_LINES}}", str(n_lines))
        .replace("{{SOURCES}}", "".join(f'<li><a href="{E(u, quote=True)}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in SOURCES))
        .replace("{{READ_SOURCES}}", "".join(f'<li><a href="{E(u, quote=True)}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in READ_SOURCES)))
open(os.path.join(HERE, "game-night.html"), "w", encoding="utf-8").write(page)
print("words", n_words, "lines", n_lines, "bytes", len(page.encode()))
