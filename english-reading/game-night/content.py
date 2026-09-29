# Content for "Game Night at George's". British English is the base variety;
# regional alternatives are listed only where a source backs them (see SOURCES).

VOICES = {"G": ("bm_george", "en-gb"), "E": ("bf_emma", "en-gb"), "W": ("am_michael", "en-us")}
NAMES = {"G": "George", "E": "Emma", "W": "Wei"}

# id, headword, 中文, example, example 中文, variants [(place, word)], note
GROUPS = [
    ("things", "桌上的東西", "On the table", [
        ("a1", "board game", "桌遊", "George has loads of board games.", "George 有一大堆桌遊。", None, None),
        ("a2", "board", "遊戲圖板", "Can you put the board in the middle?", "可以把圖板放中間嗎？", None, None),
        ("a3", "dice", "骰子", "Roll the dice and move your counter.", "擲骰子，然後移動你的棋子。", None,
         "一顆骰子口語也說 a dice，正式的單數是 a die。"),
        ("a4", "counter", "棋子", "Pick a counter. What colour do you want?", "挑一個棋子。你要什麼顏色？",
         [("UK", "counter"), ("US", "piece")], None),
        ("a5", "pack of cards", "一副牌", "I'll shuffle the pack.", "我來洗牌。",
         [("UK", "pack of cards"), ("US", "deck of cards")], None),
        ("a6", "hand", "手牌", "No peeking at other people's hands!", "不准偷看別人的手牌！", None, None),
        ("a7", "square", "格子", "Move your counter five squares.", "棋子往前走五格。", None, None),
        ("a8", "points", "分數", "First to ten points wins.", "先拿到十分的人贏。", None, None),
    ]),
    ("actions", "動作", "Actions", [
        ("b1", "set up", "擺好（遊戲）", "Right, let's set up.", "好，我們來把遊戲擺好。", None, None),
        ("b2", "roll", "擲（骰子）", "Come on, Wei, roll!", "快點，Wei，擲啊！", None, None),
        ("b3", "shuffle", "洗牌", "Shuffle the cards before you deal.", "發牌前先洗牌。", None, None),
        ("b4", "deal", "發牌", "Emma, you deal. Five cards each.", "Emma，你發牌。每人五張。", None, None),
        ("b5", "draw a card", "抽一張牌", "You draw a card from the pack.", "你從牌堆抽一張牌。", None,
         "draw 在這裡是「抽」。下面的 a draw 是「平手」，同一個字。"),
        ("b6", "swap", "交換", "Do you want to swap cards?", "要不要換牌？", None, None),
        ("b7", "land on", "停在（某一格）", "If you land on a red square, you miss a go.", "停在紅色格子的話，就要暫停一回合。", None, None),
        ("b8", "tidy away", "收好", "Let's tidy the game away.", "我們把遊戲收好吧。",
         [("UK", "tidy away"), ("US", "put away")], None),
    ]),
    ("game", "局面", "During the game", [
        ("c1", "your go", "輪到你", "It's your go.", "輪到你了。",
         [("UK", "go / turn"), ("US", "turn")], None),
        ("c2", "miss a go", "暫停一回合", "Oh no, I miss a go.", "糟了，我要暫停一回合。",
         [("UK", "miss a go"), ("US", "lose a turn")], None),
        ("c3", "the rules", "規則", "Can you explain the rules?", "可以解釋一下規則嗎？", None, None),
        ("c4", "win", "贏", "If I draw a gold card, I win.", "只要抽到金色的牌，我就贏了。", None, None),
        ("c5", "a draw", "平手", "Last week it was a draw.", "上星期是平手。",
         [("UK, Australia", "a draw"), ("US, Canada", "a tie")], None),
        ("c6", "cheat", "作弊的人", "I'm watching you, you cheat!", "我在盯著你喔，你這個作弊鬼！",
         [("UK", "cheat"), ("US, Canada", "cheater")], "cheat 也是動詞「作弊」：Don't cheat!"),
        ("c7", "sore loser", "輸不起的人", "Don't be a sore loser, George.", "別輸不起嘛，George。", None, None),
        ("c8", "beginner's luck", "新手運", "That was just beginner's luck.", "那只是新手運而已。", None, None),
        ("c9", "rematch", "再比一場", "Rematch? Best of three?", "再來一場？三戰兩勝？", None, None),
    ]),
    ("talk", "桌邊常講的話", "Table talk", [
        ("d1", "Fancy a game?", "要不要玩一局？", None, None,
         [("UK", "Fancy a game?"), ("US", "Want to play a game?")], None),
        ("d2", "Whose go is it?", "輪到誰了？", None, None,
         [("UK", "Whose go is it?"), ("US", "Whose turn is it?")], None),
        ("d3", "No peeking!", "不准偷看！", None, None, None, None),
        ("d4", "Best of three?", "三戰兩勝？", None, None, None, None),
        ("d5", "Well played!", "打得好！", None, None, None, None),
    ]),
]

