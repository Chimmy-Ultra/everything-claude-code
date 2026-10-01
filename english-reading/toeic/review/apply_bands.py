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
    pat = re.compile(r'("id": "%s",[^\n]*?"level": )(\d)(,[^\n]*\n[^\n]*?"reviewed": )(?:False|True)' % re.escape(i))
    s, n = pat.subn(lambda m: m.group(1) + str(lv) + m.group(3) + "True", s)
    if n != 1: sys.exit(f"{i}: id/level/reviewed layout not found")
    print(i, lv)
open(path, "w", encoding="utf-8").write(s)
