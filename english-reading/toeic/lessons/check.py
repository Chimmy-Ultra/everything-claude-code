# Checks lessons/<unit>.json against lessons/STYLE.md.   python3 lessons/check.py pos tense …   (no args: all units with items)
import json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

BANNED = re.compile(r"\b(let's|remember|note that|tip:|in this chapter|we will)\b|!|[\U0001F300-\U0001FAFF]", re.I)
FACTS = re.compile(r"\d+\s*%|\bpercent\b|\bevery (test|exam)\b|\bper (test|exam)\b|\bmost (common|frequent)\b|\bETS\b|\bofficial\b|\bscore\b", re.I)


def words(h): return len(re.sub(r"<[^>]+>", "", h).split())


def check(unit):
    path = os.path.join(HERE, "lessons", unit + ".json")
    if not os.path.exists(path): return [f"{unit}: missing"]
    d = json.load(open(path, encoding="utf-8")); errs = []

    def pair(where, p, limit):
        if not (isinstance(p, list) and len(p) == 2 and all(isinstance(x, str) and x.strip() for x in p)):
            errs.append(f"{where}: must be [English, Chinese]"); return
        en, zh = p
        if re.search(r"<(?!/?em>)[^>]*>", en + zh): errs.append(f"{where}: only <em> is allowed")
        if en.count("<em>") != en.count("</em>"): errs.append(f"{where}: unbalanced <em>")
        if BANNED.search(re.sub(r"<em>.*?</em>", "", en)): errs.append(f"{where}: banned word or mark")
        if FACTS.search(en) or re.search(r"每場|每次考試|考\s*\d+\s*題|最常考|官方", zh): errs.append(f"{where}: claims about the test are not allowed")
        if words(en) > limit: errs.append(f"{where}: {words(en)} words (max {limit})")
        if not re.search(r"[一-鿿]", zh): errs.append(f"{where}: Chinese twin has no Chinese")

    if d.get("unit") != unit: errs.append(f"{unit}: unit field must be '{unit}'")
    pair(f"{unit} lead", d.get("lead"), 40)
    for i, s in enumerate(d.get("steps", [])): pair(f"{unit} steps[{i}]", s, 25)
    if len(d.get("steps", [])) > 4: errs.append(f"{unit}: at most 4 steps")
    rules = d.get("rules", [])
    if not 3 <= len(rules) <= 7: errs.append(f"{unit}: 3-7 rules")
    for i, r in enumerate(rules):
        pair(f"{unit} rules[{i}].head", r.get("head"), 10); pair(f"{unit} rules[{i}].body", r.get("body"), 45)
        ex = r.get("ex", [])
        if not 1 <= len(ex) <= 3: errs.append(f"{unit} rules[{i}]: 1-3 examples")
        for j, e in enumerate(ex): pair(f"{unit} rules[{i}].ex[{j}]", e, 22)
    pairs = d.get("pairs", [])
    if not 2 <= len(pairs) <= 4: errs.append(f"{unit}: 2-4 pairs")
    for i, p in enumerate(pairs):
        if not (isinstance(p.get("right"), str) and isinstance(p.get("wrong"), str) and p["right"].strip() and p["wrong"].strip()): errs.append(f"{unit} pairs[{i}]: needs right and wrong")
        pair(f"{unit} pairs[{i}].why", p.get("why"), 35)
    lists = d.get("lists", [])
    if len(lists) > 4: errs.append(f"{unit}: at most 4 lists")
    for i, l in enumerate(lists):
        pair(f"{unit} lists[{i}].head", l.get("head"), 10)
        its = l.get("items", [])
        if not 4 <= len(its) <= 12: errs.append(f"{unit} lists[{i}]: 4-12 items")
        for j, it in enumerate(its): pair(f"{unit} lists[{i}].items[{j}]", it, 14)
    traps = d.get("traps", [])
    if not 2 <= len(traps) <= 4: errs.append(f"{unit}: 2-4 traps")
    for i, t in enumerate(traps): pair(f"{unit} traps[{i}]", t, 40)
    extra = set(d) - {"unit", "lead", "steps", "rules", "pairs", "lists", "traps", "_flags"}
    if extra: errs.append(f"{unit}: unknown keys {sorted(extra)}")
    return errs


if __name__ == "__main__":
    units = sys.argv[1:]
    if not units:
        import content
        units = [u for u in content.UNITS if any(x["unit"] == u for x in content.ITEMS)]
    bad = 0
    for u in units:
        e = check(u); bad += bool(e)
        print(u + ": " + ("ok" if not e else "\n  " + "\n  ".join(e)))
    sys.exit(1 if bad else 0)
