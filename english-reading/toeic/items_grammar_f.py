# -*- coding: utf-8 -*-
"""TOEIC 練習室：手寫文法題（f 批，依 WRITING_RULES.md 出題）。

12 題，全部 unit "prep"（時間介系詞與固定片語），id g-prep-11 … g-prep-22。
"ldbs" 是出題者依 WRITING_RULES.md 3.4 的自測（L 局部、D 距離、B 誤信、S 兩步）；
level 是出題者估計（hard 3 / medium 2 / easy 1），最終由盲審 band 換算；reviewed 由審核者改成 True。
"""

ITEMS = [
    # ------------------------------------------------------------ by vs until
    {
        "id": "g-prep-11", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "The two cranes on the eastern quay, which failed their annual safety inspection in March, must stay parked with their booms lowered ______ the end of next month, when the contractor expects to finish replacing the brake assemblies.",
        "options": ["by", "until", "since", "from"],
        "answer": 1,
        "explain": {
            "point": "stay + 持續的狀態 → until；by 只用於一次完成的動作",
            "why": "決定線索是空格前的 must stay parked：吊車要一直維持停放，直到維修完成才結束，所以用 until。when the contractor expects to finish 也說明狀態在那時結束。",
            "wrong": [
                "must … by 是常見期限句型；但 stay parked 是持續狀態",
                None,
                "since 接過去的起點；這裡是未來的終點",
                "from 表起點，與「到維修完成為止」相反",
            ],
            "wrongMore": [
                "must … by the end of next month 單看是通順的期限句型，所以 by 很眼熟。但 by 只配「做一次就完成」的動作（submit、finish）；這題的動詞是 stay parked，是要持續維持的狀態，持續到某個時間點要用 until。",
                None,
                None,
                None,
            ],
            "zh": "東側碼頭的兩台起重機在三月未通過年度安全檢查，在承包商預計完成更換煞車組件的下個月底之前，必須維持停放、吊臂放低。",
            "vocab": [["quay", "碼頭"], ["boom", "吊臂"], ["contractor", "承包商"], ["brake assembly", "煞車組件"]],
        },
    },
    # ------------------------------------------------------------ in vs within vs after
    {
        "id": "g-prep-12", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "A passenger whose checked bag was damaged on a flight must lodge a written claim at the airline's baggage office ______ seven days, excluding public holidays, of receiving it, or the carrier may reject the claim.",
        "options": ["in", "after", "within", "by"],
        "answer": 2,
        "explain": {
            "point": "within + 一段時間 + of + 起算事件：自……起算的期限內",
            "why": "決定線索是離空格很遠的 of receiving it：within seven days of … 表示自收到行李起七天之內。句尾 or the carrier may reject 也說明這是期限，不是等七天之後。",
            "wrong": [
                "in seven days 看似期限；但後面不能接 of receiving",
                "after seven days 與 or … may reject 的邏輯相反",
                None,
                "by 後面不接 days … of 這種起算結構",
            ],
            "wrongMore": [
                "must lodge a claim in seven days 單看是通順的，in + 一段時間表示從現在起算的「七天之後」。但這題的七天是從 receiving it 起算，結構是 within … of …；in 後面不能接 of receiving。",
                "after seven days 局部讀得通，但「七天之後才提出索賠」會讓 or the carrier may reject 變成矛盾；而且 after seven days of receiving it 也不是自然說法。",
                None,
                None,
            ],
            "zh": "託運行李在航程中受損的旅客，必須在收到行李後七天內（不含公共假日）向航空公司行李櫃台提出書面索賠，否則業者可拒絕該索賠。",
            "vocab": [["lodge a claim", "提出索賠"], ["excluding", "不包括"], ["public holiday", "公共假日"], ["carrier", "運送業者"]],
        },
    },
    # ------------------------------------------------------------ on / in / at with parts of the day
    {
        "id": "g-prep-13", "type": "grammar", "format": "gap", "unit": "prep", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L B",
        "stem": "Delegates who arrive early for the trade fair may collect their badges from the registration booth, which opens ______ the morning of the first day and stays open until the exhibition hall closes.",
        "options": ["on", "in", "at", "toward"],
        "answer": 0,
        "explain": {
            "point": "特定某一天的上午／晚上：on the morning of …",
            "why": "the morning of the first day 指定了特定那一天的上午，所以用 on。一般泛指的上午才用 in the morning。",
            "wrong": [
                None,
                "in the morning 很常見；但 of the first day 指定了某一天",
                "at 接時刻（at 9 a.m.）或 at night，不接 the morning of",
                "toward 表「接近」，不表開始的時間",
            ],
            "wrongMore": [
                None,
                "in the morning 是最常用的上午說法，所以 in 很眼熟。但上午一旦被指定到某一天（the morning of the first day、the morning of the flight），整個片語就要用 on。",
                None,
                None,
            ],
            "zh": "提早抵達貿易展的與會者，可到註冊櫃台領取識別證；櫃台在第一天上午開放，並開放到展覽廳關閉為止。",
            "vocab": [["delegate", "與會代表"], ["badge", "識別證"], ["registration booth", "報到櫃台"], ["exhibition hall", "展覽廳"]],
        },
    },
    # ------------------------------------------------------------ for vs during vs since
    {
        "id": "g-prep-14", "type": "grammar", "format": "gap", "unit": "prep", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L",
        "stem": "Pumps 3 and 4 at the Orsden water plant, which were overhauled in the spring, ran without a single recorded fault ______ eleven consecutive months before the board agreed to extend the maintenance contract.",
        "options": ["during", "since", "by", "for"],
        "answer": 3,
        "explain": {
            "point": "for + 時間長度；during + 事件或時期名稱",
            "why": "eleven consecutive months 是一段時間長度，前面用 for。during 後面要接事件或時期的名稱，不接「數字 + 單位」。",
            "wrong": [
                "during 接事件名稱，不接 eleven months 這種長度",
                "since 接起點（since March），不接長度",
                "by 表期限，不表持續多久",
                None,
            ],
            "wrongMore": [None, None, None, None],
            "zh": "奧斯登水廠的三號與四號泵浦在春天大修後，連續十一個月沒有任何故障紀錄，董事會因此同意延長維護合約。",
            "vocab": [["overhaul", "大修"], ["recorded", "有紀錄的"], ["consecutive", "連續的"], ["maintenance contract", "維護合約"]],
        },
    },
    # ------------------------------------------------------------ ahead of (before / better than)
    {
        "id": "g-prep-15", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "Sales of the Corvan folding tablet have so far run ______ the forecast prepared in January, which surprised planners who expected the model to sell slowly and must now add a second shift at the factory.",
        "options": ["in line with", "in view of", "ahead of", "in spite of"],
        "answer": 2,
        "explain": {
            "point": "run ahead of the forecast：超出預測",
            "why": "決定線索在句尾：which surprised planners who expected the model to sell slowly，還得 add a second shift。銷量比預測好，所以是 ahead of。in line with 表示符合，與 surprised 矛盾。",
            "wrong": [
                "run in line with the forecast 很常見；但與 surprised 矛盾",
                "in view of 表「有鑑於」，不能接 run",
                None,
                "in spite of 表讓步，不是在比較銷量與預測",
            ],
            "wrongMore": [
                "sales have run in line with the forecast 單看完全通順，是銷售報告的常見句型。但後半句說規劃人員很意外、原本預期賣得慢，現在還得加班次，代表銷量超出預測，不是符合預測，所以要 ahead of。",
                None,
                None,
                None,
            ],
            "zh": "科文折疊平板的銷量到目前為止都超出一月提出的預測，這讓原本預期這款機型賣得慢的規劃人員很意外，現在還得在工廠增開一個班次。",
            "vocab": [["forecast", "預測"], ["planner", "規劃人員"], ["second shift", "第二班次"]],
        },
    },
    # ------------------------------------------------------------ through vs throughout
    {
        "id": "g-prep-16", "type": "grammar", "format": "gap", "unit": "prep", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D",
        "stem": "The revised code of conduct applies ______ the organization, from the executive floor at head office to the smallest regional depot, and no department has been granted an exemption.",
        "options": ["throughout", "through", "between", "toward"],
        "answer": 0,
        "explain": {
            "point": "throughout + 範圍：遍及整個、從頭到尾",
            "why": "from the executive floor … to the smallest regional depot 說明規範涵蓋組織的每一處，沒有部門例外，所以用 throughout。",
            "wrong": [
                None,
                "through 表穿過或經由，不表遍及整個組織",
                "between 接兩者之間，不接單一組織",
                "toward 表朝向，不表涵蓋範圍",
            ],
            "wrongMore": [
                None,
                "through 與 throughout 長得很像，也能用在 pass through the organization 這種「穿過」的說法。但這題要說規範涵蓋組織的每一處，意思是「遍及」，只有 throughout 能表達；applies through the organization 不成立。",
                None,
                None,
            ],
            "zh": "修訂後的行為準則適用於整個組織，從總部的主管樓層到最小的區域倉庫，沒有任何部門獲得豁免。",
            "vocab": [["code of conduct", "行為準則"], ["depot", "倉庫、配送站"], ["exemption", "豁免"]],
        },
    },
    # ------------------------------------------------------------ in response to
    {
        "id": "g-prep-17", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "The refinery has trimmed its weekly output ______ the outage at Harbor Point that was reported last week, rather than waiting for the regulator to order a cut.",
        "options": ["in anticipation of", "in response to", "in contrast to", "in return for"],
        "answer": 1,
        "explain": {
            "point": "in response to + 已發生的事：作為回應",
            "why": "決定線索在空格之後：the outage … that was reported last week 是已經發生的事，煉油廠是對它作出反應，所以用 in response to。rather than waiting 也說明是主動回應。",
            "wrong": [
                "in anticipation of 表預期尚未發生的事；但停電已通報",
                None,
                "in contrast to 表對比，不表原因",
                "in return for 表交換，不表對事件的反應",
            ],
            "wrongMore": [
                "trimmed output in anticipation of … 是真實說法，表示為預期中的事先行減產，所以看起來合理。但 outage 後面的 that was reported last week 說明停電已經發生；anticipation 要接尚未發生的事。",
                None,
                None,
                None,
            ],
            "zh": "煉油廠已針對上週通報的哈柏角停電事件調降每週產量，而不是等監管機關下令減產。",
            "vocab": [["refinery", "煉油廠"], ["trim", "削減"], ["outage", "停電、停機"], ["regulator", "監管機關"]],
        },
    },
    # ------------------------------------------------------------ out of stock
    {
        "id": "g-prep-18", "type": "grammar", "format": "gap", "unit": "prep", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D",
        "stem": "The 12-inch valve fittings that the crew ordered on the third have been ______ stock at the Harlow warehouse ever since a strike halted production, so the supervisor has asked the Bexley depot to fill the order.",
        "options": ["in", "at", "by", "out of"],
        "answer": 3,
        "explain": {
            "point": "out of stock：缺貨；in stock：有現貨",
            "why": "ever since a strike halted production 說明沒有貨，所以才請 Bexley depot 出貨，要用 out of stock。",
            "wrong": [
                "in stock 是常見說法；但與 asked the Bexley depot 矛盾",
                "at stock 不是固定說法",
                "by stock 不是固定說法",
                None,
            ],
            "wrongMore": [
                "have been in stock at the warehouse 單看是通順的，in stock 也是常用片語。但 ever since a strike halted production 與 asked the Bexley depot to fill the order 都說明這裡沒有貨，所以要 out of stock。",
                None,
                None,
                None,
            ],
            "zh": "工班在三號訂購的十二吋閥門接頭，自從罷工使生產停擺以來，哈洛倉庫就一直缺貨，所以主管已請貝克斯利配送站出貨來補這張訂單。",
            "vocab": [["valve fitting", "閥門接頭"], ["halt", "使停止"], ["fill the order", "出貨、滿足訂單"]],
        },
    },
    # ------------------------------------------------------------ under review
    {
        "id": "g-prep-19", "type": "grammar", "format": "gap", "unit": "prep", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L",
        "stem": "The committee has confirmed that all four contractor bids remain ______ review while the legal team checks each firm's insurance documents, and no decision will be announced before the end of the month.",
        "options": ["under", "over", "beyond", "beside"],
        "answer": 0,
        "explain": {
            "point": "固定片語：under review（審查中）",
            "why": "remain ______ review while the legal team checks … 表示標案仍在審查，固定說法是 under review。",
            "wrong": [
                None,
                "over 不與 review 搭配成這個意思",
                "beyond review 表「超出審查範圍」，與句意不合",
                "beside 表「在旁邊」，不搭配 review",
            ],
            "wrongMore": [None, None, None, None],
            "zh": "委員會確認，在法務團隊查核各家公司的保險文件期間，四份承包商標書都仍在審查中，月底前不會公布決定。",
            "vocab": [["bid", "標書"], ["insurance documents", "保險文件"]],
        },
    },
    # ------------------------------------------------------------ in advance of
    {
        "id": "g-prep-20", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "The auditors asked that all supporting invoices for the third quarter be filed ______ their visit on the fourteenth, a request that gave the accounts team less than a week to trace the missing receipts.",
        "options": ["in lieu of", "in the course of", "in advance of", "in the absence of"],
        "answer": 2,
        "explain": {
            "point": "in advance of + 事件：在……之前先做好",
            "why": "決定線索在句尾：a request that gave the accounts team less than a week to trace the missing receipts，說明發票要在查帳來訪之前交齊，所以用 in advance of their visit。",
            "wrong": [
                "in lieu of 表「代替」；但來訪並沒有被取代",
                "in the course of 表「期間」；但 less than a week 說明要在來訪前完成",
                "in the absence of 表「缺少」，與來訪句意不合",
                None,
            ],
            "wrongMore": [
                "filed in lieu of their visit 文法上可讀，像是「用歸檔取代來訪」。但句子說的是查帳員仍會在十四日來訪，且給了會計組不到一週的時間準備，所以發票是來訪之前要交，不是取代來訪。",
                "filed in the course of their visit 局部通順，表示在來訪期間歸檔。但句尾說這項要求只給了 less than a week 去追查遺失的收據，代表截止點在來訪之前，不在期間之內。",
                None,
                None,
            ],
            "zh": "查帳人員要求在他們十四日來訪之前，交齊第三季所有佐證發票，這項要求讓會計組只有不到一週的時間去追查遺失的收據。",
            "vocab": [["auditor", "查帳人員"], ["supporting invoice", "佐證發票"], ["trace", "追查"], ["receipt", "收據"]],
        },
    },
    # ------------------------------------------------------------ with regard to
    {
        "id": "g-prep-21", "type": "grammar", "format": "gap", "unit": "prep", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D",
        "stem": "Please send any queries ______ your travel expense claim to the finance office, but direct questions about the booking itself to the travel desk, which handles all airline and hotel reservations.",
        "options": ["in accordance with", "in addition to", "in the event of", "with regard to"],
        "answer": 3,
        "explain": {
            "point": "with regard to + 主題：關於",
            "why": "queries ______ your travel expense claim 指「和費用申請有關的問題」，後面 questions about the booking itself 與它對照，所以用 with regard to。",
            "wrong": [
                "in accordance with 表依照規定，不表主題",
                "in addition to 局部可讀；但句意是「關於」，不是「另外」",
                "in the event of 表萬一，後接可能發生的事",
                None,
            ],
            "wrongMore": [
                None,
                "send any queries in addition to your travel expense claim 局部讀得通，像是「除了申請之外，還要寄問題」。但後半句 questions about the booking itself 與前半句是在分流不同主題的問題，所以前半要用表示主題的 with regard to。",
                None,
                None,
            ],
            "zh": "關於差旅費用申請的任何疑問請寄給財務辦公室，但與訂位本身有關的問題，請轉給負責所有機票與飯店預訂的差旅服務台。",
            "vocab": [["query", "疑問、詢問"], ["expense claim", "費用申請"], ["reservation", "預訂"]],
        },
    },
    # ------------------------------------------------------------ in charge of
    {
        "id": "g-prep-22", "type": "grammar", "format": "gap", "unit": "prep", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "The deputy director, who has spoken warmly about the plan at every staff briefing since March, will be ______ the pilot scheme once it launches, although he has asked to hand it over to a successor after six months.",
        "options": ["in favor of", "in charge of", "in need of", "in case of"],
        "answer": 1,
        "explain": {
            "point": "in charge of：負責管理",
            "why": "決定線索在句尾：he has asked to hand it over to a successor。能交接的是職責，所以他要負責這項計畫：in charge of。",
            "wrong": [
                "since March 他公開稱讚計畫，所以像贊成；但 hand it over 說的是交接職責",
                None,
                "in need of 表「需要」；計畫不是他需要的東西",
                "in case of 表萬一，後接可能發生的事",
            ],
            "wrongMore": [
                "has spoken warmly about the plan 把人推向「贊成」，will be in favor of the pilot scheme 單看也完全通順。但句尾 hand it over to a successor 交接的是職責，不是立場；他啟動後要負責管理，所以是 in charge of。",
                None,
                None,
                None,
            ],
            "zh": "副主任自三月起在每次員工簡報上都對這項計畫讚譽有加，試辦計畫啟動後將由他負責，不過他已要求六個月後交給接任者。",
            "vocab": [["deputy director", "副主任"], ["briefing", "簡報會"], ["pilot scheme", "試辦計畫"], ["successor", "接任者"]],
        },
    },
]
