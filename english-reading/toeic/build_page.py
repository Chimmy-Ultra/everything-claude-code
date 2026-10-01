# Builds toeic.html (The Workbook) from content.py, en/*.json and template.html, after checking every item.
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

# English explanations and word cards (en/<items file>.json, checked by en/check.py); IPA comes from the CMU dictionary.
sys.path.insert(0, os.path.join(HERE, "en"))
import importlib, check as en_check
from ipa import ipa
EN = {}
for name in ("items_grammar_a", "items_grammar_b", "items_grammar_c", "items_vocab", "items_vocab_b", "items_listen", "items_listen_b", "items_grammar_d", "items_vocab_c", "items_listen_c",
             "items_listen_d", "items_listen_e", "items_listen_f", "items_grammar_e", "items_grammar_f", "items_grammar_g", "items_grammar_h"):
    if not os.path.exists(os.path.join(HERE, name + ".py")): continue
    path = os.path.join(HERE, "en", name + ".json")
    if not os.path.exists(path): errors.append(f"en/{name}.json missing"); continue
    for e in en_check.check(name): errors.append(f"en/{name}: {e}")
    EN.update({k: v for k, v in json.load(open(path, encoding="utf-8")).items() if k != "_flags"})
no_ipa = []
for it in ITEMS:
    e = EN.get(it["id"])
    if not e:
        if it.get("source") == "hand": errors.append(f"{it['id']}: no English explanation")
        continue
    it["gloss"] = [dict(g, ipa=ipa(g["hw"]) or "") for g in e.get("gloss", [])]
    no_ipa += [g["hw"] for g in it["gloss"] if not g["ipa"]]
    if it["format"] == "gap":
        it["en"] = {k: e[k] for k in ("point", "why", "usage") if k in e}
    else:
        for q, x in zip(it["questions"], e["q"]): q["en"] = x
if no_ipa: print("no IPA in the CMU dictionary (card shows none):", ", ".join(sorted(set(no_ipa))))

# Chapter lessons (lessons/<unit>.json, checked by lessons/check.py); every chapter with questions needs one.
sys.path.insert(0, os.path.join(HERE, "lessons"))
import importlib.util
_spec = importlib.util.spec_from_file_location("lesson_check", os.path.join(HERE, "lessons", "check.py"))
lesson_check = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(lesson_check)
LESSONS = {}
for u in UNITS:
    if not any(x["unit"] == u for x in ITEMS): continue
    for e in lesson_check.check(u): errors.append("lesson " + e)
    path = os.path.join(HERE, "lessons", u + ".json")
    if os.path.exists(path):
        d = json.load(open(path, encoding="utf-8")); d.pop("_flags", None); LESSONS[u] = d

# Word cards (words/cards/*.json, checked by words/check.py): TSL 1.2 words that appear in the questions.
import csv, glob, re as _re
_spec2 = importlib.util.spec_from_file_location("word_check", os.path.join(HERE, "words", "check.py"))
word_check = importlib.util.module_from_spec(_spec2); _spec2.loader.exec_module(word_check)
_forms = {}
for row in csv.reader(l for l in open(os.path.join(HERE, "words", "tsl", "TSL_12_lemmatized_for_teaching.csv"), encoding="latin-1") if not l.startswith("#")):
    row = [x.strip().lower() for x in row if x.strip()]
    if row: _forms.setdefault(row[0], set()).update(row)
def _text(it):
    if it["format"] == "gap": return it["stem"] + " " + " ".join(it["options"])
    return " ".join(l["text"] for l in it["audio"]["lines"]) + " " + " ".join(" ".join(q.get("options") or []) for q in it["questions"])
_tok = {it["id"]: set(_re.findall(r"[a-z]+(?:-[a-z]+)?", _text(it).lower())) for it in ITEMS if it.get("reviewed") or it.get("source") != "hand"}
WORDS = []
for f in sorted(glob.glob(os.path.join(HERE, "words", "cards", "*.json"))):
    for c in json.load(open(f, encoding="utf-8")):
        for e in word_check.check_card(c): errors.append("word " + e)
        fs = _forms.get(c["w"], {c["w"]})
        c = dict(c, ipa=ipa(c["w"]) or "", items=[i for i, t in _tok.items() if t & fs][:12])
        if c["items"]: WORDS.append(c)
        else: print("word card left out (no question uses it):", c["w"])
WORDS.sort(key=lambda c: c["w"])
# Word stories (words/stories/: plan.json + one file per story, checked by words/check_stories.py)
STORIES = []
if os.path.exists(os.path.join(HERE, "words", "stories", "plan.json")):
    _spec3 = importlib.util.spec_from_file_location("story_check", os.path.join(HERE, "words", "check_stories.py"))
    story_check = importlib.util.module_from_spec(_spec3); _spec3.loader.exec_module(story_check)
    for e in story_check.check(): errors.append("story " + e)
    for s_ in json.load(open(os.path.join(HERE, "words", "stories", "plan.json"), encoding="utf-8")):
        path = os.path.join(HERE, "words", "stories", s_["id"] + ".json")
        if os.path.exists(path):
            d = json.load(open(path, encoding="utf-8"))
            STORIES.append({"id": s_["id"], "title": d["title"], "paras": d["paras"], "words": s_["words"]})

# Point each tap-to-gloss entry at a word card: its own headword, or else a card word inside the phrase
# ("under warranty" -> warranty), read right to left because the head noun usually comes last.
_head = {f: h for h, fs in _forms.items() for f in fs}
_cards = {c["w"] for c in WORDS}
for it in ITEMS:
    for g in it.get("gloss", []):
        toks = _re.findall(r"[a-z]+(?:-[a-z]+)?", (g["hw"] + " " + g["w"]).lower())
        hit = g["hw"].lower() if g["hw"].lower() in _cards else next((_head.get(t, t) for t in reversed(toks) if _head.get(t, t) in _cards), None)
        if hit: g["card"] = hit

for w in warnings: print("warning:", w)
if errors:
    for e in errors: print("error:", e)
    if "--draft" not in sys.argv: sys.exit(f"{len(errors)} errors, not building")

data = {"units": {k: {"zh": v[0], "group": v[1], "en": v[2]} for k, v in UNITS.items()}, "items": ITEMS, "lessons": LESSONS, "words": WORDS, "stories": STORIES}
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("{{BANK}}", blob)
open(os.path.join(HERE, "toeic.html"), "w", encoding="utf-8").write(page)
count = lambda t: sum(1 for x in ITEMS if x["type"] == t)
print("items", len(ITEMS), "grammar", count("grammar"), "vocab", count("vocab"), "listen", count("listen"), "bytes", len(page.encode()))
