# Round 6 listening items, written under WRITING_RULES.md (sections 2, 3, 5, 6, 7.1). Revised after blind review.
# 6 talk sets (Part 4 style, one speaker, 3 questions each = 18 questions): l-talk-06 .. l-talk-11.
# Units: 2 talk-topic (06, 09), 2 talk-detail (07, 10), 2 talk-next (08, 11). Each set mixes question types.
# Scripts are in US English even when a British voice reads them. All content is original; names of people,
# firms, places and products are invented.
# Digits in `text` are spoken from `say` (times, prices, counts, route and key numbers are spelled out there).
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` here is the highest
# self-test band in the item (easy 1, medium 2, hard 3).
# reviewed stays False until the items pass a blind review and every mp3 has been heard.
# Scenes (new against l-talk-01..05): rail-replacement announcement, radio traffic report, internet provider
# phone menu, self-storage advertisement, customer-service workshop opening, coffee roastery tour.
# Self-test summary: 18 questions = 2 easy (first question of 06 and 09), 6 medium, 10 hard; at most one
# easy per set. No answer needs arithmetic; no key repeats a content word from the audio.
# Implied-meaning questions: l-talk-06 q2 ("Those trains exist only on paper."), l-talk-08 q1 ("You don't need to
# stay on the line"), l-talk-09 q3 ("... your garage can finally be a garage again."), l-talk-07 q2 (purpose).
# Graphic questions: l-talk-09 q2 (price table with a first-month column) and l-talk-10 q2 (schedule); the audio
# never says the answer cell.
# Answer key by position (A=0 ... D=3): 06 A D C | 07 B A D | 08 C B A | 09 D B C | 10 C D A | 11 B C D.

ITEMS = [
    # l-talk-06  talk-topic. Rail-replacement announcement (UK, bm_lewis).
    # q1 topic (easy; distractors hook on tickets, east exit and the signal failure). q2 quote: "Those trains exist
    # only on paper." = the listed trains will not run; the literal reading (printed timetables) is near-correct.
    # q3 the railway pays for taxis after the buses stop at 10:00 (last third); the key is paraphrased.
    {
        "id": "l-talk-06", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 3,
        "source": "hand", "reviewed": True, "v": 2, "accent": "uk",
        "audio": {
            "dir": "audio/l-talk-06", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_lewis", "text": "Attention, passengers at Carrow Central. Because of a signal failure near Dunhaven, no trains will run on the Harbor Line this evening."},
                {"file": "02.mp3", "who": "M", "voice": "bm_lewis", "text": "Replacement buses are boarding now on the station forecourt, outside the east exit."},
                {"file": "03.mp3", "who": "M", "voice": "bm_lewis", "text": "The buses stop at every station, so allow extra time for your journey. Your tickets and passes remain valid."},
                {"file": "04.mp3", "who": "M", "voice": "bm_lewis", "text": "Some trains still appear on the departure board. Those trains exist only on paper."},
                {"file": "05.mp3", "who": "M", "voice": "bm_lewis", "text": "Staff in yellow jackets are on the concourse, so please check with them before you go to a platform."},
                {"file": "06.mp3", "who": "M", "voice": "bm_lewis", "text": "The buses will run until 10:00 tonight. After that, please use the taxi stand outside the north exit.",
                 "say": "The buses will run until ten o'clock tonight. After that, please use the taxi stand outside the north exit."},
                {"file": "07.mp3", "who": "M", "voice": "bm_lewis", "text": "The railway will cover the fare for those taxis. We apologize for the inconvenience."},
            ],
        },
        "transcriptZh": [
            "各位在 Carrow Central 車站的旅客請注意。由於 Dunhaven 附近號誌故障，今晚 Harbor 線沒有列車行駛。",
            "接駁公車現在正在站前廣場上車，就在東出口外面。",
            "公車每一站都停，所以請預留額外的時間。您的車票和通行證仍然有效。",
            "出發看板上還顯示著一些列車。那些列車只存在於紙面上。",
            "穿黃色外套的工作人員在站內大廳，所以前往月台之前請先向他們確認。",
            "公車今晚營運到 10:00。之後請使用北出口外的計程車招呼站。",
            "鐵路公司會負擔那些計程車的車資。造成不便，我們深感抱歉。",
        ],
        "questions": [
            {
                "q": "What is the announcement mainly about?",
                "options": ["A temporary change in how passengers travel", "New rules for exchanging tickets", "Directions to the station's east exit", "The cause of a signal problem"],
                "answer": 0,
                "ldbs": {"L": True, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "主旨題：開頭兩句就點出主題",
                    "why": "no trains will run 加上 Replacement buses are boarding → 改述成暫時改變旅客的搭乘方式。",
                    "evidence": [0, 1],
                    "wrong": [None, "提到但不是問的：只說車票仍有效，沒有換票規則", "提到但不是問的：east exit 只是上車處的位置", "提到但不是問的：signal failure 只是停駛的原因"],
                    "wrongMore": [
                        None,
                        "Your tickets and passes remain valid 是一句附帶說明，沒有提到任何換票或退票的規則。",
                        "outside the east exit 只告訴旅客在哪裡上車；整則廣播的重點是列車停駛、改搭公車。",
                        "signal failure 確實出現，但那是停駛的原因；廣播真正要說的是停駛後旅客怎麼搭車。",
                    ],
                    "vocab": [["signal failure", "號誌故障"], ["replacement bus", "接駁（替代）公車"], ["forecourt", "站前廣場"]],
                },
            },
            {
                "q": "Why does the speaker say, \"Those trains exist only on paper\"?",
                "options": ["To say that paper timetables are available at the station", "To promise that the board will be fixed soon", "To warn that some trains will run later than listed", "To caution passengers against relying on what the screens show"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：on paper 是提醒別信看板",
                    "why": "看板上還列著班次，但 exist only on paper；接著 check with them → 提醒別相信螢幕上的資訊。",
                    "evidence": [3, 4],
                    "wrong": ["字面陷阱：把 on paper 讀成紙本時刻表", "語境矛盾：沒有說看板會很快修好", "語境矛盾：整晚沒有列車，不是晚點", None],
                    "wrongMore": [
                        "on paper 字面上是「印在紙上」，所以聽起來合理；但這句接在「看板上還顯示列車」之後，意思是班次只存在於紙面，實際不會開。",
                        None,
                        "trains still appear 容易讓人想成晚點；但第一句就說 no trains will run，所以這些班次根本不開，而不是晚到。",
                        None,
                    ],
                    "vocab": [["departure board", "出發班次看板"], ["on paper", "只存在於紙面上、名義上"]],
                },
            },
            {
                "q": "What will the railway company do for passengers arriving after the buses stop?",
                "options": ["Keep the replacement buses running all night", "Refund their unused tickets", "Pay for a hired car once the coaches have finished", "Cover the fare for the replacement buses"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "細節題：After that 後面才是安排",
                    "why": "After that … taxi stand；The railway will cover the fare → 鐵路公司負擔計程車費。",
                    "evidence": [5, 6],
                    "wrong": ["時間錯置：公車只開到 10:00", "提到但不是問的：車票仍有效，沒說退款", None, "同字陷阱：cover the fare 是指計程車，不是公車"],
                    "wrongMore": [
                        "until 10:00 tonight 說明公車有收班時間，之後才改搭計程車。",
                        None,
                        None,
                        "cover the fare 確實出現，但後面接的是 those taxis；公車收班之後才輪到計程車，而公車本來就可用車票搭乘。",
                    ],
                    "vocab": [["cover the fare", "負擔車資"], ["remain valid", "仍然有效"]],
                },
            },
        ],
    },

    # l-talk-07  talk-detail. Radio traffic report (US, am_eric). No easy question in this set.
    # q1 cause of the revised estimate (line 4, after "But"). q2 purpose of mentioning Orchard Road: line 5 sounds
    # like a recommendation, line 6 reverses it. q3 advice in the last third; the 8:15 update is the speaker's action.
    {
        "id": "l-talk-07", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 2,
        "source": "hand", "reviewed": True, "v": 2, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-07", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_eric", "text": "This is Dale Fenner with your 7:40 traffic report. Eastgate Bridge is backed up.",
                 "say": "This is Dale Fenner with your seven forty traffic report. Eastgate Bridge is backed up."},
                {"file": "02.mp3", "who": "M", "voice": "am_eric", "text": "A truck broke down in the left lane, so only one lane is open each way."},
                {"file": "03.mp3", "who": "M", "voice": "am_eric", "text": "Crews first said they would clear it by 9:00.",
                 "say": "Crews first said they would clear it by nine o'clock."},
                {"file": "04.mp3", "who": "M", "voice": "am_eric", "text": "But a tow company arrived early."},
                {"file": "05.mp3", "who": "M", "voice": "am_eric", "text": "They now hope to open the bridge fully by 8:30.",
                 "say": "They now hope to open the bridge fully by eight thirty."},
                {"file": "06.mp3", "who": "M", "voice": "am_eric", "text": "Many drivers are turning onto Orchard Road to get around the bridge."},
                {"file": "07.mp3", "who": "M", "voice": "am_eric", "text": "But a water main repair there has closed a lane, so it's slow going as well."},
                {"file": "08.mp3", "who": "M", "voice": "am_eric", "text": "If you can, leave your car at the Lakeside lot and take the Route 12 bus this morning.",
                 "say": "If you can, leave your car at the Lakeside lot and take the Route twelve bus this morning."},
                {"file": "09.mp3", "who": "M", "voice": "am_eric", "text": "Rides are free until noon, and I'll update you again at 8:15.",
                 "say": "Rides are free until noon, and I'll update you again at eight fifteen."},
                {"file": "10.mp3", "who": "M", "voice": "am_eric", "text": "Tonight's concert will bring heavy traffic near the stadium after 5:00.",
                 "say": "Tonight's concert will bring heavy traffic near the stadium after five o'clock."},
            ],
        },
        "transcriptZh": [
            "我是 Dale Fenner，為您帶來 7:40 的路況報導。Eastgate 橋塞車了。",
            "一輛卡車在左線拋錨，所以每個方向只開放一個車道。",
            "工作人員起初說 9:00 前會清除。",
            "但是拖吊公司提早抵達。",
            "他們現在希望 8:30 前讓橋完全通車。",
            "很多駕駛改走 Orchard 路，想繞過這座橋。",
            "但是那裡因為自來水主管線維修封閉了一個車道，所以一樣走得很慢。",
            "可以的話，今天早上把車停在 Lakeside 停車場，搭乘 12 路公車。",
            "中午前搭乘免費，8:15 我會再為您更新。",
            "今晚的演唱會會讓體育場附近 5:00 以後車流很多。",
        ],
        "questions": [
            {
                "q": "What caused the crews to change their estimate?",
                "options": ["Drivers began using Orchard Road", "A recovery firm reached the scene sooner than anticipated", "A repair on another road was finished", "The truck's driver solved the problem"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "原因題：把原因和新估計兩句串起來",
                    "why": "first said … 9:00；But a tow company arrived early；They now hope … 8:30 → 拖車提早到，估計才提前。",
                    "evidence": [2, 3, 4],
                    "wrong": ["提到但不是問的：改走 Orchard Road 與估計時間無關", None, "提到但不是問的：water main 維修在 Orchard Road", "沒有提到司機修好：來的是拖吊公司"],
                    "wrongMore": [None, None, "a water main repair 是 Orchard Road 上的維修，還沒完成（has closed a lane），和橋上的清理時間無關。", None],
                    "vocab": [["tow company", "拖吊公司"], ["fully open", "完全通車"], ["clear", "排除（障礙）"]],
                },
            },
            {
                "q": "Why does the speaker mention Orchard Road?",
                "options": ["To warn that another route is also slow", "To recommend a faster way around the bridge", "To explain what caused the bridge delay", "To explain why the stadium area will be busy tonight"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "意圖題：But 之後才是提到它的原因",
                    "why": "turning onto Orchard Road 後，But a water main repair … slow going as well → 提醒改道也一樣慢。",
                    "evidence": [5, 6],
                    "wrong": [None, "字面陷阱：他只說很多人改走，沒有推薦", "沒有說 Orchard Road 造成橋上塞車", "提到但不是問的：體育場的車流是演唱會造成的"],
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
                    "why": "If you can, leave your car at the Lakeside lot and take the Route 12 bus this morning → 停車後改搭公車。",
                    "evidence": [7, 8],
                    "wrong": ["張冠李戴：下一次更新是主播自己要做的事", "提到但不是問的：Orchard Road 一樣塞", "同字陷阱：noon 是免費搭乘的期限", None],
                    "wrongMore": [
                        "I'll update you again 是主播自己的安排，不是對聽眾的建議。",
                        None,
                        "until noon 出現在 Rides are free until noon，是同一趟早上搭公車的免費期限；他沒有叫人拖到中午才出門。",
                        None,
                    ],
                    "vocab": [["lot", "停車場"], ["update", "最新消息"]],
                },
            },
        ],
    },

    # l-talk-08  talk-next. Recorded phone menu of an internet provider (US, af_bella).
    # q1 quote: "you don't need to stay on the line" = the problem is already being handled; literal reading about
    # the phone line. q2 conditional: "skip this step" applies only to callers on the registered phone.
    # q3 the offer after "If you'd rather not hold" (last two lines).
    {
        "id": "l-talk-08", "type": "listen", "format": "talk", "unit": "talk-next", "level": 2,
        "source": "hand", "reviewed": True, "v": 2, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-08", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Thank you for calling Brightline Internet."},
                {"file": "02.mp3", "who": "W", "voice": "af_bella", "text": "If you are calling about the outage in the Marlow area, you don't need to stay on the line."},
                {"file": "03.mp3", "who": "W", "voice": "af_bella", "text": "Crews expect to restore service by 3:00, and we'll send you a text message when it's done.",
                 "say": "Crews expect to restore service by three o'clock, and we'll send you a text message when it's done."},
                {"file": "04.mp3", "who": "W", "voice": "af_bella", "text": "To report a connection problem, press 1. To change or cancel a technician visit, press 2. For billing, press 3.",
                 "say": "To report a connection problem, press one. To change or cancel a technician visit, press two. For billing, press three."},
                {"file": "05.mp3", "who": "W", "voice": "af_bella", "text": "Business customers, press 0.", "say": "Business customers, press zero."},
                {"file": "06.mp3", "who": "W", "voice": "af_bella", "text": "After you choose, you'll be asked to key in your account number, which is at the top of your monthly bill."},
                {"file": "07.mp3", "who": "W", "voice": "af_bella", "text": "If you're calling from the phone number on your account, you can skip this step."},
                {"file": "08.mp3", "who": "W", "voice": "af_bella", "text": "Our wait time is currently about 10 minutes. If you'd rather not hold, press 9.",
                 "say": "Our wait time is currently about ten minutes. If you'd rather not hold, press nine."},
                {"file": "09.mp3", "who": "W", "voice": "af_bella", "text": "We'll then call you back within the hour."},
            ],
        },
        "transcriptZh": [
            "感謝您致電 Brightline 網路。",
            "如果您是為了 Marlow 地區的服務中斷來電，不需要留在線上。",
            "維修人員預計 3:00 前恢復服務，完成時我們會傳簡訊給您。",
            "要回報連線問題，請按 1。要更改或取消技術人員到府，請按 2。帳單相關請按 3。",
            "企業客戶請按 0。",
            "選擇之後，系統會請您輸入帳號，帳號印在您每月帳單的最上方。",
            "如果您是用帳戶上登記的電話號碼來電，可以略過這個步驟。",
            "目前等候時間約 10 分鐘。如果您不想等候，請按 9。",
            "我們會在一小時內回電給您。",
        ],
        "questions": [
            {
                "q": "Why does the speaker say, \"You don't need to stay on the line\"?",
                "options": ["To explain that the phone line is not working", "To suggest that callers phone back after 3:00", "To signal that the problem is already being handled", "To say that the wait time is short"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：不必等是因為問題已有人處理",
                    "why": "you don't need to stay on the line，下一句 Crews expect to restore service → 問題已在處理。",
                    "evidence": [1, 2],
                    "wrong": ["字面陷阱：把 line 讀成故障的電話線", "語境矛盾：沒有叫人三點後再打", None, "提到但不是問的：等候時間是後面才提到，也不是說很短"],
                    "wrongMore": [
                        "the line 字面上可以想成電話線；但說話者是在對來電者說不必繼續等待接聽，不是說電話線壞了。",
                        None,
                        None,
                        "wait time 要到後面才出現（about 10 minutes），而且是對不想等的人說的；這句話的原因是維修人員已在處理。",
                    ],
                    "vocab": [["outage", "（服務）中斷"], ["stay on the line", "不掛電話、繼續等待"]],
                },
            },
            {
                "q": "After choosing a menu option, what will callers who are not using the phone number on their account be asked to do?",
                "options": ["Report a connection problem", "Enter an identification number from their statement", "Cancel a technician visit", "Skip the identification step"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "條件句：skip this step 是給另一群人的",
                    "why": "key in your account number 是對大家說的；skip this step 只免除用登記電話的人 → 其他人要輸入帳號。",
                    "evidence": [5, 6],
                    "wrong": ["提到但不是問的：回報連線問題是按 1 的選項", None, "提到但不是問的：取消技術人員到府是按 2 的選項", "張冠李戴：可以略過的是用登記電話的人"],
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
                "options": ["A chance to be contacted by phone later", "A text message about the outage", "A direct line to the business desk", "A technician visit within the hour"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "提議題：If you'd rather not hold 後面是替代方案",
                    "why": "If you'd rather not hold, press 9；We'll then call you back within the hour → 之後由公司打電話聯絡。",
                    "evidence": [7, 8],
                    "wrong": [None, "張冠李戴：簡訊是給停電地區來電者的", "提到但不是問的：企業客戶按 0 是選單選項", "提到但不是問的：技術人員到府是按 2 的選項"],
                    "wrongMore": [
                        None,
                        "we'll send you a text message 確實出現，但那是服務修復後通知停電地區的人，不是給不想等候的人的選項。",
                        None,
                        "within the hour 是回電的時限，不是技術人員到府的時間。",
                    ],
                    "vocab": [["hold", "（電話）等候"], ["call back", "回電"]],
                },
            },
        ],
    },

    # l-talk-09  talk-topic. Self-storage advertisement with a price table (UK, bm_george).
    # q1 topic (easy). q2 graphic: "second-largest unit" is the coordinate (Large); the table has a first-month
    # column, so no arithmetic: the regular price in the same row ($95.00) is the trap. q3 quote with a literal trap.
    {
        "id": "l-talk-09", "type": "listen", "format": "talk", "unit": "talk-topic", "level": 3,
        "source": "hand", "reviewed": True, "v": 2, "accent": "uk",
        "graphic": {
            "caption": "Cedar Row Storage: Monthly Rates",
            "head": ["Unit", "Size", "Regular price", "First month (new customers)"],
            "rows": [
                ["Small", "5 × 5 ft", "$39.00", "$19.50"],
                ["Medium", "5 × 10 ft", "$62.00", "$31.00"],
                ["Large", "10 × 10 ft", "$95.00", "$47.50"],
                ["Extra large", "10 × 20 ft", "$140.00", "$70.00"],
            ],
        },
        "audio": {
            "dir": "audio/l-talk-09", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_george", "text": "Running out of room at home? Cedar Row Storage has the space you need, and it's closer than you think."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "We rent secure, indoor units by the month, in four sizes, with no long-term contract."},
                {"file": "03.mp3", "who": "M", "voice": "bm_george", "text": "Clearing out a two-bedroom apartment? Our second-largest unit holds everything, from the sofa to the last box of books."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Most of our customers come to us because of their garage. With us, your garage can finally be a garage again."},
                {"file": "05.mp3", "who": "M", "voice": "bm_george", "text": "And if you sign up before the end of the month, you'll pay our special first-month rate."},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "Visit us on Mill Street, or reserve a unit online at any hour."},
                {"file": "07.mp3", "who": "M", "voice": "bm_george", "text": "Units go quickly, so reserve yours today."},
            ],
        },
        "transcriptZh": [
            "家裡空間不夠用嗎？Cedar Row 倉儲有您需要的空間，而且比您想的還近。",
            "我們按月出租安全的室內儲藏單位，共有四種尺寸，不需要長期合約。",
            "正在清空兩房公寓嗎？我們第二大的單位裝得下所有東西，從沙發到最後一箱書。",
            "我們大多數客人都是因為車庫的問題來找我們。有了我們，您的車庫終於可以重新當車庫了。",
            "而且只要在月底前註冊，您第一個月就適用我們的特別優惠價。",
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
                    "why": "Running out of room? 接著 We rent secure, indoor units → 出租空間存放東西，即保管物品的服務。",
                    "evidence": [0, 1],
                    "wrong": ["聯想陷阱：clearing out 像搬家，但公司出租的是單位", "提到但不是問的：sofa 只是舉例要存的東西", "提到但不是問的：apartment 是客人搬出的地方", None],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["rent", "出租"], ["long-term contract", "長期合約"], ["clear out", "清空"]],
                },
            },
            {
                "q": "Look at the graphic. How much will a customer who signs up this month pay for the first month of the unit the speaker describes?",
                "options": ["$31.00", "$47.50", "$70.00", "$95.00"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：音檔給哪一列，表上找對的欄",
                    "why": "second-largest unit 是 Large；月底前註冊適用 first-month rate → 看 First month 欄，$47.50。",
                    "evidence": [2, 4],
                    "wrong": ["看錯列：$31.00 是 Medium 的首月價", None, "看錯列：$70.00 是 Extra large 的首月價", "看錯欄：$95.00 是 Large 的原價"],
                    "wrongMore": [
                        None,
                        None,
                        None,
                        "Large 就是對的單位，所以同一列的 $95.00 很像；但月底前註冊的人適用 first-month rate，要看 First month 那一欄。",
                    ],
                    "vocab": [["second-largest", "第二大的"], ["sign up", "註冊、報名"], ["first-month rate", "首月優惠價"]],
                },
            },
            {
                "q": "Why does the speaker say, \"Your garage can finally be a garage again\"?",
                "options": ["To say that the company is building new garages", "To offer a service that stores customers' cars", "To suggest that renting a unit will free up space at home", "To explain that the units are cheaper than a garage"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：garage again 是說空間會空出來",
                    "why": "Running out of room 加 rent … units，再說 your garage can finally be a garage again → 車庫空出來。",
                    "evidence": [0, 1, 3],
                    "wrong": ["字面陷阱：把 garage 當成公司要蓋的東西", "字面陷阱：把 garage 當成存車服務", None, "沒有拿價格和車庫比較"],
                    "wrongMore": [
                        None,
                        "garage 字面上是停車的地方，所以最像；但前面說的是出租室內單位存放家裡的東西，要說的是車庫能空出來，不是存車。",
                        None,
                        None,
                    ],
                    "vocab": [["garage", "車庫"], ["finally", "終於"]],
                },
            },
        ],
    },

    # l-talk-10  talk-detail. Workshop opening with a schedule (UK, bf_emma).
    # q1 reason after "because" (the set's one easy question). q2 graphic: the two afternoon sessions switch times and
    # each keeps its room, so the session in Room B (Using Data) now starts at 3:00; the audio names neither Room B
    # nor 3:00. q3 detail in the last third (survey by Friday); the key is a paraphrase.
    {
        "id": "l-talk-10", "type": "listen", "format": "talk", "unit": "talk-detail", "level": 3,
        "source": "hand", "reviewed": True, "v": 2, "accent": "uk",
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
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "Please wear the badge all day."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "Lunch is in the courtyard at 12:30, where staff will check each badge.",
                 "say": "Lunch is in the courtyard at twelve thirty, where staff will check each badge."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "One change to that schedule: our data presenter is stuck at the airport, so the two afternoon sessions will switch times."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "Each session keeps its original room, so please check the schedule carefully after lunch."},
                {"file": "07.mp3", "who": "W", "voice": "bf_emma", "text": "We'd also love your opinions. A short survey will be e-mailed at 4:00, and everyone who completes it by Friday enters a prize drawing.",
                 "say": "We'd also love your opinions. A short survey will be emailed at four o'clock, and everyone who completes it by Friday enters a prize drawing."},
                {"file": "08.mp3", "who": "W", "voice": "bf_emma", "text": "Now, let's begin. Please turn to the person beside you and introduce yourself."},
            ],
        },
        "transcriptZh": [
            "各位早安，歡迎參加我們的客戶服務工作坊。我是 Helen Ford，今天由我主持。",
            "您椅子上的資料夾裡有一個名牌和一份紙本行程表。",
            "請整天都戴著名牌。",
            "午餐在 12:30 於中庭供應，工作人員會在那裡檢查每個人的名牌。",
            "行程表有一項更動：我們的數據主講人被困在機場，所以下午的兩場課程要對調時間。",
            "每一場課程的教室維持原定，所以午餐後請仔細確認行程表。",
            "我們也想聽聽您的意見。4:00 會用電子郵件寄出一份簡短問卷，星期五前填完的人都可以參加抽獎。",
            "好，我們開始吧。請轉向旁邊的人，自我介紹一下。",
        ],
        "questions": [
            {
                "q": "Why are listeners asked to wear their badges all day?",
                "options": ["To get into the afternoon sessions", "To enter a prize drawing", "To show that they are entitled to a meal", "To be matched with a partner for an activity"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "原因題：要把相鄰兩句串起來",
                    "why": "wear the badge all day；Lunch … staff will check each badge → 名牌用來證明有資格用餐。",
                    "evidence": [2, 3],
                    "wrong": ["提到但不是問的：下午場次只是行程更動的背景", "提到但不是問的：抽獎要填問卷，與名牌無關", None, "沒有提到配對：只說轉向旁邊的人自我介紹"],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["name badge", "名牌"], ["hosting", "主持"], ["admitted", "獲准進入"]],
                },
            },
            {
                "q": "Look at the graphic. When will the session in Room B begin?",
                "options": ["9:30 A.M.", "11:00 A.M.", "1:30 P.M.", "3:00 P.M."],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：場次對調時間，教室跟著場次",
                    "why": "Room B 是 Using Data；sessions will switch times，Each session keeps its original room → 改到 3:00。",
                    "evidence": [4, 5],
                    "wrong": ["9:30 是 Writing Clear Replies，在 Room A", "11:00 是 Handling Difficult Calls，在 Room C", "看表沒看音檔：1:30 是 Room B 原本的時間，但兩場已對調", None],
                    "wrongMore": [
                        None,
                        None,
                        "表上 Room B 那一列寫 1:30，沒注意到下午兩場對調的人會選它；音檔說 Each session keeps its original room，所以 Room B 的場次跟著換到 3:00。",
                        None,
                    ],
                    "vocab": [["switch times", "對調時間"], ["original", "原本的"]],
                },
            },
            {
                "q": "What can listeners do to enter a prize drawing?",
                "options": ["Answer a questionnaire by the end of the week", "Switch to a rescheduled session", "Introduce themselves to a neighbor", "Reply to an e-mail before 4:00"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "細節題：抽獎條件和期限一起說",
                    "why": "completes it by Friday enters a prize drawing，it 指 A short survey → 週五前填問卷。",
                    "evidence": [6],
                    "wrong": [None, "提到但不是問的：對調場次是行程更動，與抽獎無關", "順序錯置：自我介紹是講完話後的下一步，與抽獎無關", "時間錯置：4:00 是寄出問卷的時間，期限是星期五"],
                    "wrongMore": [
                        None,
                        None,
                        None,
                        "4:00 確實出現，但那是問卷寄出的時間，不是回覆期限；問卷寄出後，星期五前填完才能抽獎。",
                    ],
                    "vocab": [["survey", "問卷"], ["prize drawing", "抽獎"], ["complete", "完成（填寫）"]],
                },
            },
        ],
    },

    # l-talk-11  talk-next. Coffee roastery tour introduction (US, af_sarah).
    # q1 who the listeners are (easy). q2 change: "Normally ... but today" (tasting moved to the end).
    # q3 next step: "Before we set off" (everyone's name on the sheet) comes before heading to storage; earplugs
    # belong to the third stop and the tasting is last; the key "Register their attendance" is a paraphrase.
    {
        "id": "l-talk-11", "type": "listen", "format": "talk", "unit": "talk-next", "level": 3,
        "source": "hand", "reviewed": True, "v": 2, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-11", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Welcome to the Alder Lane Roastery, everyone. I'm Marisol, and I'll be your guide for this 45-minute tour.",
                 "say": "Welcome to the Alder Lane Roastery, everyone. I'm Marisol, and I'll be your guide for this forty-five minute tour."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "Normally we begin with a tasting, but the tasting room is booked today, so we'll finish there instead."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "We'll follow the beans from storage to packing. The roasting room is our third stop, and it gets very loud."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Before we enter it, please take a pair of earplugs from the basket in the hallway."},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "Photos are welcome, but please turn off your flash. If you'd like to buy beans, our shop will open after the tasting."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "Before we set off, I need everyone's name on the visitor sheet. It's on the clipboard right here."},
                {"file": "07.mp3", "who": "W", "voice": "af_sarah", "text": "Once everyone's name is down, we'll head to the storage room."},
            ],
        },
        "transcriptZh": [
            "各位好，歡迎來到 Alder Lane 烘豆坊。我是 Marisol，這趟 45 分鐘的導覽由我帶領。",
            "通常我們從試喝開始，但試喝室今天已經被訂走，所以我們改在最後到那裡。",
            "我們會跟著咖啡豆從儲藏區一路走到包裝區。烘豆室是第三站，裡面非常吵。",
            "進去之前，請從走廊的籃子裡拿一副耳塞。",
            "歡迎拍照，但請關掉閃光燈。如果您想買咖啡豆，商店在試喝之後開放。",
            "出發之前，我需要每個人把名字寫在訪客登記表上，表就放在這裡的板夾上。",
            "大家的名字都寫好之後，我們就前往儲藏室。",
        ],
        "questions": [
            {
                "q": "Who most likely are the listeners?",
                "options": ["Employees of the roastery", "Visitors being shown around a workplace", "Coffee growers", "Shop customers"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "身分題：導覽加上買豆邀請，聽眾是訪客",
                    "why": "guide for this 45-minute tour，加上 If you'd like to buy beans → 是被帶著參觀、可能購買的訪客。",
                    "evidence": [0, 4],
                    "wrong": ["沒有依據：員工不會被邀請買咖啡豆", None, "沒有提到咖啡農", "同字陷阱：shop 出現，但店是參觀後才開放的選項"],
                    "wrongMore": ["新進員工也可能參加導覽；但後面說 If you'd like to buy beans, our shop will open，是對外來訪客說的。", None, None, None],
                    "vocab": [["roastery", "烘豆工坊"], ["guide", "導覽員"]],
                },
            },
            {
                "q": "What change does the speaker mention?",
                "options": ["The tour will begin with a tasting", "The tour will be shorter than usual", "The tasting will come later in the visit than usual", "The roasting room will be closed to visitors"],
                "answer": 2,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "變化題：Normally … but 後面才是新安排",
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
                "q": "What must the listeners do before the tour sets off?",
                "options": ["Collect ear protection", "Sample some coffee", "Go to the storage room", "Register their attendance"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "順序題：Before we set off 是眼前第一件事",
                    "why": "I need everyone's name on the visitor sheet → 先登記；Once … name is down 才去儲藏室。",
                    "evidence": [5, 6],
                    "wrong": ["順序錯置：耳塞是進第三站烘豆室之前才拿", "順序錯置：試喝排在最後", "順序錯置：去儲藏室要等名字寫完之後", None],
                    "wrongMore": [
                        "Before we enter it 的 it 是 the roasting room，也就是第三站；現在還沒出發，離拿耳塞還早。",
                        None,
                        "we'll head to the storage room 離得最近，所以很像；但 Once everyone's name is down 說明那是登記完之後的事。",
                        None,
                    ],
                    "vocab": [["set off", "出發"], ["visitor sheet", "訪客登記表"], ["earplugs", "耳塞"]],
                },
            },
        ],
    },
]
