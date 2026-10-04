"""Run the balance experiments and print a report.

    python3 run.py            # 20000 games per experiment
    python3 run.py --games 2000
"""

from __future__ import annotations

import argparse
import random
import statistics as st
from collections import defaultdict

from agents import InformedAgent, OracleAgent, RandomAgent
from cards import COMMODITIES, NAMES
from engine import Game, Rules


def play_many(rules, make_agents, games, seed):
    """Play `games` games, shuffling seats each game. Yields (agents, result)."""
    rng = random.Random(seed)
    for _ in range(games):
        agents = make_agents(rng)
        rng.shuffle(agents)
        yield agents, Game(rules, agents, rng).play()


def winners(coins):
    best = max(coins)
    tied = [i for i, c in enumerate(coins) if c == best]
    return {i: 1 / len(tied) for i in tied}


def pct(x):
    return f"{100 * x:5.1f}%"


def order_table(rules, games, seed):
    """Per-leverage economics of a single order."""
    def make(rng):
        return [RandomAgent(rng) for _ in range(rules.players - 2)] + [
            InformedAgent(rng, lev, rules.bury_after_orders) for lev in rng.sample(rules.leverages, 2)
        ]

    by_key = defaultdict(list)
    for agents, res in play_many(rules, make, games, seed):
        for o in res.orders:
            kind = "random" if agents[o.owner].name.startswith("random") else f"info{o.signal:+d}"
            by_key[(kind, o.lev)].append(o)

    print(f"  {'orders':<10}{'lev':>4}{'n':>9}{'liquidated':>12}{'mean P&L':>10}{'sd':>7}")
    for kind in ["random", "info+0", "info+1", "info+2", "info+3"]:
        for lev in rules.leverages:
            os_ = by_key.get((kind, lev), [])
            if len(os_) < 200:
                continue
            pnl = [o.pnl for o in os_]
            liq = sum(o.liquidated for o in os_) / len(os_)
            print(f"  {kind:<10}{lev:>3}x{len(os_):>9}{pct(liq):>12}{st.mean(pnl):>+10.2f}{st.pstdev(pnl):>7.1f}")


def tournament(rules, games, seed, pool, label):
    """Win rate and mean final coins per strategy; each game seats a random draw from the pool."""
    wins = defaultdict(float)
    coins = defaultdict(list)
    broke = defaultdict(int)

    def make(rng):
        return [f(rng) for f in rng.sample(pool, rules.players)]

    for agents, res in play_many(rules, make, games, seed):
        for i, w in winners(res.coins).items():
            wins[agents[i].name] += w
        for i, a in enumerate(agents):
            coins[a.name].append(res.coins[i])
            broke[a.name] += res.broke_at[i] is not None
    print(f"  {label}  (fair share {pct(1 / rules.players).strip()})")
    print(f"  {'strategy':<16}{'win':>8}{'mean coins':>12}{'went broke':>12}")
    for name in sorted(wins, key=lambda n: -wins[n] / len(coins[n])):
        n = len(coins[name])
        print(f"  {name:<16}{pct(wins[name] / n):>8}{st.mean(coins[name]):>12.1f}{pct(broke[name] / n):>12}")


def price_spread(rules, games, seed):
    """How far prices wander from the start, and how often they hit the track ends."""
    dev = defaultdict(list)
    hit_end = 0
    for _, res in play_many(rules, lambda rng: [RandomAgent(rng) for _ in range(rules.players)], games, seed):
        for c in COMMODITIES:
            dev[c].append(res.max_dev[c])
        hit_end += res.clamps > 0
    lo, hi = rules.track
    half = hi - rules.start_price
    cells = []
    for c in COMMODITIES:
        d = sorted(dev[c])
        cells.append(f"{NAMES[c]} 中位 {d[len(d) // 2]} / 95% {d[int(len(d) * 0.95)]}")
    print(f"  {rules.players} 人, 每回合翻 {rules.pile()} 張: 最遠偏離 " + ", ".join(cells))
    print(f"  {'':>4}有商品撞到軌道盡頭 (±{half}) 的局: {pct(hit_end / games).strip()}")


SCENARIOS = [
    ("A 原案: 先埋牌再下單, 斷頭只賠保證金", dict(liquidation="capped")),
    ("B 先埋牌再下單, 斷頭照實際跳空賠", dict(liquidation="gap")),
    ("C 先下單再埋牌 (可以獵殺別人), 斷頭照實際跳空賠", dict(liquidation="gap", bury_after_orders=True)),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    g, s = args.games, args.seed

    for title, kw in SCENARIOS:
        rules = Rules(players=4, **kw)
        hunt = rules.bury_after_orders
        print(f"\n=== {title} ===")
        print("\n[1] 單張單的期望值")
        order_table(rules, g, s)

        print("\n[2] 槓桿對打: 每局從五種策略抽四種上桌")
        pool = [lambda rng, L=L: InformedAgent(rng, L, hunt) for L in (*rules.leverages, "scaled")]
        tournament(rules, g, s, pool, "固定 1x / 2x / 3x / 6x, 或看牌力調槓桿 (scaled)")

        print("\n[3] 技術有沒有用")
        tournament(rules, g, s, [lambda rng: InformedAgent(rng, "scaled", hunt)]
                   + [lambda rng: RandomAgent(rng)] * 3, "1 個看牌下單 vs 3 個亂下")
        if not hunt:
            tournament(rules, g, s, [lambda rng: OracleAgent(rng, "scaled")]
                       + [lambda rng: InformedAgent(rng, "scaled")] * 3, "1 個完全讀懂全桌 vs 3 個只看自己")

    print("\n=== [4] C 規則換人數 (軌道 0–30) ===")
    for players in (3, 5):
        rules = Rules(players=players, liquidation="gap", bury_after_orders=True, track=(0, 30), start_price=15)
        pool = [lambda rng, L=L: InformedAgent(rng, L, True) for L in (*rules.leverages, "scaled")]
        tournament(rules, g, s, pool, f"{players} 人, 每局從五種策略抽 {players} 種上桌")

    print("\n=== [5] 價格會跑多遠 ===")
    for track, startp in (((0, 20), 10), ((0, 30), 15)):
        print(f"  軌道 {track[0]}–{track[1]}, 起點 {startp}")
        for players in (3, 4, 5):
            price_spread(Rules(players=players, track=track, start_price=startp), g, s)
        price_spread(Rules(players=3, track=track, start_price=startp, pile_size=6), g, s)
        price_spread(Rules(players=5, track=track, start_price=startp, pile_size=6), g, s)


if __name__ == "__main__":
    main()
