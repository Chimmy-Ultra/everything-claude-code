# Checks word-card files against words/STYLE.md.   python3 words/check.py words/cards/a.json [...]   (no args: all files)
import csv, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TSL = {r["Word"].strip().lower() for r in csv.DictReader(open(os.path.join(HERE, "tsl", "TSL_12_stats.csv"), encoding="latin-1"))}
POS = {"n.", "v.", "adj.", "adv.", "prep.", "conj.", "pron."}
BANNED = re.compile(r"!|[\U0001F300-\U0001FAFF]|\b(let's|remember|note that|tip:)\b|\bTOEIC\b", re.I)
ZH = re.compile(r"[一-鿿]")


def pair(errs, where, p, max_words=None):
    if not (isinstance(p, list) and len(p) == 2 and all(isinstance(x, str) and x.strip() for x in p)):
        errs.append(f"{where}: must be [English, Chinese]"); return False
    en, zh = p
    if not ZH.search(zh): errs.append(f"{where}: Chinese twin has no Chinese")
    if BANNED.search(re.sub(r"<[^>]+>", "", en)): errs.append(f"{where}: banned word or mark")
    if max_words and len(re.sub(r"<[^>]+>", "", en).split()) > max_words: errs.append(f"{where}: more than {max_words} words")
    return True


def check_card(c):
    errs, w = [], c.get("w", "?")
    if w not in TSL: errs.append(f"{w}: not a TSL headword")
    ps = [x.strip() for x in str(c.get("pos", "")).split(",")]
    if not ps or any(x not in POS for x in ps): errs.append(f"{w}: pos must be from {sorted(POS)}")
    if not ZH.search(c.get("zh", "")): errs.append(f"{w}: zh missing")
    pair(errs, f"{w} def", c.get("def"), 20)
    ex = c.get("ex", [])
    if not 4 <= len(ex) <= 6: errs.append(f"{w}: 4-6 examples (has {len(ex)})")
    for i, e in enumerate(ex):
        if pair(errs, f"{w} ex[{i}]", e, 22):
            if "<em>" not in e[0] or e[0].count("<em>") != e[0].count("</em>"): errs.append(f"{w} ex[{i}]: wrap the word in <em>")
            if re.search(r"<(?!/?em>)[^>]*>", e[0] + e[1]): errs.append(f"{w} ex[{i}]: only <em> is allowed")
    if len(set(e[0] for e in ex if isinstance(e, list))) != len(ex): errs.append(f"{w}: duplicate examples")
    coll = c.get("coll", [])
    if not 3 <= len(coll) <= 6: errs.append(f"{w}: 3-6 collocations")
    for i, x in enumerate(coll): pair(errs, f"{w} coll[{i}]", x, 8)
    for key, lo, hi in (("family", 0, 5), ("syn", 0, 4), ("ant", 0, 3), ("confuse", 0, 2)):
        xs = c.get(key, [])
        if not isinstance(xs, list) or not lo <= len(xs) <= hi: errs.append(f"{w}: {key} needs {lo}-{hi} entries"); continue
        for x in xs:
            if not isinstance(x, dict) or not x.get("w"): errs.append(f"{w} {key}: each entry needs w"); continue
            if key in ("family", "ant") and not ZH.search(x.get("zh", "")): errs.append(f"{w} {key} {x['w']}: zh missing")
            if key == "family" and x.get("pos") not in POS: errs.append(f"{w} family {x['w']}: pos")
            if key in ("syn", "confuse"): pair(errs, f"{w} {key} {x['w']} note", x.get("note"), 25)
    extra = set(c) - {"w", "pos", "zh", "def", "ex", "coll", "family", "syn", "ant", "confuse"}
    if extra: errs.append(f"{w}: unknown keys {sorted(extra)}")
    return errs


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(HERE, "cards", "*.json")))
    seen, bad = set(), 0
    for f in files:
        cards = json.load(open(f, encoding="utf-8")); errs = []
        for c in cards:
            errs += check_card(c)
            if c.get("w") in seen: errs.append(f"{c.get('w')}: duplicate card")
            seen.add(c.get("w"))
        bad += bool(errs)
        print(os.path.basename(f) + ": " + ("ok (%d cards)" % len(cards) if not errs else "\n  " + "\n  ".join(errs)))
    sys.exit(1 if bad else 0)