# Dialogue markup: [id:text] = word-bank term, {text|中文|note} = a new phrase.
SCENES = [
    ("s1", "Fancy a game?", "星期五晚上，Wei 帶著零食到 George 家。", "a1", [
        ("G", "Come in, come in! Emma's already here.", "進來進來！Emma 已經到了。"),
        ("W", "Hi, everyone. {Thanks for having me|謝謝你們邀請我|到別人家作客時的標準開場，要走的時候也可以再說一次。}. I brought some snacks.", "嗨，大家好。謝謝你們邀請我。我帶了一些零食。"),
        ("E", "Oh, lovely! So, George, what are we playing tonight?", "喔，太好了！George，我們今晚玩什麼？"),
        ("G", "I've got loads of [a1:board games], but I was thinking Dragon Market. [d1:Fancy a game], Wei?", "我有一大堆桌遊，不過我在想玩 Dragon Market。Wei，要不要玩一局？"),
        ("W", "Sure, but I've never played it before.", "好啊，不過我從來沒玩過。"),
        ("E", "Don't worry, it's really easy. You'll {pick it up in no time|很快就會上手|pick up 在這裡是「學會」，指玩著玩著自然就會，不用特別去學。}.", "別擔心，很簡單。你很快就會上手。"),
        ("G", "Right, let's [b1:set up]. Emma, can you put the [a2:board] in the middle?", "好，我們來把遊戲擺好。Emma，可以把圖板放中間嗎？"),
        ("E", "Sure. Wei, pick a [a4:counter]. What colour do you want?", "好。Wei，挑一個棋子。你要什麼顏色？"),
        ("W", "Um, the blue one, I guess.", "嗯……藍色的吧。"),
        ("G", "Blue for Wei. And I'll [b3:shuffle] the [a5:pack].", "藍色給 Wei。那我來洗牌。"),
    ]),
    ("s2", "How do you play?", "George 講解規則。Wei 第一次聽到 go 這個用法。", "c3", [
        ("W", "So, can you explain [c3:the rules]?", "所以，可以解釋一下規則嗎？"),
        ("G", "Okay. On your [c1:go], you [b2:roll] the [a3:dice] and move your [a4:counter].", "好。輪到你的時候，你擲骰子，然後移動你的棋子。"),
        ("W", "Sorry, my... go?", "不好意思，我的……go？"),
        ("E", "Your turn. We say “go” as well.", "就是 turn，輪到你。我們也會說 go。"),
        ("W", "Ah, got it.", "喔，懂了。"),
        ("G", "If you [b7:land on] a market [a7:square], you [b5:draw a card] from the [a5:pack].", "如果你停在市集格，就從牌堆抽一張牌。"),
        ("E", "And you can [b6:swap] cards with other players, if they agree.", "而且只要對方同意，你可以跟別人換牌。"),
        ("G", "Every card is worth [a8:points]. First to ten points [c4:wins].", "每張牌都有分數。先拿到十分的人贏。"),
        ("E", "Oh, and {watch out for|小心、注意|提醒別人注意會出問題的東西，比 be careful of 口語。} the red squares. If you land on one, you [c2:miss a go].", "喔，還有小心紅色的格子。停在上面的話，就要暫停一回合。"),
        ("W", "Right. Roll, move, draw a card... Okay, I think I've got it.", "好。擲骰子、移動、抽牌……好，我想我懂了。"),
        ("G", "Great. Emma, you [b4:deal]. Five cards each.", "很好。Emma，你發牌。每人五張。"),
        ("E", "And [d3:no peeking] at other people's [a6:hands]!", "還有，不准偷看別人的手牌！"),
    ]),
    ("s3", "Best of three?", "玩到最後，Wei 只差一分。", "c4", [
        ("E", "Right, [d2:whose go is it]?", "好，輪到誰了？"),
        ("G", "Mine. {Hang on|等一下|很口語的「等一下」，意思跟 wait a second 差不多。}... Emma, were you looking at my cards?", "我。等一下……Emma，你剛剛在偷看我的牌嗎？"),
        ("E", "No! You're holding them the wrong way round.", "才沒有！是你把牌拿反了。"),
        ("G", "Hmm. I'm watching you, you [c6:cheat].", "哼。我在盯著你喔，你這個作弊鬼。"),
        ("W", "Okay, my go. I've got nine points. If I draw a gold card, I win.", "好，換我。我有九分。只要抽到金色的牌，我就贏了。"),
        ("W", "Four... market square! And it's... gold! Ten points!", "四……市集格！然後是……金色的！十分！"),
        ("E", "{No way|不會吧|表示很驚訝、不敢相信。語氣是開心還是不爽，要聽聲音判斷。}! [d5:Well played], Wei!", "不會吧！打得好，Wei！"),
        ("G", "[c8:Beginner's luck]. That's all it was.", "新手運而已啦。"),
        ("E", "Don't be a [c7:sore loser], George. Last week it was [c5:a draw], and you complained all night.", "別輸不起嘛，George。上星期是平手，你就抱怨了一整晚。"),
        ("G", "Fine. [c9:Rematch]? [d4:Best of three]?", "好啦。再來一場？三戰兩勝？"),
        ("W", "I'd love to, but it's nearly eleven. Next week?", "我很想，不過快十一點了。下星期？"),
        ("G", "{Deal|一言為定|這裡的 Deal 不是發牌，是「就這麼說定了」。}. Come on, let's [b8:tidy it away].", "一言為定。來吧，把遊戲收好。"),
        ("W", "Thanks, guys. That was really fun.", "謝謝大家，今晚真的很好玩。"),
    ]),
]

