# Compares blind answers (review/solved_<name>.json: {"answers": {"<id>" or "<id>:<q>": {"answer": "B", ...}}}) with the key.
#   python review/compare.py items_grammar_a
import importlib, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
name = sys.argv[1]; short = name.replace("items_", "")
items = importlib.import_module(name).ITEMS
solved = json.load(open(os.path.join(HERE, "review", f"solved_{short}.json"), encoding="utf-8"))["answers"]
agree = 0; rows = []
for it in items:
    keys = [(it["id"], it["answer"])] if it["format"] == "gap" else \
           [(it["id"], it["questions"][0]["answer"])] if it["format"] == "qr" else \
           [(f'{it["id"]}:{i}', q["answer"]) for i, q in enumerate(it["questions"])]
    for k, a in keys:
        s = solved.get(k, {}); want = "ABCD"[a]
        ok = s.get("answer") == want
        agree += ok
        if not ok or s.get("ambiguous"):
            rows.append(f'{k}: key {want}, blind {s.get("answer")}' + (" (flagged ambiguous)" if s.get("ambiguous") else ""))
total = sum(1 if it["format"] in ("gap", "qr") else len(it["questions"]) for it in items)
print(f"{name}: blind reviewer agreed on {agree} of {total}")
for r in rows: print(" ", r)
