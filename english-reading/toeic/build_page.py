# Builds toeic.html from content.py and template.html, after checking every item.
#   python build_page.py            refuses to build if any hand-written item is not reviewed
#   python build_page.py --draft    builds anyway (for local testing only)
import json, os, sys
from content import ITEMS, UNITS

HERE = os.path.dirname(os.path.abspath(__file__))
LIMITS = {"point": 40, "why": 90, "wrong": 45}
errors, warnings = [], []

def check_explain(where, ex, n_opts, answer):
    for k in ("point", "why"):
        if not isinstance(ex.get(k), str) or not ex[k].strip(): errors.append(f"{where}: explain.{k} missing")
        elif len(ex[k]) > LIMITS[k]: warnings.append(f"{where}: explain.{k} is {len(ex[k])} chars (limit {LIMITS[k]})")
    w = ex.get("wrong")
    if not isinstance(w, list) or len(w) != n_opts: errors.append(f"{where}: explain.wrong must have {n_opts} entries"); return
    for i, x in enumerate(w):
        if i == answer and x is not None: errors.append(f"{where}: wrong[{i}] must be None (it is the answer)")
        if i != answer and (not isinstance(x, str) or not x.strip()): errors.append(f"{where}: wrong[{i}] missing")
        if isinstance(x, str) and len(x) > LIMITS["wrong"]: warnings.append(f"{where}: wrong[{i}] is {len(x)} chars")
    wm = ex.get("wrongMore")
    if wm is not None and (not isinstance(wm, list) or len(wm) != n_opts or wm[answer] is not None): errors.append(f"{where}: wrongMore must match options with None at the answer")
    for pair in ex.get("vocab") or []:
        if not (isinstance(pair, list) and len(pair) == 2): errors.append(f"{where}: vocab entries must be [word, 中文]")

seen = set()
for it in ITEMS:
    i = it.get("id", "?")
    if i in seen: errors.append(f"{i}: duplicate id")
    seen.add(i)
    if it.get("unit") not in UNITS: errors.append(f"{i}: unknown unit {it.get('unit')}")
    if it.get("level") not in (1, 2, 3): errors.append(f"{i}: level must be 1-3")
    if it.get("source") == "hand" and it.get("reviewed") is not True: errors.append(f"{i}: not reviewed yet")
    if it.get("format") == "gap":
        if it["stem"].count("______") != 1: errors.append(f"{i}: stem needs exactly one ______")
        if len(it["options"]) != 4 or len(set(it["options"])) != 4: errors.append(f"{i}: needs 4 different options")
        if not 0 <= it["answer"] < 4: errors.append(f"{i}: answer out of range")
        check_explain(i, it["explain"], 4, it["answer"])
        if not it["explain"].get("zh"): errors.append(f"{i}: explain.zh missing")
    else:
        lines = it["audio"]["lines"]
        g = it.get("graphic")
        if g is not None and not (isinstance(g.get("head"), list) and all(isinstance(r, list) and len(r) == len(g["head"]) for r in g.get("rows", []))): errors.append(f"{i}: graphic rows must match head")
        if len(it.get("transcriptZh", [])) != len(lines): errors.append(f"{i}: transcriptZh length differs from lines")
        for ln in lines:
            if not os.path.exists(os.path.join(HERE, it["audio"]["dir"], ln["file"])): errors.append(f"{i}: missing audio {ln['file']} (run make_audio.py)")
        for qi, q in enumerate(it["questions"]):
            n = 3 if it["format"] == "qr" else 4
            if it["format"] != "qr" and (len(q["options"]) != 4 or not q.get("q")): errors.append(f"{i} q{qi}: needs q and 4 options")
            if not 0 <= q["answer"] < n: errors.append(f"{i} q{qi}: answer out of range")
            check_explain(f"{i} q{qi}", q["explain"], n, q["answer"])
            for e in q["explain"].get("evidence") or []:
                if not 0 <= e < len(lines): errors.append(f"{i} q{qi}: evidence {e} out of range")

for w in warnings: print("warning:", w)
if errors:
    for e in errors: print("error:", e)
    if "--draft" not in sys.argv: sys.exit(f"{len(errors)} errors, not building")

data = {"units": {k: {"zh": v[0], "group": v[1]} for k, v in UNITS.items()}, "items": ITEMS}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("{{BANK}}", blob)
open(os.path.join(HERE, "toeic.html"), "w", encoding="utf-8").write(page)
count = lambda t: sum(1 for x in ITEMS if x["type"] == t)
print("items", len(ITEMS), "grammar", count("grammar"), "vocab", count("vocab"), "listen", count("listen"), "bytes", len(page.encode()))
