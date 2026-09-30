# Builds the Scene Lab pages from content.py and the *.template.html files.  python build.py
import json, os, re
from content import OBJECTS, INTENTS, BARISTA, STEPS

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three"]

def parts(chunk):
    out, pos = [], 0
    for m in re.finditer(r"\{([^}]+)\}", chunk):
        out += [chunk[pos:m.start()], m.group(1).split("|")]
        pos = m.end()
    out.append(chunk[pos:])
    return [p for p in out if p != ""]

def read(name):
    p = os.path.join(HERE, name)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else ""

hot = json.loads(read("cafe-hotspots.json") or "{}")
data = {
    "objects": [{"id": i, "word": w, "zh": z, "ex": e, "exzh": ez, "var": v, "at": hot.get(i)} for i, w, z, e, ez, v in OBJECTS],
    "intents": [{"id": i, "zh": z, "en": e, "phrases": [{"id": p, "parts": parts(c), "zh": pz, "note": n} for p, c, pz, n in items]}
                for i, z, e, items in INTENTS],
    "barista": [{"id": b, "en": l, "zh": z, "reply": r} for b, l, z, r in BARISTA],
    "steps": [{"en": e, "zh": z, "hear": h, "say": s} for e, z, h, s in STEPS],
}
n_frames = sum(len(i[3]) for i in INTENTS)
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
subs = {"{{BASE_CSS}}": read("base.css"), "{{DATA}}": blob, "{{SVG}}": read("cafe-scene.svg"),
        "{{N_FRAMES}}": WORDS[n_frames].capitalize(),
        # published artifact links, for the Scene Lab index
        "{{URL_A}}": "https://claude.ai/artifact/6ZAh8bGdo2RdE4ayGajFfL",
        "{{URL_B}}": "https://claude.ai/artifact/QFq6dd4QU7mSXq4zShWvoJ",
        "{{URL_C}}": "https://claude.ai/artifact/MNtaUjg3H7if7aoxXpCUxL"}
for tpl in sorted(f for f in os.listdir(HERE) if f.endswith(".template.html")):
    page = read(tpl)
    for k, v in subs.items():
        page = page.replace(k, v)
    out = tpl.replace(".template", "")
    open(os.path.join(HERE, out), "w", encoding="utf-8").write(page)
    print(out, len(page.encode()), "bytes")
