# Draws the character avatars and writes avatars.json + preview.html.   python make_avatars.py
# Each avatar is a 64×64 head-and-shoulders portrait clipped to a circle, in the flat outlined style of
# the café illustration. Presentation attributes only (no classes), so copies can sit anywhere on a page.
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
INK = "#2B2740"
S = f'stroke="{INK}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"'
LN = f'fill="none" {S}'

def eyes(y=31, dx=5, look=0):
    out = ""
    for x in (32 - dx, 32 + dx):
        out += (f'<ellipse cx="{x + look}" cy="{y}" rx="1.75" ry="2.15" fill="{INK}"/>'
                f'<circle cx="{x + look + .6}" cy="{y - .7}" r=".65" fill="#FFFFFF"/>')
    return out

def blush(y=36, dx=8):
    return "".join(f'<ellipse cx="{x}" cy="{y}" rx="2.4" ry="1.4" fill="#F28B82" opacity=".45"/>' for x in (32 - dx, 32 + dx))

def head(skin, ears=True):
    e = (f'<circle cx="19.6" cy="32" r="3" fill="{skin}" {S}/><circle cx="44.4" cy="32" r="3" fill="{skin}" {S}/>' if ears else "")
    return (f'<path d="M27.5 40h9v10h-9z" fill="{skin}" {S}/>' + e +
            f'<ellipse cx="32" cy="30" rx="12.4" ry="13.4" fill="{skin}" {S}/>')

def body(color, dark, collar=""):
    return (f'<path d="M8 66c0-11 9-17 24-17s24 6 24 17z" fill="{color}" {S}/>' + collar +
            f'<path d="M20 54c1 4 1 8 0 12M44 54c-1 4-1 8 0 12" fill="none" stroke="{dark}" stroke-width="1.4" stroke-linecap="round"/>')

def wrap(key, bg, inner):
    cid = f"av-{key}-clip"
    return (f'<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            f'<defs><clipPath id="{cid}"><circle cx="32" cy="32" r="32"/></clipPath></defs>'
            f'<g clip-path="url(#{cid})"><rect width="64" height="64" fill="{bg}"/>{inner}</g></svg>')

NOSE = f'<path d="M32 33.5q1.3 1.6 0 2.4" {LN}/>'

# George: tousled brown hair, trimmed beard, green jumper over a shirt collar, one eyebrow up, big grin.
g_skin, g_hair = "#F1C7A1", "#7A4A2A"
george = wrap("G", "#DDF0DE",
    body("#3E9B4A", "#2E7D3A", f'<path d="M26 49l6 7 6-7" fill="#FFFFFF" {S}/>')
    + head(g_skin)
    # beard: follows the jaw, leaves room for the mouth
    + f'<path d="M20 31c0 9 5 14 12 14s12-5 12-14c-2 4-4 6-6 6h-12c-2 0-4-2-6-6z" fill="#8A5A36" {S}/>'
    + f'<path d="M26.5 37.5q5.5 5 11 0z" fill="#FFFFFF" {S}/>'
    + f'<path d="M19.2 27c-1-9 5-14 12.8-14 8 0 14 5 12.8 14-1-3-3-5-5-5.5 1 2 1 3.5.5 5-2-3.5-5-5-8.5-5.5 1 1.5 1 3 .5 4-3-2.5-6-3.5-9-3-1.5 1-3 2.5-4.1 5z" fill="{g_hair}" {S}/>'
    + eyes(31) + blush(35.5, 9)
    + f'<path d="M24.5 26.8q2.5-1.6 5 0" {LN}/><path d="M34.5 25.4q2.6-2.2 5.2-.6" {LN}/>'
    + NOSE)

# Emma: copper bob with a bun, freckles, violet top, a knowing half smile.
e_skin, e_hair = "#F6D5BC", "#C0612B"
emma = wrap("E", "#E9E5FA",
    f'<circle cx="32" cy="14" r="6.5" fill="{e_hair}" {S}/>'
    + f'<path d="M17.5 32c-2-13 5-19 14.5-19s16.5 6 14.5 19l1 9h-7l-1-10H23l-1 10h-7z" fill="{e_hair}" {S}/>'
    + body("#7A68D6", "#5E4BBF", f'<path d="M25 49q7 6 14 0" fill="none" {S}/>')
    + head(e_skin, ears=False)
    + f'<path d="M19.8 29c-.6-9 5-14 12.2-14s12.8 5 12.2 14c-2-2.6-3.6-4.6-4.6-6.6-4 2.6-11 3.6-15.4 2.2-1.6 1.4-3 2.6-4.4 4.4z" fill="{e_hair}" {S}/>'
    + eyes(31.5) + blush(36, 8.5)
    + "".join(f'<circle cx="{x}" cy="{y}" r=".55" fill="#B06A45"/>' for x, y in [(23.5, 34.5), (25.5, 35.8), (22.8, 36.6), (40.5, 34.5), (38.6, 35.8), (41.2, 36.6)])
    + f'<path d="M24.8 27.2q2.4-1.2 4.8 0M34.4 27.2q2.4-1.2 4.8 0" {LN}/>'
    + NOSE
    + f'<path d="M28 39.2q4 2.2 7.8-.8" {LN}/>')

