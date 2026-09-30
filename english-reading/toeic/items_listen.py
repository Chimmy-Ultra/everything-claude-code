# Listening items for the TOEIC 練習室 (DESIGN.md sections 3, 5 and 7).
# 8 qr (Part 2 style), 4 conv (Part 3 style), 2 talk (Part 4 style). All content is original.
# `say` overrides the TTS text wherever the displayed text has digits, times, prices,
# abbreviations or the name "Wei". reviewed stays False until every mp3 has been heard.


def _qr(voice_q, who_q, voice_r, who_r, q, a, b, c):
    """Audio lines for a Part 2 item: the question in one voice, three responses in another."""
    return [
        {"file": "q.mp3", "who": who_q, "voice": voice_q, "text": q},
        {"file": "a.mp3", "who": who_r, "voice": voice_r, "text": a},
        {"file": "b.mp3", "who": who_r, "voice": voice_r, "text": b},
        {"file": "c.mp3", "who": who_r, "voice": voice_r, "text": c},
    ]


ITEMS = [
    # ------------------------------------------------------------------ qr (Part 2)
    {
        "id": "l-qr-01", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-01", "gapMs": 900,
            "lines": _qr("af_sarah", "W", "am_michael", "M",
                         "Where should I leave these boxes of paper?",
                         "Yes, they came this morning.",
                         "I read about it in the paper.",
                         "Just put them by the copier."),
        },
        "transcriptZh": ["這幾箱紙我該放在哪裡？", "是的，它們今天早上送到的。", "我是在報紙上看到的。", "放在影印機旁邊就好。"],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "explain": {
                "point": "Where 問地點，要找講「位置」的回應",
                "why": "問 where should I leave → 回 put them by the copier：leave 改述成 put，並給出位置。",
                "evidence": [3],
                "wrong": ["答錯問句類型：where 問句不能用 Yes 回", "同字陷阱：paper 在這裡是報紙，沒答地點", None],
                "vocab": [["copier", "影印機"], ["leave", "放著、留下"]],
            },
        }],
    },
    {
        "id": "l-qr-02", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-02", "gapMs": 900,
            "lines": _qr("bm_george", "M", "bf_emma", "W",
                         "Who's in charge of ordering supplies for the new office?",
                         "Mostly pens and printer ink.",
                         "Rachel at reception handles that.",
                         "The new office is really bright."),
        },
        "transcriptZh": ["新辦公室的用品是誰負責訂的？", "大多是筆和印表機墨水。", "櫃台的 Rachel 負責那件事。", "新辦公室採光很好。"],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "explain": {
                "point": "Who 問人，要找講出「某個人」的回應",
                "why": "問 who's in charge of ordering → 回 Rachel handles that：in charge of 改述成 handles。",
                "evidence": [2],
                "wrong": ["答錯問句類型：答的是訂什麼，不是誰", None, "同字陷阱：重複 new office，沒說是誰"],
                "vocab": [["in charge of", "負責"], ["supplies", "用品、耗材"], ["reception", "櫃台、接待處"]],
            },
        }],
    },
    {
        "id": "l-qr-03", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-03", "gapMs": 900,
            "lines": _qr("am_michael", "M", "bf_emma", "W",
                         "Why was the client meeting moved to the afternoon?",
                         "Their flight was delayed.",
                         "In the large meeting room.",
                         "Yes, it went very well."),
        },
        "transcriptZh": ["跟客戶的會議為什麼改到下午？", "他們的班機延誤了。", "在大會議室。", "是的，進行得很順利。"],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "explain": {
                "point": "Why 問原因，要找講「理由」的回應",
                "why": "問 why was it moved → 回 their flight was delayed：說出客戶晚到、只好改時間的原因。",
                "evidence": [1],
                "wrong": [None, "同字陷阱：重複 meeting，答的卻是地點", "答錯問句類型：why 問句不能用 Yes 回"],
                "vocab": [["client", "客戶"], ["delayed", "延誤的"]],
            },
        }],
    },
    {
        "id": "l-qr-04", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-04", "gapMs": 900,
            "lines": _qr("am_michael", "M", "af_bella", "W",
                         "Is the printer upstairs working again?",
                         "Our team is working on a new project.",
                         "Yes, someone repaired it an hour ago.",
                         "Double-sided, please."),
        },
        "transcriptZh": ["樓上那台印表機又能用了嗎？", "我們團隊正在做一個新專案。", "可以了，一個小時前有人修好了。", "麻煩印雙面。"],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "explain": {
                "point": "Yes/No 問句：回應要針對「能不能用」",
                "why": "問 is it working again → 回 someone repaired it：修好了就等於又能用了。",
                "evidence": [2],
                "wrong": ["同字陷阱：working 在這裡是「做專案」", None, "講的是列印設定，沒回答修好了沒"],
                "vocab": [["upstairs", "樓上"], ["repair", "修理"], ["double-sided", "雙面的"]],
            },
        }],
    },
    {
        "id": "l-qr-05", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-05", "gapMs": 900,
            "lines": _qr("bf_emma", "W", "bm_lewis", "M",
                         "You've already booked the hotel for the sales conference, haven't you?",
                         "The conference was very useful.",
                         "A double room, please.",
                         "Yes, I reserved rooms for everyone yesterday."),
        },
        "transcriptZh": ["業務會議的飯店你已經訂好了，對吧？", "那場會議很有收穫。", "一間雙人房，謝謝。", "對，我昨天就幫大家訂好房間了。"],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "explain": {
                "point": "附加問句：照一般 Yes/No 問句來回答",
                "why": "問 booked the hotel → 回 reserved rooms for everyone：booked 改述成 reserved。",
                "evidence": [3],
                "wrong": ["同字陷阱：重複 conference，還說成已經開過", "像在跟飯店櫃台訂房，沒回答訂好了沒", None],
                "vocab": [["book", "預訂"], ["reserve", "預訂、保留"], ["sales conference", "業務會議"]],
            },
        }],
    },
    {
        "id": "l-qr-06", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-06", "gapMs": 900,
            "lines": _qr("af_sarah", "W", "am_michael", "M",
                         "When will the new price list be ready?",
                         "Monica is still checking the numbers.",
                         "Yes, the prices are quite reasonable.",
                         "I made a list of new clients."),
        },
        "transcriptZh": ["新的價目表什麼時候會好？", "Monica 還在核對數字。", "是的，價格相當合理。", "我列了一份新客戶名單。"],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "explain": {
                "point": "間接回答：不給時間，改說「還在處理中」",
                "why": "問 when will it be ready → 回 Monica is still checking the numbers：間接表示還沒好、要再等。",
                "evidence": [1],
                "wrong": [None, "答錯問句類型：when 問句不能用 Yes 回", "同字陷阱：重複 new 和 list，講的是別的名單"],
                "vocab": [["price list", "價目表"], ["check", "核對"]],
            },
        }],
    },
    {
        "id": "l-qr-07", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-07", "gapMs": 900,
            "lines": _qr("bm_george", "M", "af_bella", "W",
                         "Would you like me to send the contract to the client today?",
                         "At the post office on Main Street.",
                         "The lawyers haven't finished going over it.",
                         "She's been our client for years."),
        },
        "transcriptZh": ["要我今天把合約寄給客戶嗎？", "在 Main Street 的郵局。", "律師還沒看完。", "她當我們的客戶很多年了。"],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "explain": {
                "point": "間接回答：不說 yes/no，用理由表示「先別寄」",
                "why": "問要不要今天寄 → 回 the lawyers haven't finished going over it：還沒審完，意思是先別寄。",
                "evidence": [2],
                "wrong": ["答錯問句類型：問要不要寄，卻回答地點", None, "同字陷阱：重複 client，沒回應要不要寄"],
                "vocab": [["contract", "合約"], ["go over", "仔細看過、審閱"]],
            },
        }],
    },
    {
        "id": "l-qr-08", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-08", "gapMs": 900,
            "lines": _qr("af_bella", "W", "bm_george", "M",
                         "How do I get to the staff kitchen from here?",
                         "Yes, the kitchen was just cleaned.",
                         "I usually take the bus.",
                         "Sorry, it's only my first week."),
        },
        "transcriptZh": ["請問從這裡要怎麼走到員工茶水間？", "是的，茶水間剛打掃過。", "我通常搭公車。", "抱歉，我才來第一個星期。"],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "explain": {
                "point": "間接回答：用「我也不熟」的理由回應",
                "why": "問 how do I get to the kitchen → 回 it's only my first week：間接表示自己也不知道怎麼走。",
                "evidence": [3],
                "wrong": ["答錯問句類型：how 問句不能用 Yes 回", "講的是通勤方式，不是從這裡怎麼走", None],
                "vocab": [["staff kitchen", "員工茶水間"], ["first week", "（上班的）第一週"]],
            },
        }],
    },

    # ------------------------------------------------------------------ conv (Part 3)
    {
        "id": "l-conv-01", "type": "listen", "format": "conv", "unit": "conv-topic", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-conv-01", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_michael", "text": "Hi Paula, do you have a minute? I heard our department is moving to the fifth floor next month."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "That's right. There's more space up there, and we'll finally have our own meeting rooms."},
                {"file": "03.mp3", "who": "M", "voice": "am_michael", "text": "Great. Do we need to pack up our own desks?"},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Just your personal things. A moving company will handle the furniture and computers."},
                {"file": "05.mp3", "who": "M", "voice": "am_michael", "text": "Okay. And when does everything need to be packed?"},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "By Thursday the 14th. I'll give everyone boxes and labels tomorrow morning.",
                 "say": "By Thursday the fourteenth. I'll give everyone boxes and labels tomorrow morning."},
            ],
        },
        "transcriptZh": [
            "嗨 Paula，有空嗎？我聽說我們部門下個月要搬到五樓。",
            "沒錯。樓上空間比較大，我們終於會有自己的會議室了。",
            "太好了。我們要自己打包辦公桌嗎？",
            "只要打包個人物品就好。家具和電腦會由搬家公司處理。",
            "好。那東西要在什麼時候之前打包好？",
            "14 號星期四之前。我明天早上會發紙箱和標籤給大家。",
        ],
        "questions": [
            {
                "q": "What are the speakers mainly discussing?",
                "options": ["Hiring a moving company", "Their team's relocation", "Buying new office furniture", "Booking a meeting room"],
                "answer": 1,
                "explain": {
                    "point": "主旨題：答案通常在前一兩句",
                    "why": "男方說 our department is moving to the fifth floor → 選項改述成 their team's relocation。",
                    "evidence": [0],
                    "wrong": ["同字陷阱：搬家公司只是細節，不是主題", None, "同字陷阱：家具是要搬，不是要買", "同字陷阱：會議室是新樓層的好處，不是主題"],
                    "vocab": [["department", "部門"], ["relocation", "搬遷"]],
                },
            },
            {
                "q": "What will the woman do tomorrow?",
                "options": ["Pack up her desk", "Contact a moving company", "Hand out packing materials", "Move the computers"],
                "answer": 2,
                "explain": {
                    "point": "細節題：鎖定題目問的人和時間",
                    "why": "女方說 I'll give everyone boxes and labels tomorrow → 改述成 hand out packing materials。",
                    "evidence": [5],
                    "wrong": ["同字陷阱：desk 出現過，但她沒說明天要打包", "沒有人提到要聯絡搬家公司", None, "張冠李戴：電腦是搬家公司負責搬"],
                    "vocab": [["label", "標籤"], ["hand out", "分發"]],
                },
            },
        ],
    },
    {
        "id": "l-conv-02", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-02", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Hello, I'd like to order sandwiches for a training session this Friday. There'll be 18 of us.",
                 "say": "Hello, I'd like to order sandwiches for a training session this Friday. There'll be eighteen of us."},
                {"file": "02.mp3", "who": "M", "voice": "am_michael", "text": "Sure. Each of our platters serves six, so you'd need three. They're $45 each.",
                 "say": "Sure. Each of our platters serves six, so you'd need three. They're forty-five dollars each."},
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "That's fine. Could you deliver them by 11:30?",
                 "say": "That's fine. Could you deliver them by eleven thirty?"},
                {"file": "04.mp3", "who": "M", "voice": "am_michael", "text": "I'm afraid our driver doesn't start deliveries until noon on Fridays. But you're welcome to come and get them earlier."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "Well, our office is just around the corner, so I'll send my assistant to collect them."},
                {"file": "06.mp3", "who": "M", "voice": "am_michael", "text": "Perfect. I'll have everything ready at the front counter by eleven."},
            ],
        },
        "transcriptZh": [
            "你好，我想為這星期五的訓練課程訂三明治。我們一共 18 個人。",
            "好的。我們的拼盤一盤六人份，所以您需要三盤。每盤 45 美元。",
            "可以。能在 11 點半前送到嗎？",
            "不好意思，我們星期五的外送司機中午才開始送。不過歡迎您提早過來拿。",
            "嗯，我們辦公室就在轉角，那我請助理過去拿。",
            "太好了。我會在 11 點前把東西都放在前面櫃台準備好。",
        ],
        "questions": [
            {
                "q": "What problem does the man mention?",
                "options": ["The order cannot arrive in time", "The platters are sold out", "The price has gone up", "The kitchen closes at noon"],
                "answer": 0,
                "explain": {
                    "point": "細節題：找男方提到的「問題」",
                    "why": "男方說 driver doesn't start deliveries until noon（她要 11:30 前）→ 改述成 cannot arrive in time。",
                    "evidence": [2, 3],
                    "wrong": [None, "同字陷阱：platter 出現過，但沒說賣完", "價格只報了一次，沒說漲價", "同字陷阱：noon 是開始外送的時間"],
                    "vocab": [["platter", "拼盤、大淺盤"], ["I'm afraid", "恐怕（委婉拒絕）"]],
                },
            },
            {
                "q": "What does the woman decide to do?",
                "options": ["Order a larger platter", "Move the session to the afternoon", "Wait for the noon delivery", "Have a staff member pick up the food"],
                "answer": 3,
                "explain": {
                    "point": "細節題：找女方最後的決定",
                    "why": "女方說 I'll send my assistant to collect them → 改述成 have a staff member pick up the food。",
                    "evidence": [4],
                    "wrong": ["同字陷阱：platter 出現過，但她沒要換大份", "沒有人提到要改訓練時間", "同字陷阱：noon 外送是男方說的，她沒選", None],
                    "vocab": [["collect", "去拿、領取"], ["around the corner", "就在附近"]],
                },
            },
        ],
    },
    {
        "id": "l-conv-03", "type": "listen", "format": "conv", "unit": "conv-intent", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-conv-03", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_lewis", "text": "Lucy, the print shop needs the final brochure by tomorrow morning. Could we go through it together this afternoon?"},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "I'd like to, but I've got a dentist appointment at three."},
                {"file": "03.mp3", "who": "M", "voice": "bm_lewis", "text": "Then how about straight after lunch? It shouldn't take more than half an hour."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "That works. And Tom has already checked the prices on the back page, so we only need to look at the photos and headings."},
                {"file": "05.mp3", "who": "M", "voice": "bm_lewis", "text": "Oh, good. That'll save time. I'll book a meeting room for one o'clock."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "Great. I'll bring a printed copy so we can mark changes by hand."},
            ],
        },
        "transcriptZh": [
            "Lucy，印刷廠明天早上就要拿到手冊的定稿。我們今天下午可以一起看一遍嗎？",
            "我是很想，可是我三點要去看牙醫。",
            "那吃完午餐馬上看怎麼樣？應該不會超過半小時。",
            "可以。而且 Tom 已經核對過封底的價格了，我們只要看照片和標題就好。",
            "喔，太好了，這樣能省點時間。我來訂一點的會議室。",
            "好。我會帶一份印出來的稿子，我們可以直接用筆標出要改的地方。",
        ],
        "questions": [
            {
                "q": "Why does the woman mention a dentist appointment?",
                "options": ["To ask for the day off", "To say she won't be free later in the day", "To suggest a later deadline", "To recommend a dentist to the man"],
                "answer": 1,
                "explain": {
                    "point": "意圖題：想這句話在對話中的作用",
                    "why": "女方用 dentist appointment at three 回應下午的邀約 → 意思是晚點沒空（won't be free later）。",
                    "evidence": [1, 2],
                    "wrong": ["她只是三點要走，不是請整天假", None, "沒有人提議延後期限", "同字陷阱：重複 dentist，但不是在推薦"],
                    "vocab": [["go through", "從頭看一遍"], ["appointment", "預約"]],
                },
            },
            {
                "q": "What has Tom already done?",
                "options": ["Taken the photos", "Booked a meeting room", "Reviewed the cost details", "Printed a copy of the brochure"],
                "answer": 2,
                "explain": {
                    "point": "細節題：注意是誰做了哪件事",
                    "why": "女方說 Tom has already checked the prices → 改述成 reviewed the cost details。",
                    "evidence": [3],
                    "wrong": ["同字陷阱：photos 是他們還要看的部分", "張冠李戴：要訂會議室的是男方", None, "張冠李戴：要帶印好稿子的是女方"],
                    "vocab": [["brochure", "宣傳手冊"], ["heading", "標題"]],
                },
            },
        ],
    },
    {
        "id": "l-conv-04", "type": "listen", "format": "conv", "unit": "conv-next", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-04", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Hi, is this the IT help desk? My laptop keeps shutting down after about twenty minutes.",
                 "say": "Hi, is this the I T help desk? My laptop keeps shutting down after about twenty minutes."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "That sounds like the battery. Is it the model the company handed out last year, or an older one?"},
                {"file": "03.mp3", "who": "W", "voice": "af_bella", "text": "An older one. I've had it for about four years."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Then the battery's probably worn out. We keep spares here, but I'll need the model number to find the right one."},
                {"file": "05.mp3", "who": "W", "voice": "af_bella", "text": "Sure. It's on the bottom, isn't it? Let me turn it over."},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "Yes, it's on the silver sticker. Once I have that, I can bring a new battery up to your desk this afternoon."},
            ],
        },
        "transcriptZh": [
            "你好，請問是 IT 服務台嗎？我的筆電用大概二十分鐘就一直自動關機。",
            "聽起來是電池的問題。是公司去年發的那款，還是比較舊的？",
            "比較舊的，我已經用了大概四年。",
            "那電池大概是老化了。我們這裡有備品，但我需要型號才能找到對的那一顆。",
            "好。型號在底部，對吧？我把它翻過來看看。",
            "對，在那張銀色貼紙上。拿到型號之後，我今天下午就能把新電池送到你的座位。",
        ],
        "questions": [
            {
                "q": "What will the woman most likely do next?",
                "options": ["Buy a new laptop", "Take her laptop to the help desk", "Replace the battery herself", "Check the underside of her computer"],
                "answer": 3,
                "explain": {
                    "point": "下一步題：答案常在最後幾句",
                    "why": "女方說 It's on the bottom… Let me turn it over → 改述成 check the underside of her computer。",
                    "evidence": [3, 4],
                    "wrong": ["沒有人提到要買新電腦", "張冠李戴：是男方要把電池送到她座位", "同字陷阱：battery 出現過，但由男方送來", None],
                    "vocab": [["model number", "型號"], ["turn over", "翻過來"]],
                },
            },
            {
                "q": "What does the man offer to do this afternoon?",
                "options": ["Deliver a part to her workspace", "Lend her a newer laptop", "Order a battery from a supplier", "Update her software"],
                "answer": 0,
                "explain": {
                    "point": "細節題：找男方說下午能做的事",
                    "why": "男方說 bring a new battery up to your desk → 改述成 deliver a part to her workspace。",
                    "evidence": [5],
                    "wrong": [None, "只提到公司去年發的機型，沒說要借她", "同字陷阱：battery 出現過，但備品就在這裡", "沒有人提到更新軟體"],
                    "vocab": [["worn out", "老化、耗損"], ["spare", "備品"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ talk (Part 4)
    {
        "id": "l-talk-01", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-talk-01", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_george", "text": "Good morning, everyone. This is an update from building management about the lifts on the east side."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "Starting on Monday, a team will be replacing those lifts, and the work should take about two weeks."},
                {"file": "03.mp3", "who": "M", "voice": "bm_george", "text": "Until then, please use the lifts by the main entrance, or take the stairs."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Since mornings may be busier than usual, the café on the ground floor will open fifteen minutes earlier."},
                {"file": "05.mp3", "who": "M", "voice": "bm_george", "text": "Thank you for your patience."},
            ],
        },
        "transcriptZh": [
            "大家早安。這是大樓管理處的通知，關於東側的電梯。",
            "從星期一開始，會有一組人員更換那幾部電梯，工程大約需要兩個星期。",
            "在工程完成之前，請搭乘大門旁邊的電梯，或是走樓梯。",
            "由於早上可能會比平常擁擠，一樓的咖啡店會提早十五分鐘開門。",
            "謝謝大家耐心配合。",
        ],
        "questions": [
            {
                "q": "What is the announcement mainly about?",
                "options": ["The opening of a new café", "A change in office hours", "The installation of new elevators", "A fire safety drill"],
                "answer": 2,
                "explain": {
                    "point": "主旨題：答案通常在開頭",
                    "why": "說 a team will be replacing those lifts → 改述成 installation of new elevators（lift＝elevator）。",
                    "evidence": [0, 1],
                    "wrong": ["同字陷阱：咖啡店本來就在，只是提早開", "只有咖啡店提早開，上班時間沒變", None, "只叫大家走樓梯，沒提到演習"],
                    "vocab": [["lift", "（英）電梯＝elevator"], ["building management", "大樓管理處"]],
                },
            },
            {
                "q": "What will the café do?",
                "options": ["Start serving sooner in the morning", "Move to the ground floor", "Close for two weeks", "Deliver breakfast to offices"],
                "answer": 0,
                "explain": {
                    "point": "細節題：鎖定題目裡的關鍵名詞 café",
                    "why": "說 the café will open fifteen minutes earlier → 改述成 start serving sooner in the morning。",
                    "evidence": [3],
                    "wrong": [None, "同字陷阱：ground floor 是它原本的位置", "同字陷阱：兩週是換電梯的工期", "沒有人提到外送早餐"],
                    "vocab": [["ground floor", "（英）一樓"], ["patience", "耐心"]],
                },
            },
        ],
    },
    {
        "id": "l-talk-02", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-02", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Hi, this is Nora Blake from the Riverside Business Forum, calling for Mr. Wei.",
                 "say": "Hi, this is Nora Blake from the Riverside Business Forum, calling for Mister Way."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "I'm confirming your talk on Thursday, May 8th, at 2 p.m. in Room 4B.",
                 "say": "I'm confirming your talk on Thursday, May eighth, at two P M in Room four B."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "Please note that it will now run 40 minutes instead of 30, because another speaker had to cancel.",
                 "say": "Please note that it will now run forty minutes instead of thirty, because another speaker had to cancel."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Could you email me your slides by Monday so our technician can load them onto the laptop in the room?"},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "And if you'd like a parking pass, just let me know. See you next week!"},
            ],
        },
        "transcriptZh": [
            "嗨，我是 Riverside 商業論壇的 Nora Blake，要找 Wei 先生。",
            "跟您確認，您的演講是在 5 月 8 日星期四下午兩點，地點在 4B 會議室。",
            "請留意，因為另一位講者必須取消，您的演講會從 30 分鐘改成 40 分鐘。",
            "可以請您在星期一前把投影片寄給我嗎？這樣我們的技術人員才能先放進會議室的筆電。",
            "還有，如果您需要停車證，跟我說一聲就好。下週見！",
        ],
        "questions": [
            {
                "q": "What change does the speaker mention?",
                "options": ["His talk has moved to Monday", "His room has been changed", "Another speaker will join his session", "He will have more time to speak"],
                "answer": 3,
                "explain": {
                    "point": "細節題：聽「改變」的訊號 instead of",
                    "why": "說 40 minutes instead of 30 → 改述成 he will have more time to speak。",
                    "evidence": [2],
                    "wrong": ["同字陷阱：Monday 是交投影片的期限", "4B 會議室只是確認，沒有更換", "同字陷阱：另一位講者是取消，不是加入", None],
                    "vocab": [["confirm", "確認"], ["instead of", "取代、而不是"]],
                },
            },
            {
                "q": "What does the speaker ask Mr. Wei to do?",
                "options": ["Buy a parking pass", "Send his presentation files", "Call the technician", "Bring his own laptop"],
                "answer": 1,
                "explain": {
                    "point": "細節題：聽請求句 Could you…",
                    "why": "說 Could you email me your slides → 改述成 send his presentation files。",
                    "evidence": [3],
                    "wrong": ["同字陷阱：停車證是需要再說，不是要他買", None, "同字陷阱：technician 是負責放檔案的人", "同字陷阱：會議室裡已經有筆電"],
                    "vocab": [["slides", "投影片"], ["technician", "技術人員"], ["parking pass", "停車證"]],
                },
            },
        ],
    },
]
