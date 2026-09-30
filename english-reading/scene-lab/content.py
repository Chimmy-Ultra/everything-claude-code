# Shared content for the Scene Lab demos: one café visit, three ways to learn it.
# Neutral everyday English; where British and American usage differ, both are given (UK first).

VOICES = {"B": ("bf_emma", "en-gb"), "C": ("bm_george", "en-gb")}   # barista, customer

# The picture. id, word, 中文, example, example 中文, variants [(place, word)]
OBJECTS = [
    ("c1", "menu board", "菜單看板", "The prices are on the menu board.", "價格在菜單看板上。", None),
    ("c2", "counter", "櫃台", "Please order at the counter.", "請在櫃台點餐。", None),
    ("c3", "barista", "咖啡師", "The barista is making my latte.", "咖啡師正在做我的拿鐵。", None),
    ("c4", "coffee machine", "咖啡機", "The coffee machine is really loud.", "咖啡機好吵。", None),
    ("c5", "queue", "排隊的隊伍", "The queue is quite long this morning.", "今天早上隊伍滿長的。", [("UK", "queue"), ("US", "line")]),
    ("c6", "card reader", "刷卡機", "Just tap your card on the card reader.", "卡片在刷卡機上感應一下就好。", [("UK", "card machine"), ("US", "card reader")]),
    ("c7", "display case", "點心櫃", "The croissants are in the display case.", "可頌在點心櫃裡。", None),
    ("c8", "croissant", "可頌", "Can I get a croissant, please?", "可以給我一個可頌嗎？", None),
    ("c9", "takeaway cup", "外帶杯", "Can I have it in a takeaway cup?", "可以用外帶杯裝嗎？", [("UK", "takeaway cup"), ("US", "to-go cup")]),
    ("c10", "lid", "杯蓋", "Could I get a lid, please?", "可以給我一個杯蓋嗎？", None),
    ("c11", "mug", "馬克杯", "I'm staying, so a mug is fine.", "我內用，用馬克杯就好。", None),
    ("c12", "napkins", "餐巾紙", "The napkins are next to the sugar.", "餐巾紙在糖旁邊。", None),
    ("c13", "sugar", "糖", "Sugar and milk are over there.", "糖和牛奶在那邊。", None),
    ("c14", "receipt", "收據", "Would you like your receipt?", "需要收據嗎？", None),
    ("c15", "till", "收銀機", "The barista opened the till.", "咖啡師打開了收銀機。", [("UK", "till"), ("US", "register")]),
    ("c16", "Wi-Fi password", "Wi-Fi 密碼", "What's the Wi-Fi password?", "Wi-Fi 密碼是什麼？", None),
    ("c17", "seat", "座位", "Is this seat taken?", "這個位子有人坐嗎？", None),
    ("c18", "tray", "托盤", "She carried the drinks on a tray.", "她用托盤端飲料。", None),
]

