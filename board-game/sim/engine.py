"""Game engine for the futures board game draft.

One round:
  1. Everyone draws up to the hand size, then buries one news card face down.
  2. In turn order, everyone places orders: commodity, long/short, leverage.
     Each order reserves a fixed margin.
     (Rules.bury_after_orders swaps steps 1 and 2.)
  3. Random cards from the deck fill the pile up to the pile size.
  4. The pile is shuffled and revealed one card at a time. After each card,
     any order whose adverse move reaches margin / leverage is liquidated.
  5. Orders still open settle at leverage x price move.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

from cards import COMMODITIES, build_deck


@dataclass
class Rules:
    players: int = 4
    rounds: int = 6
    start_coins: int = 30
    margin: int = 6
    leverages: tuple = (1, 2, 3, 6)
    orders_per_round: int = 2
    hand_size: int = 3
    pile_size: int | None = None  # None means players + 2
    track: tuple = (0, 20)
    start_price: int = 10
    # "capped": a liquidated order loses exactly its margin.
    # "gap": a liquidated order loses leverage x the full adverse move, which
    #        can exceed the margin when one card jumps past the line.
    liquidation: str = "capped"
    liq_fee: int = 0  # extra coins lost on top of the liquidation loss
    # False: bury news, then place orders. True: place orders first, then bury
    # news knowing everyone's orders (so a card can be buried to hunt them).
    bury_after_orders: bool = False

    def pile(self):
        return self.pile_size if self.pile_size is not None else self.players + 2


@dataclass
class Order:
    owner: int
    commodity: str
    direction: int  # +1 long, -1 short
    lev: int
    entry: int
    signal: int = 0  # the owner's own-card move, signed in the order's direction
    open: bool = True
    liquidated: bool = False
    pnl: int = 0


@dataclass
class GameResult:
    coins: list
    orders: list
    max_dev: dict  # commodity -> largest distance from the start price
    clamps: int  # times a card pushed a price past the end of its track
    broke_at: list  # per player: round they first could not afford an order, or None


@dataclass
class Game:
    rules: Rules
    agents: list
    rng: random.Random
    prices: dict = field(init=False)
    coins: list = field(init=False)
    deck: list = field(init=False)
    discard: list = field(init=False)
    hands: list = field(init=False)
    round_no: int = field(init=False, default=0)
    buried: list = field(init=False, default_factory=list)

    def __post_init__(self):
        r = self.rules
        self.prices = {c: r.start_price for c in COMMODITIES}
        self.coins = [r.start_coins] * r.players
        self.deck = build_deck()
        self.rng.shuffle(self.deck)
        self.discard = []
        self.hands = [[] for _ in range(r.players)]

    def draw(self):
        if not self.deck:
            self.deck, self.discard = self.discard, []
            self.rng.shuffle(self.deck)
        return self.deck.pop()

    def max_orders(self, player):
        return min(self.rules.orders_per_round, self.coins[player] // self.rules.margin)

    def bury(self, orders):
        self.buried = [self.hands[p].pop(a.bury(self, p, self.hands[p], orders))
                       for p, a in enumerate(self.agents)]

    def take_orders(self, broke_at):
        orders = []
        start = self.round_no % self.rules.players
        for i in range(self.rules.players):
            p = (start + i) % self.rules.players
            if self.max_orders(p) == 0 and broke_at[p] is None:
                broke_at[p] = self.round_no
            for commodity, direction, lev in self.agents[p].orders(self, p, orders)[: self.max_orders(p)]:
                orders.append(Order(p, commodity, direction, lev, self.prices[commodity]))
        return orders

    def play(self):
        r = self.rules
        lo, hi = r.track
        all_orders = []
        max_dev = {c: 0 for c in COMMODITIES}
        clamps = 0
        broke_at = [None] * r.players

        for self.round_no in range(r.rounds):
            for p in range(r.players):
                while len(self.hands[p]) < r.hand_size:
                    self.hands[p].append(self.draw())

            self.buried = []
            if r.bury_after_orders:
                orders = self.take_orders(broke_at)
                self.bury(orders)
            else:
                self.bury([])
                orders = self.take_orders(broke_at)
            for o in orders:
                o.signal = self.buried[o.owner][1].get(o.commodity, 0) * o.direction
            pile = list(self.buried)
            while len(pile) < r.pile():
                pile.append(self.draw())

            self.rng.shuffle(pile)
            for _, moves in pile:
                for c, d in moves.items():
                    moved = self.prices[c] + d
                    if moved < lo or moved > hi:
                        clamps += 1
                    self.prices[c] = max(lo, min(hi, moved))
                    max_dev[c] = max(max_dev[c], abs(self.prices[c] - r.start_price))
                for o in orders:
                    if not o.open:
                        continue
                    adverse = (o.entry - self.prices[o.commodity]) * o.direction
                    if adverse >= r.margin / o.lev:
                        o.open = False
                        o.liquidated = True
                        o.pnl = -r.margin if r.liquidation == "capped" else -adverse * o.lev
                        o.pnl -= r.liq_fee
            self.discard.extend(pile)

            for o in orders:
                if o.open:
                    o.pnl = (self.prices[o.commodity] - o.entry) * o.direction * o.lev
                self.coins[o.owner] = max(0, self.coins[o.owner] + o.pnl)
            all_orders.extend(orders)

        return GameResult(list(self.coins), all_orders, max_dev, clamps, broke_at)
