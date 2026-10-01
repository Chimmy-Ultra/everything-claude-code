# Round 4 listening items, written under WRITING_RULES.md (sections 2, 3, 5, 6, 7.1).
# 5 qr (Part 2 style), 2 conv (Part 3 style; l-conv-07 has three named speakers, l-conv-08 a graphic),
# 1 talk (Part 4 style); each conv/talk has 3 questions. Scripts are in US English even when a British
# voice reads them. All content is original; names of people, firms and places are invented.
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`.
# reviewed stays False until the items pass a blind review and every mp3 has been heard.

ITEMS = [
    # ------------------------------------------------------------------ qr (Part 2)
    # l-qr-13  near-correct: (A) names a person (form-correct) but Daniel is the one who is away;
    # (C) repeats cover/conference. Key (B) is indirect: the client is closed anyway, so no cover is needed.
    {
        "id": "l-qr-13", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-13", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "Who's going to cover the Hartwell account while Daniel is away at the sales conference?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "Daniel usually handles that account."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "Their offices are closed that whole week anyway."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "The conference covers the new pricing rules."},
            ],
        },
        "transcriptZh": [
            "Daniel 去參加業務研討會的時候，誰要接手 Hartwell 這個客戶？",
            "那個客戶平常都是 Daniel 在負責。",
            "反正他們公司那整個星期都休息。",
            "研討會會講新的定價規則。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "Who 問人：回答可以是「根本不用人代」",
                "why": "問 Daniel 不在時誰接 Hartwell → 回對方那整週也休息（closed that whole week anyway）：暗示不需要人代。",
                "evidence": [2],
                "wrong": ["形式對情境錯：說出人名，但 Daniel 正好不在", None, "同字陷阱：重複 cover、conference，講的是會議內容"],
                "wrongMore": ["Who 問句回一個人名，形式完全對；但問句後半 while Daniel is away 已經說他不在，只能靠這個附帶條件排除。", None, None],
                "vocab": [["cover", "代理、暫時接手"], ["account", "客戶（業務）"], ["anyway", "反正"]],
            },
        }],
    },
    # l-qr-14  near-correct: (A) Yes + flight time, (B) No + lease length -- both answer the request's form.
    # Key (C) is indirect: the landlord's assistant will collect it, so there is nothing to mail.
    {
        "id": "l-qr-14", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-14", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_eric", "text": "Could you mail the signed lease back to the landlord before you leave for the airport?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "Yes, my flight lands at six."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "No, it's a two-year lease."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "His assistant is coming by to pick it up at noon."},
            ],
        },
        "transcriptZh": [
            "你去機場之前，可以把簽好的租約寄回給房東嗎？",
            "可以，我的班機六點降落。",
            "不，那是兩年期的租約。",
            "他的助理中午會過來拿。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "請求句：用「有人會來拿」表示不必寄",
                "why": "請她出發前把租約寄給房東 → 回房東的助理中午會來拿（coming by to pick it up）：暗示不必寄。",
                "evidence": [3],
                "wrong": ["形式對情境錯：Yes 對得上，但講的是班機幾點到", "同字陷阱：No 加上重複 lease，答的是租期", None],
                "wrongMore": [
                    "Could you… 用 Yes 回是可以的，所以不能只聽開頭；後半講班機抵達時間，跟寄不寄租約無關。",
                    "No 的形式也接得上請求句，而且又出現 lease；但後半講租約是兩年期，沒有回應要不要寄。",
                    None,
                ],
                "vocab": [["lease", "租約"], ["landlord", "房東"], ["come by", "順道過來"]],
            },
        }],
    },
    # l-qr-15  statement stem. near-correct: (B) "Thanks, I'll hang them..." is a natural reply in form but
    # assumes the banners came; only "still haven't arrived" rules it out. Key (A) offers a fix.
    {
        "id": "l-qr-15", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-15", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "The banners for Saturday's open house still haven't arrived."},
                {"file": "a.mp3", "who": "M", "voice": "bm_lewis", "text": "Should I give the sign company a call?"},
                {"file": "b.mp3", "who": "M", "voice": "bm_lewis", "text": "Thanks, I'll hang them by the front entrance."},
                {"file": "c.mp3", "who": "M", "voice": "bm_lewis", "text": "The open house was a big success last year."},
            ],
        },
        "transcriptZh": [
            "星期六開放參觀日要用的布條還沒送到。",
            "要我打個電話給招牌公司嗎？",
            "謝謝，我會把它們掛在大門口旁邊。",
            "去年的開放參觀日辦得很成功。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "敘述句：回應可以是主動提出處理辦法",
                "why": "說布條 still haven't arrived → 回要不要打給招牌公司：針對「還沒到」提出去催的辦法。",
                "evidence": [1],
                "wrong": [None, "方向相反：好像東西已經到了；被 still haven't 排除", "同字陷阱：重複 open house，講的是去年"],
                "wrongMore": [None, "Thanks, I'll… 的語氣像正常接話，形式對；但對方說的是布條還沒到，現在沒有東西可以掛。", None],
                "vocab": [["banner", "布條、橫幅"], ["open house", "開放參觀日"], ["give … a call", "打電話給……"]],
            },
        }],
    },
    # l-qr-16  choice question with a condition. near-correct: (A) picks one option (form-correct) but its reason
    # contradicts "now that the budget's been cut". Key (C): the amount is not known yet, so no decision.
    {
        "id": "l-qr-16", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-16", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_george", "text": "Should we hold Paul's retirement lunch in the cafeteria or at a restaurant, now that the budget's been cut?"},
                {"file": "a.mp3", "who": "W", "voice": "af_sarah", "text": "A restaurant, since there's more room in the budget now."},
                {"file": "b.mp3", "who": "W", "voice": "af_sarah", "text": "He's retiring at the end of June."},
                {"file": "c.mp3", "who": "W", "voice": "af_sarah", "text": "Finance hasn't told us how much we can spend yet."},
            ],
        },
        "transcriptZh": [
            "既然預算被刪了，Paul 的退休午餐要辦在員工餐廳，還是外面的餐廳？",
            "外面的餐廳吧，因為現在預算比較寬裕。",
            "他六月底退休。",
            "財務部還沒告訴我們可以花多少錢。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "選擇疑問句：回答可以是「還不能決定」",
                "why": "問預算刪減後辦在員工餐廳還是餐廳 → 回財務還沒說能花多少（hasn't told us … yet）：現在還無法決定。",
                "evidence": [3],
                "wrong": ["形式對情境錯：選了一個，但理由和預算被刪相反", "同字陷阱：retire 重複，答的是退休時間", None],
                "wrongMore": ["直接選 A restaurant 完全符合選擇疑問句的形式；但理由 more room in the budget 和問句的 now that the budget's been cut 正好相反。", None, None],
                "vocab": [["retirement", "退休"], ["cafeteria", "員工餐廳"], ["budget", "預算"]],
            },
        }],
    },
    # l-qr-17  direct key on purpose (the batch's lower rung). near-correct: (C) is a length of time, exactly
    # the form "How long" asks for, but it is travel time to the warehouse. (A) repeats "down".
    {
        "id": "l-qr-17", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-17", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "How long will the network be down this weekend, now that the upgrade includes the warehouse?"},
                {"file": "a.mp3", "who": "W", "voice": "af_sarah", "text": "It went down twice last month."},
                {"file": "b.mp3", "who": "W", "voice": "af_sarah", "text": "Probably most of Saturday."},
                {"file": "c.mp3", "who": "W", "voice": "af_sarah", "text": "The warehouse is about twenty minutes away."},
            ],
        },
        "transcriptZh": [
            "既然這次升級也包括倉庫，這個週末網路要停多久？",
            "上個月斷了兩次。",
            "大概星期六大半天吧。",
            "倉庫離這裡大約二十分鐘。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": False, "B": False, "S": False, "band": "medium"},
            "explain": {
                "point": "How long 問多久：分清「停多久」和「路程多遠」",
                "why": "問網路這週末會 down 多久 → 回 most of Saturday（星期六大半天）：直接給出停機的長度。",
                "evidence": [2],
                "wrong": ["同字陷阱：重複 down，講的是上個月斷線幾次", None, "形式對情境錯：是一段時間，但講的是到倉庫的路程"],
                "wrongMore": [None, None, "about twenty minutes 正是 how long 要的「一段時間」，形式對，又重複 warehouse；但這是到倉庫要多久，不是網路要停多久。"],
                "vocab": [["network", "網路"], ["upgrade", "升級"], ["warehouse", "倉庫"]],
            },
        }],
    },

    # ------------------------------------------------------------------ conv (Part 3)
    # l-conv-07  three speakers: W = Grace (af_sarah), M1 = Ian (am_eric, US), M2 = Colin (bm_lewis, UK).
    # Grace names both men in line 1 and Colin again in lines 3 and 8; Colin names Ian in line 9.
    # Q2: "they" must be traced back to Grace's question; (A) is Ian's truck. Q3: Ian proposes, Colin objects
    # to weekends, Grace settles on weekdays; (A) Saturday is what customers want, (D) is the truck's deadline.
    {
        "id": "l-conv-07", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-07", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Ian, Colin, thanks for coming in early. Most of last month's customer complaints were about late deliveries."},
                {"file": "02.mp3", "who": "M1", "voice": "am_eric", "text": "Those are mostly sofa orders. Our truck only holds four at a time, and it's fully booked until the end of the month."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "Colin, weren't you going to look into hiring a second delivery company?"},
                {"file": "04.mp3", "who": "M2", "voice": "bm_lewis", "text": "I did. On most of our sofas, they'd charge more per delivery than we actually make on the sale."},
                {"file": "05.mp3", "who": "M1", "voice": "am_eric", "text": "Then why not let customers collect their sofas from the warehouse themselves? Plenty of them have asked about that."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "I like that. We could even take 10% off for anyone who picks up.",
                 "say": "I like that. We could even take ten percent off for anyone who picks up."},
                {"file": "07.mp3", "who": "M2", "voice": "bm_lewis", "text": "The loading dock is closed to the public on weekends, though, and most people would want to come on a Saturday."},
                {"file": "08.mp3", "who": "W", "voice": "af_sarah", "text": "Then let's offer it on weekdays only, for now. Colin, could you put together a sign for the showroom explaining the offer?"},
                {"file": "09.mp3", "who": "M2", "voice": "bm_lewis", "text": "Sure. I'll have a draft ready this afternoon, and I'll ask Ian to check the wording."},
            ],
        },
        "transcriptZh": [
            "Ian、Colin，謝謝你們提早過來。上個月顧客的抱怨，大多是送貨太慢。",
            "那些主要是沙發的訂單。我們的貨車一次只能載四張，而且到月底前都排滿了。",
            "Colin，你不是要去問問看再找一家送貨公司嗎？",
            "問過了。我們大部分的沙發，他們每送一趟收的錢，比我們賣那張沙發實際賺的還多。",
            "那何不讓顧客自己到倉庫取沙發？很多顧客都問過這件事。",
            "這個好。自取的人我們甚至可以打九折。",
            "不過裝卸區週末不對外開放，而大部分人會想星期六來。",
            "那就先只在平日提供。Colin，可以幫忙做一個放在展示間、說明這個優惠的告示牌嗎？",
            "沒問題。今天下午我會先把草稿做好，再請 Ian 看看用字。",
        ],
        "questions": [
            {
                "q": "What problem does the woman mention?",
                "options": ["A truck has broken down", "Customers are waiting too long for their orders", "Sofa sales have fallen", "The warehouse is short of staff"],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "問題題：答案在開頭第一句",
                    "why": "女方說 complaints were about late deliveries → 改述成顧客等貨等太久（waiting too long for their orders）。",
                    "evidence": [0],
                    "wrong": ["提到但不是問的：貨車是排滿，不是壞了", None, "同字陷阱：sofa 出現過，但沒說賣得不好", "沒有人提到倉庫人手不足"],
                    "vocab": [["complaint", "抱怨、客訴"], ["delivery", "送貨"]],
                },
            },
            {
                "q": "What does Colin say about hiring a second delivery company?",
                "options": ["It is fully booked until the end of the month", "The store would lose money on many orders", "Customers have already asked for it", "It could only deliver on weekdays"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：they 要回頭找前一句的送貨公司",
                    "why": "Grace 問第二家送貨公司，Colin 說 they'd charge more … than we make on the sale → 運費比賺的多，改述成很多訂單會賠錢。",
                    "evidence": [2, 3],
                    "wrong": ["張冠李戴：排滿到月底的是自家貨車（Ian 說的）", None, "張冠李戴：顧客問的是自己去倉庫取貨", "時間錯置：只限平日的是自取，不是外包送貨"],
                    "wrongMore": [
                        "fully booked until the end of the month 真的在對話裡，也是送貨慢的原因；但那是 Ian 講自家貨車，Colin 講外包公司時說的是費用。",
                        None,
                        "對話裡確實有人「問過」，但那是 Ian 說顧客問能不能自己去倉庫取沙發，不是請另一家公司送。",
                        None,
                    ],
                    "vocab": [["look into", "調查、研究"], ["charge", "收費"], ["lose money", "賠錢"]],
                },
            },
            {
                "q": "When will customers be able to pick up their sofas?",
                "options": ["Only on Saturdays", "Any day of the week", "Monday through Friday", "After the end of the month"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：提議、反對、定案，問的是最後結果",
                    "why": "Ian 提議自取，Colin 說裝卸區週末不開放，Grace 定案 weekdays only → 改述成 Monday through Friday。",
                    "evidence": [4, 6, 7],
                    "wrong": ["方向相反：星期六是顧客想來，但週末不開放", "語境矛盾：Colin 說裝卸區週末不對外開放", None, "期限錯置：月底是自家貨車排滿的期限"],
                    "wrongMore": [
                        "most people would want to come on a Saturday 確實出現，是顧客的偏好；但同一句前半說週末不開放，Grace 接著定為只限平日。",
                        None,
                        None,
                        "until the end of the month 是 Ian 說貨車排滿到什麼時候，跟自取何時開始無關；Grace 說 for now，表示現在就先這樣做。",
                    ],
                    "vocab": [["loading dock", "裝卸區"], ["for now", "暫時、目前先"], ["showroom", "展示間"]],
                },
            },
        ],
    },
    # l-conv-08  graphic: shipping rates. The audio never says a price or the name "Two-Day Air".
    # Coordinates: standard is ruled out (line 2); ground runs a day late, so the 3-day ground service lands on
    # Friday (lines 4-5); she takes air "but not overnight" (line 7) -> Two-Day Air -> $45.00.
    # (B) $32.00 is the row she wanted before the delay -- the near-correct trap.
    {
        "id": "l-conv-08", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "graphic": {
            "caption": "Shipping Rates — One Standard Box",
            "head": ["Service", "Delivery Time", "Price"],
            "rows": [
                ["Standard Ground", "5–7 business days", "$18.00"],
                ["Express Ground", "3 business days", "$32.00"],
                ["Two-Day Air", "2 business days", "$45.00"],
                ["Overnight Air", "Next business day", "$70.00"],
            ],
        },
        "audio": {
            "dir": "audio/l-conv-08", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Hi, I need to send this box of fabric samples to a client. It has to get there by Thursday at the latest."},
                {"file": "02.mp3", "who": "M", "voice": "am_michael", "text": "Since today's Monday, you can rule out our standard service. Anything else on this chart will arrive in time."},
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "I'd like to avoid the air services if I can. My manager wants us to keep shipping costs to a minimum."},
                {"file": "04.mp3", "who": "M", "voice": "am_michael", "text": "Before you decide, ground shipments to that area are running a day behind this week. There's road construction on the main highway."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "Oh. Then ground won't work at all."},
                {"file": "06.mp3", "who": "M", "voice": "am_michael", "text": "I'm afraid not. The air services aren't affected, though."},
                {"file": "07.mp3", "who": "W", "voice": "bf_emma", "text": "All right, I'll pay for air, but not overnight. Thursday is soon enough."},
                {"file": "08.mp3", "who": "M", "voice": "am_michael", "text": "Sure. Once the box is scanned, I'll e-mail you a tracking number you can forward to your client."},
                {"file": "09.mp3", "who": "W", "voice": "bf_emma", "text": "Perfect. My e-mail is on this business card."},
            ],
        },
        "transcriptZh": [
            "你好，我要把這箱布料樣品寄給一位客戶，最晚星期四一定要送到。",
            "今天是星期一，所以標準件可以不用考慮了。這張表上其他的都來得及。",
            "可以的話我想避開空運。我的主管要我們把運費壓到最低。",
            "在您決定之前，我得說一下：這星期寄往那一區的陸運都會晚一天，主要公路在施工。",
            "喔，那陸運就完全不行了。",
            "恐怕是的。不過空運不受影響。",
            "好吧，我付空運的錢，但不要隔夜件。星期四到就夠了。",
            "好的。箱子掃描進系統後，我會把追蹤號碼用電子郵件寄給您，您可以轉寄給客戶。",
            "太好了。我的電子郵件在這張名片上。",
        ],
        "questions": [
            {
                "q": "Why does the woman want to avoid the air services at first?",
                "options": ["They would not arrive by Thursday", "Her supervisor asked her to limit expenses", "Her client prefers ground delivery", "They are delayed by road construction"],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "原因題：理由在下一句，manager → supervisor",
                    "why": "她先說想避開空運，接著說 manager wants us to keep shipping costs to a minimum → 改述成主管要壓低開支。",
                    "evidence": [2],
                    "wrong": ["方向相反：男方說除了標準件，其他都來得及", None, "同字陷阱：client 出現過，但沒說客戶偏好什麼", "張冠李戴：施工延誤的是陸運，空運不受影響"],
                    "wrongMore": [None, None, None, "road construction 確實出現，也確實造成延誤；但受影響的是 ground shipments，男方明說 air services aren't affected。"],
                    "vocab": [["keep … to a minimum", "壓到最低"], ["expense", "開支、費用"]],
                },
            },
            {
                "q": "Look at the graphic. How much will the woman most likely pay?",
                "options": ["$18.00", "$32.00", "$45.00", "$70.00"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：先刪掉來不及和她不要的，再對價格",
                    "why": "陸運本週晚一天，三天的 Express Ground 會拖到星期五；她改空運但 not overnight → 表上的 Two-Day Air，$45.00。",
                    "evidence": [3, 4, 5, 6],
                    "wrong": ["標準件要 5–7 天，一開始就被男方排除", "她原本想選的陸運；本週晚一天就來不及", None, "她說 not overnight，不要隔夜件"],
                    "wrongMore": [
                        None,
                        "沒有延誤的話，Express Ground 三個工作天正好星期四送到，也是想省錢時的首選；但男方說陸運本週晚一天，會變成星期五。",
                        None,
                        None,
                    ],
                    "vocab": [["rule out", "排除"], ["run a day behind", "晚一天"], ["business day", "工作天"]],
                },
            },
            {
                "q": "What does the man say he will do?",
                "options": ["Contact the woman's client directly", "Send her a way to follow the shipment", "Switch the box to ground service", "Give her a discount on air shipping"],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "細節題：聽男方 I'll… 的那一句",
                    "why": "男方說 I'll e-mail you a tracking number → 改述成寄給她一個可以追蹤（follow）包裹的方法。",
                    "evidence": [7],
                    "wrong": ["張冠李戴：要轉寄給客戶的是女方", None, "方向相反：陸運本週會晚到，她已改空運", "沒有人提到折扣"],
                    "wrongMore": ["client 確實出現在同一句，但 you can forward to your client 是請女方自己轉寄；男方只寄給她。", None, None, None],
                    "vocab": [["tracking number", "追蹤號碼"], ["forward", "轉寄"], ["scan", "掃描"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ talk (Part 4)
    # l-talk-04  factory visit. Q2 is the quote question: the literal reading (jackets not allowed) is the trap;
    # "in there" must be traced back to the furnace room. Q3: "except the studio" is the exception;
    # (B) moves the painters from the gift shop to the studio.
    {
        "id": "l-talk-04", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-talk-04", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Good morning, and welcome to Hollis Glassworks. My name is Dana, and I'll be showing you around for the next hour."},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "We'll begin in the furnace room, where our glassblowers shape every vase and bowl by hand."},
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "Trust me, you won't need your jackets in there."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "After that, we'll walk through the packing area and stop by the design studio."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "Feel free to take pictures anywhere except the studio. Some of the pieces there won't be in stores until next spring."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "Normally we'd finish in our gift shop, but the painters are working in there until Friday."},
                {"file": "07.mp3", "who": "W", "voice": "bf_emma", "text": "Instead, before you leave, I'll give each of you a card for 10% off anything on our website.",
                 "say": "Instead, before you leave, I'll give each of you a card for ten percent off anything on our website."},
                {"file": "08.mp3", "who": "W", "voice": "bf_emma", "text": "All right, if everyone's ready, please follow me."},
            ],
        },
        "transcriptZh": [
            "早安，歡迎來到 Hollis 玻璃工坊。我叫 Dana，接下來一個小時由我帶大家四處看看。",
            "我們會先從熔爐室開始，我們的玻璃工匠在那裡用手工把每一個花瓶和碗塑形。",
            "相信我，在裡面你們用不到外套。",
            "之後我們會走過包裝區，再到設計工作室看看。",
            "除了工作室以外，到哪裡都可以隨意拍照。工作室裡有些作品要到明年春天才會在店裡販售。",
            "平常我們會在禮品店結束，但油漆工到星期五前都在裡面施工。",
            "取而代之的是，在大家離開前，我會發給每個人一張卡，可以在我們網站上買任何東西都打九折。",
            "好，如果大家都準備好了，請跟我來。",
        ],
        "questions": [
            {
                "q": "Who most likely is the speaker?",
                "options": ["A glassblower", "A tour guide", "A gift shop clerk", "A painter"],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "身分題：從 showing you around 推說話者",
                    "why": "她說 welcome to Hollis Glassworks、I'll be showing you around → 帶訪客參觀工廠的人，改述成 a tour guide。",
                    "evidence": [0, 1],
                    "wrong": ["提到但不是問的：our glassblowers 是她的同事", None, "同字陷阱：禮品店這次不會去", "同字陷阱：painters 是在禮品店施工的人"],
                    "wrongMore": ["our glassblowers 表示她在這家工坊工作，所以很像；但她自己做的事是 showing you around，帶大家參觀。", None, None, None],
                    "vocab": [["show … around", "帶……四處參觀"], ["glassblower", "玻璃吹製工匠"]],
                },
            },
            {
                "q": "Why does the speaker say, \"Trust me, you won't need your jackets in there\"?",
                "options": ["To explain that jackets are not allowed", "To warn listeners about high temperatures", "To suggest that the visit will be short", "To mention that the work is done outdoors"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：in there 指熔爐室，從場所推言外之意",
                    "why": "前一句說要去 furnace room（熔爐室），in there 就是那裡 → 用不到外套是因為很熱，改述成提醒大家溫度很高。",
                    "evidence": [1, 2],
                    "wrong": ["字面陷阱：won't need 是用不到，不是不准穿", None, "提到但不是問的：一小時是整趟參觀的長度", "語境矛盾：in there 是室內的熔爐室"],
                    "wrongMore": ["只看字面會以為是服裝規定；但 Trust me 是給建議的語氣，won't need 是「用不到」，原因要回頭看前一句的 furnace room。", None, None, None],
                    "vocab": [["furnace", "熔爐"], ["trust me", "相信我（給建議時用）"]],
                },
            },
            {
                "q": "What does the speaker say about the design studio?",
                "options": ["Visitors may take photos there", "It is being painted this week", "It contains products that are not on sale yet", "It is where items are shaped by hand"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "細節題：except 帶出例外，there 指 studio",
                    "why": "studio 不能拍照，因為 pieces there won't be in stores until next spring → 改述成裡面有還沒上市的商品。",
                    "evidence": [4],
                    "wrong": ["方向相反：只有 studio 不能拍照（except）", "張冠李戴：油漆工是在禮品店施工", None, "張冠李戴：手工塑形是在熔爐室"],
                    "wrongMore": [
                        "anywhere 讓人以為到處都能拍；但同一句後面 except the studio 正好把 studio 排除在外。",
                        "painters 確實出現，但他們是在 gift shop 施工到星期五，不是在 studio。",
                        None,
                        None,
                    ],
                    "vocab": [["feel free to", "儘管、隨意"], ["piece", "（一件）作品"]],
                },
            },
        ],
    },
]
