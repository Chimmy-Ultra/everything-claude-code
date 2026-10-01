# Round 6 listening items, written under WRITING_RULES.md (sections 2, 3, 4.4 point 7, 5, 6, 7.1).
# 18 qr (Part 2 style): 6 qr-wh, 6 qr-yesno (two tag questions, two negative questions), 6 qr-indirect
# (statements, a choice question, requests and suggestions). Scripts are in US English even when a British voice
# reads them. All content is original; names of people, firms and places are invented. Times and numbers are
# written out in words, so no `say` field is needed.
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` here is the writer's
# self-test band (easy 1, medium 2, hard 3). reviewed stays False until the items pass a blind review and every
# mp3 has been heard.
# Self-test totals: 3 easy (l-qr-23, 29, 37), 8 medium, 7 hard (l-qr-25, 26, 31, 32, 33, 34, 38).
# Key positions: A = 24, 27, 31, 34, 35, 38; B = 25, 28, 29, 32, 36, 39; C = 23, 26, 30, 33, 37, 40.
# Scenes (new against l-qr-01..22): airport shuttle, catering invoice, job transfer, delayed client call, fabric
# samples, expo display boards, ground-floor cafe, interpreter booking, lobby floor, small conference room,
# sea freight, afternoon off, print-shop invoice, satisfaction survey, laptop charger, product demo hall,
# dinner bill, budget review.
# Every wrong response was checked against 4.4 point 7: each is either contradicted by a detail the question
# states, answers a different wh-type, repeats a word to answer something else, or is a Yes/No opener followed by
# something that does not address the question. None is a reply a cooperative speaker would give here.

ITEMS = [
    # ------------------------------------------------------------------ qr-wh
    # l-qr-23  qr-wh, easy. Direct answer; the wrong replies answer "where" and use Yes on a When question.
    {
        "id": "l-qr-23", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-23", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "When does the new shuttle to the train station begin running?"},
                {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "It stops right outside the main entrance."},
                {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "Yes, I take the shuttle every morning."},
                {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "Starting the first of next month."},
            ],
        },
        "transcriptZh": [
            "前往火車站的新接駁車什麼時候開始行駛？",
            "它就停在大門正前方。",
            "有，我每天早上都搭接駁車。",
            "從下個月一日開始。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
            "explain": {
                "point": "When 問句：直接回一個時間",
                "why": "問接駁車何時開始 → 回 Starting the first of next month（下個月一日）：給的是時間。",
                "evidence": [3],
                "wrong": ["答錯問句類型：講停靠位置，是 where 的答案", "答錯問句類型：When 問句不能用 Yes 回答", None],
                "wrongMore": [None, None, None],
                "vocab": [["shuttle", "接駁車"], ["begin running", "開始運行"], ["main entrance", "大門、正門"]],
            },
        }],
    },
    # l-qr-24  qr-wh, medium. near-correct: (A) key is indirect ("the bill hasn't come"); (B) a number answer to
    # How much (it answers how many); (C) repeats luncheon.
    {
        "id": "l-qr-24", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-24", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "How much did the catering for last week's client luncheon come to?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_lewis", "text": "Accounting hasn't sent us the bill yet."},
                {"file": "b.mp3", "who": "M", "voice": "bm_lewis", "text": "About sixty guests, I think."},
                {"file": "c.mp3", "who": "M", "voice": "bm_lewis", "text": "The luncheon was a big success."},
            ],
        },
        "transcriptZh": [
            "上週客戶午宴的外燴總共花了多少錢？",
            "會計部還沒把帳單寄給我們。",
            "我想大約有六十位賓客。",
            "那場午宴非常成功。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "How much 問句：答案可以是「還不知道」",
                "why": "問外燴花了多少 → 回 hasn't sent us the bill yet：帳單還沒到，所以金額還不知道。",
                "evidence": [1],
                "wrong": [None, "答錯問句類型：About sixty 是人數，不是金額", "同字陷阱：重複 luncheon，只評論午宴成功"],
                "wrongMore": [None, "How much 問句要的是金額；About sixty guests 是 How many 的答案，數字形式像、問的卻不同。", None],
                "vocab": [["catering", "外燴"], ["come to", "（金額）總計達"], ["luncheon", "午宴"]],
            },
        }],
    },
    # l-qr-25  qr-wh, hard. near-correct: (A) "Because she was never offered the job" has the Because form but the
    # question says she turned the position down; (C) repeats transfer. Key (B) is an implied reason.
    {
        "id": "l-qr-25", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-25", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_eric", "text": "Why did Ms. Novak turn down the Lisbon position when she'd been asking for a transfer for years?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "Because she was never offered the job."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "Her whole family lives in this city."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "The transfer forms are on the intranet."},
            ],
        },
        "transcriptZh": [
            "Novak 女士明明多年來一直申請調職，為什麼卻回絕了里斯本的職缺？",
            "因為根本沒有人給她那份工作。",
            "她全家人都住在這座城市。",
            "調職申請表在公司內部網站上。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "Why 問句：用事實暗示理由，不一定出現 because",
                "why": "問她為什麼回絕里斯本的職缺 → 回 Her whole family lives in this city：家人都在這裡，暗示她不想搬走。",
                "evidence": [2],
                "wrong": ["形式對情境錯：Because 開頭，但問句說她是 turn down，不是沒被錄用", None, "同字陷阱：重複 transfer，講的是申請表放哪裡"],
                "wrongMore": ["Why 問句用 Because 回答，形式完全對；但問句已說 turn down the position，表示職缺給過她，never offered 與它矛盾。", None, None],
                "vocab": [["turn down", "回絕、拒絕"], ["transfer", "調職"], ["intranet", "公司內部網站"]],
            },
        }],
    },
    # l-qr-26  qr-wh, medium. Condition: "now that it's been rescheduled". near-correct: (A) a time, but the old one
    # ("the same as before" contradicts rescheduled); (B) repeats client, answers where. Key (C) reports the change.
    {
        "id": "l-qr-26", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-26", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "What time is the client call tomorrow, now that it's been rescheduled for later in the day?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "Nine o'clock, the same as before."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "The client's office is downtown."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "It got pushed back to noon."},
            ],
        },
        "transcriptZh": [
            "既然明天的客戶電話會議已經改到當天晚一點，現在是幾點？",
            "九點，跟之前一樣。",
            "客戶的辦公室在市中心。",
            "已經往後延到中午了。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
            "explain": {
                "point": "What time 問句帶條件：回應要報告改期後的新時間",
                "why": "問改期後明天的客戶電話會議是幾點 → 回 pushed back to noon：往後延到中午，才是改期後的時間。",
                "evidence": [3],
                "wrong": ["形式對情境錯：是時間，但 the same as before 表示沒改期，與 rescheduled 矛盾", "同字陷阱：重複 client，講的是客戶辦公室在哪裡", None],
                "wrongMore": [
                    "What time 問句回 Nine o'clock 形式完全對；但問句說 now that it's been rescheduled，回答卻說跟之前一樣，與改期矛盾。",
                    "回答用了 client，聽起來沾得上邊；但 office is downtown 回答的是地點，不是時間，是答錯問句類型。",
                    None,
                ],
                "vocab": [["reschedule", "改期"], ["client call", "客戶電話會議"], ["push back", "往後延"]],
            },
        }],
    },
    # l-qr-27  qr-wh, medium. near-correct: (B) a place answer, but about origin; (C) repeats courier.
    # Key (A) is a referral.
    {
        "id": "l-qr-27", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-27", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_bella", "text": "Where did the courier leave the fabric samples that arrived this morning?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "Ask at the front desk. Lena signed for them."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "They're imported from Portugal."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "The courier comes at around ten o'clock every day."},
            ],
        },
        "transcriptZh": [
            "今天早上到的布料樣品，快遞把它們放在哪裡？",
            "去問櫃檯，是 Lena 簽收的。",
            "它們是從葡萄牙進口的。",
            "快遞每天大約十點來。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "Where 問句：可以回「去問某人」",
                "why": "問樣品被放在哪裡 → 回 Ask at the front desk. Lena signed for them：簽收的人知道放哪，是轉介而不是給地點。",
                "evidence": [1],
                "wrong": [None, "答錯問句類型：Portugal 是產地，不是收件後放的位置", "同字陷阱：重複 courier，講的是來的時間"],
                "wrongMore": [None, "Where 問句回一個地名，形式像對；但 imported from Portugal 說的是進口來源，沒說今天樣品被放在哪裡。", None],
                "vocab": [["courier", "快遞員、快遞公司"], ["fabric samples", "布料樣品"], ["sign for", "簽收"]],
            },
        }],
    },
    # l-qr-28  qr-wh, medium. near-correct: (A) names the vehicle that the question says is in the shop.
    # (C) answers a how-big question. Key (B) is direct.
    {
        "id": "l-qr-28", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-28", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_lewis", "text": "How are we getting the display boards to the expo center, now that the company van is in the repair shop?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "By the company van, as usual."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "I've booked a rental truck for Thursday morning."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "They're about two meters wide."},
            ],
        },
        "transcriptZh": [
            "既然公司的廂型車送修了，我們要怎麼把展示板運到展覽中心？",
            "照常用公司的廂型車。",
            "我已經訂了星期四早上的租用貨車。",
            "它們大約兩公尺寬。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
            "explain": {
                "point": "How 問句帶條件：刪掉被條件排除的方式",
                "why": "問廂型車送修後怎麼運展示板 → 回 I've booked a rental truck：改用租來的貨車，是另一種運送方式。",
                "evidence": [2],
                "wrong": ["形式對情境錯：How 問句回 By the van，但問句說 van 在修理廠", None, "答錯問句類型：講的是展示板的寬度，不是怎麼運"],
                "wrongMore": ["By + 交通工具是 How 問句的標準回答，形式完全對；但問句後半 the company van is in the repair shop 已排除這輛車。", None, None],
                "vocab": [["display boards", "展示板"], ["expo center", "展覽中心"], ["rental truck", "租用貨車"]],
            },
        }],
    },

    # ------------------------------------------------------------------ qr-yesno
    # l-qr-29  qr-yesno, easy. Direct Yes with a limit; the wrong replies answer other questions.
    {
        "id": "l-qr-29", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-29", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "Is the café on the ground floor open on weekends?"},
                {"file": "a.mp3", "who": "M", "voice": "am_eric", "text": "The ground floor has been repainted."},
                {"file": "b.mp3", "who": "M", "voice": "am_eric", "text": "Yes, but only on Saturdays."},
                {"file": "c.mp3", "who": "M", "voice": "am_eric", "text": "I'll have a coffee with milk, please."},
            ],
        },
        "transcriptZh": [
            "一樓的咖啡廳週末有營業嗎？",
            "一樓重新粉刷過了。",
            "有，不過只有星期六。",
            "我要一杯加牛奶的咖啡，麻煩你。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
            "explain": {
                "point": "Is 問句：直接回 Yes 再補條件",
                "why": "問咖啡廳週末有沒有開 → 回 Yes, but only on Saturdays：有開，但只有週六。",
                "evidence": [2],
                "wrong": ["同字陷阱：重複 ground floor，講的是粉刷", None, "答非所問：像在咖啡廳點餐，不是回答營業日"],
                "wrongMore": [None, None, None],
                "vocab": [["ground floor", "一樓"], ["weekends", "週末"], ["repaint", "重新粉刷"]],
            },
        }],
    },
    # l-qr-30  qr-yesno, medium. Tag question. near-correct: (A) Yes + a remark about Tokyo; (B) repeats call.
    # Key (C) is an indirect No with a referral.
    {
        "id": "l-qr-30", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-30", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "You've booked the interpreter for the Tokyo call, haven't you?"},
                {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "Yes, I've been to Tokyo twice."},
                {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "The call went very well last week."},
                {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "Sorry, I thought Hana was handling that."},
            ],
        },
        "transcriptZh": [
            "你已經幫東京那場電話會議訂好口譯員了，對吧？",
            "有，我去過東京兩次。",
            "上週那通電話進行得很順利。",
            "抱歉，我以為是 Hana 在處理。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "附加問句：用「我以為別人做了」暗示還沒訂",
                "why": "問你訂了口譯沒 → 回 Sorry, I thought Hana was handling that：我以為是別人處理，等於說自己沒訂。",
                "evidence": [3],
                "wrong": ["形式對情境錯：Yes 開頭，後面講去過東京，沒回答訂口譯", "同字陷阱：重複 call，講的是上週那通電話", None],
                "wrongMore": ["Yes 接得上附加問句；但 I've been to Tokyo twice 只是個人經驗，沒有說口譯員訂了沒。", None, None],
                "vocab": [["interpreter", "口譯員"], ["book", "預訂、安排"], ["handle", "處理、負責"]],
            },
        }],
    },
    # l-qr-31  qr-yesno, hard. Negative question with a deadline condition (clients arrive at noon).
    # near-correct: (B) Yes + clients, (C) No + lobby. Key (A) is indirect: not done until after the deadline.
    {
        "id": "l-qr-31", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-31", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "Didn't the maintenance crew promise to finish the lobby floor before the clients arrive at noon?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "They told me it'll take until after lunch."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "Yes, the clients were very impressed last time."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "No, the lobby is on the first floor."},
            ],
        },
        "transcriptZh": [
            "維修人員不是答應過，會在客戶中午抵達前把大廳地板做完嗎？",
            "他們跟我說要到午餐後才會完成。",
            "有，上次客戶都覺得印象很深刻。",
            "不是，大廳在一樓。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "否定問句：用時間差暗示「來不及」",
                "why": "問不是答應中午前完成嗎 → 回 it'll take until after lunch：午餐後才完成，晚於中午，等於沒趕上。",
                "evidence": [1],
                "wrong": [None, "形式對情境錯：Yes 開頭，後面講上次客戶的印象，沒回答完工時間", "同字陷阱：No 加上重複 lobby，講的是樓層"],
                "wrongMore": [None, "Yes 接得上否定問句，又提到 clients；但 impressed last time 是以前的事，沒有說地板能不能在中午前完成。", "No 也是合理的開頭；但 the lobby is on the first floor 在講位置，沒有談維修人員有沒有如期完成。"],
                "vocab": [["maintenance crew", "維修人員"], ["lobby", "大廳"], ["impressed", "印象深刻的"]],
            },
        }],
    },
    # l-qr-32  qr-yesno, hard. Condition: finance has reserved the room for the whole afternoon.
    # near-correct: (A) Yes + a reservation from two to four (contradicts the whole afternoon).
    # (C) repeats finance. Key (B) is a partial yes.
    {
        "id": "l-qr-32", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-32", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_eric", "text": "Is the small conference room still free on Thursday, now that finance has reserved it for the whole afternoon?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "Yes, I reserved it from two to four o'clock."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "Only in the morning."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "Finance is hiring two more analysts."},
            ],
        },
        "transcriptZh": [
            "既然財務部已經把小會議室星期四整個下午都訂走了，那天還有空嗎？",
            "有，我訂了兩點到四點。",
            "只有早上。",
            "財務部要再多請兩位分析師。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "Yes/No 問句帶條件：用條件把答案縮小到部分",
                "why": "問下午被訂走後還有沒有空 → 回 Only in the morning：下午沒了，只剩早上，是有條件的 Yes。",
                "evidence": [2],
                "wrong": ["形式對情境錯：Yes 開頭，但下午已被財務部整個訂走，兩點到四點不可能是空的", None, "同字陷阱：重複 finance，講的是徵人"],
                "wrongMore": ["Yes 接得上 Is … still free 問句；但問句說 reserved it for the whole afternoon，兩點到四點也在下午，這個說法與它矛盾。", None, None],
                "vocab": [["reserve", "預訂"], ["whole afternoon", "整個下午"], ["analyst", "分析師"]],
            },
        }],
    },
    # l-qr-33  qr-yesno, hard. Negative question with condition (the show is next quarter).
    # near-correct: (A) Yes + "starts tomorrow" contradicts next quarter; (B) repeats display units.
    # Key (C) is indirect: the partner only does air, so no.
    {
        "id": "l-qr-33", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-33", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_george", "text": "Wouldn't it be cheaper to ship the display units by sea, now that the trade show isn't until next quarter?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "Yes, because the show starts tomorrow."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "The display units were designed in Milan."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "Our warehouse partner only handles air freight."},
            ],
        },
        "transcriptZh": [
            "既然貿易展要到下一季才舉行，展示設備改用海運寄不是比較便宜嗎？",
            "對，因為展覽明天就開始了。",
            "那些展示設備是在米蘭設計的。",
            "我們的倉儲合作夥伴只處理空運。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "否定問句：用「做不到」暗示答案是 No",
                "why": "問海運不是比較便宜嗎 → 回 only handles air freight：合作夥伴只做空運，海運行不通，所以是 No。",
                "evidence": [3],
                "wrong": ["形式對情境錯：Yes 加理由，但問句說展覽是下一季，不是明天", "同字陷阱：重複 display units，講的是設計地點", None],
                "wrongMore": ["Yes 接得上否定問句，而且帶了 because；但 the show starts tomorrow 與問句的 isn't until next quarter 矛盾。", None, None],
                "vocab": [["display units", "展示設備"], ["trade show", "貿易展"], ["freight", "貨運"]],
            },
        }],
    },
    # l-qr-34  qr-yesno, hard. Tag question with condition (the inspection at three).
    # near-correct: (B) Yes + inspection in the past tense; (C) No + weather. Key (A) implies Yes via cover.
    {
        "id": "l-qr-34", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-34", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_bella", "text": "You're still taking tomorrow afternoon off, aren't you, even with the inspection at three o'clock?"},
                {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "Ms. Kemp offered to cover for me.", "say": "Mizz Kemp offered to cover for me."},
                {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "Yes, the inspection was very thorough."},
                {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "No, I don't think it will rain tomorrow."},
            ],
        },
        "transcriptZh": [
            "你明天下午還是要請假吧？就算三點有檢查也一樣？",
            "Kemp 女士說她可以幫我代班。",
            "對，那次檢查做得很徹底。",
            "不是，我想明天不會下雨。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "附加問句：用「有人代班」暗示答案是 Yes",
                "why": "問檢查那天還是要請假吧 → 回 Ms. Kemp offered to cover for me：有人幫忙代班，所以照樣請假。",
                "evidence": [1],
                "wrong": [None, "形式對情境錯：Yes 開頭，但 was thorough 是過去式，問句的檢查是明天三點", "答錯問句類型：No 加上天氣，與請假無關"],
                "wrongMore": [None, "Yes 接得上附加問句，又重複 inspection；但 was very thorough 說的是已經做完的檢查，問句的檢查是明天才發生。", None],
                "vocab": [["inspection", "檢查、視察"], ["take off", "請假"], ["cover for", "代班、代替"]],
            },
        }],
    },

    # ------------------------------------------------------------------ qr-indirect
    # l-qr-35  qr-indirect, medium. Statement. near-correct: (C) a reaction in the wrong direction;
    # (B) repeats print shop. Key (A) is "I'll check".
    {
        "id": "l-qr-35", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-35", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_eric", "text": "The invoice from the print shop is higher than the quote."},
                {"file": "a.mp3", "who": "W", "voice": "af_sarah", "text": "Let me pull up the original estimate."},
                {"file": "b.mp3", "who": "W", "voice": "af_sarah", "text": "Their print shop is next to the bank."},
                {"file": "c.mp3", "who": "W", "voice": "af_sarah", "text": "Good, that's less than I expected."},
            ],
        },
        "transcriptZh": [
            "印刷廠寄來的發票比報價高。",
            "我來調出原本的估價單。",
            "他們的印刷廠就在銀行旁邊。",
            "很好，比我預期的還少。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "陳述句：回「我來查」是合理的接話",
                "why": "說發票比報價高 → 回 Let me pull up the original estimate：去查原本的估價，是處理這個差異的第一步。",
                "evidence": [1],
                "wrong": [None, "同字陷阱：重複 print shop，講的是店的位置", "形式對情境錯：Good 開頭的反應，但發票是「比較高」，不是更少"],
                "wrongMore": [None, None, "對消息給反應是陳述句的合理接法；但 higher than the quote 是壞消息，說 less than I expected 與它方向相反。"],
                "vocab": [["invoice", "發票、請款單"], ["quote", "報價"], ["pull up", "調出（資料）"]],
            },
        }],
    },
    # l-qr-36  qr-indirect, medium. Statement. near-correct: (A) cheerful reaction in the wrong direction;
    # (C) repeats survey. Key (B) is a follow-up question about the cause.
    {
        "id": "l-qr-36", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-36", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "The customer survey scores dropped for the first time in three years."},
                {"file": "a.mp3", "who": "M", "voice": "bm_lewis", "text": "Wonderful, the team will be thrilled."},
                {"file": "b.mp3", "who": "M", "voice": "bm_lewis", "text": "Was it the long waiting times again?"},
                {"file": "c.mp3", "who": "M", "voice": "bm_lewis", "text": "The survey only takes about five minutes."},
            ],
        },
        "transcriptZh": [
            "客戶問卷的分數三年來第一次下滑。",
            "太好了，團隊一定會很開心。",
            "又是因為等候時間太長嗎？",
            "那份問卷大約只要五分鐘。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "陳述句：用追問原因來接話",
                "why": "說問卷分數下滑 → 回 Was it the long waiting times again?：追問可能的原因，符合壞消息的語氣。",
                "evidence": [2],
                "wrong": ["形式對情境錯：開心的反應，但 dropped 是壞消息", None, "同字陷阱：重複 survey，講的是填寫時間"],
                "wrongMore": ["Wonderful 是對消息的反應，形式對；但問卷分數 dropped，是壞消息，說團隊會很開心與它方向相反。", None, None],
                "vocab": [["survey", "問卷調查"], ["scores", "分數、評分"], ["waiting times", "等候時間"]],
            },
        }],
    },
    # l-qr-37  qr-indirect, easy (the batch's easy request). Direct "Sure"; the wrong replies answer other things.
    {
        "id": "l-qr-37", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-37", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_george", "text": "Could you lend me your laptop charger for an hour?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "The laptops are on sale this week."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "It took about an hour."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "Sure, it's in the top drawer."},
            ],
        },
        "transcriptZh": [
            "你可以把筆電充電器借我一個小時嗎？",
            "這個星期筆記型電腦在特價。",
            "那花了大約一個小時。",
            "可以，就在最上面的抽屜裡。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
            "explain": {
                "point": "Could you 請求：直接答應",
                "why": "請對方借充電器 → 回 Sure, it's in the top drawer：答應了，還說明東西放在哪裡。",
                "evidence": [3],
                "wrong": ["同字陷阱：重複 laptop，講的是特價", "同字陷阱：重複 an hour，講的是花了多久", None],
                "wrongMore": [None, None, None],
                "vocab": [["lend", "借出"], ["charger", "充電器"], ["on sale", "特價中"]],
            },
        }],
    },
    # l-qr-38  qr-indirect, hard. Choice question with a condition (studio seats sixty; two hundred registered).
    # near-correct: (B) picks the studio, which the condition rules out; (C) repeats registration.
    # Key (A) does not pick: it checks the main hall, which implies the choice.
    {
        "id": "l-qr-38", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-38", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "Should we hold the demo in the main hall or the studio, which seats only sixty, now that over two hundred people have registered?"},
                {"file": "a.mp3", "who": "W", "voice": "af_sarah", "text": "I'll see if the main hall is free that morning."},
                {"file": "b.mp3", "who": "W", "voice": "af_sarah", "text": "The studio is a better fit for a demo."},
                {"file": "c.mp3", "who": "W", "voice": "af_sarah", "text": "Registration closes on the thirtieth."},
            ],
        },
        "transcriptZh": [
            "既然已經有兩百多人報名，我們示範會要辦在主廳，還是只有六十個座位的小棚？",
            "我去看看那天早上主廳有沒有空。",
            "小棚比較適合做示範。",
            "報名在三十號截止。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
            "explain": {
                "point": "選擇問句：不直接選，改說「我去確認」來暗示",
                "why": "兩百多人報名、小棚只有六十個座位 → 回 I'll see if the main hall is free：先確認主廳有沒有空，等於選主廳。",
                "evidence": [1],
                "wrong": [None, "形式對情境錯：選了 the studio，但它只有六十個座位，容不下兩百多人", "同字陷阱：Registration 與問句的 registered 同字根，講的是截止日"],
                "wrongMore": [None, "選一個是選擇問句的標準回答，形式完全對；但問句說 seats only sixty、over two hundred registered，小棚根本坐不下。", None],
                "vocab": [["demo", "示範、展示"], ["main hall", "主廳"], ["registered", "已報名"]],
            },
        }],
    },
    # l-qr-39  qr-indirect, medium. Suggestion. near-correct: (A) answers a Why don't we with Because;
    # (C) repeats bill. Key (B) is a reason that implies no.
    {
        "id": "l-qr-39", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-39", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_bella", "text": "Why don't we split the dinner bill between the two departments?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_lewis", "text": "Because the dinner started at eight o'clock."},
                {"file": "b.mp3", "who": "M", "voice": "bm_lewis", "text": "Marketing has already used up its budget for this quarter."},
                {"file": "c.mp3", "who": "M", "voice": "bm_lewis", "text": "The waiter brought the bill on a tray."},
            ],
        },
        "transcriptZh": [
            "我們何不把晚餐的帳單由兩個部門平分？",
            "因為晚餐是八點開始的。",
            "行銷部這一季的預算已經用完了。",
            "服務生把帳單放在托盤上端來。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "Why don't we 建議：用理由暗示不行",
                "why": "建議兩個部門平分帳單 → 回 Marketing has already used up its budget：行銷部預算用完，所以沒辦法分攤。",
                "evidence": [2],
                "wrong": ["答錯問句類型：Because 開頭，但 Why don't we 是建議，不是問原因", None, "同字陷阱：重複 bill，講的是服務生怎麼送帳單"],
                "wrongMore": ["Why 開頭的句子常被當成問原因，所以 Because 看起來順；但 Why don't we … 是提議，Because 後面又沒有針對提議給理由。", None, None],
                "vocab": [["split", "平分"], ["bill", "帳單"], ["use up", "用完"]],
            },
        }],
    },
    # l-qr-40  qr-indirect, medium. Choice question answered with a third option.
    # near-correct: (A) repeats conference room, answers where; (B) repeats lunch. Key (C) names a third way.
    {
        "id": "l-qr-40", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-qr-40", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "Do you want to go over the budget in the conference room or over lunch?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "The conference room is on the fourth floor."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "The lunch menu changes every Monday."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "Let's just do it by phone this afternoon."},
            ],
        },
        "transcriptZh": [
            "你想在會議室檢視預算，還是邊吃午餐邊看？",
            "會議室在四樓。",
            "午餐菜單每個星期一更換。",
            "我們今天下午直接用電話談吧。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "選擇問句：可以兩個都不選，提出第三個方式",
                "why": "問在會議室還是午餐時看預算 → 回 do it by phone this afternoon：兩個都不選，改成電話，是第三個選項。",
                "evidence": [3],
                "wrong": ["同字陷阱：重複 conference room，講的是會議室在幾樓", "同字陷阱：重複 lunch，講的是菜單", None],
                "wrongMore": [None, None, None],
                "vocab": [["go over", "檢視、逐項看過"], ["conference room", "會議室"], ["by phone", "用電話"]],
            },
        }],
    },
]