# What you want to do → chunks that do it. {a|b|c} is a slot: the first option is the default,
# the others can be swapped in. id, chunk, 中文, note
INTENTS = [
    ("i1", "點東西", "Order", [
        ("p1", "Can I get a {latte|flat white|cappuccino|tea}, please?", "可以給我一杯＿＿嗎？", "最萬用的點餐句。get 在這裡就是「拿到、要」。"),
        ("p2", "I'd like a {croissant|muffin|brownie}, please.", "我想要一個＿＿。", "I'd like 比 I want 客氣，點餐時用這個。"),
        ("p3", "I'll have the same, please.", "我也要一樣的。", None),
    ]),
    ("i2", "改做法", "Change it", [
        ("p4", "Can I get it with {oat milk|soy milk|an extra shot}?", "可以加＿＿嗎？／可以換成＿＿嗎？", "with 後面接你要加或換的東西。"),
        ("p5", "A {medium|small|large} one, please.", "＿＿杯，謝謝。", "one 代替前面說過的飲料，不用再講一次名字。"),
        ("p6", "Could you make it {decaf|extra hot}?", "可以做成＿＿嗎？", "decaf = 低咖啡因。"),
    ]),
    ("i3", "內用外帶", "Here or to go", [
        ("p7", "For here, please.", "內用。", "英美都通。"),
        ("p8", "To take away, please.", "外帶。（英式）", "美式說 To go, please."),
        ("p9", "To go, please.", "外帶。（美式）", None),
    ]),
    ("i4", "付錢", "Pay", [
        ("p10", "Can I pay by card?", "可以刷卡嗎？", "by card、by cash 不加 the。付現也常說 pay in cash。"),
        ("p11", "Do you take cash?", "你們收現金嗎？", "take 在這裡是「接受」。"),
        ("p12", "Could I get a receipt, please?", "可以給我收據嗎？", None),
    ]),
    ("i5", "問問題", "Ask", [
        ("p13", "What's the Wi-Fi password?", "Wi-Fi 密碼是什麼？", None),
        ("p14", "Where's the {toilet|restroom}?", "廁所在哪裡？", "toilet 是英式，restroom 是美式。"),
        ("p15", "What do you recommend?", "你推薦什麼？", None),
        ("p16", "Is this seat taken?", "這個位子有人坐嗎？", "英美都通。"),
        ("p17", "Do you have anything {without dairy|vegan|gluten-free}?", "有沒有＿＿的東西？", None),
    ]),
    ("i6", "出狀況", "Fix a problem", [
        ("p18", "Sorry, I think this is someone else's.", "不好意思，這杯好像是別人的。", None),
        ("p19", "Sorry, I asked for {oat milk|a large|no sugar}.", "不好意思，我點的是＿＿。", "asked for = 我要的是。直接說事實，不用道歉太多。"),
        ("p20", "Could I get {a lid|some napkins|a spoon}, please?", "可以給我＿＿嗎？", None),
        ("p21", "Sorry, could you say that again?", "不好意思，可以再說一次嗎？", "聽不懂時最好用的一句。"),
    ]),
]

# What the barista says, in the order of a visit. id, line, 中文, a reply you can use
BARISTA = [
    ("b1", "Hi there, what can I get you?", "你好，要點什麼？", "Can I get a latte, please?"),
    ("b2", "What size would you like?", "要什麼尺寸？", "Medium, please."),
    ("b3", "Any milk?", "要加什麼奶嗎？", "Oat milk, please."),
    ("b4", "Is that to eat in or take away?", "內用還是外帶？（英式）", "To take away, please."),
    ("b5", "Is that for here or to go?", "內用還是外帶？（美式）", "For here, please."),
    ("b6", "Anything else?", "還需要別的嗎？", "No, that's all, thanks."),
    ("b7", "Can I get a name for the order?", "可以留個名字嗎？", "It's Wei."),
    ("b8", "That's four pounds twenty.", "總共四鎊二十。", "Can I pay by card?"),
    ("b9", "Just tap whenever you're ready.", "準備好就感應一下。", "Okay, thanks."),
    ("b10", "Do you want your receipt?", "需要收據嗎？", "No, I'm fine, thanks."),
    ("b11", "Sorry, we're out of oat milk. Is soy okay?", "抱歉，燕麥奶沒了。豆奶可以嗎？", "Sure, soy is fine."),
    ("b12", "Your latte will be ready at the end of the counter.", "你的拿鐵會在櫃台另一頭給你。", "Great, thanks."),
]

# The visit as steps, for the illustrated scene. step, 中文, barista ids, phrase ids
STEPS = [
    ("Queue and read the menu", "排隊、看菜單", [], []),
    ("Order", "點餐", ["b1", "b6"], ["p1", "p2"]),
    ("Size and milk", "尺寸和奶", ["b2", "b3", "b11"], ["p4", "p5"]),
    ("Here or takeaway", "內用或外帶", ["b4", "b5"], ["p7", "p8", "p9"]),
    ("Name and pay", "留名字、付錢", ["b7", "b8", "b9", "b10"], ["p10", "p12"]),
    ("Collect and sit down", "取餐、找位子", ["b12"], ["p16", "p20", "p13"]),
]
