"""Hand-played test game: a person makes every decision, the script deals,
shuffles and keeps score. Rules match engine.py with the balanced settings
(orders before burying, full loss on gaps, track 0-30 from 15).

    python3 playtest.py new --players 4 --seed 7 [--names A,B,C,D]
    python3 playtest.py show
    python3 playtest.py order P1 WTI long 3     # commodity: CORN WHEAT WTI NG GOLD
    python3 playtest.py bury P1 2               # index into that player's hand
    python3 playtest.py reveal                  # once everyone has buried

State lives in playtest_state.json in the current directory.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

from cards import COMMODITIES, NAMES, build_deck

STATE = Path("playtest_state.json")
MARGIN, HAND, ROUNDS, LO, HI, START = 6, 3, 6, 0, 30, 15
LEVERAGES = (1, 2, 3, 6)


def load():
    return json.loads(STATE.read_text())


def save(s):
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=1))


def rng(s):
    s["shuffles"] += 1
    return random.Random(f"{s['seed']}-{s['shuffles']}")


def draw(s):
    if not s["deck"]:
        s["deck"], s["discard"] = s["discard"], []
        rng(s).shuffle(s["deck"])
        print("  (deck empty: discard reshuffled)")
    return s["deck"].pop()


def card_text(card):
    title, moves = card
    return f"{title}: " + ", ".join(f"{NAMES[c]} {d:+d}" for c, d in moves.items())


def turn_order(s):
    n = len(s["names"])
    start = (s["round"] - 1) % n
    return [(start + i) % n for i in range(n)]


def deal(s):
    for hand in s["hands"]:
        while len(hand) < HAND:
            hand.append(draw(s))


def show(s):
    names = s["names"]
    print(f"Round {s['round']}/{ROUNDS}   order of play: " + " → ".join(names[p] for p in turn_order(s)))
    print("  prices: " + "  ".join(f"{NAMES[c]} {s['prices'][c]}" for c in COMMODITIES))
    print("  coins:  " + "  ".join(f"{names[p]} {s['coins'][p]}" for p in range(len(names))))
    for p, hand in enumerate(s["hands"]):
        print(f"  {names[p]} hand: " + " | ".join(f"[{i}] {card_text(c)}" for i, c in enumerate(hand)))
    for o in s["orders"]:
        print(f"  order: {names[o['p']]} {NAMES[o['c']]} {'long' if o['dir'] > 0 else 'short'} "
              f"{o['lev']}x @ {o['entry']}, liquidated at {o['line']}")
    if s["buried"]:
        print("  buried so far: " + ", ".join(names[p] for p in map(int, s["buried"])))


def player(s, key):
    key = key.upper()
    if key.startswith("P") and key[1:].isdigit():
        return int(key[1:]) - 1
    return [n.upper() for n in s["names"]].index(key)


def cmd_new(a):
    names = a.names.split(",") if a.names else [f"P{i + 1}" for i in range(a.players)]
    s = {"seed": a.seed, "shuffles": 0, "names": names, "round": 1,
         "prices": {c: START for c in COMMODITIES}, "coins": [30] * len(names),
         "deck": build_deck(), "discard": [], "hands": [[] for _ in names],
         "orders": [], "buried": {}, "log": []}
    rng(s).shuffle(s["deck"])
    deal(s)
    save(s)
    show(s)


def cmd_order(a):
    s = load()
    p = player(s, a.player)
    c, lev = a.commodity.upper(), int(a.lev)
    assert c in COMMODITIES, f"commodity must be one of {COMMODITIES}"
    assert lev in LEVERAGES, f"leverage must be one of {LEVERAGES}"
    assert not s["buried"], "orders close once burying starts"
    mine = sum(o["p"] == p for o in s["orders"])
    assert mine < min(2, s["coins"][p] // MARGIN), f"{s['names'][p]} cannot place another order"
    d = 1 if a.side.lower() == "long" else -1
    entry = s["prices"][c]
    s["orders"].append({"p": p, "c": c, "dir": d, "lev": lev, "entry": entry,
                        "line": entry - d * MARGIN // lev, "open": True, "pnl": 0})
    save(s)
    o = s["orders"][-1]
    print(f"{s['names'][p]}: {NAMES[c]} {a.side} {lev}x @ {entry}, liquidation marker on {o['line']}")


def cmd_bury(a):
    s = load()
    p = player(s, a.player)
    assert str(p) not in s["buried"], "already buried"
    s["buried"][str(p)] = s["hands"][p].pop(int(a.index))
    save(s)
    print(f"{s['names'][p]} buried a card face down")


def cmd_reveal(a):
    s = load()
    names, n = s["names"], len(s["names"])
    assert len(s["buried"]) == n, "everyone must bury first"
    pile = list(s["buried"].values())
    while len(pile) < n + 2:
        pile.append(draw(s))
    rng(s).shuffle(pile)
    # The deck holds two copies of every card, so match buried cards by owner list.
    owners = [(card, names[int(p)]) for p, card in s["buried"].items()]
    print(f"Round {s['round']} reveal ({len(pile)} cards):")
    for i, card in enumerate(pile, 1):
        who = next((o for o in owners if o[0] == card), None)
        if who:
            owners.remove(who)
        who = who[1] if who else "deck"
        moves = []
        for c, d in card[1].items():
            before = s["prices"][c]
            s["prices"][c] = max(LO, min(HI, before + d))
            moves.append(f"{NAMES[c]} {before}→{s['prices'][c]}" + (" (LIMIT)" if before + d != s["prices"][c] else ""))
        print(f"  {i}. {card[0]} [{who}]  " + ", ".join(moves))
        for o in s["orders"]:
            if not o["open"]:
                continue
            adverse = (o["entry"] - s["prices"][o["c"]]) * o["dir"]
            if adverse >= MARGIN / o["lev"]:
                o["open"], o["pnl"] = False, -adverse * o["lev"]
                print(f"     ✗ LIQUIDATED: {names[o['p']]} {NAMES[o['c']]} {o['lev']}x, loses {adverse * o['lev']}")
    s["discard"].extend(pile)
    print("Settle:")
    for o in s["orders"]:
        if o["open"]:
            o["pnl"] = (s["prices"][o["c"]] - o["entry"]) * o["dir"] * o["lev"]
        s["coins"][o["p"]] = max(0, s["coins"][o["p"]] + o["pnl"])
        state = "liquidated" if not o["open"] else f"{o['entry']}→{s['prices'][o['c']]}"
        print(f"  {names[o['p']]} {NAMES[o['c']]} {'long' if o['dir'] > 0 else 'short'} {o['lev']}x: {state}, {o['pnl']:+d}")
    s["log"].append({"round": s["round"], "orders": s["orders"], "pile": pile})
    s["orders"], s["buried"] = [], {}
    s["round"] += 1
    if s["round"] > ROUNDS:
        print("\nGAME OVER  " + "  ".join(f"{names[p]} {s['coins'][p]}" for p in range(n)))
    else:
        deal(s)
        print()
        show(s)
    save(s)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new")
    p.add_argument("--players", type=int, default=4)
    p.add_argument("--seed", type=int, default=1)
    p.add_argument("--names")
    sub.add_parser("show")
    p = sub.add_parser("order")
    for arg in ("player", "commodity", "side", "lev"):
        p.add_argument(arg)
    p = sub.add_parser("bury")
    p.add_argument("player")
    p.add_argument("index")
    sub.add_parser("reveal")
    a = ap.parse_args()
    if a.cmd == "show":
        show(load())
    else:
        {"new": cmd_new, "order": cmd_order, "bury": cmd_bury, "reveal": cmd_reveal}[a.cmd](a)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        sys.exit(f"error: {e}")
