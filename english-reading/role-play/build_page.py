# Builds role-play.html from ../game-night/content.py.  python build_page.py
# The page reads audio from audio/ (artifact publish) and falls back to ../game-night/audio/ (repo checkout).
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "game-night"))
from content import SCENES, NAMES, BIOS

def plain(markup):
    s = re.sub(r"\[[a-d]\d:([^\]]+)\]", r"\1", markup)
    return re.sub(r"\{([^|}]+)\|[^|}]*\|[^}]*\}", r"\1", s)

def keys(markup):
    # Word-bank terms and new phrases in the line: the words worth hinting at.
    return [m.group(1) or m.group(2) for m in re.finditer(r"\[[a-d]\d:([^\]]+)\]|\{([^|}]+)\|", markup)]

AV_PATH = os.path.join(HERE, "..", "avatars", "avatars.json")
AVATARS = json.load(open(AV_PATH, encoding="utf-8")) if os.path.exists(AV_PATH) else {}

data = {
    "names": NAMES,
    "bios": BIOS,
    "avatars": {k: v for k, v in AVATARS.items() if k in NAMES},
    "scenes": [
        {"id": sid, "title": title, "intro": intro,
         "lines": [{"who": who, "en": plain(markup), "zh": zh, "keys": keys(markup), "src": f"{sid}/{i:02d}.mp3"}
                   for i, (who, markup, zh) in enumerate(lines, 1)]}
        for sid, title, intro, _, lines in SCENES
    ],
}

blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
page = tpl.replace("{{DATA}}", blob)
open(os.path.join(HERE, "role-play.html"), "w", encoding="utf-8").write(page)
print("scenes", len(data["scenes"]), "lines", sum(len(s["lines"]) for s in data["scenes"]), "bytes", len(page.encode()))
