# Builds ffh-game-night.html from content.py.  python build_page.py
import html, os, re
from content import SOCIAL, GAMES, NIGHT

HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape
PLAY = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 1l9 5-9 5z"/></svg>'

def en_html(text):
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="slot">{E(m.group(1))}</span>', E(text))

def phrase_rows(items):
    out = []
    for pid, en, zh, note in items:
        label = E(re.sub(r"[\[\]]", "", en))
        out.append(
            f'<li class="row"><button class="say" type="button" data-src="audio/p/{pid}.mp3" aria-label="Play: {label}">{PLAY}</button>'
            f'<p class="en">{en_html(en)}</p><button class="reveal" type="button">顯示英文</button>'
            f'<p class="zh">{E(zh)}</p>' + (f'<p class="note">{E(note)}</p>' if note else "") + "</li>")
    return f'<ul class="list">{"".join(out)}</ul>'

def social_section(sid, zh, en, sub, items):
    return (f'<section class="part" id="{sid}" aria-labelledby="{sid}-h"><div class="part-head">'
            f'<div><p class="kicker">{E(zh)}</p><h2 id="{sid}-h">{E(en)}</h2></div>'
            f'<button class="playall" type="button" data-all="{sid}">{PLAY} 全部播放</button>'
            f'<p class="sub">{E(sub)}</p></div>{phrase_rows(items)}</section>')

def game_panel(g):
    gid = g["id"]
    parts = [f'<article class="game" id="g-{gid}" aria-labelledby="g-{gid}-h"><div class="game-top">'
             f'<h3 id="g-{gid}-h">{E(g["name"])}</h3><span>{E(g["zh"])}</span><em>{E(g["kind"])}</em></div><div class="game-body">']
    parts.append(f'<h4>How it works</h4><p class="how">{E(" ".join(g["how"]))}</p><p class="how-zh">{E(g["how_zh"])}</p>')
    if g.get("warn"):
        parts.append(f'<p class="warn">{E(g["warn"])}</p>')
    if g.get("terms"):
        terms = "".join(f'<button class="term" type="button" data-src="audio/t/{gid}-{tid}.mp3">{PLAY}<b>{E(t)}</b><i>{E(zh)}</i></button>'
                        for tid, t, zh in g["terms"])
        parts.append(f'<h4>Words you\'ll hear</h4><div class="terms">{terms}</div>')
    if g.get("phrases"):
        parts.append(f'<h4>Things to say</h4>{phrase_rows(g["phrases"])}')
    if g.get("script"):
        sc = g["script"]
        lines = "".join(f'<li><button class="say" type="button" data-src="audio/s/{gid}-{i:02d}.mp3" aria-label="Play line {i}">{PLAY}</button>'
                        f'<p class="en">{E(en)}</p><p class="zh">{E(zh)}</p></li>' for i, (en, zh) in enumerate(sc["lines"], 1))
        parts.append(f'<h4>{E(sc["title"])}</h4><p class="how-zh">{E(sc["intro"])}</p>'
                     f'<div class="part-head" style="margin:8px 0 0"><button class="playall" type="button" data-all="sc-{gid}">{PLAY} 播放整段</button></div>'
                     f'<ol class="script" id="sc-{gid}">{lines}</ol>')
    src = " · ".join(f'<a href="{E(u)}" target="_blank" rel="noopener">{E(l)}</a>' for l, u in g["sources"])
    parts.append(f'<p class="src">Sources: {src}</p></div></article>')
    return "".join(parts)

def build():
    body = []
    by_id = {s[0]: s for s in SOCIAL}
    for key in [k for k, _ in NIGHT]:
        if key == "games":
            body.append('<section class="part" id="games" aria-labelledby="games-h"><div class="part-head">'
                        '<div><p class="kicker">遊戲</p><h2 id="games-h">The games on the flyer</h2></div>'
                        '<p class="sub">每款遊戲：怎麼玩、會聽到的字（點了會唸）、你可能要說的話。規則都附來源。</p></div>'
                        f'<div class="games">{"".join(game_panel(g) for g in GAMES)}</div></section>')
        else:
            body.append(social_section(*by_id[key]))
    night = "".join(f'<li><a href="#{k}"><b>{i:02d}</b>{E(label)}</a></li>' for i, (k, label) in enumerate(NIGHT, 1))
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    page = tpl.replace("%%NIGHT%%", night).replace("%%BODY%%", "\n".join(body))
    open(os.path.join(HERE, "ffh-game-night.html"), "w", encoding="utf-8").write(page)
    print("wrote ffh-game-night.html", len(page))

if __name__ == "__main__":
    build()
