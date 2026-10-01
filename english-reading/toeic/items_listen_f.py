# Round 6 listening items, written under WRITING_RULES.md (sections 2, 3, 5, 6, 7.1).
# 6 talk sets (Part 4 style, one speaker, 3 questions each = 18 questions): l-talk-06 .. l-talk-11.
# Units: 2 talk-topic (06, 09), 2 talk-detail (07, 10), 2 talk-next (08, 11). Each set mixes question types.
# Scripts are in US English even when a British voice reads them. All content is original; names of people,
# firms, places and products are invented.
# Digits in `text` are spoken from `say` (times, prices, counts, route and key numbers are spelled out there).
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` here is the highest
# self-test band in the item (easy 1, medium 2, hard 3).
# reviewed stays False until the items pass a blind review and every mp3 has been heard.
# Scenes (new against l-talk-01..05: east-side elevators, forum-speaker voicemail, store inventory training,
# glassworks tour, hotel banquet voicemail): rail-replacement announcement, radio traffic report, internet
# provider phone menu, self-storage advertisement, customer-service workshop opening, coffee roastery tour.
# Self-test summary: 18 questions = 4 easy (the first question of 06, 09, 10, 11), 6 medium, 8 hard.
# Implied-meaning (quote or purpose) questions: l-talk-06 q2 ("The board hasn't caught up yet."),
# l-talk-09 q3 ("... your garage can finally be a garage again."), l-talk-07 q2 (why Orchard Road is mentioned).
# Graphic questions: l-talk-09 q2 (price table) and l-talk-10 q2 (schedule); the audio never says the answer cell.
# Answer key by position (A=0 ... D=3): 06 A D C | 07 B A D | 08 C B A | 09 D B C | 10 C D A | 11 B C D.

ITEMS = [
    # l-talk-06  talk-topic. Rail-replacement announcement (UK, bm_lewis).
    # q1 topic (easy). q2 quote: "The board hasn't caught up yet." = the display is out of date; the literal
    # reading (screens are broken) is the near-correct option. q3 two-step number: normal time is in line 2,
    # "twice the normal travel time" in line 5 (last third).
    {
        "id": "l-talk-06", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "audio": {
            "dir": "audio/l-talk-06", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_lewis", "text": "Attention, passengers at Carrow Central. Because of a signal failure near Dunhaven, no trains will run on the Harbor Line this evening."},
                {"file": "02.mp3", "who": "M", "voice": "bm_lewis", "text": "Replacement buses are boarding now on the station forecourt, outside the east exit."},
                {"file": "03.mp3", "who": "M", "voice": "bm_lewis", "text": "The train normally reaches Dunhaven in 30 minutes, but the buses will stop at every station along the way.",
                 "say": "The train normally reaches Dunhaven in thirty minutes, but the buses will stop at every station along the way."},
                {"file": "04.mp3", "who": "M", "voice": "bm_lewis", "text": "Some trains still appear on the departure board. The board hasn't caught up yet."},
                {"file": "05.mp3", "who": "M", "voice": "bm_lewis", "text": "Staff in yellow jackets are on the concourse, so please check with them before you go to a platform."},
                {"file": "06.mp3", "who": "M", "voice": "bm_lewis", "text": "Please allow twice the normal travel time for your journey. Your tickets and passes remain valid on the buses."},
                {"file": "07.mp3", "who": "M", "voice": "bm_lewis", "text": "We apologize for the inconvenience, and we will announce when trains are running again."},
            ],
        },
        "transcriptZh": [
            "各位在 Carrow Central 車站的旅客請注意。由於 Dunhaven 附近號誌故障，今晚 Harbor 線沒有列車行駛。",
            "接駁公車現在正在站前廣場上車，就在東出口外面。",
            "火車平常 30 分鐘就到 Dunhaven，但公車沿途每一站都會停。",
            "出發看板上還顯示著一些列車。看板還沒有更新。",
            "穿黃色外套的工作人員在站內大廳，所以前往月台之前請先向他們確認。",
            "請預留平常兩倍的行車時間。您的車票和通行證在公車上仍然有效。",
            "造成不便，我們深感抱歉，列車恢復行駛時我們會廣播通知。",
        ],
        "questions": [
            {
                "q": "What is the announcement mainly about?",
                "options": ["A temporary disruption to train service", "A fare increase on the Harbor Line", "The opening of a new bus station", "A delay affecting a single train"],
                "answer": 0,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "主旨題：開頭兩句就點出主題",
                    "why": "no trains will run 加上 Replacement buses are boarding → 改述成列車服務暫時中斷、改搭公車。",
                    "evidence": [0, 1],
                    "wrong": [None, "沒有提到票價：只說車票仍然有效", "同字陷阱：buses 與 station 出現，但沒有新車站", "形式對情境錯：停駛的是整條線，不是單一班次"],
                    "wrongMore": [
                        None,
                        None,
                        "buses 與 station 確實出現，但 boarding on the station forecourt 是接駁公車的上車處，沒有人說要開新車站。",
                        "delay 看起來接近；但 no trains will run 是整條 Harbor Line 整晚停駛，不是某一班晚到。",
                    ],
                    "vocab": [["signal failure", "號誌故障"], ["replacement bus", "接駁（替代）公車"], ["forecourt", "站前廣場"]],
                },
            },
            {
                "q": "Why does the speaker say, \"The board hasn't caught up yet\"?",
                "options": ["To report that the screens are being repaired", "To promise that trains will be running again soon", "To ask passengers to wait beside the board", "To warn that the displayed information may be out of date"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：hasn't caught up 是說資訊還沒更新",
                    "why": "前一句 Some trains still appear on the departure board，接著 hasn't caught up yet → 畫面是舊的；下一句叫旅客問工作人員。",
                    "evidence": [3, 4],
                    "wrong": ["字面陷阱：把 board 讀成壞掉要修的螢幕", "語境矛盾：廣播只說復駛時會再通知", "語境矛盾：叫旅客先問工作人員，不是在看板旁等", None],
                    "wrongMore": [
                        "hasn't caught up 字面上像是螢幕壞了；但前一句說班次還顯示在螢幕上，意思是畫面沒有跟上實際狀況，不是在維修。",
                        "最後一句只說 we will announce when trains are running again，沒有說很快；這句話也不是在談復駛。",
                        None,
                        None,
                    ],
                    "vocab": [["departure board", "出發班次看板"], ["concourse", "站內大廳"]],
                },
            },
            {
                "q": "How long will the bus trip to Dunhaven most likely take?",
                "options": ["About 30 minutes", "About 45 minutes", "About 1 hour", "About 2 hours"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "兩步推算：平常時間在前，倍數在後",
                    "why": "第三句說火車 normally … in 30 minutes；後面說 allow twice the normal travel time → 30 分鐘的兩倍，約一小時。",
                    "evidence": [2, 5],
                    "wrong": ["同字陷阱：30 minutes 是火車平常的時間", "沒有依據：音檔沒有 45 分鐘", None, "誤用 twice：是平常時間的兩倍，不是兩小時"],
                    "wrongMore": [
                        "30 minutes 確實出現，但那是火車的 normal 時間；公車要 allow twice the normal travel time。",
                        None,
                        None,
                        "twice 是乘在 normal travel time 上，30 分鐘的兩倍是 60 分鐘；選 2 hours 是把 twice 當成 two hours。",
                    ],
                    "vocab": [["normally", "通常、平常"], ["remain valid", "仍然有效"]],
                },
            },
        ],
    },

    # l-talk-07  talk-detail. Radio traffic report (US, am_eric). No easy question in this set.
    # q1 compare the first estimate with the new one (lines 3-4). q2 purpose of mentioning Orchard Road: line 5
    # sounds like a recommendation, line 6 reverses it. q3 advice in the last third; the update at 8:15 is the
    # speaker's own action.
    {
        "id": "l-talk-07", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-07", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_eric", "text": "Good morning, this is Dale Fenner with your 7:40 traffic report. Eastgate Bridge is backed up.",
                 "say": "Good morning, this is Dale Fenner with your seven forty traffic report. Eastgate Bridge is backed up."},
                {"file": "02.mp3", "who": "M", "voice": "am_eric", "text": "A delivery truck broke down in the left lane, so only one lane is open each way."},
                {"file": "03.mp3", "who": "M", "voice": "am_eric", "text": "Crews first said they would clear the truck by 9:00.",
                 "say": "Crews first said they would clear the truck by nine o'clock."},
                {"file": "04.mp3", "who": "M", "voice": "am_eric", "text": "But a tow company arrived early, and they now hope to have the bridge fully open by 8:30.",
                 "say": "But a tow company arrived early, and they now hope to have the bridge fully open by eight thirty."},
                {"file": "05.mp3", "who": "M", "voice": "am_eric", "text": "Many drivers are turning onto Orchard Road to get around the bridge."},
                {"file": "06.mp3", "who": "M", "voice": "am_eric", "text": "But a water main repair there has closed a lane, so it's slow going as well."},
                {"file": "07.mp3", "who": "M", "voice": "am_eric", "text": "Tonight's concert will bring heavy traffic near the stadium after 5:00.",
                 "say": "Tonight's concert will bring heavy traffic near the stadium after five o'clock."},
                {"file": "08.mp3", "who": "M", "voice": "am_eric", "text": "If you can, leave your car at the Lakeside lot and take the Route 12 bus, which runs every 10 minutes.",
                 "say": "If you can, leave your car at the Lakeside lot and take the Route twelve bus, which runs every ten minutes."},
                {"file": "09.mp3", "who": "M", "voice": "am_eric", "text": "Rides are free until noon today. I'll be back with another update at 8:15.",
                 "say": "Rides are free until noon today. I'll be back with another update at eight fifteen."},
            ],
        },
        "transcriptZh": [
            "早安，我是 Dale Fenner，為您帶來 7:40 的路況報導。Eastgate 橋塞得很嚴重。",
            "一輛貨運卡車在左線拋錨，所以每個方向只開放一個車道。",
            "工作人員起初說 9:00 前會把卡車清走。",
            "但是拖吊公司提早抵達，他們現在希望 8:30 前讓橋完全通車。",
            "很多駕駛改走 Orchard 路，想繞過這座橋。",
            "但是那裡因為自來水主管線維修封閉了一個車道，所以一樣走得很慢。",
            "今晚的演唱會會讓體育場附近 5:00 以後車流很多。",
            "可以的話，把車停在 Lakeside 停車場，搭乘每 10 分鐘一班的 12 路公車。",
            "今天中午前搭乘免費。8:15 我會再回來為您更新。",
        ],
        "questions": [
            {
                "q": "What does the speaker say about the crews' estimate?",
                "options": ["It has been put off until noon", "It has been moved earlier", "It was changed because of the concert", "It has not changed since this morning"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "對照 first 與 now：問變化就找新的版本",
                    "why": "Crews first said … by 9:00；But … now hope … by 8:30 → 完工時間提前，改述成 moved earlier。",
                    "evidence": [2, 3],
                    "wrong": ["時間錯置：noon 是公車免費的截止時間", None, "沒有提到演唱會影響完工時間", "方向相反：先說 9:00，現在改成 8:30"],
                    "wrongMore": [
                        "until noon 確實出現，但那是 Rides are free until noon today；道路完工的估計是從 9:00 提前到 8:30。",
                        None,
                        None,
                        "first said 與 now hope 就是在對照新舊說法，所以估計有變，而且是變早。",
                    ],
                    "vocab": [["tow company", "拖吊公司"], ["fully open", "完全通車"], ["clear", "排除（障礙）"]],
                },
            },
            {
                "q": "Why does the speaker mention Orchard Road?",
                "options": ["To warn that another route is also slow", "To recommend a faster way around the bridge", "To explain what caused the bridge delay", "To give directions to the Lakeside lot"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "意圖題：But 之後才是提到它的原因",
                    "why": "turning onto Orchard Road to get around 之後，But … slow going as well → 提醒改道也一樣慢。",
                    "evidence": [4, 5],
                    "wrong": [None, "字面陷阱：他只說很多人改走，沒有推薦", "沒有說 Orchard Road 造成橋上塞車", "沒有提到停車場的路線"],
                    "wrongMore": [
                        None,
                        "Many drivers are turning onto Orchard Road 聽起來像建議改道；但下一句 But … slow going as well 把它否定了，他是在提醒。",
                        None,
                        None,
                    ],
                    "vocab": [["water main", "自來水主管線"], ["slow going", "進展緩慢"], ["get around", "繞過"]],
                },
            },
            {
                "q": "What does the speaker advise listeners to do?",
                "options": ["Wait for the next report before leaving home", "Take Orchard Road instead of the bridge", "Put off their trips until noon", "Switch to public transportation for part of the trip"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "建議題：If you can 後面才是他的建議",
                    "why": "If you can, leave your car at the Lakeside lot and take the Route 12 bus → 停車後改搭公車。",
                    "evidence": [7],
                    "wrong": ["張冠李戴：下一次更新是主播自己要做的事", "提到但不是問的：Orchard Road 一樣塞", "同字陷阱：noon 是免費搭乘的期限", None],
                    "wrongMore": [
                        "I'll be back with another update 是主播自己的安排，不是對聽眾的建議。",
                        None,
                        "until noon 出現在 Rides are free until noon today，是公車免費的期限；他沒有叫人拖到中午才出門。",
                        None,
                    ],
                    "vocab": [["lot", "停車場"], ["update", "最新消息"]],
                },
            },
        ],
    },

    # l-talk-08  talk-next. Recorded phone menu of an internet provider (US, af_bella).
    # q1 expectation by 3:00. q2 conditional: the account-number step is skipped only for callers on the
    # registered phone, so a caller on another phone is still asked (hard). q3 the offer after "If you'd rather
    # not hold" (last line).
    {
        "id": "l-talk-08", "type": "listen", "format": "talk", "unit": "talk-next", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-08", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Thank you for calling Brightline Internet. Please listen carefully, because our menu options have changed."},
                {"file": "02.mp3", "who": "W", "voice": "af_bella", "text": "If you are calling about the outage in the Marlow area, you don't need to stay on the line."},
                {"file": "03.mp3", "who": "W", "voice": "af_bella", "text": "Crews expect to restore service by 3:00, and we'll send you a text message when it's done.",
                 "say": "Crews expect to restore service by three o'clock, and we'll send you a text message when it's done."},
                {"file": "04.mp3", "who": "W", "voice": "af_bella", "text": "To report a problem with your connection, press 1. To change or cancel a technician visit, press 2. For billing, press 3.",
                 "say": "To report a problem with your connection, press one. To change or cancel a technician visit, press two. For billing, press three."},
                {"file": "05.mp3", "who": "W", "voice": "af_bella", "text": "Business customers, press 0.", "say": "Business customers, press zero."},
                {"file": "06.mp3", "who": "W", "voice": "af_bella", "text": "After you choose, you'll be asked to key in your account number, which is at the top of your monthly bill."},
                {"file": "07.mp3", "who": "W", "voice": "af_bella", "text": "If you're calling from the phone number on your account, you can skip this step."},
                {"file": "08.mp3", "who": "W", "voice": "af_bella", "text": "Our wait time is currently about 10 minutes. If you'd rather not hold, press 9, and we'll call you back within the hour.",
                 "say": "Our wait time is currently about ten minutes. If you'd rather not hold, press nine, and we'll call you back within the hour."},
            ],
        },
        "transcriptZh": [
            "感謝您致電 Brightline 網路。請仔細聆聽，因為我們的選單選項已經更改。",
            "如果您是為了 Marlow 地區的服務中斷來電，不需要留在線上。",
            "維修人員預計 3:00 前恢復服務，完成時我們會傳簡訊給您。",
            "要回報連線問題，請按 1。要更改或取消技術人員到府，請按 2。帳單相關請按 3。",
            "企業客戶請按 0。",
            "選擇之後，系統會請您輸入帳號，帳號印在您每月帳單的最上方。",
            "如果您是用帳戶上登記的電話號碼來電，可以略過這個步驟。",
            "目前等候時間約 10 分鐘。如果您不想等候，請按 9，我們會在一小時內回電給您。",
        ],
        "questions": [
            {
                "q": "What is expected to happen by three o'clock?",
                "options": ["A technician will visit customers' homes", "The wait time will drop to ten minutes", "A service problem will be fixed", "Every caller will receive a return call"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "時間題：by 3:00 後面接的是預期的結果",
                    "why": "outage 之後說 Crews expect to restore service by 3:00 → 三點前修好，改述成問題被解決。",
                    "evidence": [1, 2],
                    "wrong": ["提到但不是問的：技術人員到府是按 2 才有的選項", "同字陷阱：10 minutes 是目前的等候時間", None, "時間錯置：回電是按 9 的人，在一小時內"],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["outage", "（服務）中斷"], ["restore", "恢復"], ["technician", "技術人員"]],
                },
            },
            {
                "q": "What will callers who are not using the phone number on their account be asked to do?",
                "options": ["Wait for a text message about service", "Enter a number printed on their bill", "Wait for a return call within the hour", "Skip the identification step"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "條件句：skip this step 是給另一群人的",
                    "why": "key in your account number 是對大家說的；skip this step 只免除用登記電話的人 → 其他人要輸入帳號。",
                    "evidence": [5, 6],
                    "wrong": ["提到但不是問的：簡訊是通知停電地區修復用的", None, "時間錯置：回電是選 9 之後的事", "張冠李戴：可以略過的是用登記電話的人"],
                    "wrongMore": [
                        None,
                        None,
                        None,
                        "skip this step 確實出現，所以很像；但那是 If you're calling from the phone number on your account 的人，題目問的剛好是不是這種人。",
                    ],
                    "vocab": [["key in", "輸入"], ["account number", "帳號"], ["skip", "略過"]],
                },
            },
            {
                "q": "What does the speaker offer callers who do not want to hold?",
                "options": ["A chance to be contacted by phone later", "A text message about the outage", "A direct line to the business desk", "A shorter wait for billing questions"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "提議題：If you'd rather not hold 後面是替代方案",
                    "why": "If you'd rather not hold, press 9, and we'll call you back → 改述成稍後以電話聯絡。",
                    "evidence": [7],
                    "wrong": [None, "張冠李戴：簡訊是給停電地區來電者的", "提到但不是問的：企業客戶按 0 是選單選項", "沒有提到帳單問題等候較短"],
                    "wrongMore": [
                        None,
                        "we'll send you a text message 確實出現，但那是服務修復後通知停電地區的人，不是給不想等候的人的選項。",
                        None,
                        None,
                    ],
                    "vocab": [["hold", "（電話）等候"], ["call back", "回電"]],
                },
            },
        ],
    },

    # l-talk-09  talk-topic. Self-storage advertisement with a price table (UK, bm_george).
    # q1 topic (easy). q2 graphic: "second-largest unit" is the coordinate (Large, $95); the half-price offer is in
    # line 5 (last third); answer is $47.50, which is not on the table. q3 quote with a literal trap.
    {
        "id": "l-talk-09", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "graphic": {
            "caption": "Cedar Row Storage: Monthly Rates",
            "head": ["Unit", "Size", "Monthly price"],
            "rows": [
                ["Small", "5 × 5 ft", "$39.00"],
                ["Medium", "5 × 10 ft", "$62.00"],
                ["Large", "10 × 10 ft", "$95.00"],
                ["Extra large", "10 × 20 ft", "$140.00"],
            ],
        },
        "audio": {
            "dir": "audio/l-talk-09", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_george", "text": "Running out of room at home? Cedar Row Storage has the space you need, and it's closer than you think."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "We rent secure, indoor units by the month, in four sizes, with no long-term contract."},
                {"file": "03.mp3", "who": "M", "voice": "bm_george", "text": "Clearing out a two-bedroom apartment? Our second-largest unit holds everything, from the sofa to the last box of books."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Most of our customers start with a garage full of boxes. With us, your garage can finally be a garage again."},
                {"file": "05.mp3", "who": "M", "voice": "bm_george", "text": "And if you sign up before the end of the month, your first month is half price."},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "Visit us on Mill Street, or reserve a unit online at any hour."},
                {"file": "07.mp3", "who": "M", "voice": "bm_george", "text": "Units go quickly, so reserve yours today."},
            ],
        },
        "transcriptZh": [
            "家裡空間不夠用嗎？Cedar Row 倉儲有您需要的空間，而且比您想的還近。",
            "我們按月出租安全的室內儲藏單位，共有四種尺寸，不需要長期合約。",
            "正在清空兩房公寓嗎？我們第二大的單位裝得下所有東西，從沙發到最後一箱書。",
            "我們大多數客人一開始都是車庫堆滿箱子。有了我們，您的車庫終於可以重新當車庫了。",
            "而且只要在月底前註冊，第一個月就是半價。",
            "歡迎到 Mill 街找我們，或隨時上網預訂一個單位。",
            "單位很快就會被租走，所以今天就預訂吧。",
        ],
        "questions": [
            {
                "q": "What is being advertised?",
                "options": ["A moving company", "A furniture store", "An apartment complex", "A service for keeping belongings"],
                "answer": 3,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "廣告題：開頭點出產品或服務",
                    "why": "Running out of room? 接著 We rent secure, indoor units → 出租空間給人存放東西，即保管物品。",
                    "evidence": [0, 1],
                    "wrong": ["聯想陷阱：clearing out 像搬家，但公司出租的是單位", "提到但不是問的：sofa 只是舉例要存的東西", "提到但不是問的：apartment 是客人搬出的地方", None],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["rent", "出租"], ["long-term contract", "長期合約"], ["clear out", "清空"]],
                },
            },
            {
                "q": "Look at the graphic. How much would a new customer who signs up this month pay for the first month of the unit the speaker describes?",
                "options": ["$31.00", "$47.50", "$70.00", "$95.00"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：先找出是哪一格，再套用折扣",
                    "why": "second-largest 是 Large，$95.00；first month is half price → $95.00 的一半是 $47.50。",
                    "evidence": [2, 4],
                    "wrong": ["算錯單位：$31.00 是 Medium 的半價", None, "算錯單位：$70.00 是 Extra large 的半價", "漏掉折扣：$95.00 是 Large 的原價"],
                    "wrongMore": [
                        None,
                        None,
                        None,
                        "Large 就是對的單位，所以 $95.00 很像；但 new customer 在月底前註冊，第一個月只付半價。",
                    ],
                    "vocab": [["second-largest", "第二大的"], ["sign up", "註冊、報名"], ["half price", "半價"]],
                },
            },
            {
                "q": "Why does the speaker say, \"Your garage can finally be a garage again\"?",
                "options": ["To say that the company is building new garages", "To offer a service that stores customers' cars", "To suggest that renting a unit will free up space at home", "To explain that the units are cheaper than a garage"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：garage again 是說空間會空出來",
                    "why": "a garage full of boxes，再說 your garage can finally be a garage again → 搬走箱子，空間空出來。",
                    "evidence": [3],
                    "wrong": ["字面陷阱：把 garage 當成公司要蓋的東西", "字面陷阱：把 garage 當成存車服務", None, "沒有拿價格和車庫比較"],
                    "wrongMore": [
                        None,
                        "garage 字面上是停車的地方，所以最像；但前一句說的是 a garage full of boxes，要說的是把箱子搬走，不是存車。",
                        None,
                        None,
                    ],
                    "vocab": [["garage", "車庫"], ["finally", "終於"]],
                },
            },
        ],
    },

    # l-talk-10  talk-detail. Workshop opening with a schedule (UK, bf_emma).
    # q1 reason after "because" (easy). q2 graphic: the two afternoon sessions switch times and each keeps its
    # room, so the 1:30 slot now has the 3:00 session's room (Room D); the audio never names the room.
    # q3 detail in the last third (survey by Friday -> prize drawing).
    {
        "id": "l-talk-10", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "uk",
        "graphic": {
            "caption": "Customer Service Workshop: Printed Schedule",
            "head": ["Time", "Session", "Room"],
            "rows": [
                ["9:30 A.M.", "Writing Clear Replies", "Room A"],
                ["11:00 A.M.", "Handling Difficult Calls", "Room C"],
                ["1:30 P.M.", "Using Data in Presentations", "Room B"],
                ["3:00 P.M.", "Planning Your Next Project", "Room D"],
            ],
        },
        "audio": {
            "dir": "audio/l-talk-10", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Good morning, everyone, and welcome to our customer service workshop. I'm Helen Ford, and I'll be hosting today."},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "You'll find a name badge and a printed schedule in the folder on your chair."},
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "Please wear the badge all day, because you'll need it to get into lunch."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "One change to that schedule: our data presenter is stuck at the airport, so the two afternoon sessions will switch times."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "Each session keeps its original room, so please check the schedule carefully after lunch."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "We'd also love your opinions. A short survey will be e-mailed at 4:00, and everyone who completes it by Friday enters a prize drawing.",
                 "say": "We'd also love your opinions. A short survey will be emailed at four o'clock, and everyone who completes it by Friday enters a prize drawing."},
                {"file": "07.mp3", "who": "W", "voice": "bf_emma", "text": "Now, let's begin. Please turn to the person beside you and introduce yourself."},
            ],
        },
        "transcriptZh": [
            "各位早安，歡迎參加我們的客戶服務工作坊。我是 Helen Ford，今天由我主持。",
            "您椅子上的資料夾裡有一個名牌和一份紙本行程表。",
            "請整天都戴著名牌，因為您需要它才能進去用午餐。",
            "行程表有一項更動：我們的數據主講人被困在機場，所以下午的兩場課程要對調時間。",
            "每一場課程的教室維持原定，所以午餐後請仔細確認行程表。",
            "我們也想聽聽您的意見。4:00 會用電子郵件寄出一份簡短問卷，星期五前填完的人都可以參加抽獎。",
            "好，我們開始吧。請轉向旁邊的人，自我介紹一下。",
        ],
        "questions": [
            {
                "q": "Why are listeners asked to wear their badges all day?",
                "options": ["To get a printed schedule at the door", "To enter a prize drawing", "To be admitted to a meal", "To be matched with a partner for an activity"],
                "answer": 2,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "原因題：because 後面就是理由",
                    "why": "wear the badge all day, because you'll need it to get into lunch → get into lunch 即用餐。",
                    "evidence": [2],
                    "wrong": ["提到但不是問的：行程表已經在資料夾裡", "提到但不是問的：抽獎要填問卷，與名牌無關", None, "沒有提到配對：只說轉向旁邊的人自我介紹"],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["name badge", "名牌"], ["hosting", "主持"], ["admitted", "獲准進入"]],
                },
            },
            {
                "q": "Look at the graphic. In which room will the 1:30 P.M. session now take place?",
                "options": ["Room A", "Room B", "Room C", "Room D"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：場次對調時間，房間跟著場次走",
                    "why": "two afternoon sessions will switch times，Each session keeps its original room → 3:00 那場移到 1:30，仍是 Room D。",
                    "evidence": [3, 4],
                    "wrong": ["Room A：是早上 9:30 的場次，不受影響", "同字陷阱：表上 1:30 那列是 Room B，但場次已對調", "Room C：是 11:00 的場次，不受影響", None],
                    "wrongMore": [
                        None,
                        "表上 1:30 那一列是 Room B，沒注意到下午兩場對調的人會選它；音檔說 Each session keeps its original room，所以房間跟著場次不動。",
                        None,
                        None,
                    ],
                    "vocab": [["switch times", "對調時間"], ["original", "原本的"]],
                },
            },
            {
                "q": "What can listeners do to enter a prize drawing?",
                "options": ["Give their opinions of the workshop", "Switch to a rescheduled session", "Introduce themselves to a neighbor", "Check the schedule after lunch"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "細節題：by Friday 前面的條件才是答案",
                    "why": "completes it by Friday enters a prize drawing，it 指 short survey → 填問卷表達意見。",
                    "evidence": [5],
                    "wrong": [None, "提到但不是問的：對調場次是行程更動，與抽獎無關", "順序錯置：自我介紹是講完話後的下一步，與抽獎無關", "提到但不是問的：看行程表是為了找對教室"],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["survey", "問卷"], ["prize drawing", "抽獎"], ["complete", "完成（填寫）"]],
                },
            },
        ],
    },

    # l-talk-11  talk-next. Coffee roastery tour introduction (US, af_sarah).
    # q1 who the listeners are (easy). q2 change: "Normally ... but today" (tasting moved to the end).
    # q3 next step: "Before we set off" (sign the sheet) comes before heading to storage; earplugs belong to the
    # third stop and the tasting is last (last third).
    {
        "id": "l-talk-11", "type": "listen", "format": "talk", "unit": "talk-next", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-11", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Welcome to the Alder Lane Roastery, everyone. I'm Marisol, and I'll be your guide for this 45-minute tour.",
                 "say": "Welcome to the Alder Lane Roastery, everyone. I'm Marisol, and I'll be your guide for this forty-five minute tour."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "Normally we begin with a tasting, but the tasting room is booked today, so we'll finish there instead."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "We'll follow the beans from storage to packing. The roasting room is our third stop, and it gets very loud."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Before we enter it, please take a pair of earplugs from the basket in the hallway."},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "Please stay behind the yellow line near the machines, since the drums get extremely hot."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "Photos are welcome, but please turn off your flash. If you'd like to buy beans, our shop will open after the tasting."},
                {"file": "07.mp3", "who": "W", "voice": "af_sarah", "text": "Before we set off, I need everyone's name on the visitor sheet. It's on the clipboard right here."},
                {"file": "08.mp3", "who": "W", "voice": "af_sarah", "text": "Once everyone's name is down, we'll head to the storage room."},
            ],
        },
        "transcriptZh": [
            "各位好，歡迎來到 Alder Lane 烘豆坊。我是 Marisol，這趟 45 分鐘的導覽由我帶領。",
            "通常我們從試喝開始，但試喝室今天已經被訂走，所以我們改在最後到那裡。",
            "我們會跟著咖啡豆從儲藏區一路走到包裝區。烘豆室是第三站，裡面非常吵。",
            "進去之前，請從走廊的籃子裡拿一副耳塞。",
            "請站在機器旁邊的黃線後面，因為滾筒會非常燙。",
            "歡迎拍照，但請關掉閃光燈。如果您想買咖啡豆，商店在試喝之後開放。",
            "出發之前，我需要每個人把名字寫在訪客登記表上，表就放在這裡的板夾上。",
            "大家的名字都寫好之後，我們就前往儲藏室。",
        ],
        "questions": [
            {
                "q": "Who most likely are the listeners?",
                "options": ["Employees of the roastery", "People on a guided visit", "Coffee growers", "Shop customers"],
                "answer": 1,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "身分題：guide 與 tour 點出聽眾是參觀者",
                    "why": "I'll be your guide for this 45-minute tour → 說話者是導覽員，聽眾是參加導覽的人。",
                    "evidence": [0],
                    "wrong": ["沒有提到他們在這裡工作：guide 帶領的是參觀者", None, "沒有提到咖啡農", "同字陷阱：shop 出現，但店是參觀後才開放的選項"],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["roastery", "烘豆工坊"], ["guide", "導覽員"]],
                },
            },
            {
                "q": "What change does the speaker mention?",
                "options": ["The tour will begin with a tasting", "The tour will be shorter than usual", "The tasting will come later in the visit than usual", "The roasting room will be closed to visitors"],
                "answer": 2,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "變化題：Normally … but today 後面才是新安排",
                    "why": "Normally we begin with a tasting, but … we'll finish there instead → 試喝從開頭改到最後，改述成比平常晚。",
                    "evidence": [1],
                    "wrong": ["方向相反：先試喝是平常的做法", "沒有提到縮短：45 分鐘是整趟導覽的長度", None, "同字陷阱：roasting room 只是太吵要戴耳塞"],
                    "wrongMore": [
                        "begin with a tasting 是 Normally 的做法，所以最像；but today 之後改成 finish there instead，順序反過來了。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["tasting", "試飲"], ["booked", "被預訂"]],
                },
            },
            {
                "q": "What will the listeners most likely do next?",
                "options": ["Collect ear protection", "Sample some coffee", "Go to the storage room", "Write their names on a list"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "順序題：Before we set off 是眼前第一件事",
                    "why": "Before we set off, I need everyone's name on the visitor sheet；Once … name is down → 先寫名字才出發。",
                    "evidence": [6, 7],
                    "wrong": ["順序錯置：耳塞是進第三站烘豆室之前才拿", "順序錯置：試喝排在最後", "順序錯置：去儲藏室要等名字寫完之後", None],
                    "wrongMore": [
                        "Before we enter it 的 it 是 the roasting room，也就是第三站；現在還沒出發，離拿耳塞還早。",
                        None,
                        "we'll head to the storage room 離得最近，所以很像；但 Once everyone's name is down 說明那是寫完名字之後的事。",
                        None,
                    ],
                    "vocab": [["set off", "出發"], ["visitor sheet", "訪客登記表"], ["earplugs", "耳塞"]],
                },
            },
        ],
    },
]
