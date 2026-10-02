# Round 7 reading items (Part 7 triple passages), written under WRITING_RULES.md (sections 0, 3, 4, 6, 8).
# 3 p7t sets, 5 questions each (15 questions): r-p7-01 conference schedule + registration change,
# r-p7-02 office-furniture order with a back-ordered chair, r-p7-03 job advertisement + interview arrangements.
# Each set has one purpose question, one "closest in meaning to" question, one NOT / indicated / suggested question
# and at least two cross-document questions (in every set one question needs all three documents). Questions roughly
# follow the order of the documents; options are short and parallel (format update after the sample-test check).
# Revised after the first blind review (15/15 keys matched, no ambiguity): r-p7-01 word question now on
# "collected", r-p7-03 word and purpose questions hardened, r-p7-02 order form made a table, keys respread.
# All names of people, firms, streets, towns and products are invented.
# `ldbs` on each question is the writer's self-test (WRITING_RULES 8.3) and its band; the blind reviewer sets the
# final band and `level`. `level` stays 3 until the blind review.
# Evidence indexes are [document, paragraph] with 0-based numbers; for a table document the second number is the row.
# Self-test summary: easy 0, medium 4, hard 11.
# Answer positions over the 15 questions: A 4, B 4, C 3, D 4.

ITEMS = [
    # ------------------------------------------------------------------ r-p7-01  conference
    # Doc 0 program table; doc 1 Kessler asks to move from Workshop B (1:30) to Workshop A (late morning);
    # doc 2 Sato: Workshop A is full, Workshop B is repeated in Room 112 in Workshop A's slot, opening moved +15 min.
    {
        "id": "r-p7-01", "type": "read", "format": "p7t", "unit": "p7-triple", "level": 3,
        "source": "hand", "reviewed": False, "v": 1,
        "docs": [
            {"kind": "Web page",
             "head": [],
             "title": "Brightwater Packaging Summit: Program for Thursday, April 16, Harlow Convention Center",
             "table": {
                 "head": ["Time", "Session", "Speaker", "Room"],
                 "rows": [
                     ["8:30–9:15", "Opening address: Where packaging goes next", "Helen Marsh", "Main Hall"],
                     ["9:30–10:30", "Panel: Lighter boxes, lower freight costs", "Owen Batista and guests", "Main Hall"],
                     ["10:45–12:00", "Workshop A: Labels that survive cold storage (separate ticket required, $45)", "Keiko Tran", "Room 204"],
                     ["12:00–1:15", "Lunch (included with all passes)", "—", "Terrace Café"],
                     ["1:30–2:45", "Workshop B: Designing with recycled board (separate ticket required, $45)", "Samuel Adeyemi", "Room 210"],
                     ["3:00–4:00", "Closing panel: What retailers now expect from suppliers", "Lucia Ortega and guests", "Main Hall"],
                 ],
             },
             "zh": []},
            {"kind": "E-mail",
             "head": [["From", "Martin Kessler <mkessler@dalbrookfoods.com>"],
                      ["To", "registration@brightwatersummit.com"],
                      ["Date", "April 2"],
                      ["Subject", "Change to my registration"]],
             "title": None,
             "paras": [
                 "I am registered for the Thursday program of the summit, including the 1:30 workshop on designing with recycled board. Unfortunately, our plant in Fenwold has just scheduled a supplier audit for the afternoon of April 16, and as the plant's quality manager I will need to leave the convention center by 1:00 P.M. to get there in time.",
                 "Would it be possible to transfer my workshop ticket to the late-morning workshop instead? We are about to replace the labels on our entire frozen range, so that topic would be almost as useful to me as the one I originally chose. I would still like to attend the opening address and the panel that follows it.",
                 "If a transfer cannot be arranged, please cancel the workshop ticket alone and refund the fee to my company card. I will attend the morning sessions either way. My registration number is BPS-4471.",
             ],
             "zh": [
                 "我已報名大會星期四的議程，包括一點半那場以再生紙板做設計的工作坊。不巧的是，我們位於 Fenwold 的工廠剛把一場供應商稽核排在四月十六日下午，而身為工廠的品質經理，我必須在下午一點前離開會議中心，才來得及趕到。",
                 "請問能不能把我的工作坊票券改到上午稍晚的那場工作坊？我們即將更換整個冷凍產品系列的標籤，所以那個主題對我來說，幾乎和我原本選的那場一樣有用。我仍然想參加開幕演講，以及緊接在後的那場座談。",
                 "如果沒辦法改場，請只取消工作坊的票券，並把費用退到我的公司信用卡。無論如何，我都會參加上午的場次。我的報名編號是 BPS-4471。",
             ]},
            {"kind": "E-mail",
             "head": [["From", "Ayumi Sato <registration@brightwatersummit.com>"],
                      ["To", "Martin Kessler <mkessler@dalbrookfoods.com>"],
                      ["Date", "April 3"],
                      ["Subject", "RE: Change to my registration"]],
             "title": None,
             "paras": [
                 "Dear Mr. Kessler, thank you for letting us know about the change in your plans. I am sorry to say that the cold-storage labeling workshop filled up last week, and eleven people are already on the waiting list for it.",
                 "There is, however, another solution. Because so many attendees asked for Mr. Adeyemi's session, he has agreed to give it twice. The extra session will run in Room 112, in the same time slot as the cold-storage workshop, and its content will be identical to that of the afternoon session. I have already moved your ticket to it, so there is nothing more you need to do, and no refund will be necessary.",
                 "Please also note that the convention center needs extra time to set up the Main Hall, so the opening address will begin fifteen minutes later than shown in the online program. The rest of the day's schedule is unchanged. Badges can be collected at the registration desk on the ground floor from 7:30 A.M. Please wear yours at all sessions. We look forward to seeing you on the 16th.",
             ],
             "zh": [
                 "Kessler 先生您好：謝謝您告知行程有變。很抱歉，冷藏標籤那場工作坊上週已經額滿，候補名單上也已經有十一個人。",
                 "不過，還有另一個辦法。由於很多與會者都想上 Adeyemi 先生的課，他已同意講兩次。加開的那一場會在 112 室舉行，時段與冷藏標籤工作坊相同，內容則與下午那場完全一樣。我已經把您的票券改到這一場，所以您不需要再做任何事，也不必辦理退費。",
                 "另外請留意，會議中心需要多一點時間布置主廳，所以開幕演講會比線上議程所列的時間晚十五分鐘開始。當天其餘的議程不變。早上七點半起，可以在一樓的報到櫃台領取識別證。參加每一場活動時都請配戴。期待十六日與您見面。",
             ]},
        ],
        "questions": [
            {
                "q": "What is the purpose of the first e-mail?",
                "options": [
                    "To withdraw from the summit",
                    "To ask to switch to another session",
                    "To ask for advice about product labels",
                    "To say he will miss the opening address",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：把「為什麼」和「要什麼」合起來，排除信裡順帶提到的事",
                    "why": "文件二第 1 段說明原因：他下午一點前必須離開去工廠稽核，而他報名的是 1:30 的工作坊；第 2 段 Would it be possible to transfer my workshop ticket to the late-morning workshop instead? 是這封信要的事 → 請求改到另一場。",
                    "evidence": [[1, 0], [1, 1]],
                    "wrong": [
                        "方向相反：他只要退工作坊的錢，而且說 I will attend the morning sessions either way，沒有要退出大會",
                        None,
                        "提到但不是問的：換標籤是他想上冷藏標籤那場課的理由，不是寫信的目的",
                        "方向相反：他說 I would still like to attend the opening address，是會參加，不是會錯過",
                    ],
                    "wrongMore": [
                        "cancel 和 refund the fee 確實出現在第 3 段；但那是「改不成」時的備案，而且只取消 the workshop ticket alone，同一段還說上午的場次照樣參加。",
                        None,
                        "replace the labels 是真的（第 2 段），但他提這件事是解釋為什麼上午那場課對他也有用；他沒有向主辦單位請教標籤怎麼換。",
                        None,
                    ],
                    "vocab": [["audit", "稽核"], ["transfer", "轉讓；改換"], ["registration", "報名"]],
                },
            },
            {
                "q": "What is indicated about Workshop A?",
                "options": [
                    "It is led by Samuel Adeyemi.",
                    "It is included with all passes.",
                    "It will be held twice.",
                    "It has more applicants than places.",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件 indicated 題：回信沒有寫 Workshop A，要用表格把「冷藏標籤那場」對回 A",
                    "why": "文件一第 3 行：Workshop A＝Labels that survive cold storage。文件三第 1 段 the cold-storage labeling workshop filled up … eleven people are already on the waiting list → 想上的人比名額多。",
                    "evidence": [[0, 2], [2, 0]],
                    "wrong": [
                        "相鄰那一行：Samuel Adeyemi 是 Workshop B 的講者；Workshop A 是 Keiko Tran",
                        "相鄰那一行：included with all passes 是午餐那一行；工作坊要另外買 $45 的票",
                        "張冠李戴：講兩次的是 Adeyemi 的 Workshop B，不是 A",
                        None,
                    ],
                    "wrongMore": [
                        "回信第 2 段一直在談 Mr. Adeyemi，很容易以為他就是 Kessler 想上的那場的講者；但表格裡 Adeyemi 在 Workshop B 那一行（第 5 行），Workshop A 那一行的講者是 Keiko Tran。",
                        "表格第 4 行 Lunch (included with all passes) 緊接在 Workshop A 下面；Workshop A 自己那一格寫的是 separate ticket required, $45。",
                        "twice 真的出現，加開場次也真的排在 A 的時段（第 2 段 in the same time slot as the cold-storage workshop）；但加開的是 B 的內容，A 本身只有一場，而且已經額滿。",
                        None,
                    ],
                    "vocab": [["waiting list", "候補名單"], ["fill up", "額滿"], ["separate ticket", "另外購買的票"]],
                },
            },
            {
                "q": "Where will Mr. Kessler most likely be at 11:00 A.M. on April 16?",
                "options": [
                    "In Room 204",
                    "In Room 210",
                    "In Room 112",
                    "In the Main Hall",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件：回信給地點但沒給時間，時間要回表格查",
                    "why": "文件三第 2 段：他的票已改到加開場次，地點 Room 112，時段是 the same time slot as the cold-storage workshop。文件一第 3 行：冷藏標籤工作坊是 10:45–12:00 → 十一點他在 112 室。",
                    "evidence": [[2, 1], [0, 2]],
                    "wrong": [
                        "他原本想改去的 Workshop A 在 204 室，但那場已額滿，他沒有被排進去",
                        "被更正的資訊：210 室是 Workshop B 原本下午場的教室，他已被改到上午加開的場次",
                        None,
                        "主廳十一點沒有活動：開幕演講與座談在 10:30 前結束，閉幕座談 3:00 才開始",
                    ],
                    "wrongMore": [
                        "Room 204 和 10:45–12:00 在表格同一行，所以只看表格、只看他的請求會選它；但回信第 1 段說那場已滿、有十一人候補，第 2 段說他的票改到 112 室。",
                        "表格裡 Workshop B（他原本報名的課）在 Room 210；但那是下午 1:30 的場次。回信說加開的同一門課在 Room 112、上午時段，他的票已經改過去。",
                        None,
                        None,
                    ],
                    "vocab": [["most likely", "最有可能"], ["time slot", "時段"]],
                },
            },
            {
                "q": "When will the first session that Mr. Kessler plans to attend most likely begin?",
                "options": [
                    "At 7:30 A.M.",
                    "At 8:30 A.M.",
                    "At 8:45 A.M.",
                    "At 9:30 A.M.",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "三篇整合＋計算：他要參加哪一場（信）、原定幾點（表）、改了多少（回信）",
                    "why": "文件二第 2 段：他要參加 the opening address。文件一第 1 行：開幕演講原定 8:30。文件三第 3 段：will begin fifteen minutes later than shown in the online program → 8:30 加十五分鐘＝8:45。",
                    "evidence": [[1, 1], [0, 0], [2, 2]],
                    "wrong": [
                        "提到但不是問的：7:30 是開始領識別證的時間，不是場次",
                        "被更正的資訊：8:30 是表格上的原定時間，回信說晚十五分鐘",
                        None,
                        "相鄰那一行：9:30 是開幕之後那場座談的開始時間",
                    ],
                    "wrongMore": [
                        "回信第 3 段 Badges can be collected … from 7:30 A.M. 是領證時間；題目問的是他要參加的第一個 session，那是開幕演講。",
                        "表格第 1 行確實寫 8:30–9:15；但回信第 3 段說會議中心要多花時間布置，開幕演講比 online program 晚十五分鐘，其他不變。",
                        None,
                        "他也會參加座談（the panel that follows it），而且回信說其餘議程不變，所以 9:30 確實是他要去的場次；但座談在開幕演講之後，不是第一場。",
                    ],
                    "vocab": [["opening address", "開幕演講"], ["set up", "布置"], ["unchanged", "不變的"]],
                },
            },
            {
                "q": "In the second e-mail, the word \"collected\" in paragraph 3 is closest in meaning to",
                "options": [
                    "picked up",
                    "gathered up",
                    "put together",
                    "saved up",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "字義題：badges can be collected＝與會者去櫃台領取",
                    "why": "文件三第 3 段 Badges can be collected at the registration desk … from 7:30 A.M. 下一句 Please wear yours at all sessions：識別證要在每一場戴著，所以一早在櫃台是與會者把自己的識別證「領走」，等於 picked up。",
                    "evidence": [[2, 2]],
                    "wrong": [
                        None,
                        "collect 最常見的「收集、收齊」義（collect the forms）；放進本句也通，像是工作人員在櫃台把識別證收起來，但下一句要他每場都戴，一早是領走，不是被收走",
                        "collect 有「把東西湊在一起」的意思；put together 放進本句也通（在櫃台把識別證組好），但 collect 不是「製作、組裝」",
                        "collect 的「累積、存」義（collect stamps、collect points）；識別證不是存起來的東西",
                    ],
                    "wrongMore": [
                        None,
                        "collect 最常用的意思就是把分散的東西收到一起（The forms will be collected at the end of the session），而 Badges can be gathered up at the registration desk 單看這一句也說得通，好像識別證要在櫃台被收齊。但時間是 from 7:30 A.M.，一天的開始；下一句 Please wear yours at all sessions 要他在每一場都戴著，所以是一早去領自己的識別證，不是把它交回去讓人收齊。",
                        "Badges can be put together at the registration desk 單看這一句說得通，好像識別證是現場組裝的。但 collect 的「湊在一起」是把分散的東西集中起來（collect data、collect signatures），不是把一件東西做出來；而且這一段講的是與會者什麼時候、在哪裡拿到識別證（下一句 Please wear yours）。",
                        None,
                    ],
                    "vocab": [["badge", "識別證"], ["registration desk", "報到櫃台"], ["ground floor", "一樓"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p7-02  office furniture
    # Doc 0 price list; doc 1 order form (table: 6 x DK-160 oak, 6 x CH-40 black, 6 x ST-02 graphite = $4,968);
    # doc 2 CH-40 back-ordered; substitute = same model without headrest (CH-35, black or gray, $189); refund
    # 6 x $37 = $222; or wait and pay $85 on the second shipment.
    {
        "id": "r-p7-02", "type": "read", "format": "p7t", "unit": "p7-triple", "level": 3,
        "source": "hand", "reviewed": False, "v": 1,
        "docs": [
            {"kind": "Price list",
             "head": [],
             "title": "Corbel Workspace Supply: Autumn Price List",
             "table": {
                 "head": ["Item no.", "Product", "Colors", "Unit price"],
                 "rows": [
                     ["DK-140", "Height-adjustable desk, 140 cm wide", "White, oak", "$415"],
                     ["DK-160", "Height-adjustable desk, 160 cm wide", "White, oak, graphite", "$468"],
                     ["CH-35", "Mesh-back task chair", "Black, gray", "$189"],
                     ["CH-40", "Mesh-back task chair with headrest", "Black", "$226"],
                     ["ST-02", "Mobile storage unit, three drawers", "White, graphite", "$134"],
                     ["SC-12", "Acoustic desk screen", "Gray, blue", "$72"],
                     ["—", "Delivery within the metro area (free on orders of $3,000 or more)", "—", "$85"],
                 ],
             },
             "zh": []},
            {"kind": "Order form",
             "head": [["Order no.", "40-1187"],
                      ["Order date", "September 8"],
                      ["Customer", "Brennick & Hale Architects"],
                      ["Contact", "Yusuf Demir, office manager"],
                      ["Delivery address", "77 Marlow Street, 3rd floor, Edgeton"],
                      ["Required by", "September 25 (six new members of our design team start work the following Monday)"],
                      ["Special instructions", "Deliveries must arrive before 9:00 A.M.; after that time, the building's freight elevator is reserved for the other tenants. Please call the front desk at 555-0148 when the truck is fifteen minutes away, and place the desks in the open area beside the windows."]],
             "title": "Corbel Workspace Supply: Customer Order Form",
             "table": {
                 "head": ["Item no.", "Description", "Color", "Quantity"],
                 "rows": [
                     ["DK-160", "Height-adjustable desk, 160 cm", "Oak", "6"],
                     ["CH-40", "Task chair with headrest", "Black", "6"],
                     ["ST-02", "Mobile storage unit", "Graphite", "6"],
                 ],
             },
             "zh": []},
            {"kind": "E-mail",
             "head": [["From", "Ingrid Solberg <isolberg@corbelworkspace.com>"],
                      ["To", "Yusuf Demir <ydemir@brennickhale.com>"],
                      ["Date", "September 10"],
                      ["Subject", "Your order 40-1187"]],
             "title": None,
             "paras": [
                 "Dear Mr. Demir, thank you for your order, and congratulations on your growing team. The desks and storage units are in stock and will be delivered on Tuesday, September 22, before 9:00 A.M., as you requested. Our crew will bring everything up to your floor, set up the desks, and take all packaging away with them. Unfortunately, the chair you selected is on back order, and our manufacturer does not expect to ship more until the middle of October.",
                 "As an alternative, we can supply the same model without the headrest, which we carry in the color you chose. Its seat, frame, and adjustments are identical, and several of our clients actually prefer it for shorter staff members. If you accept this substitute, we will refund the difference in price for all six chairs, and they will arrive with the rest of your order.",
                 "Alternatively, we can deliver the chairs you ordered on their own once they arrive. In that case, however, the standard delivery fee would apply to the second shipment, since it would fall below our free-delivery threshold. Please let me know which option you prefer by Monday, September 14, so that I can reserve the chairs for you. I apologize for the inconvenience and thank you for your patience.",
             ],
             "zh": [
                 "Demir 先生您好：謝謝您的訂購，也恭喜貴團隊壯大。辦公桌和收納櫃都有現貨，會依您的要求在九月二十二日星期二上午九點前送達。我們的人員會把所有物品搬上您的樓層、把桌子組裝好，並把包材全部帶走。很遺憾，您選的椅子目前缺貨待補，製造商預計要到十月中才會再出貨。",
                 "替代方案是，我們可以提供同一款但沒有頭枕的椅子，這款我們有您選的顏色。它的座墊、椅架和調整功能都完全相同，有好幾位客戶其實更喜歡讓個子較矮的同仁使用這款。如果您接受這個替代品，我們會退還六張椅子的價差，椅子也會和訂單的其他品項一起送達。",
                 "另一個做法是，等您訂的椅子到貨後，我們再單獨送過去。不過這樣的話，第二批貨要收標準運費，因為它的金額會低於我們的免運門檻。請在九月十四日星期一前告訴我您選哪個方案，好讓我替您保留椅子。造成您的不便，非常抱歉，謝謝您的耐心。",
             ]},
        ],
        "questions": [
            {
                "q": "What is NOT indicated about Mr. Demir's order?",
                "options": [
                    "Its total qualified for free delivery.",
                    "It was placed over two weeks before the required-by date.",
                    "It specified a time of day for delivery.",
                    "It includes an item offered only in graphite.",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "NOT 題：三個選項要用訂單＋價目表逐一核對，剩下的那個才是答案；顏色要查價目表的 Colors 欄",
                    "why": "訂單上的石墨灰是 ST-02，但文件一第 5 行 ST-02 有 White, graphite 兩種；另外兩項 DK-160（White, oak, graphite）、CH-40（只有 Black）也都不是只有石墨灰 → 沒有任何一項「只出石墨灰」，D 不成立，是答案。其他三項都成立：(A) 文件二表格三行都是 6 件，6×468＋6×226＋6×134＝4,968 元，超過文件一最後一行的 3,000 元免運門檻；(B) 文件二表頭 Order date 9 月 8 日、Required by 9 月 25 日，中間有十七天；(C) 表頭 Special instructions 寫 must arrive before 9:00 A.M.。",
                    "evidence": [[1, 2], [0, 4], [1, 0], [1, 1], [0, 1], [0, 3], [0, 6]],
                    "wrong": [
                        "成立：三項合計 4,968 元，超過 3,000 元的免運門檻",
                        "成立：9 月 8 日下單，Required by 9 月 25 日，相隔十七天",
                        "成立：Special instructions 要求上午九點前送達",
                        None,
                    ],
                    "wrongMore": [
                        "e-mail 第 3 段提到 delivery fee，容易以為這筆訂單要付運費；但那是分開送的第二批（只有椅子 6×226＝1,356 元）低於門檻。整筆訂單 4,968 元本身是免運的，信裡 since it would fall below our free-delivery threshold 也暗示原本那筆是過門檻的。",
                        "兩個日期都在訂單表頭，但分在兩欄（Order date: September 8、Required by: September 25），要自己算：相差十七天，所以成立。不要拿 e-mail 第 1 段的實際送貨日 9 月 22 日來算（那樣正好兩週）；選項比的是 required-by date。",
                        None,
                        None,
                    ],
                    "vocab": [["qualify for", "符合…的資格"], ["required-by date", "最晚需要的日期"], ["freight elevator", "貨梯"]],
                },
            },
            {
                "q": "What is the purpose of the e-mail?",
                "options": [
                    "To confirm delivery of the full order",
                    "To report a supply problem with one product",
                    "To request payment of a delivery fee",
                    "To announce new furniture prices",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：整封信的重點是一個品項缺貨，不是第一句的出貨確認",
                    "why": "文件三第 1 段 the chair you selected is on back order … until the middle of October；第 2、3 段各給一個方案（換款、或等貨分批送）→ 寫信是為了說明一項商品供貨出了問題（並請他選方案）。",
                    "evidence": [[2, 0], [2, 1], [2, 2]],
                    "wrong": [
                        "只對一半：九月二十二日送的是桌子和收納櫃，椅子缺貨",
                        None,
                        "提到但不是問的：運費只在他選擇等原款椅子時才收，信裡沒有要他付款",
                        "提到但不是問的：信裡有 difference in price，但那是兩款椅子的價差，不是公布新價格",
                    ],
                    "wrongMore": [
                        "第 1 段第二句確實在確認 September 22 的送貨，這也是信的開頭；但主詞是 The desks and storage units，下一句就說椅子 on back order，信的其餘部分都在處理椅子。",
                        None,
                        "standard delivery fee 出現在第 3 段，但那是「如果選第二個方案」才會發生的事；信裡沒有要求他付款。",
                        None,
                    ],
                    "vocab": [["back order", "缺貨待補"], ["manufacturer", "製造商"], ["in stock", "有現貨"]],
                },
            },
            {
                "q": "In the e-mail, the word \"carry\" in paragraph 2 is closest in meaning to",
                "options": [
                    "stock",
                    "transport",
                    "support",
                    "publish",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "字義題：商店 carry 某商品＝有販售、有庫存",
                    "why": "文件三第 2 段 the same model without the headrest, which we carry in the color you chose：主詞是賣家 we，受詞是商品，後面接 in the color → 「這款我們有您選的顏色可賣」，等於 stock（備有庫存、有販售）。",
                    "evidence": [[2, 1]],
                    "wrong": [
                        None,
                        "最常見義陷阱：carry 最基本是搬運；整封信也在談送貨，但這裡講的是有沒有這個顏色",
                        "carry 有「承重」義（the beam carries the roof），椅子的話題容易聯想；但主詞是賣家 we",
                        "報紙 carry 一篇報導＝刊登，是真的用法；但受詞是椅子，不是文章",
                    ],
                    "wrongMore": [
                        None,
                        "這封信本來就在談送貨（delivered、ship、arrive），所以「運送」很順。但 which we carry in the color you chose 說的是這款有沒有黑色可供應；運送跟顏色無關，代進去 which we transport in the color you chose 說的不是這件事。",
                        None,
                        None,
                    ],
                    "vocab": [["headrest", "頭枕"], ["substitute", "替代品"], ["alternative", "替代方案"]],
                },
            },
            {
                "q": "What is suggested about the substitute chair?",
                "options": [
                    "It will arrive in mid-October.",
                    "It comes in two colors.",
                    "It has a headrest.",
                    "It costs more than the original.",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件：信沒有寫型號，要用「同款、沒有頭枕」回價目表找到那一行",
                    "why": "文件三第 2 段 the same model without the headrest；文件二第 2 行說他訂的是 CH-40（附頭枕）；價目表第 3、4 行，同款無頭枕的是 CH-35，顏色 Black, gray → 有兩種顏色。",
                    "evidence": [[2, 1], [1, 1], [0, 2], [0, 3]],
                    "wrong": [
                        "張冠李戴：十月中才有貨的是他原本訂的椅子（CH-40），替代品會和其他品項一起送",
                        None,
                        "相鄰那一行：附頭枕的是 CH-40；替代品正是 without the headrest",
                        "方向相反：CH-35 是 189 元，比 CH-40 的 226 元便宜，所以信裡才說要退價差",
                    ],
                    "wrongMore": [
                        "middle of October 確實在信裡（第 1 段），但主詞是 the chair you selected；第 2 段說替代品 will arrive with the rest of your order，也就是 9 月 22 日。",
                        None,
                        "價目表 CH-35 與 CH-40 上下相鄰，名稱只差 with headrest；只看到 Mesh-back task chair 就容易選錯行。",
                        None,
                    ],
                    "vocab": [["mesh-back", "網背的"], ["model", "型號、款式"]],
                },
            },
            {
                "q": "How much will Brennick & Hale most likely be refunded if Mr. Demir accepts the substitute?",
                "options": [
                    "$37",
                    "$85",
                    "$222",
                    "$1,134",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "三篇整合＋計算：價差（價目表）× 數量（表單）× 退款條件（信）",
                    "why": "文件三第 2 段 refund the difference in price for all six chairs。文件一：CH-40 226 元、CH-35 189 元，每張差 37 元。文件二表格第 2 行（CH-40）：數量 6 → 37 × 6 ＝ 222 元。",
                    "evidence": [[2, 1], [0, 2], [0, 3], [1, 1]],
                    "wrong": [
                        "只算一張的價差；信上說 for all six chairs",
                        "提到但不是問的：85 元是運費，而且只有選第二個方案才會收",
                        None,
                        "算成六張替代椅的價錢（6 × 189）；退的是價差，不是椅子的價錢",
                    ],
                    "wrongMore": [
                        "226 − 189 ＝ 37 是正確的第一步，所以很像答案；但信裡退的是 the difference in price for all six chairs，還要乘以表單上的數量 6。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["refund", "退款"], ["difference in price", "價差"], ["unit price", "單價"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p7-03  hiring
    # Doc 0 ad (new warehouse in Ashcombe; team of about 25; 3 years' experience; interviews at the Dunmore head office,
    # exercise on interview day); doc 1 Reyes (4 years, crew of 18, no forklift certificate yet, away Nov 21-25,
    # offers to go to Dunmore); doc 2 Whitcombe: Nov 30, at the new warehouse, exercise e-mailed Nov 26 and returned first.
    {
        "id": "r-p7-03", "type": "read", "format": "p7t", "unit": "p7-triple", "level": 3,
        "source": "hand", "reviewed": False, "v": 1,
        "docs": [
            {"kind": "Advertisement",
             "head": [],
             "title": "Operations Coordinator, Ferrow Logistics",
             "paras": [
                 "Ferrow Logistics, a distributor of medical supplies with warehouses in Redmarsh and Dunmore, will open a third warehouse in Ashcombe in January. We are looking for an operations coordinator to help run the new site from its first day.",
                 "The coordinator will plan shifts for a team of about 25 warehouse staff, track incoming shipments, and address any problems with deliveries as they arise. The coordinator will also prepare a weekly report for our regional director.",
                 "Applicants should have at least three years of experience in warehouse or distribution work and be comfortable using inventory software. A forklift certificate is an advantage but is not required. Some weekend work will be needed during busy periods.",
                 "To apply, send a résumé and cover letter to careers@ferrowlogistics.com by November 13. Interviews will be held at our head office in Dunmore during the week of November 23, and short-listed candidates will complete a brief scheduling exercise on the day of their interview.",
             ],
             "zh": [
                 "Ferrow Logistics 是一家醫療用品經銷商，在 Redmarsh 和 Dunmore 設有倉庫，明年一月將在 Ashcombe 開設第三座倉庫。我們正在招募一位營運協調專員，從開幕第一天起協助管理這個新據點。",
                 "協調專員要為約二十五名倉庫人員排班、追蹤進貨，並在送貨出問題時隨時處理。協調專員也要每週為我們的區域總監準備一份報告。",
                 "應徵者應具備至少三年倉儲或物流相關經驗，並能熟練使用庫存管理軟體。有堆高機證照者佳，但非必要。旺季期間需要配合部分週末上班。",
                 "應徵請於十一月十三日前將履歷與求職信寄到 careers@ferrowlogistics.com。面試將於十一月二十三日那一週在我們位於 Dunmore 的總公司舉行，進入面試名單的應徵者會在面試當天完成一份簡短的排班練習。",
             ]},
            {"kind": "E-mail",
             "head": [["From", "Tobias Reyes <t.reyes@quillpost.com>"],
                      ["To", "careers@ferrowlogistics.com"],
                      ["Date", "November 9"],
                      ["Subject", "Application: Operations Coordinator"]],
             "title": None,
             "paras": [
                 "I am writing to apply for the operations coordinator position at your new Ashcombe site. For the past four years, I have supervised the night shift at Glenhaven Foods' distribution center in Pellford, where I lead a crew of eighteen and oversee the unloading and checking of all incoming deliveries.",
                 "I use inventory software every day and recently completed a course in shift planning. I do not yet hold a forklift certificate, but I am booked to take the test in early December.",
                 "My résumé is attached. I should mention that I will be away at a family wedding from November 21 to 25. If I am invited for an interview, I would be grateful if it could be held outside those dates. I would be happy to travel to Dunmore on any other day.",
             ],
             "zh": [
                 "我寫這封信是要應徵貴公司 Ashcombe 新據點的營運協調專員一職。過去四年，我在 Glenhaven Foods 位於 Pellford 的物流中心擔任夜班主管，帶領十八人的團隊，並負責督導所有進貨的卸貨與點收。",
                 "我每天都使用庫存管理軟體，最近也完成了一門排班規劃的課程。我目前還沒有堆高機證照，但已經預約在十二月初考試。",
                 "附上我的履歷。另外要說明的是，十一月二十一日到二十五日我會去參加家人的婚禮。如果我獲邀面試，希望能安排在這段日期以外。其他任何一天，我都很樂意前往 Dunmore。",
             ]},
            {"kind": "E-mail",
             "head": [["From", "Hannah Whitcombe <hwhitcombe@ferrowlogistics.com>"],
                      ["To", "Tobias Reyes <t.reyes@quillpost.com>"],
                      ["Date", "November 18"],
                      ["Subject", "Interview invitation"]],
             "title": None,
             "paras": [
                 "Dear Mr. Reyes, thank you for applying. We were impressed by your application and would like to meet you. Since you will be away for most of the week we had planned, we have arranged your interview for the following Monday, November 30, at 10:00 A.M.",
                 "Please note that the interviews will no longer take place at our head office. Because most of the short-listed candidates live near the new site, we will hold them at the new warehouse itself, which also gives candidates a chance to see the building. Our regional director, Carla Mendes, will lead the interview panel.",
                 "We have also changed the arrangements for the scheduling exercise. Instead of completing it at the interview, you will receive it by e-mail on November 26 and should send it back to me before your interview. It should take about an hour. Please bring photo identification with you on the day.",
             ],
             "zh": [
                 "Reyes 先生您好：謝謝您來應徵。您的申請資料讓我們印象深刻，我們想和您見個面。由於我們原定的那一週您大半時間都不在，我們已把您的面試安排在下一週的星期一，十一月三十日上午十點。",
                 "請注意，面試將不再於總公司舉行。由於進入面試名單的應徵者大多住在新據點附近，我們會直接在新倉庫舉行面試，這也讓應徵者有機會看看那棟建築。我們的區域總監 Carla Mendes 將主持面試小組。",
                 "排班練習的安排也有所調整。您不必在面試時完成，而是會在十一月二十六日以 e-mail 收到題目，並應在面試前寄回給我。完成時間大約一小時。面試當天請攜帶附照片的身分證件。",
             ]},
        ],
        "questions": [
            {
                "q": "In the advertisement, the word \"address\" in paragraph 2 is closest in meaning to",
                "options": [
                    "handle",
                    "forward",
                    "label",
                    "greet",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": False, "B": True, "S": True, "band": "medium"},
                "explain": {
                    "point": "字義題：address a problem＝處理問題",
                    "why": "文件一第 2 段 address any problems with deliveries as they arise：受詞是 problems，後面沒有 to + 收件人，又接 as they arise（問題一出現就…）→ 是「處理」，等於 handle。",
                    "evidence": [[0, 1]],
                    "wrong": [
                        None,
                        "address a complaint to the manager 是「把…送交給某人」；放進本句 forward any problems 也通，但句中沒有 to + 對象，協調專員是要自己處理",
                        "address a parcel 是在包裹上寫地址；跟 deliveries 有聯想，但被 address 的是 problems，不是包裹",
                        "address someone 可以是「稱呼、對…說話」；受詞是問題，不是人",
                    ],
                    "wrongMore": [
                        None,
                        "address 確實可以表示「把信件、意見送給某人」，但那個用法一定帶 to 某人（address your questions to the front desk）。這一句沒有對象，而且整段是在列協調專員自己要做的事（plan shifts、track incoming shipments），所以是自己處理問題，不是轉給別人。下一句提到 regional director，容易讓人以為是把問題轉給總監；但那是另一件事（每週報告）。",
                        "deliveries 讓人想到包裹、地址，address a parcel 也是真的用法；但被 address 的是 problems，代進去 label any problems 意思就變成「替問題貼標籤」。",
                        None,
                    ],
                    "vocab": [["shift", "班次"], ["incoming shipment", "進貨"], ["arise", "出現、發生"]],
                },
            },
            {
                "q": "What is suggested about Mr. Reyes?",
                "options": [
                    "He holds a forklift certificate.",
                    "He manages more staff than the job involves.",
                    "He works for Ferrow Logistics.",
                    "He has more experience than the job requires.",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件推論：應徵者的條件（第一封 e-mail）對照職缺要求（廣告）",
                    "why": "文件一第 3 段要求 at least three years of experience in warehouse or distribution work；文件二第 1 段 For the past four years, I have supervised the night shift at … distribution center → 四年多於三年。",
                    "evidence": [[0, 2], [1, 0]],
                    "wrong": [
                        "方向相反：他說 I do not yet hold a forklift certificate，十二月初才考",
                        "數字對調：他帶十八人，新倉庫的團隊約二十五人",
                        "張冠李戴：他在 Glenhaven Foods 位於 Pellford 的物流中心工作；Ferrow 的倉庫在 Redmarsh 和 Dunmore",
                        None,
                    ],
                    "wrongMore": [
                        None,
                        "兩個數字分在兩份文件：廣告第 2 段 a team of about 25，他的信第 1 段 a crew of eighteen。他現在帶的人比較少，不是比較多。",
                        "他在 distribution center 工作，Ferrow 也有 warehouses，所以容易混；但他的雇主是 Glenhaven Foods，地點 Pellford，不在廣告列出的 Redmarsh、Dunmore 裡。",
                        None,
                    ],
                    "vocab": [["supervise", "督導、擔任主管"], ["crew", "工作小組"], ["distribution center", "物流中心"]],
                },
            },
            {
                "q": "What is the purpose of the second e-mail?",
                "options": [
                    "To schedule an appointment with a candidate",
                    "To offer Mr. Reyes the coordinator job",
                    "To say the head office has moved",
                    "To announce that a warehouse has opened",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "目的題：邀請面試≠錄取；地點換了≠總公司搬家",
                    "why": "文件三第 1 段 would like to meet you … we have arranged your interview for … November 30, at 10:00 A.M.，整封信都在交代這次面試（第 2 段地點、第 3 段排班練習）→ 目的是和應徵者約定面試。",
                    "evidence": [[2, 0], [2, 1], [2, 2]],
                    "wrong": [
                        None,
                        "過度推論：impressed by your application 只是邀請面試，還沒有錄取",
                        "字面誤讀：no longer take place at our head office 是說面試不在總公司辦，不是總公司搬家",
                        "時間錯置：新倉庫要到一月才開（廣告第 1 段）；回信只是借新倉庫的場地面試",
                    ],
                    "wrongMore": [
                        None,
                        "We were impressed by your application 語氣很正面，容易讀成錄取；但同一句接 would like to meet you，後面是面試時間，這是面試邀請。",
                        "第 2 段第一句 the interviews will no longer take place at our head office 單獨看很像「總公司不在那裡了」；但主詞是 the interviews，下一句說改在新倉庫辦，是因為多數應徵者住在附近，總公司本身沒有變動。",
                        "回信提到 the new warehouse 和 a chance to see the building，所以很像在宣布新倉庫啟用；但廣告第 1 段說 will open a third warehouse in Ashcombe in January，面試在十一月底，倉庫還沒開。就算撇開日期，這也只是面試地點，不是寫信的目的。",
                    ],
                    "vocab": [["short-listed", "進入決選名單的"], ["panel", "面試小組"], ["no longer", "不再"]],
                },
            },
            {
                "q": "Where will Mr. Reyes most likely be interviewed?",
                "options": [
                    "In Dunmore",
                    "In Ashcombe",
                    "In Pellford",
                    "In Redmarsh",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨文件＋被更正的資訊：回信說「在新倉庫」，新倉庫在哪要回廣告找",
                    "why": "文件三第 2 段 the interviews will no longer take place at our head office … we will hold them at the new warehouse itself；文件一第 1 段 will open a third warehouse in Ashcombe（文件二第 1 段也說 your new Ashcombe site）→ 面試在 Ashcombe。",
                    "evidence": [[2, 1], [0, 0]],
                    "wrong": [
                        "被更正的資訊：廣告原本說在 Dunmore 總公司面試，他也表示願意去 Dunmore，但回信改成新倉庫",
                        None,
                        "他目前工作的地方，跟面試地點無關",
                        "另一座倉庫：Ferrow 在 Redmarsh 也有倉庫，但不是新開的那一座",
                    ],
                    "wrongMore": [
                        "Dunmore 出現兩次：廣告第 4 段 Interviews will be held at our head office in Dunmore，以及他的信第 3 段 I would be happy to travel to Dunmore。但回信第 2 段明說 no longer … at our head office，改在新倉庫。",
                        None,
                        None,
                        "回信說的是 the new warehouse；Redmarsh 是廣告第 1 段既有的兩座倉庫之一，新開的第三座在 Ashcombe。",
                    ],
                    "vocab": [["head office", "總公司"], ["no longer", "不再"]],
                },
            },
            {
                "q": "When will Mr. Reyes most likely complete the scheduling exercise?",
                "options": [
                    "During his interview on November 30",
                    "Before he leaves for the wedding",
                    "At the head office with others",
                    "Just after he returns from traveling",
                ],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "三篇整合：原本的做法（廣告）被更正（回信），再對照他不在的日期（他的信）",
                    "why": "文件三第 3 段：排班練習 11 月 26 日用 e-mail 寄給他，要在面試（11 月 30 日，第 1 段）前寄回。文件二第 3 段：他 11 月 21 日到 25 日去參加婚禮 → 他是在婚禮回來後、面試前的那幾天做。",
                    "evidence": [[2, 2], [2, 0], [1, 2], [0, 3]],
                    "wrong": [
                        "被更正的資訊：廣告說面試當天做，回信改成事先做完寄回",
                        "時間錯置：練習 11 月 26 日才寄出，他 21 日就出發了",
                        "被更正的資訊兩次：面試不在總公司，練習也不在現場做",
                        None,
                    ],
                    "wrongMore": [
                        "廣告第 4 段 complete a brief scheduling exercise on the day of their interview，面試日期也真的是 11 月 30 日，所以這個選項看起來兩半都對；但回信第 3 段 Instead of completing it at the interview，改成 11 月 26 日寄給他、面試前寄回。",
                        "他會去參加婚禮是真的（信第 3 段），但時間順序反了：婚禮 21–25 日，練習 26 日才寄到。",
                        None,
                        None,
                    ],
                    "vocab": [["arrangement", "安排"], ["instead of", "而不是"], ["be away", "不在、外出"]],
                },
            },
        ],
    },
]
