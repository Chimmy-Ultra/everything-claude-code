# Builds grammar.html (文法地基) from chapters/*.json and template.html, after checking every chapter (check.py).
#   python3 build.py            refuses to build if any chapter fails the check
#   python3 build.py --draft    builds whatever chapters exist and pass (for local testing)
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "toeic"))
import check
from content import UNITS            # The Workbook's chapter names, so "practise next" points at what the learner sees there

chapters, errors = [], []
for p in sorted(glob.glob(os.path.join(HERE, "chapters", "*.json"))):
    e = check.check(p)
    if e: errors += e; continue
    d = json.load(open(p, encoding="utf-8")); d.pop("_flags", None); chapters.append(d)
missing = [i for i in check.IDS if i not in {c["id"] for c in chapters}]
if missing: errors.append("missing chapters: " + ", ".join(missing))
if errors:
    for e in errors: print("error:", e)
    if "--draft" not in sys.argv: sys.exit(f"{len(errors)} errors, not building")
chapters.sort(key=lambda c: c["n"])
book = {"chapters": chapters, "units": {k: v[2] for k, v in UNITS.items()}}
blob = json.dumps(book, ensure_ascii=False).replace("</", "<\\/")
page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("{{BOOK}}", blob)
open(os.path.join(HERE, "grammar.html"), "w", encoding="utf-8").write(page)
print("chapters", len(chapters), "bytes", len(page.encode()))
