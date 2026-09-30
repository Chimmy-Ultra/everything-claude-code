# Writes review/blind_<name>.json: the items of one items_*.py file with every answer and explanation removed,
# for reviewers who solve the items without seeing the key.   python review/make_blind.py items_grammar_a
import importlib, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
name = sys.argv[1]
only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None   # optional: just these ids (a re-review round)
items = [it for it in importlib.import_module(name).ITEMS if not only or it["id"] in only]
out = []
for it in items:
    b = {"id": it["id"], "format": it["format"]}
    if it["format"] == "gap":
        b.update(stem=it["stem"], options={"ABCD"[i]: o for i, o in enumerate(it["options"])})
    else:
        lines = it["audio"]["lines"]
        if it["format"] == "qr":
            b.update(heard=lines[0]["text"], responses={"ABC"[i]: ln["text"] for i, ln in enumerate(lines[1:4])})
        else:
            if it.get("graphic"): b["graphic"] = it["graphic"]
            b.update(transcript=[f'{ln["who"]}: {ln["text"]}' for ln in lines],
                     questions=[{"q": q["q"], "options": {"ABCD"[i]: o for i, o in enumerate(q["options"])}} for q in it["questions"]])
    out.append(b)
path = os.path.join(HERE, "review", f"blind_{name.replace('items_', '')}{'_round2' if only else ''}.json")
json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(path, len(out))
