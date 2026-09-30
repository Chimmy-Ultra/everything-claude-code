# Listening items for the TOEIC 練習室 (DESIGN.md sections 3, 5 and 7).
# 12 qr (Part 2 style), 6 conv (Part 3 style, 3 questions each; l-conv-05 has three speakers, l-conv-06 a graphic),
# 3 talk (Part 4 style, 3 questions each). Scripts are written in US English even when a British voice reads them.
# All content is original. `say` overrides the TTS text wherever the displayed text has digits, times,
# prices, abbreviations or the name "Wei". reviewed stays False until the items pass a blind review
# and every mp3 has been heard.

ITEMS = [
    # ------------------------------------------------------------------ qr (Part 2)
    {
        "id": "l-qr-01", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-01", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "Where's the orientation for the new interns being held?"},
                {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "Mostly business students."},
                {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "In the training room next to the cafeteria."},
                {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "It starts at nine thirty."},
            ],
        },
        "transcriptZh": ["新進實習生的說明會在哪裡舉行？", "大多是商科的學生。", "在員工餐廳旁邊的訓練教室。", "九點半開始。"],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "explain": {
                "point": "Where 問地點：找說出「在哪裡」的回應",
                "why": "問 where's the orientation being held → 回 in the training room next to the cafeteria：給出地點。",
                "evidence": [2],
                "wrong": ["答錯問句類型：講實習生是哪些人，不是地點", None, "答錯問句類型：回答開始時間，不是地點"],
                "vocab": [["orientation", "新人說明會"], ["intern", "實習生"], ["cafeteria", "員工餐廳"]],
            },
        }],
    },
    {
        "id": "l-qr-02", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-02", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_george", "text": "I can't open the quarterly sales spreadsheet on the shared drive."},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "Sales were up again this quarter."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "I'll drive you there after lunch."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "Martin was editing it a few minutes ago."},
            ],
        },
        "transcriptZh": ["我打不開共用磁碟上那份季度業績試算表。", "這一季業績又成長了。", "午餐後我開車載你過去。", "Martin 幾分鐘前還在編輯那個檔案。"],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "explain": {
                "point": "敘述句：沒有疑問詞，要找合理的接話",
                "why": "說打不開試算表 → 回 Martin was editing it：暗示有人正在用、檔案被鎖住，所以才打不開。",
                "evidence": [3],
                "wrong": ["同字陷阱：重複 sales 和 quarter，講的是業績", "同字陷阱：drive 在這裡是開車，不是磁碟", None],
                "vocab": [["spreadsheet", "試算表"], ["shared drive", "共用磁碟"], ["quarterly", "每季的"]],
            },
        }],
    },
    {
        "id": "l-qr-03", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": False, "v": 2, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-03", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_lewis", "text": "Are you taking the train to the trade fair, or driving?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "Parking near the exhibition center is really expensive."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "The fair opens on Thursday."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "I've already trained the new staff."},
            ],
        },
        "transcriptZh": ["你去商展是搭火車還是開車？", "展覽中心附近停車真的很貴。", "商展星期四開幕。", "我已經訓練過新員工了。"],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "explain": {
                "point": "選擇疑問句：回答不一定直接說選哪一個",
                "why": "問搭火車還是開車 → 回展覽中心附近停車很貴：暗示不想開車，會搭火車。",
                "evidence": [1],
                "wrong": [None, "同字陷阱：重複 fair，回答的是開幕時間", "同字陷阱：trained 是訓練員工，不是搭火車"],
                "vocab": [["trade fair", "商展"], ["exhibition center", "展覽中心"]],
            },
        }],
    },
    {
        "id": "l-qr-04", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-04", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "Haven't the new name badges come in yet?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "Yes, I came in through the side door."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "Please write your name on the list."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "No, they should be here by Friday."},
            ],
        },
        "transcriptZh": ["新的名牌還沒送到嗎？", "對，我是從側門進來的。", "請把你的名字寫在名單上。", "還沒，應該星期五前會到。"],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "explain": {
                "point": "否定問句：照一般 Yes/No 問句回答",
                "why": "問名牌還沒到嗎 → 回 No, they should be here by Friday：還沒到，come in 改述成 be here。",
                "evidence": [3],
                "wrong": ["同字陷阱：came in 講的是自己進門，不是到貨", "同字陷阱：重複 name，沒回答到了沒", None],
                "vocab": [["name badge", "名牌、識別證"], ["come in", "（貨品）送到"]],
            },
        }],
    },
    {
        "id": "l-qr-05", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-05", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "You're presenting at tomorrow's budget meeting, aren't you?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "That's right, I'll be the first speaker."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "Thanks, it's a lovely present."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "It went better than I expected."},
            ],
        },
        "transcriptZh": ["明天的預算會議你要上台報告，對吧？", "沒錯，我是第一個上台的。", "謝謝，這份禮物好漂亮。", "結果比我預期的好。"],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "explain": {
                "point": "附加問句：照一般 Yes/No 問句來回答",
                "why": "問明天要報告吧 → 回 That's right（＝yes），再用 I'll be the first speaker 改述 presenting。",
                "evidence": [1],
                "wrong": [None, "同字陷阱：present 在這裡是禮物", "時態不對：會議明天才開，不能說已經進行得如何"],
                "vocab": [["present", "報告（動詞）；禮物（名詞）"], ["budget", "預算"]],
            },
        }],
    },
    {
        "id": "l-qr-06", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-06", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "When will the new price list be ready?"},
                {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "Monica is still checking the numbers."},
                {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "Yes, the prices are quite reasonable."},
                {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "I made a list of new clients."},
            ],
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
        "id": "l-qr-07", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-07", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_george", "text": "Would you like me to send the contract to the client today?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "At the post office on Main Street."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "The lawyers haven't finished going over it."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "She's been our client for years."},
            ],
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
        "id": "l-qr-08", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-08", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_bella", "text": "How do I get to the staff kitchen from here?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "Yes, the kitchen was just cleaned."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "I usually take the bus."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "Sorry, it's only my first week."},
            ],
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
        "id": "l-conv-01", "type": "listen", "format": "conv", "unit": "conv-topic", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
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
                {"file": "07.mp3", "who": "M", "voice": "am_michael", "text": "I'll be at a client's office all day tomorrow. Could you leave mine on my chair?"},
            ],
        },
        "transcriptZh": [
            "嗨 Paula，有空嗎？我聽說我們部門下個月要搬到五樓。",
            "沒錯。樓上空間比較大，我們終於會有自己的會議室了。",
            "太好了。我們要自己打包辦公桌嗎？",
            "只要打包個人物品就好。家具和電腦會由搬家公司處理。",
            "好。那東西要在什麼時候之前打包好？",
            "14 號星期四之前。我明天早上會發紙箱和標籤給大家。",
            "我明天一整天都在客戶的辦公室。可以把我的那份放在我椅子上嗎？",
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
                "q": "According to the woman, what will a moving company do?",
                "options": ["Pack employees' personal items", "Hand out boxes and labels", "Transport office equipment", "Set up the new meeting rooms"],
                "answer": 2,
                "explain": {
                    "point": "細節題：鎖定題目裡的 moving company",
                    "why": "女方說搬家公司會 handle the furniture and computers → 改述成 transport office equipment。",
                    "evidence": [3],
                    "wrong": ["個人物品要員工自己打包，不歸搬家公司", "張冠李戴：紙箱和標籤是女方要發的", None, "同字陷阱：會議室是新樓層的好處，沒人說要布置"],
                    "vocab": [["handle", "處理、負責"], ["equipment", "設備"]],
                },
            },
            {
                "q": "What does the man ask the woman to do?",
                "options": ["Set aside some packing materials for him", "Visit a client with him", "Postpone the packing deadline", "Pack up his personal items"],
                "answer": 0,
                "explain": {
                    "point": "請求題：聽 Could you…；mine 要往前一句找",
                    "why": "mine 指前一句的 boxes and labels；leave mine on my chair → 改述成 set aside packing materials。",
                    "evidence": [5, 6],
                    "wrong": [None, "同字陷阱：client 是他明天自己要去拜訪的", "他只問了期限，沒要求延後", "個人物品要自己打包，他沒請她代勞"],
                    "vocab": [["set aside", "留下、預留"], ["label", "標籤"]],
                },
            },
        ],
    },
    {
        "id": "l-conv-02", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
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
            "不好意思，我們的司機星期五要到中午才開始外送。不過歡迎您提早過來拿。",
            "嗯，我們辦公室就在轉角，那我請助理過去拿。",
            "太好了。我會在 11 點前把東西都放在前面櫃台準備好。",
        ],
        "questions": [
            {
                "q": "Where does the man most likely work?",
                "options": ["At a training center", "At a courier company", "At a catering business", "At an office supply store"],
                "answer": 2,
                "explain": {
                    "point": "場所題：從「我們的」產品和服務推工作地點",
                    "why": "男方說 each of our platters serves six 並報每盤價格 → 他在賣餐點拼盤，改述成 a catering business。",
                    "evidence": [1],
                    "wrong": ["同字陷阱：training session 是女方公司的活動", "聯想陷阱：有司機外送，但他賣的是餐點", None, "沒有人提到辦公用品"],
                    "vocab": [["platter", "拼盤、大淺盤"], ["catering", "餐飲外燴"]],
                },
            },
            {
                "q": "What problem does the man mention?",
                "options": ["The order cannot arrive in time", "The platters are sold out", "The price has gone up", "The kitchen closes at noon"],
                "answer": 0,
                "explain": {
                    "point": "細節題：找男方提到的「問題」",
                    "why": "男方說 driver doesn't start deliveries until noon（她要 11:30 前）→ 改述成 cannot arrive in time。",
                    "evidence": [2, 3],
                    "wrong": [None, "同字陷阱：platter 出現過，但沒說賣完", "價格只報了一次，沒說漲價", "同字陷阱：noon 是開始外送的時間"],
                    "vocab": [["I'm afraid", "恐怕（委婉帶出壞消息）"], ["in time", "來得及、及時"]],
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
        "id": "l-conv-03", "type": "listen", "format": "conv", "unit": "conv-intent", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-conv-03", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_lewis", "text": "Lucy, the print shop needs the final brochure by tomorrow morning. Could we go through it together this afternoon?"},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "I'd like to, but I've got a dentist appointment at three."},
                {"file": "03.mp3", "who": "M", "voice": "bm_lewis", "text": "Then how about straight after lunch? It shouldn't take more than half an hour."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "That works. And we can skip the back page. Tom went over it yesterday."},
                {"file": "05.mp3", "who": "M", "voice": "bm_lewis", "text": "The page with all the prices? Oh, good. That'll save us some time."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "So we only need to check the photos and headings. I'll bring a printed copy so we can mark changes by hand."},
                {"file": "07.mp3", "who": "M", "voice": "bm_lewis", "text": "Great. I'll book a meeting room for one o'clock, then."},
            ],
        },
        "transcriptZh": [
            "Lucy，印刷廠明天早上就要拿到手冊的定稿。我們今天下午可以一起看一遍嗎？",
            "我是很想，可是我三點要去看牙醫。",
            "那吃完午餐馬上看怎麼樣？應該不會超過半小時。",
            "可以。而且封底那頁可以跳過，Tom 昨天已經看過了。",
            "就是列了所有價格的那一頁？喔，太好了，這樣能省一點時間。",
            "所以我們只要檢查照片和標題就好。我會帶一份印出來的稿子，我們可以直接用筆標出要改的地方。",
            "好。那我來訂一點的會議室。",
        ],
        "questions": [
            {
                "q": "What does the woman imply when she says, \"I've got a dentist appointment at three\"?",
                "options": ["She cannot work on the brochure today", "She thinks the deadline should be extended", "She would prefer to meet tomorrow morning", "She will not be free later in the afternoon"],
                "answer": 3,
                "explain": {
                    "point": "引句題：看這句話在回應對方的什麼提議",
                    "why": "男方約今天下午，她回三點要看牙醫 → 意思是下午晚一點沒空，改述成 not free later in the afternoon。",
                    "evidence": [0, 1],
                    "wrong": ["後來兩人約午餐後一起看，她今天還是能處理", "沒有人提議延後交稿時間", "印刷廠明早就要，明早才看來不及", None],
                    "vocab": [["go through", "從頭看一遍"], ["appointment", "預約"]],
                },
            },
            {
                "q": "What has Tom already done?",
                "options": ["Taken the photos for the brochure", "Booked a meeting room", "Reviewed the cost information", "Printed a copy of the brochure"],
                "answer": 2,
                "explain": {
                    "point": "細節題：兩句接起來看，並分清誰做了什麼",
                    "why": "女方說 Tom went over 封底，男方確認那頁是 all the prices → 改述成 reviewed the cost information。",
                    "evidence": [3, 4],
                    "wrong": ["同字陷阱：photos 是他們還要檢查的部分", "張冠李戴：要訂會議室的是男方", None, "張冠李戴：要帶印好稿子的是女方"],
                    "vocab": [["go over", "仔細看過、檢查"], ["back page", "封底"]],
                },
            },
            {
                "q": "What does the man say he will do?",
                "options": ["Reserve a room for their meeting", "Call the print shop", "Bring a printed copy", "Check the prices again"],
                "answer": 0,
                "explain": {
                    "point": "細節題：聽男方說 I'll… 的那一句",
                    "why": "男方說 I'll book a meeting room for one o'clock → book 改述成 reserve a room for their meeting。",
                    "evidence": [6],
                    "wrong": [None, "同字陷阱：print shop 只在開頭提到期限", "張冠李戴：要帶印好稿子的是女方", "價格頁 Tom 看過了，他們決定跳過"],
                    "vocab": [["book", "預訂"], ["heading", "標題"]],
                },
            },
        ],
    },
    {
        "id": "l-conv-04", "type": "listen", "format": "conv", "unit": "conv-next", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-04", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Hi, is this the IT help desk? My laptop keeps shutting down after about twenty minutes.",
                 "say": "Hi, is this the I T help desk? My laptop keeps shutting down after about twenty minutes."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "That sounds like the battery. Is it one of the models the company handed out last year, or an older one?"},
                {"file": "03.mp3", "who": "W", "voice": "af_bella", "text": "An older one. I've had it for four years. We were promised new laptops this spring, but I'm not holding my breath."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Well, a new battery should fix the problem for now. We keep spares here, but I'll need the model number to find the right one."},
                {"file": "05.mp3", "who": "W", "voice": "af_bella", "text": "Where would I find that?"},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "On a silver sticker on the bottom. Read it out to me, and I'll bring a battery up to your desk this afternoon.", "say": "On a silver sticker on the bottom. Reed it out to me, and I'll bring a battery up to your desk this afternoon."},
                {"file": "07.mp3", "who": "W", "voice": "af_bella", "text": "All right, just a second. I'll turn it over."},
            ],
        },
        "transcriptZh": [
            "你好，請問是 IT 服務台嗎？我的筆電用大概二十分鐘就一直自動關機。",
            "聽起來是電池的問題。是公司去年發的那幾款，還是比較舊的？",
            "比較舊的，我已經用了四年。公司答應過今年春天要換新筆電，但我不抱什麼期望。",
            "那先換一顆新電池應該就能解決。我們這裡有備品，但我需要型號才能找到對的那一顆。",
            "型號要去哪裡找？",
            "在底部的一張銀色貼紙上。你念給我聽，我今天下午就把電池送到你的座位。",
            "好，等我一下，我把它翻過來。",
        ],
        "questions": [
            {
                "q": "What does the woman mean when she says, \"I'm not holding my breath\"?",
                "options": ["She is not feeling well", "She doubts the new laptops will arrive as promised", "She has been on hold for a long time", "She would rather keep her old laptop"],
                "answer": 1,
                "explain": {
                    "point": "引句題：用前後文判斷慣用語的意思",
                    "why": "not holding my breath 指「不抱期望」；接在 promised new laptops this spring 後面 → 她不信新筆電會照承諾送來。",
                    "evidence": [2],
                    "wrong": ["字面陷阱：不是真的憋氣或身體不舒服", None, "同字陷阱：hold 出現過，但她沒說電話等很久", "她只說用了四年，沒說想留著舊的"],
                    "vocab": [["not hold one's breath", "不抱期望"], ["promise", "承諾、答應"]],
                },
            },
            {
                "q": "What does the man offer to do this afternoon?",
                "options": ["Deliver a part to her workspace", "Lend her a newer laptop", "Order a battery from a supplier", "Update her software"],
                "answer": 0,
                "explain": {
                    "point": "細節題：找男方說下午能做的事",
                    "why": "男方說 I'll bring a battery up to your desk → 改述成 deliver a part to her workspace。",
                    "evidence": [5],
                    "wrong": [None, "聯想陷阱：新筆電是春天的事，他沒說要借", "同字陷阱：battery 出現過，但備品就在這裡", "沒有人提到更新軟體"],
                    "vocab": [["spare", "備品"], ["for now", "暫時、眼下先"]],
                },
            },
            {
                "q": "What will the woman most likely do next?",
                "options": ["Take her laptop to the help desk", "Wait for a new laptop", "Replace the battery herself", "Check the underside of her laptop"],
                "answer": 3,
                "explain": {
                    "point": "下一步題：答案常在最後一兩句",
                    "why": "男方說型號在 on the bottom，女方說 I'll turn it over → 改述成 check the underside of her laptop。",
                    "evidence": [5, 6],
                    "wrong": ["方向相反：是男方要把電池送上樓", "聯想陷阱：新筆電是春天的事，不是接下來", "同字陷阱：電池下午才由男方送來，她現在換不了", None],
                    "vocab": [["model number", "型號"], ["turn over", "翻過來"], ["underside", "底面"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ talk (Part 4)
    {
        "id": "l-talk-01", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 2,
        "source": "hand", "reviewed": False, "v": 2, "accent": "uk",
        "audio": {
            "dir": "audio/l-talk-01", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_george", "text": "Good morning, everyone. This is building management with an update about the elevators on the east side."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "Starting on Monday, a contractor will be replacing those elevators, and the work should take about two weeks."},
                {"file": "03.mp3", "who": "M", "voice": "bm_george", "text": "While the work is going on, please use the elevators by the main entrance, or take the stairs."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Those elevators will be very busy between 8:30 and 9:00, so if you can, try to come in a little earlier.",
                 "say": "Those elevators will be very busy between eight thirty and nine, so if you can, try to come in a little earlier."},
                {"file": "05.mp3", "who": "M", "voice": "bm_george", "text": "If you work on the east side and can't manage the stairs, the front desk can give you a pass for the freight elevator at the back."},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "Maps of the temporary routes will also be posted beside each staircase. Thank you for your patience."},
            ],
        },
        "transcriptZh": [
            "大家早安。這是大樓管理處的通知，關於東側的電梯。",
            "從星期一開始，承包商會更換那幾部電梯，工程大約需要兩個星期。",
            "施工期間，請搭乘大門旁邊的電梯，或是走樓梯。",
            "那幾部電梯在八點半到九點之間會非常擁擠，所以可以的話，請盡量早一點到。",
            "如果您在東側上班、走樓梯有困難，可以到櫃台領取後方貨梯的通行證。",
            "每座樓梯旁邊也會張貼臨時動線的地圖。謝謝大家耐心配合。",
        ],
        "questions": [
            {
                "q": "What is the announcement mainly about?",
                "options": ["The opening of a new entrance", "A change in office hours", "The installation of new elevators", "A fire safety drill"],
                "answer": 2,
                "explain": {
                    "point": "主旨題：答案通常在開頭",
                    "why": "承包商要 replace 東側的 elevators → 改述成 installation of new elevators：換掉舊的＝裝新的。",
                    "evidence": [0, 1],
                    "wrong": ["同字陷阱：main entrance 本來就有，不是新開", "只建議早點到，上班時間沒變", None, "聯想陷阱：走樓梯是施工期間的替代方式，不是演習"],
                    "vocab": [["replace", "更換、替換"], ["contractor", "承包商"]],
                },
            },
            {
                "q": "Why does the speaker ask listeners to come in earlier?",
                "options": ["The building will close early", "The remaining elevators will be crowded", "The main entrance will be closed", "The front desk will give out passes only in the morning"],
                "answer": 1,
                "explain": {
                    "point": "原因題：so 前面是理由；those elevators 要往前找",
                    "why": "those elevators 指前一句大門旁的電梯，very busy 改述成 crowded → 還能搭的電梯會很擠。",
                    "evidence": [2, 3],
                    "wrong": ["聯想陷阱：earlier 是請大家早到，不是大樓早關", None, "同字陷阱：大門旁的電梯照常使用", "櫃台發通行證是另一件事，沒說只在早上"],
                    "vocab": [["remaining", "剩下的、其餘的"], ["busy", "（地方）擁擠、人多"]],
                },
            },
            {
                "q": "What can some listeners get from the front desk?",
                "options": ["A map of alternative routes", "A parking permit", "A revised work schedule", "Access to a service elevator"],
                "answer": 3,
                "explain": {
                    "point": "細節題：注意限定對象，並聽出強改述",
                    "why": "櫃台可給 a pass for the freight elevator → 改述成 access to a service elevator（freight elevator＝貨梯）。",
                    "evidence": [4],
                    "wrong": ["地圖是貼在樓梯旁，不是去櫃台拿", "聯想陷阱：pass 是貨梯通行證，不是停車證", "只建議早點到，沒有新的時間表", None],
                    "vocab": [["freight elevator", "貨梯＝service elevator"], ["front desk", "櫃台、服務台"]],
                },
            },
        ],
    },
    {
        "id": "l-talk-02", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-02", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Hi, this is Nora Blake from the Riverside Business Forum, calling for Mr. Wei.",
                 "say": "Hi, this is Nora Blake from the Riverside Business Forum, calling for Mister Way."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "I'm confirming your talk on Thursday, May 8th, at 2 p.m. in Room 4B.",
                 "say": "I'm confirming your talk on Thursday, May eighth, at two P M in Room four B."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "Please note that it will now run 40 minutes instead of 30. Another speaker had to cancel, so we've given you part of that time.",
                 "say": "Please note that it will now run forty minutes instead of thirty. Another speaker had to cancel, so we've given you part of that time."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Could you email me your slides by Monday? Our technician will load them onto the laptop in the room before you arrive."},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "Also, the garage next to the venue fills up early on forum days."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "If you'd like a reserved space, just let me know by Wednesday and I'll send you a pass. See you next week!"},
            ],
        },
        "transcriptZh": [
            "嗨，我是 Riverside 商業論壇的 Nora Blake，要找 Wei 先生。",
            "跟您確認，您的演講是在 5 月 8 日星期四下午兩點，地點在 4B 會議室。",
            "請留意，演講時間會從 30 分鐘改成 40 分鐘。另一位講者必須取消，所以我們把那段時間分了一部分給您。",
            "可以請您在星期一前把投影片寄給我嗎？我們的技術人員會在您到之前先放進會議室的筆電。",
            "還有，論壇那幾天，會場隔壁的停車場很早就會停滿。",
            "如果您需要保留車位，星期三前跟我說一聲，我會把停車證寄給您。下週見！",
        ],
        "questions": [
            {
                "q": "Who most likely is Mr. Wei?",
                "options": ["A guest speaker", "An event organizer", "A technician", "A parking attendant"],
                "answer": 0,
                "explain": {
                    "point": "推論題：從 your talk 推聽者的身分",
                    "why": "說 I'm confirming your talk → Mr. Wei 是要來演講的人，改述成 a guest speaker。",
                    "evidence": [1],
                    "wrong": [None, "張冠李戴：論壇主辦方的人是打電話的 Nora", "同字陷阱：technician 是論壇負責放投影片的人", "聯想陷阱：停車場只是附帶提到"],
                    "vocab": [["confirm", "確認"], ["forum", "論壇"]],
                },
            },
            {
                "q": "What change does the speaker mention?",
                "options": ["The talk has moved to Monday", "The talk will be held in a different room", "Mr. Wei will share his session with another speaker", "Mr. Wei will have more time to speak"],
                "answer": 3,
                "explain": {
                    "point": "細節題：聽「改變」的訊號 instead of",
                    "why": "說 40 minutes instead of 30 → 改述成 he will have more time to speak。",
                    "evidence": [2],
                    "wrong": ["同字陷阱：Monday 是交投影片的期限", "4B 會議室只是確認，沒有更換", "曲解：另一位講者是取消，時間分給了他", None],
                    "vocab": [["instead of", "取代、而不是"], ["slides", "投影片"], ["technician", "技術人員"]],
                },
            },
            {
                "q": "Why does the speaker mention the garage next to the venue?",
                "options": ["To explain why the talk was extended", "To give directions to Room 4B", "To suggest that Mr. Wei reserve parking in advance", "To ask Mr. Wei to pick up a parking pass"],
                "answer": 2,
                "explain": {
                    "point": "意圖題：看這句話接著引出什麼",
                    "why": "先說停車場 fills up early，接著說要車位就 let me know by Wednesday → 用意是建議他提早預約車位。",
                    "evidence": [4, 5],
                    "wrong": ["演講延長是前面另一件事，跟停車場無關", "沒有提到怎麼走到 4B 會議室", None, "停車證是她寄過去，不用自己去拿"],
                    "vocab": [["venue", "會場"], ["fill up", "客滿、停滿"], ["reserved", "保留的、預約的"]],
                },
            },
        ],
    },
]
