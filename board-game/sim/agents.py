"""Simple player strategies for the balance simulation.

None of these read other players' orders to guess their cards; they bound the
game from below (random) and above (oracle) rather than play it well. The
hunter variant does look at orders, but only to aim its buried card.
"""

from __future__ import annotations

from cards import COMMODITIES


class RandomAgent:
    """Buries a random card and places random orders."""

    def __init__(self, rng, lev=None):
        self.rng = rng
        self.lev = lev
        self.name = "random" if lev is None else f"random-{lev}x"

    def bury(self, game, me, hand, orders):
        return self.rng.randrange(len(hand))

    def orders(self, game, me, public):
        levs = game.rules.leverages
        return [
            (self.rng.choice(COMMODITIES), self.rng.choice((1, -1)), self.lev or self.rng.choice(levs))
            for _ in range(game.rules.orders_per_round)
        ]


def _strongest(hand):
    return max(range(len(hand)), key=lambda i: max(abs(d) for d in hand[i][1].values()))


def _trade_on(signal, game, lev_for):
    """Orders on the commodities with the biggest known moves, strongest first."""
    ranked = sorted((c for c in COMMODITIES if signal.get(c)), key=lambda c: -abs(signal[c]))
    return [(c, 1 if signal[c] > 0 else -1, lev_for(abs(signal[c]))) for c in ranked[: game.rules.orders_per_round]]


class InformedAgent:
    """Trades only on the strongest card in hand, which it plans to bury.

    lev is a fixed leverage, or "scaled" to pick leverage from the size of the
    known move (1 -> 1x, 2 -> 3x, 3 -> 6x).

    hunt: when news is buried after orders, also weigh how many rival orders a
    card would liquidate on its own, and bury that card if it scores higher.
    """

    SCALED = {1: 1, 2: 3, 3: 6}

    def __init__(self, rng, lev, hunt=False):
        self.rng = rng
        self.lev = lev
        self.hunt = hunt
        tag = "scaled" if lev == "scaled" else f"{lev}x"
        self.name = f"{'hunter' if hunt else 'informed'}-{tag}"

    def lev_for(self, strength):
        return self.SCALED[min(strength, 3)] if self.lev == "scaled" else self.lev

    def known(self, game, me):
        if len(game.buried) > me:
            return game.buried[me][1]
        return game.hands[me][_strongest(game.hands[me])][1]

    def orders(self, game, me, public):
        return _trade_on(self.known(game, me), game, self.lev_for)

    def bury(self, game, me, hand, orders):
        if not (self.hunt and orders):
            return _strongest(hand)
        margin = game.rules.margin

        def score(card):
            moves = card[1]
            own = sum(o.direction * o.lev * moves.get(o.commodity, 0) for o in orders if o.owner == me)
            kills = sum(margin for o in orders if o.owner != me
                        and -moves.get(o.commodity, 0) * o.direction >= margin / o.lev)
            return own + kills

        return max(range(len(hand)), key=lambda i: score(hand[i]))


class OracleAgent(InformedAgent):
    """Knows every buried card (a perfect reader of the table), not the random ones."""

    def __init__(self, rng, lev):
        super().__init__(rng, lev)
        self.name = self.name.replace("informed", "oracle")

    def orders(self, game, me, public):
        total = {c: 0 for c in COMMODITIES}
        for _, moves in game.buried:
            for c, d in moves.items():
                total[c] += d
        return _trade_on(total, game, self.lev_for)