# Wei: straight black hair with a fringe, round glasses, blue hoodie with drawstrings, gentle smile.
w_skin, w_hair = "#EFC9A4", "#1F1B2E"
wei = wrap("W", "#DDEBF8",
    body("#3D8AD2", "#2A6FB0",
         f'<path d="M18 52c3-3 7-4 14-4s11 1 14 4c-4 5-9 7-14 7s-10-2-14-7z" fill="#5AA0E0" {S}/>'
         f'<path d="M28.5 55v7M35.5 55v7" fill="none" stroke="#FFFFFF" stroke-width="1.4" stroke-linecap="round"/>')
    + head(w_skin)
    + f'<path d="M19.4 30c-1.4-11 4.8-17 12.6-17s14 6 12.6 17c-.8-3-1.4-4.4-2.4-5.2-4 .6-9.5.2-14.2-2.4-1.6 2.4-4.4 4.2-8.6 7.6z" fill="{w_hair}" {S}/>'
    + eyes(31.5, look=.2) + blush(36.5, 8.5)
    + f'<circle cx="27" cy="31.5" r="4.4" fill="none" {S}/><circle cx="37" cy="31.5" r="4.4" fill="none" {S}/><path d="M31.4 31.2h1.2" {LN}/>'
    + f'<path d="M25 25.6q2-1 4 0M35 25.6q2-1 4 0" {LN}/>'
    + f'<path d="M32 34.6q1 1.4 0 2" {LN}/>'
    + f'<path d="M28.8 39.4q3.2 2 6.4 0" {LN}/>')

# Barista: the café figure (coral cap, teal shirt, amber apron straps, same skin and hair), open cheerful smile.
b_skin, b_hair = "#E2B288", "#1E222C"
barista = wrap("B", "#FDE7DF",
    body("#1FB5A3", "#168C7E",
         f'<path d="M24 50l3 16M40 50l-3 16" fill="none" stroke="#FFB22E" stroke-width="4" stroke-linecap="round"/>'
         f'<path d="M24 50l3 16M40 50l-3 16" fill="none" stroke="{INK}" stroke-width=".8" stroke-linecap="round" opacity=".35"/>')
    + head(b_skin)
    + f'<path d="M20 29c0-6 3-10 7-11h10c4 1 7 5 7 11-3-3-7-4.5-12-4.5s-9 1.5-12 4.5z" fill="{b_hair}" {S}/>'
    + f'<path d="M19 22c0-7 6-11 13-11s13 4 13 11z" fill="#FF7A59" {S}/>'
    + f'<path d="M19 22h31q2 0 1.5 2.2c-.3 1-1.2 1.4-2.2 1.4H19z" fill="#D65A3A" {S}/>'
    + f'<circle cx="32" cy="11.6" r="1.6" fill="#D65A3A" {S}/>'
    + eyes(31.5) + blush(36.2, 8.6)
    + f'<path d="M25 27.6q2.2-1.4 4.4 0M34.6 27.6q2.2-1.4 4.4 0" {LN}/>'
    + NOSE
    + f'<path d="M27.2 38.4h9.6q-.6 5-4.8 5t-4.8-5z" fill="#FFFFFF" {S}/><path d="M29.4 41.6q2.6 1.2 5.2 0" fill="#F28B82" stroke="none"/>')

# You: stands for the real learner, so no face, gender or ethnicity. A soft two-tone head and shoulders.
you = wrap("Y", "#DCEAF8",
    f'<path d="M8 66c0-12 10-18 24-18s24 6 24 18z" fill="#2A6FB0" {S}/>'
    + f'<path d="M26 48.6q6 5 12 0" fill="none" stroke="#9CC3EA" stroke-width="1.6" stroke-linecap="round"/>'
    + f'<circle cx="32" cy="29" r="12.5" fill="#5B97D6" {S}/>'
    + f'<path d="M24.5 24.5a9 9 0 0 1 7-5" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" opacity=".75"/>'
    + f'<circle cx="23.2" cy="28.4" r="1.1" fill="#FFFFFF" opacity=".75"/>')

AV = {"G": george, "E": emma, "W": wei, "B": barista, "Y": you}
json.dump(AV, open(os.path.join(HERE, "avatars.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

NAMES = {"G": "George", "E": "Emma", "W": "Wei", "B": "Barista", "Y": "You"}
rows = []
for bg, fg in (("#F3F2F7", "#1B1830"), ("#13111C", "#ECEAF3")):
    cells = "".join(f'<div style="display:grid;gap:6px;justify-items:center"><div style="display:flex;gap:10px;align-items:center">'
                    + "".join(f'<div style="width:{s}px;height:{s}px;border-radius:50%;overflow:hidden">{AV[k]}</div>' for s in (28, 38, 64, 128))
                    + f'</div><b>{NAMES[k]}</b></div>' for k in AV)
    rows.append(f'<div style="background:{bg};color:{fg};padding:20px;display:flex;flex-wrap:wrap;gap:28px;font:14px system-ui">{cells}</div>')
open(os.path.join(HERE, "preview.html"), "w", encoding="utf-8").write(
    '<!doctype html><meta charset="utf-8"><title>Avatars</title><style>svg{width:100%;height:100%;display:block}</style>' + "".join(rows))
print({k: len(v) for k, v in AV.items()})
