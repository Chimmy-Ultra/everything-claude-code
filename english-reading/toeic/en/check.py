# Checks en/<items file>.json against the items and en/STYLE.md.   python3 en/check.py items_grammar_a
import importlib, json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

POS = {"n.", "v.", "adj.", "adv.", "prep.", "phr."}
BANNED = re.compile(r"\b(let's|remember|note that|tip:|great|well done|nice)\b|!|[\U0001F300-\U0001FAFF]", re.I)


def check(name):
    items = importlib.import_module(name).ITEMS
    path = os.path.join(HERE, "en", name + ".json")
    data = json.load(open(path, encoding="utf-8"))
    errs = []

    def pair(where, p):
        if not (isinstance(p, list) and len(p) == 2 and all(isinstance(x, str) and x.strip() for x in p)):
            errs.append(f"{where}: must be [English, Chinese]"); return
        en, zh = p
        if re.search(r"<(?!/?em>)[^>]*>", en): errs.append(f"{where}: only <em> is allowed")
        if en.count("<em>") != en.count("</em>"): errs.append(f"{where}: unbalanced <em>")
        if BANNED.search(re.sub(r"<em>.*?</em>", "", en)): errs.append(f"{where}: banned word or mark")
        if not re.search(r"[一-鿿]", zh): errs.append(f"{where}: Chinese twin has no Chinese")

    for it in items:
        i, e = it["id"], data.get(it["id"])
        if e is None: errs.append(f"{i}: missing"); continue
        if it["format"] == "gap":
            text = it["stem"]
            pair(f"{i} point", e.get("point")); pair(f"{i} why", e.get("why"))
            if it["type"] == "vocab":
                u = e.get("usage")
                if not (isinstance(u, list) and len(u) == len(it["options"])): errs.append(f"{i} usage: need one entry per option")
                else:
                    for k, line in enumerate(u):
                        if k == it["answer"]:
                            if line is not None: errs.append(f"{i} usage[{k}]: the answer's slot must be null")
                        else: pair(f"{i} usage[{k}]", line)
            elif "usage" in e: errs.append(f"{i}: grammar items have no usage lines")
            lo, hi = 2, 4
        else:
            if it["type"] == "read":
                text = " ".join(" ".join(d.get("paras") or [" ".join(" ".join(r) for r in d["table"]["rows"])]) for d in it["docs"])
            else:
                text = " ".join(ln["text"] for ln in it["audio"]["lines"])
            q = e.get("q")
            if not (isinstance(q, list) and len(q) == len(it["questions"])): errs.append(f"{i} q: need one entry per question")
            else:
                for n, x in enumerate(q):
                    pair(f"{i} q{n} point", x.get("point")); pair(f"{i} q{n} why", x.get("why"))
            lo, hi = {"qr": (2, 4), "p6": (3, 6), "p7t": (5, 8)}.get(it["format"], (3, 5))
        g = e.get("gloss", [])
        if not lo <= len(g) <= hi: errs.append(f"{i} gloss: {len(g)} entries (want {lo}-{hi})")
        for x in g:
            w = x.get("w", "")
            if not re.search(r"(?<![A-Za-z])" + re.escape(w) + r"(?![A-Za-z])", text): errs.append(f"{i} gloss '{w}': not found in the text")
            if x.get("pos") not in POS: errs.append(f"{i} gloss '{w}': pos must be one of {sorted(POS)}")
            if not x.get("hw") or not re.search(r"[一-鿿]", x.get("zh", "")): errs.append(f"{i} gloss '{w}': needs hw and zh")
            ex = x.get("ex", "")
            if not ex or len(ex.split()) > 12: errs.append(f"{i} gloss '{w}': ex must be 1-12 words")
            stem4 = x.get("hw", "").split()[0][:4].lower()
            if stem4 and stem4 not in ex.lower(): errs.append(f"{i} gloss '{w}': ex should use '{x.get('hw')}'")
            if "ipa" in x: errs.append(f"{i} gloss '{w}': don't write ipa")
    extra = set(data) - {it["id"] for it in items} - {"_flags"}
    if extra: errs.append(f"unknown ids: {sorted(extra)}")
    return errs


if __name__ == "__main__":
    errs = check(sys.argv[1])
    print("\n".join(errs) if errs else "ok")
    sys.exit(1 if errs else 0)
