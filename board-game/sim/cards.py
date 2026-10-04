"""Commodities and the news deck for the futures board game draft.

Every card has a mirror card with the opposite moves, so across the full deck
each commodity's moves sum to zero: the deck itself has no up or down bias.
"""

COMMODITIES = ("CORN", "WHEAT", "WTI", "NG", "GOLD")

NAMES = {
    "CORN": "玉米",
    "WHEAT": "小麥",
    "WTI": "原油",
    "NG": "天然氣",
    "GOLD": "黃金",
}

# (up card, down card) pairs; each card is (title, {commodity: move}).
CARD_PAIRS = [
    # Grains
    (("美國中西部乾旱", {"CORN": 3, "WHEAT": 1}),
     ("美國玉米大豐收", {"CORN": -3, "WHEAT": -1})),
    (("黑海出口受阻", {"WHEAT": 3, "CORN": 1}),
     ("俄羅斯小麥豐收", {"WHEAT": -3, "CORN": -1})),
    (("美國提高乙醇摻混", {"CORN": 2}),
     ("中國取消玉米訂單", {"CORN": -2})),
    (("印度禁止小麥出口", {"WHEAT": 2}),
     ("阿根廷小麥豐收", {"WHEAT": -2})),
    # Energy
    (("OPEC+ 減產", {"WTI": 3}),
     ("OPEC+ 增產", {"WTI": -3})),
    (("寒流來襲", {"NG": 3, "WTI": 1}),
     ("暖冬", {"NG": -3, "WTI": -1})),
    (("颶風進墨西哥灣", {"WTI": 2, "NG": 2}),
     ("頁岩產量創新高", {"WTI": -2, "NG": -2})),
    (("歐洲天然氣斷供", {"NG": 3}),
     ("LNG 出口廠爆炸", {"NG": -3})),
    # Macro
    (("地緣衝突", {"WTI": 2, "GOLD": 2, "WHEAT": 1}),
     ("停火協議", {"WTI": -2, "GOLD": -2, "WHEAT": -1})),
    (("聯準會降息", {"GOLD": 2, "WTI": 1}),
     ("聯準會升息", {"GOLD": -2, "WTI": -1})),
    (("景氣過熱", {"WTI": 2, "CORN": 1, "GOLD": -2}),
     ("衰退恐慌", {"WTI": -2, "CORN": -1, "GOLD": 2})),
    (("美元走弱", {c: 1 for c in COMMODITIES}),
     ("美元走強", {c: -1 for c in COMMODITIES})),
    (("央行搶購黃金", {"GOLD": 3}),
     ("黃金 ETF 大舉拋售", {"GOLD": -3})),
]

COPIES = 2


def build_deck():
    """Return the full deck as a list of (title, moves) cards."""
    cards = [card for pair in CARD_PAIRS for card in pair]
    return cards * COPIES