SOURCES = [
    ("Cambridge Dictionary: counter", "https://dictionary.cambridge.org/dictionary/english/counter"),
    ("Longman: counter (board games)", "https://www.ldoceonline.com/Board+games-topic/counter"),
    ("Cambridge Dictionary: pack of cards", "https://dictionary.cambridge.org/dictionary/english/pack-of-cards"),
    ("Cambridge Dictionary: deck of cards", "https://dictionary.cambridge.org/us/dictionary/english/deck-of-cards"),
    ("Oxford Learner's: go (noun)", "https://www.oxfordlearnersdictionaries.com/us/definition/english/go_2"),
    ("WordReference: miss a turn / miss a go", "https://forum.wordreference.com/threads/board-games-miss-a-turn-miss-a-go-go-forward-go-back.1110953/"),
    ("Wikipedia: Tie (draw)", "https://en.wikipedia.org/wiki/Tie_(draw)"),
    ("Oxford Learner's: cheat (noun)", "https://www.oxfordlearnersdictionaries.com/us/definition/english/cheat_2"),
    ("Oxford Learner's: cheater", "https://www.oxfordlearnersdictionaries.com/definition/english/cheater"),
    ("Cambridge Dictionary: tidy something away", "https://dictionary.cambridge.org/dictionary/english/tidy-away"),
    ("Cambridge Dictionary: fancy", "https://dictionary.cambridge.org/dictionary/english/fancy"),
    ("Cambridge Dictionary blog: ways of saying ‘want’", "https://dictionaryblog.cambridge.org/2023/09/06/ways-of-saying-want/"),
    ("Grammarist: dice vs. die", "https://grammarist.com/usage/dice-die/"),
]
