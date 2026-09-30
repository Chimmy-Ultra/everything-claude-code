# How much space each linking word gets. Base entries and their first six examples
# live in content.py (their audio is ex/<id>-<n>.mp3); this file adds the rest.

# New entries: (id, word, 中文, types, register, pattern, examples)
NEW = {
    "evenif": ("even if", "就算、即使（假設）", ["JOIN"], None, "Even if A, B.", [
        ("**Even if** you hurry, you won't catch the last train.", "就算你趕，也搭不上末班車了。"),
        ("I'll finish this tonight, **even if** it takes me until midnight.", "我今晚會做完，就算要做到半夜。"),
        ("**Even if** you don't win, it's a fun game.", "就算沒贏，這遊戲也很好玩。"),
        ("**Even if** I had the money, I wouldn't buy that car.", "就算我有錢，也不會買那台車。"),
        ("Call me when you land, **even if** it's late.", "落地了就打給我，就算很晚也沒關係。"),
        ("**Even if** the rent goes up, we'll stay here.", "就算房租漲了，我們還是會住這裡。"),
        ("You should apply, **even if** you don't meet every requirement.", "就算不完全符合條件，你也應該去應徵。"),
        ("**Even if** nobody else comes, I'll be there.", "就算沒有別人來，我也會到。"),
    ]),
    "otherhand": ("on the other hand", "另一方面", ["START"], None, "A. On the other hand, B.", [
        ("The flat in town is small. **On the other hand**, it's close to work.", "市區那間公寓很小。但另一方面，離公司很近。"),
        ("On the one hand, I miss my family. **On the other hand**, I love my life here.", "一方面我想念家人，另一方面我很喜歡在這裡的生活。"),
        ("Trains are faster. Buses, **on the other hand**, are much cheaper.", "火車比較快。公車呢，則便宜很多。"),
        ("I could take the job in London. **On the other hand**, the one in Bristol pays more.", "我可以接倫敦的工作。但另一方面，布里斯托那份薪水比較高。"),
        ("Emma is very organised. George, **on the other hand**, always loses his keys.", "Emma 很有條理。George 則是老是弄丟鑰匙。"),
        ("Working from home saves time. **On the other hand**, it can feel lonely.", "在家工作省時間。另一方面，也可能覺得孤單。"),
        ("The course is expensive. **On the other hand**, it includes a certificate.", "這門課很貴。另一方面，它有附證書。"),
        ("I love cooking. My brother, **on the other hand**, can't even boil an egg.", "我很愛煮飯。我弟弟則是連蛋都不會煮。"),
    ]),
    "despite": ("despite / in spite of", "儘管（＋名詞）", ["NOUN"], None, "Despite + noun / -ing, B.", [
        ("**Despite** the rain, the park was full of people.", "儘管下雨，公園裡還是滿滿的人。"),
        ("We had a great time **despite** the long wait.", "儘管等了很久，我們還是玩得很開心。"),
        ("**Despite** living here for years, he still gets lost.", "儘管在這裡住了好幾年，他還是會迷路。"),
        ("She got the job **despite** having no experience.", "她沒有經驗，卻還是拿到了那份工作。"),
        ("**In spite of** the traffic, we arrived on time.", "儘管塞車，我們還是準時到了。"),
        ("**Despite** everything, I'm glad I moved here.", "儘管發生了這麼多事，我還是很高興搬來這裡。"),
        ("The shop stayed open **in spite of** the storm.", "儘管有暴風雨，那家店還是照常營業。"),
        ("**Despite** feeling nervous, Wei spoke English all evening.", "儘管很緊張，Wei 整晚都在講英文。"),
    ]),
}

