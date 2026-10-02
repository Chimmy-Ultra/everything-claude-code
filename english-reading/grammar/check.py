# Checks grammar book chapters against STYLE.md.   python3 check.py [chapters/01-pos.json …]   (no args: all chapters)
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = ["pos", "skeleton", "clause", "tense", "voice", "verbforms", "agree", "connect", "relative", "conditional",
       "pronoun", "compare", "quantity", "parallel", "prep", "mandative"]
UNITS = {"pos", "tense", "voice", "participle", "connect", "agree", "relative", "pronoun", "prep", "toing", "mandative",
         "conditional", "compare", "quantity", "parallel"}
TAGS = re.compile(r"<(?!/?(em|b|u)>)[^>]*>")
BANNED = re.compile(r"最常考|必考|每場|每次考試|考\s*\d+\s*題|出現率|官方規定|讓我們|記住|小提醒|！|!")


def check(path):
    errs = []
    try: d = json.load(open(path, encoding="utf-8"))
    except Exception as e: return [f"{path}: not valid JSON ({e})"]
    name = os.path.basename(path)
    if d.get("id") not in IDS: return [f"{name}: unknown id {d.get('id')}"]
    if d.get("n") != IDS.index(d["id"]) + 1 or name != f"{d['n']:02d}-{d['id']}.json": errs.append(f"{name}: n/id/file name disagree")

    def text(where, s, html=True):
        if not isinstance(s, str) or not s.strip(): errs.append(f"{where}: missing"); return
        if html and TAGS.search(s): errs.append(f"{where}: only <em>, <b>, <u> allowed")
        for t in ("em", "b", "u"):
            if s.count(f"<{t}>") != s.count(f"</{t}>"): errs.append(f"{where}: unbalanced <{t}>")
        if BANNED.search(re.sub(r"<em>.*?</em>", "", s)): errs.append(f"{where}: banned phrase or mark ({BANNED.search(s).group(0)})")

    def quiz(where, q):
        t = q.get("type")
        text(f"{where}.q", q.get("q")); text(f"{where}.why", q.get("why"))
        if t == "choose":
            o = q.get("options")
            if not (isinstance(o, list) and 2 <= len(o) <= 4 and len(set(o)) == len(o)): errs.append(f"{where}: 2-4 different options")
            elif not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(o)): errs.append(f"{where}: answer out of range")
            for i, x in enumerate(o or []): text(f"{where}.options[{i}]", x)
        elif t == "tap":
            s = q.get("sentence", ""); n = len(s.split())
            text(f"{where}.sentence", s, html=False)
            if "<" in s: errs.append(f"{where}: sentence must be plain text")
            a = q.get("answer")
            if not (isinstance(a, list) and a and all(isinstance(i, int) and 0 <= i < n for i in a) and len(set(a)) == len(a)): errs.append(f"{where}: answer must be word positions 0..{n - 1}")
        else: errs.append(f"{where}: type must be choose or tap")

    text("title", d.get("title"), html=False); text("en", d.get("en"), html=False); text("lead", d.get("lead"))
    ch = d.get("check", [])
    if not 3 <= len(ch) <= 5: errs.append(f"{name}: check needs 3-5 items")
    for i, q in enumerate(ch): quiz(f"{name} check[{i}]", q)
    secs = d.get("sections", [])
    if not 4 <= len(secs) <= 9: errs.append(f"{name}: 4-9 sections")
    nq = 0
    for i, s in enumerate(secs):
        w = f"{name} sections[{i}]"
        text(f"{w}.h", s.get("h"), html=False); text(f"{w}.takeaway", s.get("takeaway"))
        if not s.get("body"): errs.append(f"{w}: body missing")
        for j, p in enumerate(s.get("body", [])): text(f"{w}.body[{j}]", p)
        ex = s.get("ex", [])
        if not 1 <= len(ex) <= 5: errs.append(f"{w}: 1-5 examples")
        for j, e in enumerate(ex):
            text(f"{w}.ex[{j}].en", e.get("en")); text(f"{w}.ex[{j}].zh", e.get("zh"))
            if "note" in e: text(f"{w}.ex[{j}].note", e["note"])
        t = s.get("table")
        if t is not None and not (isinstance(t.get("head"), list) and t.get("rows") and all(len(r) == len(t["head"]) for r in t["rows"])): errs.append(f"{w}: table rows must match head")
        for r in (t or {}).get("rows", []):
            for c in r: text(f"{w}.table cell", c)
        for j, q in enumerate(s.get("quiz", [])): quiz(f"{w}.quiz[{j}]", q); nq += 1
        extra = set(s) - {"h", "body", "ex", "table", "quiz", "takeaway"}
        if extra: errs.append(f"{w}: unknown keys {sorted(extra)}")
    if not 4 <= nq <= 10: errs.append(f"{name}: {nq} section quizzes (want 4-10)")
    ms = d.get("mistakes", [])
    if not 2 <= len(ms) <= 5: errs.append(f"{name}: 2-5 mistakes")
    for i, m in enumerate(ms):
        for k in ("wrong", "right", "why"): text(f"{name} mistakes[{i}].{k}", m.get(k))
        if m.get("wrong") == m.get("right"): errs.append(f"{name} mistakes[{i}]: wrong equals right")
    wb = d.get("workbook")
    if not isinstance(wb, list) or not set(wb) <= UNITS: errs.append(f"{name}: workbook must list Workbook unit ids")
    extra = set(d) - {"id", "n", "title", "en", "lead", "check", "sections", "mistakes", "workbook", "_flags"}
    if extra: errs.append(f"{name}: unknown keys {sorted(extra)}")
    return errs


if __name__ == "__main__":
    paths = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "chapters", "*.json")))
    bad = 0
    for p in paths:
        e = check(p); bad += bool(e)
        print("\n".join(e) if e else f"{os.path.basename(p)}: ok")
    sys.exit(1 if bad else 0)
