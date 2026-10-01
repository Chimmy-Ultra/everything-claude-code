# Checks words/stories/ against words/STORIES.md.   python3 words/check_stories.py [s01 s02 …]
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ZH = re.compile(r"[一-鿿]")
MARK = re.compile(r"\{\{([^|{}]+)\|([^{}]+)\}\}")
BANNED = re.compile(r"!{2,}|[\U0001F300-\U0001FAFF]|\bTOEIC\b|\btoday we will\b|\blet's learn\b", re.I)


def cards():
    out = set()
    for f in glob.glob(os.path.join(HERE, "cards", "*.json")):
        out |= {c["w"] for c in json.load(open(f, encoding="utf-8"))}
    return out


def check(only=()):
    errs = []
    plan = json.load(open(os.path.join(HERE, "stories", "plan.json"), encoding="utf-8"))
    cw = cards(); seen = {}
    for s in plan:
        for w in s["words"]:
            if w not in cw: errs.append(f"plan {s['id']}: '{w}' has no card")
            if w in seen: errs.append(f"plan: '{w}' in both {seen[w]} and {s['id']}")
            seen[w] = s["id"]
    missing = cw - set(seen)
    if missing: errs.append(f"plan: {len(missing)} card words in no story: {sorted(missing)[:12]}")
    for s in plan:
        if only and s["id"] not in only: continue
        path = os.path.join(HERE, "stories", s["id"] + ".json")
        if not os.path.exists(path): errs.append(f"{s['id']}: missing"); continue
        d = json.load(open(path, encoding="utf-8"))
        t = d.get("title")
        if not (isinstance(t, list) and len(t) == 2 and ZH.search(t[1])): errs.append(f"{s['id']}: title must be [English, Chinese]")
        paras = d.get("paras", [])
        if not 3 <= len(paras) <= 5: errs.append(f"{s['id']}: 3-5 paragraphs")
        marked, words = [], 0
        for i, p in enumerate(paras):
            if not (isinstance(p, list) and len(p) == 2 and ZH.search(p[1])): errs.append(f"{s['id']} para {i}: must be [English, Chinese]"); continue
            if BANNED.search(p[0]): errs.append(f"{s['id']} para {i}: banned phrase or mark")
            if "{{" in MARK.sub("", p[0]) or "}}" in MARK.sub("", p[0]): errs.append(f"{s['id']} para {i}: broken {{…}} mark")
            marked += [m.group(1).strip() for m in MARK.finditer(p[0])]
            words += len(MARK.sub(lambda m: m.group(2), p[0]).split())
        if not 130 <= words <= 220: errs.append(f"{s['id']}: {words} words (want 130-220)")
        want = set(s["words"])
        for w in marked:
            if w not in want: errs.append(f"{s['id']}: marks '{w}', which is not in its plan")
        for w in want:
            n = marked.count(w)
            if n != 1: errs.append(f"{s['id']}: '{w}' marked {n} times (want 1)")
    return errs


if __name__ == "__main__":
    e = check(set(sys.argv[1:]))
    print("\n".join(e) if e else "ok")
    sys.exit(1 if e else 0)