# Extra examples for existing entries; their audio is ex/<id>-7.mp3 onwards.
EXTRA = {
    "although": [
        ("The interview went well, **although** I was very nervous.", "面試很順利，雖然我很緊張。"),
        ("**Although** she's British, she's never been to Scotland.", "雖然她是英國人，她卻從沒去過蘇格蘭。"),
    ],
    "eventhough": [
        ("**Even though** it was my day off, my boss called me three times.", "明明是我休假，老闆還打了三次電話給我。"),
        ("He still hasn't replied, **even though** I sent the email last week.", "我上週就寄信了，他到現在還是沒回。"),
    ],
    "however": [
        ("Thank you for your application. **However**, the position has already been filled.", "謝謝您的應徵。然而，這個職位已經有人了。"),
        ("Our rent usually goes up every year. This year, **however**, it stayed the same.", "我們的房租通常每年都會漲。不過今年沒有。"),
    ],
    "thoughend": [
        ("“Do you like your new flat?” “It's nice. The walls are thin, **though**.”", "「你喜歡新公寓嗎？」「不錯啊。不過牆很薄。」"),
        ("Thanks for the invite. I can't make it tonight, **though**.", "謝謝邀請。不過我今晚去不了。"),
    ],
    "since": [
        ("I've lived in London **since** last spring.", "我從去年春天就住在倫敦了。"),
        ("We've known each other **since** we were kids.", "我們從小就認識了。"),
        ("It's been raining **since** this morning.", "從早上到現在一直在下雨。"),
    ],
    "while": [
        ("My phone rang **while** I was in the shower.", "我在洗澡的時候手機響了。"),
        ("**While** I understand your point, I don't agree.", "雖然我懂你的意思，但我不同意。"),
    ],
    "once": [
        ("**Once** you've tried it, you'll love it.", "你一旦試過，就會愛上它。"),
        ("**Once** the kids are in bed, we can finally relax.", "等孩子上床，我們終於可以放鬆了。"),
    ],
    "unless": [
        ("You won't get better **unless** you practise.", "除非練習，否則不會進步。"),
        ("**Unless** I hear from you, I'll see you at six.", "除非你再通知我，不然六點見。"),
    ],
    "incase": [
        ("I'll give you my number **in case** you need anything.", "我把電話給你，以防你需要什麼。"),
        ("Keep the receipt **in case** you want to return it.", "收據留著，以防你想退貨。"),
    ],
    "otherwise": [
        ("Please reply by Friday. **Otherwise**, we'll give the room to someone else.", "請在星期五前回覆，否則我們會把房間給別人。"),
        ("It rained a bit in the morning. **Otherwise**, it was a lovely day.", "早上下了點雨。除此之外，是很美好的一天。"),
    ],
}

