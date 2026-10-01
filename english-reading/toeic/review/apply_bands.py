# Marks a round's items reviewed and sets `level` from the blind reviewer's band (later solved files win).
#   python3 review/apply_bands.py items_listen_c solved_listen_c_round5.json solved_listen_c_round5b.json
import json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
name, files = sys.argv[1], sys.argv[2:]
BAND = {"easy": 1, "medium": 2, "hard": 3}
band = {}
for f in files:
    for k, v in json.load(open(os.path.join(HERE, "review", f), encoding="utf-8"))["answers"].items():
        band[k] = BAND[v["band"]]
level = {}
for k, b in band.items():
    i = k.split(":")[0]
    level.setdefault(i, {})[k] = b
path = os.path.join(HERE, name + ".py"); s = open(path, encoding="utf-8").read()
for i, ks in level.items():
    lv = max(ks.values())                       # a conversation or talk takes its hardest question's band
    # the item's block runs from its "id" key to the next item's "id" key; either quote style
    start = re.search(r'["\']id["\']: ["\']%s["\']' % re.escape(i), s)
    if not start: sys.exit(f"{i}: id not found")
    nxt = re.compile(r'["\']id["\']: ["\']').search(s, start.end())
    end = nxt.start() if nxt else len(s)
    block, n1 = re.subn(r'(["\']level["\']: )\d', lambda m: m.group(1) + str(lv), s[start.start():end], count=1)
    block, n2 = re.subn(r'(["\']reviewed["\']: )(?:False|True)', lambda m: m.group(1) + "True", block, count=1)
    if n1 != 1 or n2 != 1: sys.exit(f"{i}: level/reviewed not found")
    s = s[:start.start()] + block + s[end:]
    print(i, lv)
open(path, "w", encoding="utf-8").write(s)
