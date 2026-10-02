# Round 7 reading items (Part 7 style triple passages), written under WRITING_RULES.md (sections 0, 3, 4, 6, 8).
# 2 p7t sets, 5 questions each (10 questions): r-p7-04 catering (web page + booking e-mail + invoice table),
# r-p7-05 coach day tour (itinerary table + change e-mail + online review). All names of people, firms, towns and
# places are invented. US spelling.
# Question order roughly follows the documents (document 1 first, cross-document questions in the middle and later,
# a document-3-only question may come last); options are short and parallel (2-10 words).
# `ldbs` on each question is the writer's self-test (WRITING_RULES 8.3: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` is 3 for now and will be set
# from the blind review.
# reviewed stays False until the items pass a blind review.
# Self-test summary: easy 0, medium 4, hard 6. Answer positions over the 10 questions: A 3, B 2, C 2, D 3.

ITEMS = [
    # ------------------------------------------------------------------ r-p7-04  catering
    # Doc 0 web page (packages + booking policy), doc 1 customer's booking e-mail, doc 2 invoice (table).
    # The invoice has two lines that only make sense with the policy and the e-mail together: a $35 delivery fee
    # (free only inside Corbridge; the e-mail says the firm has left Corbridge) and a $60 "Staffing" line (the policy's
    # weekend charge; the e-mail's fallback date is Saturday, March 22). 34 guests x $26 = $884; deposit 25% of
    # 30 x $26 = $195; 884 + 35 + 60 - 195 = 784.
    # Q1 word (D) "carry" = involve. Q2 purpose (B). Q3 (A) dessert+coffee -> Banquet -> one more main than Harvest.
    # Q4 (C) delivery fee. Q5 (D) weekend staffing line -> Saturday 22 -> two days after the hoped-for Thursday 20.
    {
        "id": "r-p7-04", "type": "read", "format": "p7t", "unit": "p7-triple", "level": 3,
        "source": "hand", "reviewed": False, "v": 1,
        "docs": [
            {
                "kind": "Web page",
                "head": [],
                "title": "Larkspur Table Catering: Office Lunch Packages",
                "paras": [
                    "For eleven years, Larkspur Table has supplied lunches to businesses across the Halden Valley. "
                    "Every dish is cooked in our Fenwick Road kitchen on the morning of your event and delivered ready "
                    "to serve.",
                    "Garden Package ($14 per person): seasonal salads, two vegetable dishes, fresh bread and a fruit "
                    "platter. Harvest Package ($19 per person): everything in the Garden Package, plus one hot main "
                    "course of chicken or baked fish. Banquet Package ($26 per person): everything in the Harvest "
                    "Package, plus a second hot main course, a dessert table and coffee service.",
                    "Booking policy: Please book at least ten days in advance. A deposit of 25 percent of the estimated "
                    "food cost secures your date. Final guest numbers are due five days before the event, and your "
                    "invoice will be based on that figure. Delivery is free anywhere within Corbridge city limits; a "
                    "flat fee of $35 applies to all other addresses. Events held on a Saturday or Sunday carry an "
                    "additional $60 staffing charge.",
                ],
                "zh": [
                    "十一年來，Larkspur Table 為 Halden 河谷各地的公司行號供應午餐。每一道菜都在活動當天早上於我們位於 Fenwick 路的廚房烹調，送達時即可上桌。",
                    "田園套餐（每人 14 美元）：當季沙拉、兩道蔬菜料理、新鮮麵包和一盤水果。豐收套餐（每人 19 美元）：田園套餐的全部內容，外加一道熱主菜，雞肉或烤魚。宴會套餐（每人 26 美元）：豐收套餐的全部內容，外加第二道熱主菜、甜點桌和咖啡服務。",
                    "訂餐規定：請至少提前十天預訂。支付預估餐費的 25% 作為訂金，即可保留您的日期。最終用餐人數須於活動前五天告知，帳單將依該人數計算。Corbridge 市區範圍內一律免運費；其他地址一律收取 35 美元的固定運費。在星期六或星期日舉行的活動，另收 60 美元的人員費用。",
                ],
            },
            {
                "kind": "E-mail",
                "head": [["From", "Dana Whitfield, Coldharbor Surveying"], ["To", "Larkspur Table Catering"],
                         ["Date", "March 3"], ["Subject", "Training day lunch"]],
                "title": None,
                "paras": [
                    "Our staff enjoyed the Harvest Package you provided for Arthur Penrose's retirement lunch in "
                    "January, so we are coming back to you for our spring training day. Please note that we have since "
                    "left our Corbridge premises; our new office is at 14 Mill Lane in Ashby.",
                    "This time, several colleagues have asked for dessert and coffee, so please put us down for the "
                    "package that includes them. We expect about 30 people and will send you the exact number before "
                    "your deadline.",
                    "The date is less certain. We would like Thursday, March 20, but the session will be held in our "
                    "new conference room, which the builders have promised to finish by March 18. If they run late, we "
                    "will move the training to Saturday, March 22. I will confirm the date by March 12. Either way, "
                    "could the food arrive by 11:30? Our morning session breaks at noon.",
                    "Our accounts team will pay the deposit tomorrow.\nMany thanks,\nDana Whitfield, Office Manager",
                ],
                "zh": [
                    "我們的員工很喜歡你們一月為 Arthur Penrose 退休午宴提供的豐收套餐，所以這次春季訓練日我們又來找你們了。請留意，我們之後已經搬離 Corbridge 的辦公處；新辦公室在 Ashby 的 Mill 巷 14 號。",
                    "這次有好幾位同事希望有甜點和咖啡，所以請幫我們登記包含這兩樣的套餐。我們預計大約 30 人，會在你們的截止日前把確切人數告訴你們。",
                    "日期就比較不確定了。我們希望是 3 月 20 日星期四，但訓練會在我們新的會議室舉行，而施工人員答應 3 月 18 日前完工。如果他們進度落後，我們會把訓練改到 3 月 22 日星期六。我會在 3 月 12 日前確認日期。不管是哪一天，餐點能在 11:30 前送到嗎？我們上午的課程中午休息。",
                    "我們的會計部門明天會支付訂金。\n非常感謝，\nDana Whitfield，辦公室經理",
                ],
            },
            {
                "kind": "Invoice",
                "head": [["Invoice no.", "LT-2217"], ["Client", "Coldharbor Surveying, 14 Mill Lane, Ashby"],
                         ["Issued", "March 24"]],
                "title": "Larkspur Table Catering: Invoice",
                "table": {
                    "head": ["Item", "Details", "Amount"],
                    "rows": [
                        ["Lunch package", "34 guests at $26.00", "$884.00"],
                        ["Delivery", "Flat fee", "$35.00"],
                        ["Staffing", "Service team surcharge", "$60.00"],
                        ["Deposit", "Received March 4", "-$195.00"],
                        ["Balance due", "Payable within 14 days", "$784.00"],
                    ],
                },
                "zh": [],
            },
        ],
        "questions": [
            {
                "q": "In the Web page, the word \"carry\" in paragraph 3 is closest in meaning to",
                "options": ["transport", "stock", "support", "involve"],
                "answer": 3,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "字義題：carry a charge＝附帶、需要（付）一筆費用，不是「搬運」",
                    "why": "網頁第 3 段 Events held on a Saturday or Sunday carry an additional $60 staffing charge：主詞是「活動」，受詞是「費用」，意思是週末舉行的活動會附帶一筆 60 美元的人員費用，也就是 involve（涉及、需要）。carry 最常見的「搬運」在這裡講不通——活動不會搬運費用。",
                    "evidence": [[0, 2]],
                    "wrong": [
                        "最常見義陷阱：carry 最常用的意思是搬運，但「活動搬運一筆費用」不通。",
                        "carry 另一個真實意思是商店「有賣、有庫存」（The shop carries organic food），但這句的主詞是活動，不是商店。",
                        "carry 也有「支撐（重量）」的意思（The beams carry the roof），放進這句沒有意思。",
                        None,
                    ],
                    "wrongMore": [
                        "這家公司的工作確實包含運送（第 1 段 delivered ready to serve；同一段前一句也在講 Delivery），所以 transport 跟整篇的情境很搭，更容易被選；但這一句的主詞是 Events、受詞是 charge，carry 在這裡是「帶有（某種後果或條件）」，像 The offense carries a fine（這項違規要罰款）。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["staffing", "人員配置、人力"], ["flat fee", "固定費用"], ["city limits", "市界、市區範圍"]],
                },
            },
            {
                "q": "Why did Ms. Whitfield send the e-mail?",
                "options": [
                    "To report a change of address",
                    "To book a meal for a company event",
                    "To praise an earlier lunch",
                    "To give a final guest count",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：信裡提到很多事，要找出寫信要對方「做」的那件事",
                    "why": "E-mail 第 1 段說 we are coming back to you for our spring training day，第 2 段 please put us down for the package…、We expect about 30 people，第 3 段談日期與送達時間——整封信都在為訓練日訂午餐。選項的 book a meal 對應 put us down for the package（登記訂購），a company event 對應 our spring training day。第 1 段的搬家與一月的午餐都只是背景。",
                    "evidence": [[1, 0], [1, 1], [1, 2]],
                    "wrong": [
                        "提到但不是目的：搬到 Ashby 是第 1 段的附帶說明（Please note…），是讓外燴知道送到哪裡，不是寫信的理由。",
                        None,
                        "提到但不是目的：一月退休午宴 enjoyed 只是開場，用來說明為什麼再找這家。",
                        "方向相反：第 2 段說 will send you the exact number before your deadline——確切人數之後才給，這封信只給了大約 30 人。",
                    ],
                    "wrongMore": [
                        "Please note that we have since left our Corbridge premises 看起來像在通知地址變更，而且新地址寫得很清楚；但它只是一句附帶說明，整封信後面三段都在談這次要訂什麼、多少人、哪一天、幾點送到。目的題要選整封信要對方做的事。",
                        None,
                        "Our staff enjoyed the Harvest Package … 確實是稱讚，而且是第一句，很容易被當成主旨；但它後面接 so we are coming back to you——稱讚是再次訂購的理由，不是寫信的目的。",
                        "信裡確實談到人數，所以 guest count 沾得上邊；但 about 30 people 是估計，而 will send you the exact number 說明最終人數還沒給。",
                    ],
                    "vocab": [["premises", "（公司的）營業處所、辦公處"], ["put … down for", "幫…登記（訂購）…"], ["retirement", "退休"]],
                },
            },
            {
                "q": "What is suggested about the lunch Ms. Whitfield ordered?",
                "options": [
                    "It offered more main dishes than the January lunch.",
                    "It was paid for in full in advance.",
                    "It was the same package as in January.",
                    "It was cooked at Coldharbor's new office.",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件推論：信只描述套餐的內容，要回網頁對出是哪一個套餐，再跟一月那次比",
                    "why": "E-mail 第 1 段：一月用的是 Harvest Package；第 2 段：這次要 the package that includes them（dessert and coffee）。網頁第 2 段：三個套餐裡只有 Banquet Package 有 a dessert table and coffee service，而它是 Harvest 的全部內容再加 a second hot main course。發票第 1 行每人 $26.00 也證實是 Banquet。所以這次比一月多一道主菜（一道 → 兩道）。",
                    "evidence": [[1, 0], [1, 1], [0, 1], [2, 0]],
                    "wrong": [
                        None,
                        "發票第 4 行只收到訂金 $195（Deposit），第 5 行還有 Balance due $784、Payable within 14 days——不是事先付清。",
                        "被取代的舊資訊：一月是 Harvest Package，但這次要有甜點與咖啡的套餐，Harvest 沒有，所以換成了 Banquet。",
                        "網頁第 1 段 Every dish is cooked in our Fenwick Road kitchen——餐點在外燴自己的廚房做好再送去；新辦公室只是送達地點。",
                    ],
                    "wrongMore": [
                        None,
                        None,
                        "信一開頭就說很喜歡一月的 Harvest Package，接著 so we are coming back to you，很容易以為照舊訂同一個；要讀到第 2 段 This time … dessert and coffee，再回網頁看 Harvest 沒有甜點與咖啡，才知道換成了 Banquet。發票上每人 $26（不是 $19）也證實不是同一個套餐。",
                        None,
                    ],
                    "vocab": [["platter", "大淺盤（裝的一盤拼盤）"], ["seasonal", "當季的"], ["deposit", "訂金"]],
                },
            },
            {
                "q": "Why was Coldharbor Surveying charged $35?",
                "options": [
                    "Its event was held on a weekend.",
                    "It wanted the food by a set time.",
                    "Its office has moved beyond the no-charge zone.",
                    "It booked less than ten days ahead.",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件：發票上的一筆費用，要回政策找對應的規定，再用信判斷為什麼適用",
                    "why": "發票第 2 行 Delivery，Flat fee，$35.00。網頁第 3 段：Delivery is free anywhere within Corbridge city limits; a flat fee of $35 applies to all other addresses。E-mail 第 1 段：we have since left our Corbridge premises; our new office is at 14 Mill Lane in Ashby。合起來：新辦公室已不在 Corbridge，也就不在免運範圍內，所以收 $35。選項的 moved beyond the no-charge zone 改述 left our Corbridge premises＋free anywhere within Corbridge city limits。",
                    "evidence": [[2, 1], [0, 2], [1, 0]],
                    "wrong": [
                        "另一行陷阱：週末的費用是發票第 3 行的 $60（網頁第 3 段的 $60 staffing charge），不是 $35。",
                        "提到但不是問的：11:30 前送達是信第 3 段的請求，網頁的規定裡沒有任何「指定時間」的收費。",
                        None,
                        "信寫於 3 月 3 日，活動在 3 月 20 或 22 日，提前十七天以上，符合 at least ten days in advance；規定也沒有說晚訂要多收錢。",
                    ],
                    "wrongMore": [
                        "這場活動確實辦在週六（見第 5 題），所以這句話本身是對的，而且週末加價就寫在運費那句的下一句，眼睛很容易一起掃到；但題目問的是 $35 那一筆，規定裡週末對應的是 $60，發票上也是另一行 Staffing。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["surcharge", "附加費"], ["balance due", "應付餘額"], ["flat fee", "固定費用"]],
                },
            },
            {
                "q": "What is most likely true about the training day?",
                "options": [
                    "It was held on March 20.",
                    "Its final guest count was under 30.",
                    "It was held on March 18.",
                    "It took place two days later than requested.",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "三份合併：發票上 $60 那一筆要回網頁對成「週末加價」，再用信裡的備案日期算出活動辦在哪天",
                    "why": "發票第 3 行 Staffing，Service team surcharge，$60.00。網頁第 3 段：只有 Events held on a Saturday or Sunday 才 carry an additional $60 staffing charge，所以活動辦在週末。E-mail 第 3 段：她希望 Thursday, March 20；如果施工人員 run late，就 move the training to Saturday, March 22。發票有週末人員費 → 活動辦在 3 月 22 日星期六，比她要求的 20 日晚兩天（two days later than requested）。",
                    "evidence": [[2, 2], [0, 2], [1, 2]],
                    "wrong": [
                        "被取代的資訊：3 月 20 日星期四是她希望的日子，但發票的 $60 週末人員費說明最後辦在週六。",
                        "方向相反：信估計 about 30 people；網頁說帳單依最終人數計算，發票收了 34 人——最終人數比估計多，不是少。",
                        "鄰近日期：3 月 18 日是施工人員答應完工的期限，不是活動日；活動是 3 月 22 日。",
                        None,
                    ],
                    "wrongMore": [
                        "信裡第一個出現、而且寫得最確定的日期是 Thursday, March 20，發票上又沒有寫活動日期，所以很容易直接當成答案；要先認出發票第 3 行 $60 就是網頁裡週末才收的費用，才知道備案的 Saturday, March 22 才是實際日期。",
                        "活動人數常常比估計少，這個選項很像常識；但網頁第 3 段說 your invoice will be based on that figure（最終人數），而發票第 1 行是 34 guests，所以最終人數是 34，比 30 多。",
                        None,
                        None,
                    ],
                    "vocab": [["conference room", "會議室"], ["run late", "延誤、進度落後"], ["confirm", "確認"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p7-05  coach day tour
    # Doc 0 itinerary (table), doc 1 tour company's change e-mail, doc 2 customer's online review.
    # The e-mail supersedes two things in the itinerary: the Lindell Water boat (replaced by a cheese dairy, lunch and
    # return later) and the departure bay (Bay 6 -> Bay 2, beside the main ticket hall).
    # Q1 purpose (C). Q2 word (A) "stands" = remains valid. Q3 (B) couple waiting at Bay 6 -> old itinerary bay.
    # Q4 (A) "the stop I had been looking forward to ... dropped" -> e-mail: the boat -> itinerary: cruise to the tea
    # house. Q5 NOT (D) full refund: offered in the e-mail, not in the review (she got a voucher).
    {
        "id": "r-p7-05", "type": "read", "format": "p7t", "unit": "p7-triple", "level": 3,
        "source": "hand", "reviewed": False, "v": 1,
        "docs": [
            {
                "kind": "Itinerary",
                "head": [["Date", "Saturday, June 14"], ["Fare", "$68 per adult, including lunch and all entry fees"]],
                "title": "Thornfield Coach Tours: Valley Heritage Day Tour",
                "table": {
                    "head": ["Time", "Stop", "Details"],
                    "rows": [
                        ["7:45 a.m.", "Kingsgate Bus Station, Bay 6", "Departure (please arrive 15 minutes early)"],
                        ["9:30 a.m.", "Corvale Abbey", "Guided walk through the twelfth-century ruins"],
                        ["11:15 a.m.", "Lindell Water", "Forty-minute cruise to the island tea house"],
                        ["12:45 p.m.", "Pennock", "Lunch at the Old Mill Inn, then free time in the village"],
                        ["3:00 p.m.", "Fellbrook House", "Tour of the house and its walled gardens"],
                        ["5:30 p.m.", "Kingsgate Bus Station", "Return (approximate)"],
                    ],
                },
                "zh": [],
            },
            {
                "kind": "E-mail",
                "head": [["From", "Imogen Castell, Thornfield Coach Tours"],
                         ["To", "Valley Heritage Day Tour passengers, June 14"],
                         ["Date", "June 9"], ["Subject", "Saturday's tour"]],
                "title": None,
                "paras": [
                    "Thank you for booking the Valley Heritage Day Tour. We look forward to welcoming you on Saturday. "
                    "Before then, please take a moment to read the information below.",
                    "The boat that serves the island tea house on Lindell Water has been taken out of service for "
                    "engine repairs. In its place, we will visit Hessle Farm Dairy, where the owners will show you how "
                    "their cheeses are made and offer a tasting. As the dairy is a short drive beyond Pennock, lunch at "
                    "the Old Mill Inn will now begin at 1:30 p.m., and we expect to return to Kingsgate at about "
                    "6:15 p.m.",
                    "In addition, resurfacing work will close Bays 5 to 8 at Kingsgate Bus Station to coaches that "
                    "weekend. Your coach will therefore leave from Bay 2, beside the main ticket hall, at the usual "
                    "time.",
                    "We know that some of you chose this tour for the lake. If you would prefer not to travel, you may "
                    "cancel for a full refund or move to our Lakeside Day Tour on June 28 at no extra cost. This offer "
                    "stands until 5:00 p.m. on Thursday, June 12. Passengers who travel as planned will receive a $10 "
                    "voucher toward a future tour.",
                    "Kind regards,\nImogen Castell, Customer Service",
                ],
                "zh": [
                    "感謝您報名「河谷古蹟一日遊」。我們期待星期六與您見面。在那之前，請花一點時間閱讀以下資訊。",
                    "往返 Lindell 湖島上茶館的那艘船，因引擎維修已停止營運。取而代之，我們將參觀 Hessle 農場乳品場，場主會向各位示範他們的乳酪怎麼製作，並提供試吃。由於乳品場在 Pennock 再過去一小段車程，Old Mill 旅店的午餐將改為下午 1:30 開始，預計返回 Kingsgate 的時間約為下午 6:15。",
                    "此外，Kingsgate 巴士站的路面重鋪工程將使 5 至 8 號月台在那個週末不開放給遊覽車停靠。因此，您的遊覽車將改從售票大廳旁的 2 號月台出發，時間不變。",
                    "我們知道有些人是為了那座湖才選這個行程的。如果您不想參加了，可以取消並全額退款，或免費改參加 6 月 28 日的「湖畔一日遊」。這項方案的有效期限到 6 月 12 日星期四下午五點為止。照原計畫出行的旅客，將獲得一張 10 美元的抵用券，可用於日後的行程。",
                    "敬祝順心，\nImogen Castell，客服部",
                ],
            },
            {
                "kind": "Online review",
                "head": [["Reviewer", "Rosalind Quaye"], ["Posted", "June 16"], ["Rating", "4 out of 5 stars"]],
                "title": "Better than expected",
                "paras": [
                    "My sister and I booked this tour mainly for the stop I had been looking forward to for months, so "
                    "my heart sank when Thornfield wrote to say it had been dropped. We decided to go anyway, and I'm "
                    "glad we did.",
                    "The day did not start well: we left Kingsgate almost twenty minutes late because an elderly couple "
                    "had been waiting at Bay 6, and the driver had to go and find them. After that, though, everything "
                    "ran smoothly. Our guide, Fergus, knew the history of the abbey inside out, and the replacement stop "
                    "turned out to be the surprise of the day. The samples were generous, and I bought two wedges to "
                    "take home.",
                    "My only real complaint is the timing. By the time we sat down at the inn, most of us were starving, "
                    "and we didn't get back until well after six. Still, I've already put my voucher toward another "
                    "Thornfield tour later this month.",
                ],
                "zh": [
                    "我和姊姊報名這個行程，主要是為了其中一站，那一站我已經期待好幾個月了，所以當 Thornfield 來信說那一站取消了，我的心一沉。我們還是決定去，而我很慶幸我們去了。",
                    "這一天的開頭並不順利：我們晚了將近二十分鐘才離開 Kingsgate，因為有一對老夫婦一直在 6 號月台等，司機只好去找他們。不過在那之後，一切都很順利。我們的導遊 Fergus 對修道院的歷史瞭若指掌，而替代的那一站竟成了當天的驚喜。試吃的分量很大方，我還買了兩塊帶回家。",
                    "我唯一真正的不滿是時間安排。等到我們在旅店坐下來吃飯時，大部分人都餓壞了，而且我們過了六點很久才回到家。不過，我已經用抵用券訂了 Thornfield 這個月稍晚的另一個行程。",
                ],
            },
        ],
        "questions": [
            {
                "q": "Why did Ms. Castell send the e-mail?",
                "options": [
                    "To ask passengers to confirm bookings",
                    "To promote a tour later in June",
                    "To announce changes to a planned trip",
                    "To apologize for a late departure",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：第一段沒有說明目的，要讀完各段才知道信在通知行程變動",
                    "why": "E-mail 第 1 段只有道謝與 please take a moment to read the information below；第 2 段：船停駛，In its place 改去乳品場，午餐延到 1:30、回程延到約 6:15；第 3 段：上車處改到 Bay 2；第 4 段：不想去的人可以退費或改團。跟行程表對照，整封信都在說明這趟週六的行程哪裡跟原本不一樣——announce changes to a planned trip。",
                    "evidence": [[1, 1], [1, 2], [1, 3]],
                    "wrong": [
                        "第 4 段只對「不想去的人」（If you would prefer not to travel）提供取消或改團；照原計畫去的人什麼都不用做，信沒有要每個人確認。",
                        "提到但不是目的：6 月 28 日的 Lakeside Day Tour 是給不想去的人的替代方案，是補償措施的一部分，不是在推銷。",
                        None,
                        "時間錯置：晚了二十分鐘出發是評論（6 月 16 日）寫的週六當天的事；e-mail 是 6 月 9 日、出發前寄的，不可能為那件事道歉。",
                    ],
                    "wrongMore": [
                        "This offer stands until 5:00 p.m. on Thursday, June 12 有期限、有選項，看起來像在要求回覆；但對象只是 If you would prefer not to travel 的人，其他人 travel as planned 就好。",
                        "信裡確實出現另一個行程的名稱、日期，還強調 at no extra cost，讀起來像廣告；但它出現在第 4 段，是給因為湖而報名、現在不想去的人的補償選項，信的主體是第 2、3 段的變動。",
                        None,
                        "晚出發這件事確實發生過，而且就在評論裡，容易被當成這次通知的起因；但它發生在 6 月 14 日，e-mail 的日期是 6 月 9 日。",
                    ],
                    "vocab": [["resurfacing", "（路面）重新鋪設"], ["in its place", "取而代之"], ["voucher", "抵用券"]],
                },
            },
            {
                "q": "In the e-mail, the word \"stands\" in paragraph 4 is closest in meaning to",
                "options": ["remains valid", "is located", "rises", "is tolerated"],
                "answer": 0,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "字義題：an offer stands＝（提議、方案）仍然有效，不是「站立」",
                    "why": "E-mail 第 4 段 This offer stands until 5:00 p.m. on Thursday, June 12：前一句講取消退款或改團的方案，這句說這個方案在 6 月 12 日下午五點前都有效，也就是 remains valid。後面接的 until … 是期限，正好配「維持有效」。",
                    "evidence": [[1, 3]],
                    "wrong": [
                        None,
                        "stand 可以指建築物「坐落」（The inn stands by the river），但主詞是 offer，不是建築物；until … 是期限，不是地點。",
                        "最常見義陷阱：stand 最常見是「站立、起立」，方案不會站起來。",
                        "can't stand（受不了）的 stand 是「忍受」，要接受詞；這裡 stands 後面沒有受詞，而且主詞是方案。",
                    ],
                    "wrongMore": [
                        None,
                        "行程表裡有修道院、旅店、莊園，stand 表「坐落於」的用法在旅遊文件裡很常見，容易往這裡想；但這一句的主詞是 This offer，後面的 until 5:00 p.m. on Thursday, June 12 是時間，不是位置。",
                        "stand 最先學到的是 stand up；但 offer 不是人，後面接的是期限 until …，只有「維持有效」講得通。",
                        None,
                    ],
                    "vocab": [["full refund", "全額退款"], ["at no extra cost", "不另收費"], ["as planned", "照原計畫"]],
                },
            },
            {
                "q": "What is suggested about the couple mentioned in the review?",
                "options": [
                    "They were at the bay by the ticket hall.",
                    "They relied on outdated departure details.",
                    "They had canceled their booking.",
                    "They misread the departure time.",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件：評論裡的 Bay 6 要對回行程表（原本的上車處）與 e-mail（改到 Bay 2）",
                    "why": "行程表第 1 行：出發地是 Kingsgate Bus Station, Bay 6。E-mail 第 3 段：Bays 5 to 8 那個週末不開放給遊覽車，Your coach will therefore leave from Bay 2。評論第 2 段：一對老夫婦 had been waiting at Bay 6，司機得去找他們。三份合起來：他們去的是行程表上已被更改的舊上車處，也就是照著過時的出發資訊行動（outdated departure details）。",
                    "evidence": [[0, 0], [1, 2], [2, 1]],
                    "wrong": [
                        "鄰近資訊：e-mail 第 3 段說售票大廳旁的月台是 Bay 2（beside the main ticket hall），也就是遊覽車真正出發的地方；評論說他們在 Bay 6，司機還得 go and find them，所以他們不在那裡。",
                        None,
                        "他們最後有跟團：評論說司機去找他們，大家晚了二十分鐘才出發；取消退款是 e-mail 第 4 段的選項，跟他們無關。",
                        "他們早就在車站等（had been waiting），問題在地點不在時間；e-mail 也說 at the usual time，出發時間沒變。",
                    ],
                    "wrongMore": [
                        "ticket hall 就在 e-mail 談上車地點的那一句裡，跟 Bay 同一句，很容易一起被當成「等車的地方」；但 the bay by the ticket hall 指的是新的 Bay 2。他們等的是 Bay 6（行程表上的舊月台），所以司機才需要去找。",
                        None,
                        None,
                        "晚出發很容易讓人以為有人遲到或記錯時間；但 had been waiting 表示他們已經到了，只是等錯了地方，而時間 at the usual time 本來就沒改。",
                    ],
                    "vocab": [["elderly", "年長的"], ["bay", "（車站的）上下車月台、停車格"], ["ticket hall", "售票大廳"]],
                },
            },
            {
                "q": "What had Ms. Quaye most looked forward to?",
                "options": [
                    "A ride by water to a café",
                    "A cheese-making demonstration",
                    "A guided walk through ruins",
                    "A visit to walled gardens",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件：評論只說「被取消的那一站」，要用 e-mail 找出取消的是哪一站，再回行程表看那一站是什麼",
                    "why": "評論第 1 段：她報名主要是為了 the stop I had been looking forward to for months，而 Thornfield 來信說 it had been dropped。E-mail 第 2 段：停駛的是 The boat that serves the island tea house on Lindell Water，In its place 改去乳品場。行程表第 3 行：Lindell Water，Forty-minute cruise to the island tea house。所以她最期待的是搭船過湖到島上的茶館——a ride by water to a café。e-mail 第 4 段 some of you chose this tour for the lake 也呼應。",
                    "evidence": [[2, 0], [1, 1], [0, 2]],
                    "wrong": [
                        None,
                        "提到但不是問的：做乳酪是取代那一站的新行程；評論說它是 the surprise of the day——意外的驚喜，不是原本期待的。",
                        "鄰近一行：修道院導覽（行程表第 2 行）照常進行，評論還稱讚了導遊；被取消的不是這一站。",
                        "鄰近一行：Fellbrook House 的花園（行程表第 5 行）照常進行，e-mail 沒有取消它。",
                    ],
                    "wrongMore": [
                        None,
                        "評論花最多篇幅稱讚的就是這一站（samples were generous、還買了兩塊），讀者很容易把「最喜歡的」當成「最期待的」；但 surprise 表示事前沒料到，而且它是 replacement stop，是在她期待的那一站被取消之後才加進來的。",
                        None,
                        None,
                    ],
                    "vocab": [["drop", "取消、刪去"], ["replacement", "替代（的東西）"], ["out of service", "停止營運"]],
                },
            },
            {
                "q": "What is NOT mentioned in the review?",
                "options": [
                    "Traveling with a relative",
                    "Buying a product",
                    "Being hungry before a meal",
                    "Receiving a full refund",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "NOT 題：三個選項在評論裡都能找到改述，逐一排除；剩下的那個是另一份文件提到、但評論者沒有拿到的東西",
                    "why": "評論第 1 段 My sister and I → A（和家人同行）；第 2 段 I bought two wedges to take home → B（買了東西）；第 3 段 By the time we sat down at the inn, most of us were starving → C（用餐前很餓）。D 的全額退款是 e-mail 第 4 段給「取消行程的人」的選項；Ms. Quaye 照原計畫去了（We decided to go anyway），拿到的是抵用券（my voucher），不是退款。",
                    "evidence": [[2, 0], [2, 1], [2, 2], [1, 3]],
                    "wrong": [
                        "第 1 段 My sister and I booked this tour——有提到（sister＝relative）。",
                        "第 2 段 I bought two wedges to take home——有提到（買了乳酪）。",
                        "第 3 段 By the time we sat down at the inn, most of us were starving——有提到。",
                        None,
                    ],
                    "wrongMore": [
                        None,
                        "wedges 單看不知道是什麼，要接前一句 The samples were generous 和 e-mail 第 2 段的乳酪試吃，才知道是買了兩塊乳酪——是有提到購物的。",
                        "starving 是「餓壞了」，句子沒有出現 hungry 或 lunch，要把 the inn 對回行程表與 e-mail 的午餐地點（Old Mill Inn）才看得出是「用餐前很餓」。",
                        None,
                    ],
                    "vocab": [["my heart sank", "心一沉、很失望"], ["inside out", "徹底、透徹地（了解）"], ["wedge", "楔形的一塊（如乳酪）"]],
                },
            },
        ],
    },
]