# The tricky ones: (id, section, why it's tricky, compare [(label, example, 中文)], don't [(wrong, right)])
TRICKY = [
    ("although", "Contrast",
     "中文「雖然」通常會配「但是」，英文的 although 已經帶有轉折，句子的另一半不能再加 but。although 子句放前面或後面都可以。",
     [("although", "**Although** it was late, we kept playing.", "雖然很晚了，我們還是繼續玩。"),
      ("but", "It was late, **but** we kept playing.", "很晚了，但我們還是繼續玩。")],
     [("Although it was late, but we kept playing.", "Although it was late, we kept playing.")]),
    ("eventhough", "Contrast",
     "even though 後面接的是真的發生了的事，意思是「明明……還是」，語氣比 although 強。最常跟 even if 搞混，見下一張。",
     [("although", "**Although** I was tired, I stayed.", "雖然很累，我還是留下來了。"),
      ("even though", "**Even though** I was exhausted, I stayed until the very end.", "明明累壞了，我還是撐到最後。")],
     [("Even I was tired, I stayed.", "Even though I was tired, I stayed.")]),
    ("evenif", "Contrast",
     "even if 後面接的是「假設」，可能發生、也可能不會發生；even though 後面接的是事實。中文兩個都常翻成「即使」，所以很容易混用。",
     [("even though", "**Even though** it's raining, we're going out.", "明明在下雨，我們還是要出門。（真的在下雨）"),
      ("even if", "**Even if** it rains, we're going out.", "就算下雨，我們也要出門。（還不知道會不會下）")],
     [("Even if I'm tired right now, I'll finish this.", "Even though I'm tired right now, I'll finish this.")]),
    ("however", "Contrast",
     "however 跟 but 意思接近，文法卻不一樣：but 把兩個句子連成一句；however 開始新的一句，前面用句號（寫作也可用分號），後面加逗號。however 也可以放在句子中間。語氣比 but 正式，email 和報告很常用。",
     [("but", "It was expensive, **but** we bought it.", "很貴，但我們還是買了。"),
      ("however", "It was expensive. **However**, we bought it.", "很貴。不過，我們還是買了。")],
     [("I was tired, however I went to the party.", "I was tired. However, I went to the party.")]),
    ("otherhand", "Contrast",
     "用來比較一件事的兩面，或兩個不同的選擇。常跟 on the contrary 搞混：on the contrary 是「恰恰相反」，用來否定前面的話，不是拿來比較的。",
     [("on the other hand", "City life is exciting. **On the other hand**, it's expensive.", "城市生活很刺激。另一方面，也很貴。"),
      ("on the contrary", "“Was it boring?” “No. **On the contrary**, it was great fun.”", "「很無聊嗎？」「不，恰恰相反，超好玩。」")],
     [("I like cats. On the contrary, my sister likes dogs.", "I like cats. My sister, on the other hand, likes dogs.")]),
    ("thoughend", "Contrast",
     "though 放句尾，意思像「不過」，是口語裡最自然的轉折之一，比 however 輕鬆很多。though 放句首的話，意思就跟 although 一樣。",
     [("…, though", "The film was long. I enjoyed it, **though**.", "那部電影很長，不過我很喜歡。"),
      ("although", "**Although** the film was long, I enjoyed it.", "雖然那部電影很長，我還是很喜歡。")],
     []),
    ("despite", "Contrast",
     "despite 的意思跟 although 一樣，但後面只能接名詞或 V-ing，不能接完整的句子。另外 despite 沒有 of，in spite of 才有。",
     [("although + sentence", "**Although** it was raining, we went out.", "雖然在下雨，我們還是出門了。"),
      ("despite + noun", "**Despite** the rain, we went out.", "儘管下雨，我們還是出門了。"),
      ("despite + -ing", "**Despite** being tired, I stayed until the end.", "儘管很累，我還是待到最後。")],
     [("Despite of the rain, we went out.", "Despite the rain, we went out."),
      ("Despite it was raining, we went out.", "Although it was raining, we went out.")]),
    ("since", "Reasons",
     "since 有兩個完全不同的意思：「既然、因為」和「自從」。表示原因時，通常是雙方都知道的原因。表示「自從」時，主要子句常用完成式。",
     [("since = because", "**Since** you're here, can you help me?", "既然你在這裡，可以幫我嗎？"),
      ("since = from a time", "I've lived here **since** March.", "我從三月就住在這裡了。")],
     [("I live here since 2023.", "I've lived here since 2023.")]),
    ("while", "Time",
     "while 有兩種用法：「在……的同時」和「而、雖然」（對比）。表示時間時常配進行式：while I was cooking。",
     [("while = at the same time", "I listen to music **while** I work.", "我工作時會聽音樂。"),
      ("while = but / although", "I like tea, **while** my wife prefers coffee.", "我喜歡茶，而我太太比較喜歡咖啡。")],
     []),
    ("once", "Time",
     "once 當連接詞是「一旦、等到……之後」，強調先完成一件事，接下來才……。跟表示「一次」的 once 是不同的用法。",
     [("once = as soon as", "**Once** you know the rules, it's easy.", "一旦知道規則，就很簡單。"),
      ("once = one time", "I've only played it **once**.", "我只玩過一次。")],
     []),
    ("unless", "Conditions",
     "unless = if … not，本身已經有否定的意思，後面不要再加 not。講未來的事，unless 後面一樣用現在式。",
     [("unless", "**Unless** you hurry, you'll be late.", "你不快一點的話，會遲到。"),
      ("if … not", "**If** you don't hurry, you'll be late.", "如果你不快一點，會遲到。（意思一樣）")],
     [("Unless you don't hurry, you'll be late.", "Unless you hurry, you'll be late.")]),
    ("incase", "Conditions",
     "in case 是「先做好準備，以防萬一」：不管事情有沒有發生，都先準備好。if 則是「事情發生了才做」。in case 後面用現在式，不用 will。",
     [("in case", "I'll take an umbrella **in case** it rains.", "我會帶把傘，以防下雨。（現在就帶）"),
      ("if", "I'll take an umbrella **if** it rains.", "如果下雨，我就會帶傘。（下雨才帶）")],
     []),
    ("otherwise", "Conditions",
     "otherwise 有兩個意思：「不然、否則」和「除此之外」。它不能像 or 一樣直接把兩個句子連起來，前面最好用句號。口語也常直接說 or。",
     [("otherwise", "Hurry up. **Otherwise**, we'll miss the train.", "快一點，不然會趕不上火車。"),
      ("or", "Hurry up, **or** we'll miss the train.", "快一點，不然會趕不上火車。")],
     []),
]

# Useful ones: which of the six base examples to keep.
MEDIUM = [("besides", [1, 2, 4, 6]), ("ontop", [1, 2, 3, 4]), ("becauseof", [1, 2, 3, 4]), ("thatswhy", [1, 2, 4, 6]),
          ("until", [1, 2, 3, 5]), ("assoonas", [1, 2, 4, 6]), ("aslongas", [1, 2, 4, 5]), ("like", [1, 2, 4, 6]),
          ("suchas", [1, 2, 4, 5]), ("forexample", [1, 2, 4, 5]), ("imean", [1, 2, 3, 4])]

# The basics: a quick review with two examples each.
BASICS = [("but", [2, 6]), ("so", [1, 5]), ("because", [1, 2]), ("also", [1, 5]), ("too", [1, 2]),
          ("when", [1, 2]), ("beforeafter", [2, 3]), ("if", [2, 3])]

# Extra traps, appended to content.TRAPS.
MORE_TRAPS = [
    ("I live here since 2023.", ["I've lived here since 2023."],
     "表示「自從……到現在」時，主要子句用完成式。"),
    ("Despite it was raining, we went out.", ["Although it was raining, we went out.", "Despite the rain, we went out."],
     "despite 後面不能接完整的句子。"),
    ("Even if I'm tired right now, I'll finish this.", ["Even though I'm tired right now, I'll finish this."],
     "已經是事實的事，用 even though；even if 是假設。"),
]
