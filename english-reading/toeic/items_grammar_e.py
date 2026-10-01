# -*- coding: utf-8 -*-
"""TOEIC 練習室：手寫文法題（e 批，connect 單元加強，依 WRITING_RULES.md 出題）。

18 題，全部是 connect（連接詞、介系詞、連接副詞）：
  讓步 although / despite（09、10）、原因 because / owing to（11、12）、
  while / during（13、14）、before / after（15、16）、unless / without（17、18）、
  whereas 與連接副詞 vs 連接詞（19、20、21）、目的與結果（22、23）、
  條件與讓步詞 even if / in case / as long as（24、25、26）。
"ldbs" 是出題者依 WRITING_RULES.md 3.4 的自測（L 局部、D 距離、B 誤信、S 兩步），
"-" 表示四項都沒過；level 是出題者估計，最終由盲審 band 換算；reviewed 由審核者改成 True。
"""

ITEMS = [
    # ------------------------------------------------------------ although / despite
    {
        "id": "g-connect-09", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "The museum kept all three galleries open to visitors ______ the renovation work that its trustees had scheduled to close them for most of the spring.",
        "options": ["even though", "in light of", "due to", "in spite of"],
        "answer": 3,
        "explain": {
            "point": "空格後是名詞片語、沒有自己的動詞 → 讓步介系詞 in spite of",
            "why": "空格後 the renovation work that … had scheduled 是名詞片語，had scheduled 屬於 that 子句，work 沒有動詞。要用介系詞，句意是讓步。",
            "wrong": [
                "even though 要接子句；這裡 work 後面沒有動詞",
                "in light of 是介系詞，但意思是「有鑑於」，與讓步不合",
                "due to 是介系詞，但表原因，與句意相反",
                None,
            ],
            "wrongMore": [
                "even though the renovation work that its trustees had scheduled 讀起來像子句：work 像主詞，had scheduled 像動詞。但 had scheduled 是 that 子句的動詞，在修飾 work；even though 引導的部分自己沒有動詞，所以不成立。",
                "in light of 與 due to 結構上都能接名詞片語，要靠意思排除：「有鑑於（或因為）原定要關閉展廳的整修」不會讓展廳繼續開放，需要的是讓步。",
                None,
                None,
            ],
            "zh": "儘管受託人原定在春季大部分時間為整修工程關閉那三個展廳，博物館仍讓三個展廳持續開放參觀。",
            "vocab": [["renovation", "整修"], ["trustee", "受託人、董事"], ["gallery", "展廳"]],
        },
    },
    {
        "id": "g-connect-10", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "Ticket sales for the autumn concert series were strong, ______ the seating capacity that the fire marshal had approved in April was a third lower than in previous years.",
        "options": ["despite", "although", "however", "even so"],
        "answer": 1,
        "explain": {
            "point": "逗號後接完整子句 → 連接詞 although",
            "why": "空格後有主詞 the seating capacity … 和動詞 was，是完整子句，前面只有逗號，所以要連接詞。although 表讓步；despite 接名詞，however 與 even so 是副詞。",
            "wrong": [
                "despite 後面接名詞；但這裡一路到 was 才出現動詞",
                None,
                "however 是連接副詞，逗號不能連接兩個子句",
                "even so 是連接副詞，逗號不能連接兩個子句",
            ],
            "wrongMore": [
                "despite the seating capacity that the fire marshal had approved in April 單看通順，像 despite + 名詞。但後面還有 was a third lower，那是這個子句的動詞，所以空格後是子句，不能用 despite。",
                None,
                "however 與 even so 的對比意思都對，但它們是連接副詞；前面只用逗號就成了 comma splice，要改成分號或句號才行。",
                None,
            ],
            "zh": "秋季音樂會系列的票房很好，儘管消防主管四月核准的座位數比往年少了三分之一。",
            "vocab": [["fire marshal", "消防安全主管"], ["seating capacity", "座位容量"]],
        },
    },
    # ------------------------------------------------------------ because / owing to
    {
        "id": "g-connect-11", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "Waiting times at the clinic fell sharply in May ______ hiring two temporary receptionists for the front desk cleared the backlog of unanswered calls within three weeks.",
        "options": ["due to", "thanks to", "because", "as a result of"],
        "answer": 2,
        "explain": {
            "point": "動名詞當主詞的子句 → 連接詞 because",
            "why": "hiring two temporary receptionists … 是動名詞片語，當 cleared 的主詞。有主詞也有動詞 cleared，所以空格後是完整子句，要用連接詞 because。",
            "wrong": [
                "due to + 動名詞很常見；但這樣 cleared 就沒有主詞",
                "thanks to + 動名詞也順；但同樣讓 cleared 沒有主詞",
                None,
                "as a result of + 動名詞通順；但 cleared 沒有主詞",
            ],
            "wrongMore": [
                "due to hiring two temporary receptionists for the front desk 本身是完整的介系詞片語，due to 後面接動名詞也是正常用法。問題在於 cleared the backlog … 之後就沒有主詞了；hiring … 本身才是 cleared 的主詞，所以前面要用連接詞。",
                None,
                None,
                None,
            ],
            "zh": "五月份診所的候診時間大幅縮短，因為聘請兩名櫃台臨時接待員，三週內就清掉了積壓的未接來電。",
            "vocab": [["backlog", "積壓的工作"], ["receptionist", "接待員"], ["unanswered", "未回應的"]],
        },
    },
    {
        "id": "g-connect-12", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "______ a fault in the cooling system that technicians first detected during the January shutdown, daily output at the main plant has been held to roughly four-fifths of capacity.",
        "options": ["Owing to", "As a result", "Therefore", "Thus"],
        "answer": 0,
        "explain": {
            "point": "名詞片語 + 逗號 + 主要子句 → 原因介系詞 owing to",
            "why": "a fault in the cooling system … 是名詞片語，到逗號為止沒有動詞；主要子句在逗號之後。名詞片語前用介系詞 Owing to。",
            "wrong": [
                None,
                "As a result 的因果意思對；但後面要加 of 才能接名詞",
                "Therefore 是連接副詞，後面接子句",
                "Thus 是連接副詞，後面接子句",
            ],
            "wrongMore": [
                None,
                "As a result a fault in the cooling system 讀起來像連接副詞開頭，因果意思也對，而且 as a result of 是真的介系詞片語。但這裡少了 of，而且到逗號前沒有動詞；要用 Owing to 直接接名詞。",
                None,
                None,
            ],
            "zh": "由於冷卻系統出現一個技術人員在一月停機期間首次發現的故障，主廠的每日產量一直被限制在約五分之四的產能。",
            "vocab": [["cooling system", "冷卻系統"], ["shutdown", "停機、停工"], ["output", "產量"]],
        },
    },
    # ------------------------------------------------------------ while / during
    {
        "id": "g-connect-13", "type": "grammar", "format": "gap", "unit": "connect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L B S",
        "stem": "The two agents assigned to the gate must stay at the podium ______ boarding passengers who need wheelchair assistance, and they may leave only when the lead agent releases them.",
        "options": ["throughout", "meanwhile", "while", "by"],
        "answer": 2,
        "explain": {
            "point": "帶受詞的 Ving → while + Ving；throughout 要接名詞",
            "why": "boarding 後面直接接受詞 passengers who need …，所以是動詞 -ing，不是名詞。while + Ving 表「在……的同時」，動作者是主詞 the two agents。",
            "wrong": [
                "throughout 後面要接名詞；boarding 這裡帶了受詞",
                "meanwhile 是副詞，不能放在 Ving 前面連接",
                None,
                "by + Ving 表方式，不是「在……期間」",
            ],
            "wrongMore": [
                "throughout boarding 單看通順，像 throughout the boarding，意思也是「整段期間」。但 boarding 後面直接接 passengers who need … 當受詞，表示它是動詞 -ing；throughout 是介系詞，要接名詞（throughout the boarding of passengers）。",
                None,
                None,
                None,
            ],
            "zh": "分派到登機門的兩名地勤人員，在為需要輪椅協助的旅客辦理登機時必須留在櫃台，只有在組長放行後才可離開。",
            "vocab": [["podium", "講台、櫃台"], ["wheelchair assistance", "輪椅協助"]],
        },
    },
    {
        "id": "g-connect-14", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D S",
        "stem": "No engineer may deploy updates to the payment servers ______ the quarterly audit, when every production system is frozen and access is limited to the security team.",
        "options": ["during", "whenever", "when", "once"],
        "answer": 0,
        "explain": {
            "point": "名詞片語、沒有動詞 → 介系詞 during",
            "why": "the quarterly audit 是名詞片語；後面的 when every production system is frozen … 只是補充 audit，沒有替它提供動詞。要用介系詞 during。",
            "wrong": [
                None,
                "whenever 要接子句；the quarterly audit 沒有動詞",
                "when 要接子句；後面的 when 子句另有所屬",
                "once 要接子句；the quarterly audit 沒有動詞",
            ],
            "wrongMore": [
                None,
                None,
                "when the quarterly audit … when every production system is frozen 看起來像時間子句，後面真的有動詞 is frozen。但第二個 when 子句是在補充說明 audit，不屬於前一個 when；空格後的 the quarterly audit 自己沒有動詞，所以連接詞不成立。",
                None,
            ],
            "zh": "在每季稽核期間，任何工程師都不得在付款伺服器上部署更新，那段時間所有正式系統都被凍結，只有資安團隊能存取。",
            "vocab": [["deploy", "部署"], ["audit", "稽核"], ["production system", "正式（上線）系統"]],
        },
    },
    # ------------------------------------------------------------ before / after
    {
        "id": "g-connect-15", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "The customs broker asked to see the original invoices ______ the warehouse supervisor, who had been on leave since the previous Monday, had a chance to compare them with the manifest.",
        "options": ["in advance of", "before", "prior to", "ahead of"],
        "answer": 1,
        "explain": {
            "point": "後面接子句的時間連接詞 → before；prior to 只接名詞",
            "why": "插入的 who 子句之後，主詞 the warehouse supervisor 的動詞出現了：had a chance to compare。所以空格後是完整子句，要連接詞 before。",
            "wrong": [
                "in advance of 是介系詞，後面接名詞",
                None,
                "prior to 是介系詞，不接子句",
                "ahead of 是介系詞，不接子句",
            ],
            "wrongMore": [
                None,
                None,
                "prior to the warehouse supervisor 單看通順，而且是更正式的「在……之前」。但插入語 who had been on leave since the previous Monday 之後出現 had a chance to compare，是動詞，表示整串是子句；prior to 只接名詞或動名詞，所以要用 before。",
                None,
            ],
            "zh": "報關行要求在倉庫主管（他從上週一起就在休假）有機會把發票與貨物艙單核對之前，先看原始發票。",
            "vocab": [["customs broker", "報關行"], ["manifest", "貨物艙單"], ["on leave", "休假中"]],
        },
    },
    {
        "id": "g-connect-16", "type": "grammar", "format": "gap", "unit": "connect", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "-",
        "stem": "Kitchen staff will reset the banquet room ______ the wedding reception that the hotel hosts every Saturday evening, in time for the Sunday brunch service.",
        "options": ["afterward", "later", "then", "after"],
        "answer": 3,
        "explain": {
            "point": "後面接名詞片語 → 介系詞 after；afterward 是副詞",
            "why": "空格後 the wedding reception that the hotel hosts … 是名詞片語，前面要介系詞。after 能接名詞；afterward 是副詞，不能直接接名詞。",
            "wrong": [
                "afterward 是副詞，後面不能直接接名詞",
                "later 是副詞，後面不能直接接名詞",
                "then 是副詞，後面不能直接接名詞",
                None,
            ],
            "wrongMore": [None, None, None, None],
            "zh": "廚房人員會在飯店每週六晚間舉辦的婚宴結束後重新布置宴會廳，趕在週日早午餐服務前完成。",
            "vocab": [["banquet room", "宴會廳"], ["reception", "宴會、招待會"]],
        },
    },
    # ------------------------------------------------------------ unless / without
    {
        "id": "g-connect-17", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "The bank cannot reverse a wire transfer ______ the sender, or the accountant who authorized it on the sender's behalf, has submitted a signed recall request within twenty-four hours.",
        "options": ["whether", "unless", "without", "as though"],
        "answer": 1,
        "explain": {
            "point": "unless + 完整子句（= if not）；without 只接名詞",
            "why": "the sender, or the accountant …, has submitted 有主詞也有動詞 has submitted，是完整子句。意思是「除非寄款人提出申請，否則不能撤回」，所以用 unless。",
            "wrong": [
                "whether 需要 or (not)，且句意不合",
                None,
                "without 帶否定意味；但後面是子句，不能用",
                "as though 表示「好像」，句意不合",
            ],
            "wrongMore": [
                None,
                None,
                "without the sender, or the accountant who authorized it on the sender's behalf 單看通順，而且「沒有……就不能」的否定意思和 unless 很接近。但 has submitted 是動詞，整串是子句；without 是介系詞，只接名詞或動名詞，所以不行。",
                None,
            ],
            "zh": "除非寄款人，或代表寄款人授權此筆匯款的會計師，在二十四小時內提交簽署的撤回申請，否則銀行無法撤銷這筆電匯。",
            "vocab": [["wire transfer", "電匯"], ["on the sender's behalf", "代表寄款人"], ["recall request", "撤回申請"]],
        },
    },
    {
        "id": "g-connect-18", "type": "grammar", "format": "gap", "unit": "connect", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "B",
        "stem": "The reading room may not be used after midnight ______ authorized in writing by the facilities office, which keeps a log of every request.",
        "options": ["without", "once", "regardless", "unless"],
        "answer": 3,
        "explain": {
            "point": "unless + 過去分詞（省略 it is）",
            "why": "authorized in writing … 是省略了 it is 的被動，意思是「除非獲得書面授權」，unless 可以接這種省略。without 要接名詞或 Ving，不接過去分詞。",
            "wrong": [
                "without 帶否定意味；但後面接名詞或 Ving，不接過去分詞",
                "once authorized 表「一旦獲授權」，句意相反",
                "regardless 後面要加 of，且接名詞",
                None,
            ],
            "wrongMore": [
                "without 的否定意思與 unless 相近，容易被選。但 without authorized 文法不通，要說 without being authorized 或 without authorization。",
                None,
                None,
                None,
            ],
            "zh": "閱覽室在午夜後不得使用，除非經設施管理處書面授權，該處會記錄每一筆申請。",
            "vocab": [["authorized", "經授權的"], ["facilities office", "設施管理處"], ["log", "紀錄"]],
        },
    },
    # ------------------------------------------------------------ whereas / linking adverbs
    {
        "id": "g-connect-19", "type": "grammar", "format": "gap", "unit": "connect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L B",
        "stem": "Mortgage applications at the bank's urban branches rose by 14 percent last year, ______ applications at its rural branches fell for the third year in a row.",
        "options": ["however", "in contrast", "whereas", "consequently"],
        "answer": 2,
        "explain": {
            "point": "只用逗號連接兩個子句 → 連接詞 whereas",
            "why": "逗號前後是兩個完整子句（applications … rose；applications … fell），中間只有逗號，必須用連接詞。whereas 還表示都會與鄉村分行的對比。",
            "wrong": [
                "however 意思對，但是副詞，逗號不能連接兩個子句",
                "in contrast 意思對，但是副詞片語，同樣不能只靠逗號",
                None,
                "consequently 是副詞，而且表結果，意思不合",
            ],
            "wrongMore": [
                "however 的對比意思沒有問題，也有很多人以為 ', however' 可以連接兩個子句。但 however 是連接副詞，前面只用逗號就成了 comma splice，要改成 '; however,' 或句號。",
                "in contrast 也是對比，但屬於副詞片語；放在逗號後面連接兩個子句同樣是 comma splice。",
                None,
                None,
            ],
            "zh": "該銀行都會區分行的房貸申請去年成長 14%，而鄉村分行的申請則連續第三年下滑。",
            "vocab": [["mortgage application", "房貸申請"], ["urban", "都會的"], ["rural", "鄉村的"]],
        },
    },
    {
        "id": "g-connect-20", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D S",
        "stem": "The report found that moving the printing plant would cost a fifth more over five years. ______, the board voted to move, citing the lower rents expected from the third year onward.",
        "options": ["Moreover", "Nevertheless", "Therefore", "As a result"],
        "answer": 1,
        "explain": {
            "point": "前後兩句方向相反 → 連接副詞 nevertheless",
            "why": "前一句說搬遷比較貴（不利），後一句卻說 the board voted to move，兩句方向相反。「儘管如此」要用 Nevertheless。",
            "wrong": [
                "Moreover 表補充；前句是缺點，兩句不同向",
                None,
                "Therefore 表結果；成本較高不會導致決定搬遷",
                "As a result 表結果；成本較高不會導致決定搬遷",
            ],
            "wrongMore": [
                "Moreover, the board voted to move, citing the lower rents 單看通順，因為後半像是又一個支持搬遷的理由。但前一句講的是成本較高，不利於搬遷，所以兩句不是同方向的補充。",
                None,
                "Therefore 與 As a result 都要求後句是前句的結果；但「搬遷較貴」不會帶來「決定搬遷」，這個決定是不顧成本做出的。",
                None,
            ],
            "zh": "報告發現，搬遷印刷廠五年下來要多花五分之一的成本。儘管如此，董事會仍投票決定搬遷，理由是第三年起預期的租金較低。",
            "vocab": [["citing", "引用（作為理由）"], ["onward", "往後"], ["printing plant", "印刷廠"]],
        },
    },
    {
        "id": "g-connect-21", "type": "grammar", "format": "gap", "unit": "connect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D",
        "stem": "Please return the signed loan agreement to the museum registrar by Friday; ______, the painting will be sent back to its owner at the end of the month.",
        "options": ["Consequently", "Moreover", "However", "Otherwise"],
        "answer": 3,
        "explain": {
            "point": "otherwise = 如果不這樣做；前句是要求，後句是不做的後果",
            "why": "前句是要求 return … by Friday，後句 the painting will be sent back 是沒做到的後果。連接副詞 otherwise 表示「否則」。",
            "wrong": [
                "Consequently 表結果；寄回協議不會導致畫被退回",
                "Moreover 表補充；後句不是同方向的補充",
                "However 表轉折；後句是沒做的後果，不是轉折",
                None,
            ],
            "wrongMore": [
                None,
                None,
                "However 單看通順，因為前句是要求、後句像壞消息。但 however 表示轉折，並不是「如果不照做就會怎樣」；這裡需要的是條件的反面，所以要 Otherwise。",
                None,
            ],
            "zh": "請在週五前將簽署的借展協議交回博物館登錄組；否則，這幅畫將在月底被退還給所有人。",
            "vocab": [["loan agreement", "借展協議"], ["registrar", "（博物館）登錄人員"]],
        },
    },
    # ------------------------------------------------------------ purpose and result
    {
        "id": "g-connect-22", "type": "grammar", "format": "gap", "unit": "connect", "level": 1,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "B",
        "stem": "The registrar's office spread the enrollment appointments over four days ______ the online portal, which was rebuilt over the summer, would not be overloaded on the first morning.",
        "options": ["so that", "in order to", "so as to", "to"],
        "answer": 0,
        "explain": {
            "point": "目的 + 另一個主詞的子句 → so that；in order to 後接原形",
            "why": "空格後 the online portal … would not be overloaded 有自己的主詞和 would，是子句，所以要用連接詞 so that 表目的。",
            "wrong": [
                None,
                "in order to 後面接原形動詞，不接子句",
                "so as to 後面接原形動詞，不接子句",
                "to 後面接原形動詞，不接子句",
            ],
            "wrongMore": [
                None,
                "in order to 也表目的，而且同樣能放在 over four days 之後。但它後面要接原形動詞，動作者要與主句主詞（the office）相同；這裡 the online portal would … 是另一個主詞的子句。",
                None,
                None,
            ],
            "zh": "註冊組把選課報到時間分散在四天內，好讓暑假期間重建的線上入口網站不會在第一天早上不堪負荷。",
            "vocab": [["enrollment", "註冊、選課"], ["overloaded", "超載的"], ["portal", "入口網站"]],
        },
    },
    {
        "id": "g-connect-23", "type": "grammar", "format": "gap", "unit": "connect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L B",
        "stem": "The help desk received ______ detailed feedback from the pilot group of forty clerks that it rewrote the entire onboarding guide before the rollout.",
        "options": ["so", "too", "such", "very"],
        "answer": 2,
        "explain": {
            "point": "such + 形容詞 + 名詞 + that（結果）",
            "why": "空格後是 detailed feedback：形容詞加名詞（feedback 不可數，前面沒有 a）。這種「形容詞 + 名詞」前面用 such；that 子句說明結果。",
            "wrong": [
                "so 要直接接形容詞；這裡 detailed 後面還有名詞",
                "too 表「太……而不能」，不搭配 that 結果子句",
                None,
                "very 不搭配 that 結果子句",
            ],
            "wrongMore": [
                "so detailed … that 的形狀很常見，所以 so 眼熟。但 so 後面要直接接形容詞或副詞；形容詞後面還接名詞 feedback 時，要用 such。",
                None,
                None,
                None,
            ],
            "zh": "客服中心收到試辦組四十位職員如此詳盡的意見回饋，因此在正式推出前重寫了整份新人訓練手冊。",
            "vocab": [["pilot group", "試辦組"], ["onboarding guide", "新人訓練手冊"], ["rollout", "正式推出"]],
        },
    },
    # ------------------------------------------------------------ condition and contrast words
    {
        "id": "g-connect-24", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B S",
        "stem": "Ms. Aldana, who has not yet decided whether she will make the trip, will receive no credit for her non-refundable ticket ______ she cancels more than a month in advance.",
        "options": ["even if", "even though", "even so", "as though"],
        "answer": 0,
        "explain": {
            "point": "尚未發生的假設 → even if；已知為真的事 → even though",
            "why": "who has not yet decided whether she will make the trip 說明取消只是還沒發生的可能，所以用 even if。even though 用在已知為真的事。",
            "wrong": [
                None,
                "even though 要接已知為真的事；她還沒決定",
                "even so 是連接副詞，不能連接子句",
                "as though 表「好像」，句意不合",
            ],
            "wrongMore": [
                None,
                "even though 與 even if 都表讓步，句型也完全相同，所以最容易選錯。但 even though 預設後面的事是事實；句中 who has not yet decided whether she will make the trip 說明取消尚未發生，只是假設，要用 even if。",
                None,
                None,
            ],
            "zh": "Aldana 女士還沒決定是否成行，她的不可退款機票就算提前一個多月取消，也拿不到任何抵用金額。",
            "vocab": [["non-refundable", "不可退款的"], ["credit", "抵用額度"], ["cancels", "取消"]],
        },
    },
    {
        "id": "g-connect-25", "type": "grammar", "format": "gap", "unit": "connect", "level": 3,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L D B",
        "stem": "The organizers have already booked a second, smaller room at the hotel ______ more than two hundred delegates register, although only about a hundred and fifty have done so to date.",
        "options": ["if", "once", "in case", "whether"],
        "answer": 2,
        "explain": {
            "point": "in case = 為預防萬一，先做準備；if = 條件成立才做",
            "why": "organizers have already booked 表示房間已經訂好，而報名人數至今只有約一百五十人。先訂房是預防人數超過，用 in case。",
            "wrong": [
                "if 表條件成立才做；但房間已經訂好了",
                "once 表「一旦」，句意不合",
                None,
                "whether 需要 or (not)，句意不合",
            ],
            "wrongMore": [
                "if more than two hundred delegates register 本身是順的條件句。但主句是 have already booked，訂房已經完成，不能再等報名人數決定；這種「先準備、以防萬一」的意思要用 in case。",
                None,
                None,
                None,
            ],
            "zh": "主辦單位已經先在飯店訂了第二間較小的房間，以防報名人數超過兩百人，不過到目前為止只有約一百五十人報名。",
            "vocab": [["delegate", "代表、與會者"], ["to date", "到目前為止"], ["organizer", "主辦人員"]],
        },
    },
    {
        "id": "g-connect-26", "type": "grammar", "format": "gap", "unit": "connect", "level": 2,
        "source": "hand", "reviewed": False, "v": 1, "ldbs": "L B",
        "stem": "The bank will keep the promotional rate on the savings account in place for twelve months ______ the balance never falls below the minimum shown in the product guide.",
        "options": ["as long as", "as far as", "even though", "now that"],
        "answer": 0,
        "explain": {
            "point": "as long as = 只要（必須持續成立的條件）",
            "why": "只要 the balance never falls below the minimum，利率就維持十二個月；這是必須持續成立的條件，用 as long as。",
            "wrong": [
                None,
                "as far as 表範圍（據我所知），不是條件",
                "even though 表讓步；這裡是條件，不是讓步",
                "now that 表「既然」，與 never falls 的條件不合",
            ],
            "wrongMore": [
                None,
                "as far as 與 as long as 長得很像，也都能接子句。但 as far as 表示範圍或限度（as far as I know），不是條件；這裡需要的是「只要……就」。",
                None,
                None,
            ],
            "zh": "只要帳戶餘額始終不低於商品說明書上標示的最低金額，銀行就會把儲蓄帳戶的優惠利率維持十二個月。",
            "vocab": [["promotional rate", "優惠利率"], ["balance", "餘額"], ["minimum", "最低限額"]],
        },
    },
]
