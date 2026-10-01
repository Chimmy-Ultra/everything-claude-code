# Round 6 listening items (Part 3 style conversations), written under WRITING_RULES.md (sections 2, 3, 5, 6, 7.1).
# 8 conv sets, 3 questions each (24 questions): l-conv-11/12 conv-topic, 13/14 conv-detail (both with a graphic),
# 15/16 conv-intent (both with a quoted-sentence question), 17/18 conv-next. l-conv-12 and l-conv-16 have three
# named speakers. Scripts are in US English even when a British voice reads them. All content is original; names of
# people, firms, streets and cities are invented.
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` here is the highest
# self-test band in the item (easy 1, medium 2, hard 3).
# reviewed stays False until the items pass a blind review and every mp3 has been heard.
# Scenes (new against l-conv-01..10): bottling factory, university special collections, hotel room change,
# airport rebooking, cookbook cover at a publisher, restaurant seafood supply, physical-therapy clinic,
# city sidewalk-seating permit.
# Revision after the first blind review (24/24 matched the key, but the batch read as too easy): every opening
# question that was answered in the first line now has evidence across two turns or a mentioned-but-wrong option that
# passes a first listen; the endings were varied (no more "I'll ..." plus a rejected alternative in 11, 12, 15, 16).
# Self-test summary: easy 1 (l-conv-14 q1), medium 10, hard 13 (see ldbs on each question).
# Answer positions over the 24 questions: A 6, B 6, C 6, D 6.

ITEMS = [
    # ------------------------------------------------------------------ l-conv-11  conv-topic, factory
    # W = a supervisor (af_bella), M = Dev (bm_george). Nobody says "inspection" or "defect detection".
    # Q1 topic (C): assembled from lines 1-3 (returns + sampling + camera). Q2 detail (D): forty cracked bottles in a
    # test, it caught thirty-eight -> nearly all (A "every one" is the near-correct option). Q3 (A, second half): the
    # plant manager only reads it once the finance office has checked the numbers; "it" = the summary, "them" = finance.
    {
        "id": "l-conv-11", "type": "listen", "format": "conv", "unit": "conv-topic", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-11", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Dev, I read the report from our beverage distributor. Almost every returned case had bottles with hairline cracks."},
                {"file": "02.mp3", "who": "M", "voice": "bm_george", "text": "Our inspectors only pull a few bottles from each pallet, so a cracked one can easily slip through."},
                {"file": "03.mp3", "who": "W", "voice": "af_bella", "text": "A vendor told me a camera above the conveyor can look at every bottle as it passes and push the bad ones off the line."},
                {"file": "04.mp3", "who": "M", "voice": "bm_george", "text": "Every single bottle? At our line speed, I'd need to see that to believe it. Did they test it?"},
                {"file": "05.mp3", "who": "W", "voice": "af_bella", "text": "They ran forty of our own cracked bottles through a test rig last week. It caught thirty-eight."},
                {"file": "06.mp3", "who": "M", "voice": "bm_george", "text": "Impressive. But the price is steep, and the plant manager is already worried about this year's equipment budget."},
                {"file": "07.mp3", "who": "W", "voice": "af_bella", "text": "The returns cost us more in one year than the camera would. I can put the figures in a one-page summary."},
                {"file": "08.mp3", "who": "M", "voice": "bm_george", "text": "Do that. The plant manager won't look at it unless the finance office has checked the numbers first."},
                {"file": "09.mp3", "who": "W", "voice": "af_bella", "text": "Then I'll take it over to them first thing tomorrow."},
            ],
        },
        "transcriptZh": [
            "Dev，我讀了飲料經銷商的報告。幾乎每一箱退回的貨裡，都有瓶身出現細微裂縫的瓶子。",
            "我們的檢查員只從每個棧板上抽幾瓶來看，所以有裂縫的瓶子很容易漏掉。",
            "有家廠商告訴我，輸送帶上方的一台相機可以在每個瓶子經過時檢查，並把不良品推出生產線。",
            "每一瓶都檢查？以我們的產線速度，我得親眼看到才相信。他們有測試過嗎？",
            "他們上週拿四十瓶我們自己的裂瓶放進測試機台跑過。它抓到了三十八瓶。",
            "很厲害。但價格很高，而且廠長已經在擔心今年的設備預算了。",
            "一年下來，退貨讓我們損失的比這台相機還多。我可以把數字整理成一頁的摘要。",
            "照做。不過廠長要等財務室先核對過數字，才會看這份東西。",
            "那我明天一早就把它拿過去給他們。",
        ],
        "questions": [
            {
                "q": "What are the speakers mainly discussing?",
                "options": [
                    "Why a distributor has stopped ordering from the plant",
                    "How to get inspectors to check bottles more quickly",
                    "A way to catch damaged products before they leave the factory",
                    "Whether to slow the line to protect the bottles",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "主旨題：把問題和對策串起來",
                    "why": "第一句退回的貨有裂瓶是問題；第三句 a camera … push the bad ones off the line 是做法 → 合起來是出廠前找出受損產品。",
                    "evidence": [0, 1, 2],
                    "wrong": ["沒有人說經銷商停止下單，只提到退貨報告", "提到但不是問的：檢查員只抽查，沒說要訓練他們加快", None, "提到但不是問的：線速是男方的疑慮，沒人提議放慢"],
                    "wrongMore": [
                        None,
                        "inspectors 和 speed 都出現；但談的是抽檢會漏掉裂瓶、相機跟不跟得上產線，沒有人要檢查員檢查得更快。",
                        None,
                        "At our line speed 是男方懷疑相機跟不跟得上；他沒有提議放慢產線，女方也沒有。",
                    ],
                    "vocab": [["distributor", "經銷商"], ["pallet", "棧板"], ["conveyor", "輸送帶"]],
                },
            },
            {
                "q": "What does the woman say about the vendor's test?",
                "options": [
                    "It found every one of the cracked bottles",
                    "It missed roughly half of them",
                    "It slowed down the production line",
                    "Nearly all of the faulty bottles were found",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "數字題：四十瓶抓到三十八瓶",
                    "why": "forty cracked bottles … It caught thirty-eight → 兩個數字相比，幾乎全部找出來。",
                    "evidence": [3, 4],
                    "wrong": ["同字陷阱：every 出現過，但三十八瓶不是全部", "數字錯誤：只漏掉兩瓶，不是一半", "語境矛盾：測試結果沒有提到拖慢產線", None],
                    "wrongMore": [
                        "every bottle 是她描述相機能做到的事；但測試只抓到 forty 裡的 thirty-eight，還差兩瓶，不是每一瓶。",
                        None,
                        "At our line speed 是男方對速度的懷疑；但女方講測試結果時只給了瓶數，沒有提到產線變慢。",
                        None,
                    ],
                    "vocab": [["test rig", "測試機台"], ["vendor", "廠商"], ["faulty", "有瑕疵的"]],
                },
            },
            {
                "q": "What will the woman do tomorrow morning?",
                "options": [
                    "Bring her cost figures to a different department for checking",
                    "Present the proposal to the plant manager",
                    "Arrange a second test with the vendor",
                    "Ask the distributor for another report",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨句：it 和 them 要回頭找",
                    "why": "廠長 won't look at it unless the finance office has checked；她答 I'll take it over to them → 把摘要拿給財務室。",
                    "evidence": [6, 7, 8],
                    "wrong": [None, "順序錯置：廠長要等財務室核對後才會看", "沒有人提到第二次測試", "同字陷阱：經銷商的報告是她已經讀過的"],
                    "wrongMore": [
                        None,
                        "plant manager 是她最終要說服的對象；但男方說要先過財務室，她明天一早做的是把摘要拿給財務室。",
                        None,
                        "distributor 的報告是第一句她已經讀過的東西；她要拿去給別人的是自己整理的 summary。",
                    ],
                    "vocab": [["figures", "數字、金額"], ["finance office", "財務室"], ["steep", "（價格）很高"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-12  conv-topic, university, three speakers
    # W = Professor Lang (af_sarah, US), M1 = Joel, a graduate student (am_eric, US), M2 = Mr. Dunmore, a librarian
    # (bm_lewis, UK). Line 1 names Joel and Mr. Dunmore; Joel (line 2) and Mr. Dunmore (line 7) say "Professor Lang".
    # Q1 topic (B). Q2 (A): teaches until four thirty, reading room closes at five -> little time; (B) is the time trap.
    # Q3 (D, second half): Dunmore wants a letter, Lang asks Joel to draft it, Joel agrees; (C) "first draft" is the
    # same-word trap (his thesis draft).
    {
        "id": "l-conv-12", "type": "listen", "format": "conv", "unit": "conv-topic", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-12", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Joel, Mr. Dunmore, thanks for meeting with me. Joel's thesis depends on a set of nineteenth-century harbor maps in the library's special collections.",
                 "say": "Joel, Mister Dunmore, thanks for meeting with me. Joel's thesis depends on a set of nineteenth-century harbor maps in the library's special collections."},
                {"file": "02.mp3", "who": "M1", "voice": "am_eric", "text": "I need to compare them with modern charts, Professor Lang, but the reading room closes at five, and I teach until four thirty."},
                {"file": "03.mp3", "who": "M2", "voice": "bm_lewis", "text": "I'm afraid those maps are too delicate to photograph or take out of the building. That rule is firm."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Could the library scan them instead? Then Joel could study the images wherever he likes."},
                {"file": "05.mp3", "who": "M2", "voice": "bm_lewis", "text": "We do offer scanning, but the waiting list is about three weeks."},
                {"file": "06.mp3", "who": "M1", "voice": "am_eric", "text": "That's too long. My first draft is due in two weeks."},
                {"file": "07.mp3", "who": "M2", "voice": "bm_lewis", "text": "Then let me see what I can do, Professor Lang. I could move Joel up the list if you write a short letter of support."},
                {"file": "08.mp3", "who": "W", "voice": "af_sarah", "text": "Joel, could you draft it tonight? I'll sign it tomorrow morning, and then you can take it to Mr. Dunmore.",
                 "say": "Joel, could you draft it tonight? I'll sign it tomorrow morning, and then you can take it to Mister Dunmore."},
                {"file": "09.mp3", "who": "M1", "voice": "am_eric", "text": "Of course. I'll have it in your inbox before I go to bed."},
            ],
        },
        "transcriptZh": [
            "Joel、Dunmore 先生，謝謝你們來見我。Joel 的論文需要用到圖書館特藏室裡的一批十九世紀港口地圖。",
            "Lang 教授，我需要把它們和現代海圖比對，但閱覽室五點關門，而我教課教到四點半。",
            "恐怕那些地圖太脆弱了，不能拍照，也不能帶出館外。這是硬性規定。",
            "那圖書館能改用掃描嗎？這樣 Joel 就可以在任何他想去的地方研究影像。",
            "我們確實有掃描服務，但等候名單大約要三週。",
            "太久了。我的初稿兩週後就要交。",
            "那我來看看能怎麼辦，Lang 教授。如果您寫一封簡短的支持信，我可以把 Joel 往名單前面移。",
            "Joel，你今晚能起草嗎？我明天早上簽名，然後你再拿去給 Dunmore 先生。",
            "沒問題。我睡前就會把它放進您的收件匣。",
        ],
        "questions": [
            {
                "q": "What are the speakers mainly discussing?",
                "options": [
                    "Whether the library should extend its opening hours",
                    "How a student can study materials that cannot be borrowed",
                    "How to schedule a thesis presentation",
                    "Which research topic a student should choose",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "主旨題：問題加上解決辦法",
                    "why": "too delicate to … take out 是問題；scan them instead 是辦法 → 如何研究不能外借的資料。",
                    "evidence": [0, 2, 3],
                    "wrong": ["提到但不是問的：五點關門是 Joel 的困難，沒人提議延長", None, "同字陷阱：thesis 出現過，但沒人談簡報的時間", "沒有人談選題：Joel 的論文主題早已確定"],
                    "wrongMore": [
                        "the reading room closes at five 確實出現；但那只是 Joel 的困難，後面談的是改用掃描，沒有人提議延長開放時間。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["thesis", "學位論文"], ["special collections", "特藏室"], ["delicate", "脆弱的"]],
                },
            },
            {
                "q": "What problem does Joel have with using the reading room?",
                "options": [
                    "His teaching schedule leaves him little time there",
                    "It closes before his class ends",
                    "He has not been given permission to enter it",
                    "The modern charts are kept in a different building",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "推論題：兩個時間要自己算",
                    "why": "閱覽室 closes at five，他 teach until four thirty → 下課後只剩半小時，改述成教課讓他在那裡的時間很少。",
                    "evidence": [1],
                    "wrong": [None, "時間錯置：五點關門，他四點半就下課", "沒有人提到他沒有進入許可", "同字陷阱：modern charts 出現過，但沒說放在別處"],
                    "wrongMore": [
                        None,
                        "closes at five 和 teach until four thirty 兩個時間都聽到，容易湊成 closes before class ends；但四點半比五點早，下課後還有半小時。",
                        None,
                        None,
                    ],
                    "vocab": [["reading room", "閱覽室"], ["compare", "比對"]],
                },
            },
            {
                "q": "What does Joel agree to do?",
                "options": [
                    "Take photographs of the maps",
                    "Add his name to the waiting list",
                    "Hand in his first draft early",
                    "Write a letter for his professor to sign",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：it 指前面提到的信",
                    "why": "a short letter of support；Lang 說 Joel, could you draft it tonight?；Joel 答 Of course → 他寫信讓教授簽名。",
                    "evidence": [6, 7, 8],
                    "wrong": ["張冠李戴：館員說不能拍照，這是被禁止的事", "沒有人要 Joel 自己排名單；館員說的是把他往前移", "同字陷阱：draft 出現過，但 draft it 是起草那封信", None],
                    "wrongMore": [
                        "photograph 在第三句出現，但是館員說這些地圖不能拍；Joel 答應的是寫信，不是拍照。",
                        "the list 在 Dunmore 那句出現；但把 Joel 往前移是館員要做的，Joel 答應的是起草信。",
                        "My first draft 是 Joel 的論文初稿，兩週後才要交；Lang 說的 draft it 是起草支持信，沒有人要他提早交初稿。",
                        None,
                    ],
                    "vocab": [["letter of support", "支持信、推薦信"], ["waiting list", "等候名單"], ["draft", "起草"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-13  conv-detail, hotel, graphic (rates)
    # M = Mr. Hollis (am_michael), W = front-desk agent (bf_emma, UK). The audio never says a price or a room name.
    # Q2 needs three coordinates: Friday night (line 1 -> Fri-Sat column), two beds (line 4), no sitting area (line 5)
    # -> Family Room, Fri-Sat = $195. (B) $175 is the same room's Sun-Thu rate; (A) $140 / (D) $260 other rows.
    {
        "id": "l-conv-13", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "graphic": {
            "caption": "Lakeview Hotel — Nightly Room Rates",
            "head": ["Room", "Beds", "Sun–Thu", "Fri–Sat"],
            "rows": [
                ["Standard", "One queen bed", "$120", "$140"],
                ["Deluxe", "One king bed", "$150", "$170"],
                ["Family Room", "Two queen beds", "$175", "$195"],
                ["Executive Suite", "Two queen beds and a sitting area", "$230", "$260"],
            ],
        },
        "audio": {
            "dir": "audio/l-conv-13", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_michael", "text": "Hello, I have a reservation under Hollis for this Friday night, and I need to change the room."},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "Certainly, Mr. Hollis. At the moment you're in our least expensive room, with one queen bed.",
                 "say": "Certainly, Mister Hollis. At the moment you're in our least expensive room, with one queen bed."},
                {"file": "03.mp3", "who": "M", "voice": "am_michael", "text": "Right. My wife and our daughter are coming along after all."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "Then you'll want more than one bed. Two of our rooms have two beds. One of them also comes with a separate sitting area."},
                {"file": "05.mp3", "who": "M", "voice": "am_michael", "text": "We don't need that. Last time we had one, we never used it, and it pushed the price up."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "Then I'll put you in the other one. It's on a quiet corridor, away from the elevators."},
                {"file": "07.mp3", "who": "M", "voice": "am_michael", "text": "Perfect. One more thing: our flight lands at noon. Could we check in before the usual three o'clock?"},
                {"file": "08.mp3", "who": "W", "voice": "bf_emma", "text": "I can't promise that. If housekeeping finishes early, I'll text you. Otherwise, we can keep your bags at the desk until three."},
                {"file": "09.mp3", "who": "M", "voice": "am_michael", "text": "That works. Thanks for your help."},
            ],
        },
        "transcriptZh": [
            "你好，我用 Hollis 這個名字訂了這個星期五晚上的房間，我需要換房。",
            "沒問題，Hollis 先生。您目前訂的是我們最便宜的房間，一張大床。",
            "對。我太太和女兒後來決定一起來了。",
            "那您會需要不只一張床。我們有兩種房型有兩張床。其中一種還附一個獨立的起居區。",
            "我們不需要那個。上次住過附起居區的，我們從沒用到，卻讓房價變貴。",
            "那我幫您安排另外那一種。它在安靜的走廊上，離電梯很遠。",
            "太好了。還有一件事：我們的班機中午降落。能不能在平常的三點之前入住？",
            "我不能保證。如果房務提早打掃完，我會傳簡訊給您。否則我們可以把您的行李寄放在櫃檯到三點。",
            "好的。謝謝你的幫忙。",
        ],
        "questions": [
            {
                "q": "Why does the man want to change his reservation?",
                "options": [
                    "He wants to pay less per night",
                    "More guests will be traveling with him",
                    "He would like a quieter location",
                    "His flight now arrives earlier than planned",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "原因題：理由要從兩句接起來",
                    "why": "coming along after all；接 Then you'll want more than one bed → 同行的人變多，所以換房。",
                    "evidence": [2, 3],
                    "wrong": ["提到但不是問的：價格是他不要起居區的理由", None, "提到但不是問的：安靜是女方介紹新房間的描述", "沒有人說班機提早：只說中午降落，想早點入住"],
                    "wrongMore": [
                        "it pushed the price up 是他不要起居區的理由，不是他換房的原因；他換房是因為家人加入。",
                        None,
                        "quiet corridor 是女方介紹新房間的特色，在他決定換房之後才出現。",
                        None,
                    ],
                    "vocab": [["reservation", "訂房"], ["coming along", "一起來"]],
                },
            },
            {
                "q": "Look at the graphic. How much will the man pay for his room on Friday night?",
                "options": ["$140", "$175", "$195", "$260"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：房型和日期兩個座標",
                    "why": "要兩張床但不要 a separate sitting area → Family Room；入住是 this Friday night，要看 Fri–Sat 欄 → $195。",
                    "evidence": [0, 3, 4, 5],
                    "wrong": ["Standard 的星期五價格：只有一張床", "Family Room 的平日價；他住星期五晚上", None, "Executive Suite 的週末價：附起居區，他不要"],
                    "wrongMore": [
                        None,
                        "房型選對了，這是最容易選的數字；但 Sun–Thu 是平日價，他訂的是 this Friday night，要用 Fri–Sat 那一欄。",
                        None,
                        "Executive Suite 也有兩張床；但他說 We don't need that，指的就是它附的起居區。",
                    ],
                    "vocab": [["sitting area", "起居區"], ["rate", "房價、費率"]],
                },
            },
            {
                "q": "What will the hotel do if the room is ready before three o'clock?",
                "options": [
                    "Let the guest know right away",
                    "Charge an additional fee",
                    "Hold the family's luggage at the front desk",
                    "Offer the family a larger room",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "條件句：If … 後面接要做的事",
                    "why": "她說 If housekeeping finishes early, I'll text you → 房間提早好就傳簡訊，改述成馬上通知客人。",
                    "evidence": [6, 7],
                    "wrong": [None, "沒有人提到加收費用", "條件相反：行李寄放是房間還沒好的做法（Otherwise）", "沒有人提到換更大的房間"],
                    "wrongMore": [
                        None,
                        None,
                        "keep your bags at the desk 確實出現；但它接在 Otherwise 後面，是房間沒提早好時的做法。",
                        None,
                    ],
                    "vocab": [["housekeeping", "房務"], ["check in", "辦理入住"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-14  conv-detail, airport, graphic (departures)
    # M = traveler (am_michael), W = airline agent (af_sarah). The audio never says a flight number, a gate, or the
    # arrival time of the answer flight. Coordinates: the two-thirty is full; the last flight to Lakeport lands too
    # late; the one between them (4:50, lands 6:35) is the only one that gets him in by seven -> Gate C3.
    # (A) B12 = the full flight; (C) A7 = the flight in between that goes to the other city; (D) B9 = the last flight.
    # Q3 (C): his bag is checked through (line 5), he has no time for baggage claim (line 7), the baggage team will
    # handle it (line 8) -> staff move it to the new flight; (A) collect it is the option he rules out.
    {
        "id": "l-conv-14", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "us",
        "graphic": {
            "caption": "Afternoon and Evening Departures",
            "head": ["Flight", "Destination", "Departs", "Arrives", "Gate"],
            "rows": [
                ["512", "Lakeport", "2:30 P.M.", "4:15 P.M.", "B12"],
                ["640", "Northgate", "3:10 P.M.", "5:20 P.M.", "A7"],
                ["655", "Lakeport", "4:50 P.M.", "6:35 P.M.", "C3"],
                ["719", "Lakeport", "6:20 P.M.", "8:05 P.M.", "B9"],
            ],
        },
        "audio": {
            "dir": "audio/l-conv-14", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_michael", "text": "Excuse me, my first flight sat on the runway for an hour, so I missed my connection to Lakeport."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "I'm sorry about that, sir. The next Lakeport flight leaves at two thirty, but it's completely full."},
                {"file": "03.mp3", "who": "M", "voice": "am_michael", "text": "What are my other options? I have a client dinner at seven thirty, and the restaurant is half an hour from the airport."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Then you'll need to land by seven. The last flight to Lakeport gets in too late, but there's one between it and the two thirty."},
                {"file": "05.mp3", "who": "M", "voice": "am_michael", "text": "Is there still a seat on that one? My suitcase is checked all the way through to Lakeport."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "Yes, I'll put you on it now."},
                {"file": "07.mp3", "who": "M", "voice": "am_michael", "text": "And my bag? I don't have time to go to baggage claim and check it in again."},
                {"file": "08.mp3", "who": "W", "voice": "af_sarah", "text": "You won't have to. Our baggage team will handle it from here."},
                {"file": "09.mp3", "who": "M", "voice": "am_michael", "text": "That's a relief. Do I need to do anything else?"},
                {"file": "10.mp3", "who": "W", "voice": "af_sarah", "text": "Just head to the gate. I'm printing your new boarding pass now."},
            ],
        },
        "transcriptZh": [
            "不好意思，我的第一班飛機在跑道上等了一個小時，所以我錯過了飛往 Lakeport 的轉機。",
            "真抱歉，先生。下一班到 Lakeport 的飛機兩點半起飛，但已經完全客滿。",
            "那我還有什麼選擇？我七點半有客戶晚餐，餐廳離機場半小時車程。",
            "那您必須在七點以前降落。最後一班到 Lakeport 的飛機太晚到，不過在它和兩點半那班之間還有一班。",
            "那一班還有位子嗎？我的行李已經一路託運到 Lakeport 了。",
            "有，我現在就幫您劃位。",
            "那我的行李呢？我沒有時間去行李提領處再重新託運一次。",
            "您不用這麼做。我們的行李組會從這裡接手處理。",
            "那真是鬆了一口氣。我還需要做什麼嗎？",
            "直接去登機門就好。我正在列印您的新登機證。",
        ],
        "questions": [
            {
                "q": "Why is the man at the service desk?",
                "options": [
                    "His checked bag has been lost",
                    "His flight was canceled because of weather",
                    "He wants to change his dinner plans",
                    "A delay made him unable to board his next flight",
                ],
                "answer": 3,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "原因題：開頭的問題就是答案",
                    "why": "sat on the runway for an hour, so I missed my connection → 前一班延誤，沒趕上下一班。",
                    "evidence": [0],
                    "wrong": ["沒有人說行李遺失：行李的事只談怎麼轉運", "沒有人提到天氣或取消：是延誤造成錯過轉機", "晚餐是他選班機的限制，不是來櫃檯的原因", None],
                    "wrongMore": [None, None, None, None],
                    "vocab": [["connection", "轉機班次"], ["runway", "跑道"]],
                },
            },
            {
                "q": "Look at the graphic. Which gate will the man most likely go to?",
                "options": ["B12", "C3", "A7", "B9"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "圖表題：先刪客滿和太晚的，再看降落時間",
                    "why": "兩點半那班客滿；最後一班太晚到；中間還有一班（往 Lakeport 的 4:50，6:35 降落，趕得上七點）→ 表上的 Gate C3。",
                    "evidence": [1, 2, 3],
                    "wrong": ["同字陷阱：兩點半那班就是客滿的那班", None, "中間那班飛 Northgate，不是 Lakeport", "最後一班八點多才降落，趕不上七點"],
                    "wrongMore": [
                        "女方先提到 two thirty，所以很容易直接選那一行；但她同一句就說 it's completely full。",
                        None,
                        "表上兩點半和最後一班之間確實有一班，但它飛往 Northgate；男方要去的是 Lakeport。",
                        "The last flight … gets in too late：它 8:05 才降落，他要在七點以前到。",
                    ],
                    "vocab": [["land", "降落"], ["gate", "登機門"]],
                },
            },
            {
                "q": "What will happen to the man's suitcase?",
                "options": [
                    "He will need to collect it at baggage claim first",
                    "It will wait at the service desk until he returns",
                    "Airline staff will move it to his new flight",
                    "It will be delivered to the restaurant by courier",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨句推論：他的疑慮加上她的保證",
                    "why": "他沒時間 go to baggage claim；她說 Our baggage team will handle it → 地勤把行李轉到新班機。",
                    "evidence": [4, 6, 7],
                    "wrong": ["方向相反：他沒時間去提領行李，她說不用", "沒有人提到把行李放在櫃檯等他", None, "沒有人提到把行李送到餐廳"],
                    "wrongMore": [
                        "baggage claim 是男方提到、而且是他不想做的事；女方回 You won't have to，所以不用先去領。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["baggage claim", "行李提領處"], ["handle", "處理"], ["boarding pass", "登機證"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-15  conv-intent, publishing
    # W = editor (af_sarah), M = Marcus, the cover designer (bm_lewis). Q1 (A): Marcus guesses a typo (wrong), she says it
    # is not that; the subtitle sounds wrong for her readers. Q2 quote: "That's a tall order." = hard to do; (A) is the
    # literal reading, (B) contradicts "takes me an hour". Q3 (B): he gives the cost, she says it depends on whether
    # the author pays the fee.
    {
        "id": "l-conv-15", "type": "listen", "format": "conv", "unit": "conv-intent", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-15", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Marcus, do you have a minute? The author just e-mailed me about the cookbook cover."},
                {"file": "02.mp3", "who": "M", "voice": "bm_lewis", "text": "Did she find a typo? The proofs were approved on Monday."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "No, it's nothing like that. She thinks the current subtitle sounds like it's written for professional chefs, and her readers are home cooks."},
                {"file": "04.mp3", "who": "M", "voice": "bm_lewis", "text": "That's what the sales team requested, though. And the cover files are supposed to reach the printer on Thursday."},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "Could you make the change and still have the files ready by Thursday?"},
                {"file": "06.mp3", "who": "M", "voice": "bm_lewis", "text": "That's a tall order. Changing the words takes me an hour, but the printer charges a fee for any change after the proofs are approved."},
                {"file": "07.mp3", "who": "W", "voice": "af_sarah", "text": "How big is the fee?"},
                {"file": "08.mp3", "who": "M", "voice": "bm_lewis", "text": "Four hundred dollars, plus an extra day on the schedule."},
                {"file": "09.mp3", "who": "W", "voice": "af_sarah", "text": "Then it depends on the author. If she pays the fee herself, we'll go ahead. If not, the cover stays as it is."},
            ],
        },
        "transcriptZh": [
            "Marcus，你有空嗎？作者剛寄電子郵件給我，是關於食譜書的封面。",
            "她發現錯字了嗎？樣稿星期一已經核可了。",
            "不是，跟那個無關。她覺得現在的副標題聽起來像是寫給專業廚師的，但她的讀者是家庭料理的人。",
            "可是那是業務團隊要求的。而且封面檔案應該星期四送到印刷廠。",
            "你能改好，又還能在星期四前把檔案準備好嗎？",
            "那要求太高了。改字我一個小時就能完成，但印刷廠對樣稿核可後的任何更動都要收費。",
            "費用多少？",
            "四百美元，再加上行程多一天。",
            "那就要看作者了。如果她自己付這筆費用，我們就照辦。如果不付，封面就維持原樣。",
        ],
        "questions": [
            {
                "q": "Why did the author contact the woman?",
                "options": [
                    "She is not satisfied with how the cover presents the book",
                    "She noticed an error in the proofs",
                    "She wants to meet the sales team",
                    "She would like to postpone the printing date",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：第二句的猜測被第三句否定",
                    "why": "猜 a typo 被 No, it's nothing like that 否定；副標題 written for professional chefs → 作者不滿意封面呈現方式。",
                    "evidence": [0, 1, 2],
                    "wrong": [None, "提到但不是問的：錯字是男方的猜測，被女方否定", "沒有人提到作者要見業務團隊", "沒有人提到延後印刷：星期四是檔案的期限"],
                    "wrongMore": [
                        None,
                        "typo 和 proofs 都出現；但 Did she find a typo 只是男方的猜測，女方馬上說 No, it's nothing like that。",
                        None,
                        None,
                    ],
                    "vocab": [["typo", "錯字"], ["proofs", "樣稿"], ["subtitle", "副標題"]],
                },
            },
            {
                "q": "What does the man mean when he says, \"That's a tall order\"?",
                "options": [
                    "The printer's order is unusually large",
                    "The change cannot be finished in an hour",
                    "The request will be hard to fulfill",
                    "The sales team will refuse the new subtitle",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：tall order 是「很難辦到」",
                    "why": "她問能否改完又趕上星期四；他答 That's a tall order，再說要收費 → 這個要求很難辦到。",
                    "evidence": [4, 5],
                    "wrong": ["字面陷阱：照字面把 order 讀成訂單量", "語境矛盾：他說改字只要一個小時", None, "沒有人說業務團隊會拒絕"],
                    "wrongMore": [
                        "order 照字面可以是「訂單」；但 a tall order 是慣用語，指難以達成的要求，後面他也在說費用和日程的問題。",
                        "an hour 確實在下一句出現；但他說的是 Changing the words takes me an hour，改字很快，難處在費用。",
                        None,
                        "sales team 在前一句出現，但那是說副標題原本是業務要的；他沒有說業務會拒絕新的。",
                    ],
                    "vocab": [["tall order", "很難達成的要求"], ["fee", "費用"]],
                },
            },
            {
                "q": "According to the woman, what will decide whether the cover is changed?",
                "options": [
                    "Whether the sales team approves the new wording",
                    "Whether the author is willing to cover the charge",
                    "Whether the printer can finish a day early",
                    "Whether the man can finish the new cover by Thursday",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：他報費用，她把決定交給作者",
                    "why": "Four hundred dollars；她答 it depends on the author. If she pays the fee herself → 看作者肯不肯付費。",
                    "evidence": [5, 7, 8],
                    "wrong": ["提到但不是問的：業務團隊是副標題原本的來源，沒說由它決定", None, "提到但不是問的：多一天是代價，她沒說要印刷廠提早", "提到但不是問的：星期四是原本的期限，她沒說由它決定"],
                    "wrongMore": [
                        "sales team 出現在前面；但女方說 it depends on the author，決定權不在業務團隊。",
                        None,
                        "an extra day 是男方列出的代價之一；女方沒有談印刷廠能否提早，她把決定交給作者付不付費用。",
                        "by Thursday 是原本的期限；女方說的是 If she pays the fee herself，條件是作者付費，不是男方趕不趕得上。",
                    ],
                    "vocab": [["depend on", "取決於"], ["go ahead", "照辦、繼續進行"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-16  conv-intent, restaurant, three speakers
    # W = Elena, the manager (af_bella, US), M1 = Gus, the chef (bm_george, UK), M2 = Theo, a server (am_michael, US).
    # Elena names both men in line 1; Gus and Theo name her (lines 2-3); Elena names Gus in line 4; Theo names Gus in line 6.
    # Gus names Theo in line 8 and Theo names Gus in line 9.
    # Q2 quote: "put all our eggs in one basket" = relying on one supplier is risky; (A) is the literal reading.
    # Q3 (C): Gus needs weekend booking numbers early in the week; Theo says he will give the count every Tuesday.
    {
        "id": "l-conv-16", "type": "listen", "format": "conv", "unit": "conv-intent", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-16", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_bella", "text": "Gus, Theo, thanks for staying after the lunch rush. The seafood supplier called again; half of today's fish never arrived."},
                {"file": "02.mp3", "who": "M1", "voice": "bm_george", "text": "That's the second short delivery this month, Elena. And tonight's special is the grilled sea bass."},
                {"file": "03.mp3", "who": "M2", "voice": "am_michael", "text": "Should I stop recommending it to tables, Elena? I've already told a few reservations about it."},
                {"file": "04.mp3", "who": "W", "voice": "af_bella", "text": "Keep mentioning it, but tell guests it's limited. Gus, how many portions can you cover?"},
                {"file": "05.mp3", "who": "M1", "voice": "bm_george", "text": "Fourteen. To avoid this in future, I'd move all our seafood orders to Harbor Fresh. They're cheaper, and they've never been late with us."},
                {"file": "06.mp3", "who": "M2", "voice": "am_michael", "text": "Hmm. Gus, I'd hate to put all our eggs in one basket. If they have one bad week, we have no fish at all."},
                {"file": "07.mp3", "who": "W", "voice": "af_bella", "text": "Theo has a point. Gus, what if we keep both suppliers and split the order, about sixty and forty?"},
                {"file": "08.mp3", "who": "M1", "voice": "bm_george", "text": "Fine by me. But I'll have to order two days ahead, so I'll need your weekend reservation numbers early in the week, Theo."},
                {"file": "09.mp3", "who": "M2", "voice": "am_michael", "text": "No problem. I'll give you the count every Tuesday morning, Gus."},
            ],
        },
        "transcriptZh": [
            "Gus、Theo，謝謝你們在午餐尖峰後留下來。海鮮供應商又打來了；今天的魚有一半沒送到。",
            "Elena，這個月已經是第二次短缺了。而且今晚的特餐是烤鱸魚。",
            "Elena，我該不該不要再向各桌推薦它了？我已經跟幾組訂位的客人提過了。",
            "繼續推薦，但要告訴客人數量有限。Gus，你能做幾份？",
            "十四份。為了以後避免這種事，我會把所有海鮮訂單都改給 Harbor Fresh。他們比較便宜，而且對我們從來沒有遲到過。",
            "嗯。Gus，我不想把所有的雞蛋放在同一個籃子裡。如果他們有一週出狀況，我們就完全沒有魚了。",
            "Theo 說得有道理。Gus，如果我們兩家供應商都留著，把訂單大約六四分，怎麼樣？",
            "我沒意見。但我得提前兩天下單，所以 Theo，我需要你在每週初給我週末的訂位人數。",
            "沒問題。Gus，我每週二早上會把數字給你。",
        ],
        "questions": [
            {
                "q": "What problem does Elena mention at the beginning?",
                "options": [
                    "A delivery arrived late again",
                    "Several guests complained about the sea bass",
                    "The kitchen ran out of fish during lunch",
                    "Only part of an order was delivered",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "問題題：第一句就是問題，不是遲到",
                    "why": "她說 half of today's fish never arrived → 魚只送來一半，改述成訂單只送到一部分。",
                    "evidence": [0],
                    "wrong": ["同字陷阱：late 是 Gus 稱讚 Harbor Fresh 的話", "沒有人提到客人抱怨：客人只是被告知數量有限", "沒有人說午餐時魚賣完：問題是魚根本沒送來", None],
                    "wrongMore": [
                        "never been late 是 Gus 說 Harbor Fresh 的優點；Elena 說的是 half of today's fish never arrived，是沒送到，不是晚到。",
                        None,
                        "lunch rush 出現在她的第一句；但她說的是 half of today's fish never arrived，不是午餐時賣完。",
                        None,
                    ],
                    "vocab": [["supplier", "供應商"], ["lunch rush", "午餐尖峰"]],
                },
            },
            {
                "q": "What does Theo mean when he says, \"I'd hate to put all our eggs in one basket\"?",
                "options": [
                    "He wants the kitchen to buy more eggs",
                    "Depending on a single company could cause trouble",
                    "He thinks Harbor Fresh charges too much",
                    "He doubts the kitchen can serve fourteen portions",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：eggs in one basket 是不要只靠一個",
                    "why": "Gus 要 move all our seafood orders；Theo 說 one bad week, we have no fish → 只靠一家有風險。",
                    "evidence": [4, 5],
                    "wrong": ["字面陷阱：照字面讀成要買更多雞蛋", None, "語境矛盾：Gus 說 Harbor Fresh 比較便宜", "提到但不是問的：十四份是 Gus 回答今晚能做的量"],
                    "wrongMore": [
                        "eggs 和 basket 照字面是雞蛋與籃子；但這是慣用語，Theo 在說的是把鮮魚全押在一家供應商身上。",
                        None,
                        "價格是 Gus 支持 Harbor Fresh 的理由（They're cheaper）；Theo 擔心的是萬一他們出狀況，沒有魚可賣。",
                        "Fourteen 是 Gus 前一句回答今晚能做幾份；Theo 的話是針對 all our seafood orders 只給一家，不是質疑份數。",
                    ],
                    "vocab": [["put all our eggs in one basket", "孤注一擲、把風險放在同一處"], ["supplier", "供應商"]],
                },
            },
            {
                "q": "What does Theo agree to give Gus?",
                "options": [
                    "A revised menu for the weekend",
                    "Prices from both suppliers",
                    "A weekly update on expected guest numbers",
                    "A plan for dividing the order between suppliers",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：誰提出需求、誰答應",
                    "why": "Gus 要 weekend reservation numbers early in the week；Theo 答 every Tuesday morning → 每週提供客人數。",
                    "evidence": [7, 8],
                    "wrong": ["沒有人提到週末菜單", "提到但不是問的：價格是 Gus 支持 Harbor Fresh 的理由", None, "張冠李戴：兩家分單的方案是 Elena 提的"],
                    "wrongMore": [
                        None,
                        "cheaper 在 Gus 的第五句出現；但 Theo 答應的是 count，不是供應商的報價。",
                        None,
                        "split the order 是 Elena 在上一輪提出的做法；Theo 答應的是提供訂位人數，不是提供分單計畫。",
                    ],
                    "vocab": [["reservation", "訂位"], ["split", "分配、分攤"], ["portion", "一份（餐點）"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-17  conv-next, physical-therapy clinic
    # M = Paul Greer (am_eric), W = receptionist (bf_emma, UK). Q1 (C): car goes into the shop -> his vehicle is unavailable;
    # (B) coverage running out is true but is not why he asks to move it. Q2 (A): five of six used -> Thursday's is the last
    # covered. Q3 (D): the woman offers mail or fax; he rejects mail, says the doctor's office closes at five and he'd
    # better hurry -> he will contact his physician's office.
    {
        "id": "l-conv-17", "type": "listen", "format": "conv", "unit": "conv-next", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-17", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "am_eric", "text": "Hi, this is Paul Greer. I have a physical therapy session on Tuesday at nine, but my car goes into the shop that morning."},
                {"file": "02.mp3", "who": "W", "voice": "bf_emma", "text": "Hello, Mr. Greer. Wednesday is full, but Thursday afternoon has openings. Would two o'clock work?",
                 "say": "Hello, Mister Greer. Wednesday is full, but Thursday afternoon has openings. Would two o'clock work?"},
                {"file": "03.mp3", "who": "M", "voice": "am_eric", "text": "It would. Will my insurance cover it? I've already used five of the six visits my plan allows."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "Yes, that one is covered. It will be your last, though."},
                {"file": "05.mp3", "who": "M", "voice": "am_eric", "text": "My knee still isn't right, so I'd like to book three more visits now."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "I can't until we get a new referral from your doctor. I can mail you the form, or the doctor's office can fax it directly."},
                {"file": "07.mp3", "who": "M", "voice": "am_eric", "text": "Mail would take too long. The doctor's office closes at five, so I'd better hurry."},
                {"file": "08.mp3", "who": "W", "voice": "bf_emma", "text": "Good idea. Give them our fax number, and your Thursday time will be held for you."},
                {"file": "09.mp3", "who": "M", "voice": "am_eric", "text": "I will. Thanks for your help."},
            ],
        },
        "transcriptZh": [
            "你好，我是 Paul Greer。我星期二九點有一堂物理治療，但那天早上我的車要送修。",
            "您好，Greer 先生。星期三已經滿了，但星期四下午還有空檔。兩點可以嗎？",
            "可以。我的保險會給付嗎？我已經用掉保單允許的六次裡的五次了。",
            "會，那一次有給付。不過那會是您的最後一次。",
            "我的膝蓋還是沒好，所以我想現在再預約三次。",
            "在收到您醫師開的新轉診單之前不行。我可以把表格郵寄給您，或者讓醫師的診所直接傳真過來。",
            "郵寄會太久。醫師的診所五點關門，所以我最好趕快。",
            "好主意。把我們的傳真號碼給他們，您星期四的時段會替您保留。",
            "我會的。謝謝你的幫忙。",
        ],
        "questions": [
            {
                "q": "Why does the man ask to change his appointment?",
                "options": [
                    "His therapist is unavailable on Tuesday",
                    "His insurance coverage is about to run out",
                    "His vehicle will be unavailable that morning",
                    "His knee has already healed",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "原因題：說法換掉，car → vehicle",
                    "why": "他說 my car goes into the shop that morning → 那天早上沒有車，改述成交通工具那天早上用不了。",
                    "evidence": [0],
                    "wrong": ["沒有人說治療師不在：星期三才是客滿", "提到但不是問的：保險快用完是後面才談的事", None, "方向相反：他說膝蓋還沒好"],
                    "wrongMore": [
                        "Wednesday is full 在女方第二句出現；但客滿的是診所的星期三時段，沒有人說治療師星期二不在。",
                        "five of the six visits 和 your last 確實在後面出現；但他是因為車要送修才改期，保險是改期之後才問的。",
                        None,
                        None,
                    ],
                    "vocab": [["physical therapy", "物理治療"], ["session", "（一次）療程"]],
                },
            },
            {
                "q": "What does the woman say about the Thursday session?",
                "options": [
                    "It is the last one his insurance will pay for",
                    "It cannot be booked until a new referral arrives",
                    "It will be held in the morning",
                    "He will have to pay for it himself",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "細節題：this one = 星期四那次",
                    "why": "已用五次；她答 that one is covered. It will be your last → 星期四是最後給付的一次。",
                    "evidence": [2, 3],
                    "wrong": [None, "提到但不是問的：轉診單是之後再預約三次才需要", "時間錯置：她提的是 Thursday afternoon，兩點", "方向相反：她說這一次有給付"],
                    "wrongMore": [
                        None,
                        "referral 確實出現；但她說要等新轉診單才能預約的是之後那三次，星期四這一次已經有給付、也已替他保留。",
                        None,
                        None,
                    ],
                    "vocab": [["cover", "（保險）給付"], ["plan", "保險方案"]],
                },
            },
            {
                "q": "What will the man most likely do next?",
                "options": [
                    "Wait for a form to arrive in the mail",
                    "Visit the clinic to sign a form",
                    "Reschedule his appointment for Wednesday",
                    "Get in touch with his physician's office",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "下一步題：被否決的選項不是下一步",
                    "why": "他說 Mail would take too long，診所 closes at five, so I'd better hurry → 趕快聯絡醫師診所。",
                    "evidence": [5, 6, 7],
                    "wrong": ["方向相反：郵寄的選項被他以太慢否決", "沒有人提到要去診所簽名", "時間錯置：星期三已經客滿", None],
                    "wrongMore": [
                        "I can mail you the form 是女方提的辦法；但他說 Mail would take too long，沒有採用。",
                        None,
                        "Wednesday is full 是女方改約星期四的原因，他已經同意星期四。",
                        None,
                    ],
                    "vocab": [["referral", "轉診單"], ["fax", "傳真"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ l-conv-18  conv-next, city sidewalk-seating permit
    # M = café owner (bm_george), W = permit clerk (af_sarah). Q1 (B): purpose; "same word" trap (A) sidewalk.
    # Q2 (D): "Will four tables fit?" -> she cannot say; if fewer fit he can go ahead with fewer or withdraw for a refund
    # -> the choice is his. Q3 (A): he asks about cards (and offers a bank for cash), she says cards are fine and the form
    # needs a drawing, he has the building plans in his car and will bring them in -> fetches a document.
    {
        "id": "l-conv-18", "type": "listen", "format": "conv", "unit": "conv-next", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-18", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "M", "voice": "bm_george", "text": "Good morning. I own a café on Pine Street, and I'd like to put four tables on the sidewalk this summer."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "Then you'll need an outdoor seating permit. I can start the application for you right now."},
                {"file": "03.mp3", "who": "M", "voice": "bm_george", "text": "Wonderful. How long does it take?"},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "About three weeks. First an inspector measures the sidewalk, because five feet must stay clear for people walking by."},
                {"file": "05.mp3", "who": "M", "voice": "bm_george", "text": "My sidewalk is pretty narrow, to be honest. Will four tables fit?"},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "I can't say until the inspector measures. If fewer fit, you can go ahead with fewer, or withdraw and get your fee back."},
                {"file": "07.mp3", "who": "M", "voice": "bm_george", "text": "Fair enough. I'll apply. Do you take cards, or should I go to the bank for cash?"},
                {"file": "08.mp3", "who": "W", "voice": "af_sarah", "text": "Cards are fine at the counter. The form also needs a drawing of the sidewalk showing your door and the tree out front."},
                {"file": "09.mp3", "who": "M", "voice": "bm_george", "text": "I have the building plans in my car. I'll bring them in and be right back."},
            ],
        },
        "transcriptZh": [
            "早安。我在 Pine 街開了一間咖啡館，今年夏天想在人行道上擺四張桌子。",
            "那您需要申請戶外座位許可。我現在就可以幫您開始辦理申請。",
            "太好了。要花多久時間？",
            "大約三週。首先會有檢查員來丈量人行道，因為必須留五英尺的空間給路過的行人。",
            "老實說，我那邊的人行道滿窄的。四張桌子放得下嗎？",
            "在檢查員丈量之前我沒辦法說。如果放不下那麼多，您可以少放幾張繼續辦，也可以撤回申請並拿回費用。",
            "有道理。我來申請。你們收信用卡嗎？還是我該先去銀行領現金？",
            "櫃檯可以刷卡。表格還需要一張人行道的圖，標示出您的店門和門前那棵樹。",
            "我車上有建築平面圖。我把它們拿進來，馬上回來。",
        ],
        "questions": [
            {
                "q": "Why has the man come to the office?",
                "options": [
                    "To report a damaged sidewalk",
                    "To ask for permission to serve customers outdoors",
                    "To renew his café's business license",
                    "To complain about foot traffic",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：做法改述成目的",
                    "why": "他說想 put four tables on the sidewalk，女方說要 an outdoor seating permit → 改述成申請在戶外招待客人。",
                    "evidence": [0, 1],
                    "wrong": ["同字陷阱：sidewalk 出現過，但他沒有說人行道壞了", None, "沒有人提到續辦營業執照", "沒有人抱怨人潮"],
                    "wrongMore": [
                        "sidewalk 是他第一句的字；但他是要把桌子擺在人行道上，不是回報人行道損壞。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["permit", "許可證"], ["sidewalk", "人行道"]],
                },
            },
            {
                "q": "What does the woman say will happen if fewer than four tables fit?",
                "options": [
                    "The application will be refused",
                    "A higher fee will apply",
                    "The permit will take longer to process",
                    "He will be able to decide whether to go ahead",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "條件句：If … 後面有兩個選擇",
                    "why": "Will four tables fit；她答 go ahead with fewer, or withdraw and get your fee back → 由他決定。",
                    "evidence": [4, 5],
                    "wrong": ["方向相反：她說他可以選擇繼續，不是被拒絕", "同字陷阱：fee 出現過，但是退費，不是加收", "沒有人說放不下會拖長時間：三週是一般的時間", None],
                    "wrongMore": [
                        "refused 聽起來像放不下的合理後果；但她說的是 you can go ahead with fewer，少放幾張也能繼續辦。",
                        "fee 確實在她那句出現；但那是 get your fee back，退費，不是多收。",
                        None,
                        None,
                    ],
                    "vocab": [["withdraw", "撤回"], ["go ahead", "繼續進行"]],
                },
            },
            {
                "q": "What will the man most likely do next?",
                "options": [
                    "Get a document from his vehicle",
                    "Go to a bank for cash",
                    "Measure the sidewalk himself",
                    "Withdraw his application",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "下一步題：「馬上回來」交代接下來做什麼",
                    "why": "表格要 a drawing；他說 the building plans in my car. I'll bring them in → 先去車上拿文件。",
                    "evidence": [6, 7, 8],
                    "wrong": [None, "方向相反：他問過要不要去銀行，女方說櫃檯可以刷卡", "沒有人說他要自己丈量：丈量是檢查員的工作", "沒有人要撤回：他說 I'll apply"],
                    "wrongMore": [
                        None,
                        "should I go to the bank for cash 是他的問題；但女方回 Cards are fine at the counter，所以不用去銀行，他緊接著說的是去拿平面圖。",
                        None,
                        "withdraw 是女方說放不下四張時的選項；他一開始就說 I'll apply，也沒說要撤回。",
                    ],
                    "vocab": [["building plans", "建築平面圖"], ["withdraw", "撤回"]],
                },
            },
        ],
    },
]
