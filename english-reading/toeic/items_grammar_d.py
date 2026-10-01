# -*- coding: utf-8 -*-
"""TOEIC 練習室：手寫文法題（d 批，第五輪，依 WRITING_RULES.md 出題）。

14 題：voice 2、mandative 2、conditional 2、parallel 2，quantity / compare /
participle / relative / agree / prep 各 1。schema 見 DESIGN.md 第 5 節；
"ldbs" 是出題者依 WRITING_RULES.md 3.4 的自測（L 局部、D 距離、B 誤信、S 兩步），
level 是出題者估計，最終由盲審 band 換算；reviewed 由審核者改成 True。
"""

ITEMS = [
    # ------------------------------------------------------------ voice
    {
        "id": "g-voice-05", "type": "grammar", "format": "gap", "unit": "voice", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "Only twelve of the eighty technicians who applied for the three-year apprenticeship at the Davenholt Motors plant ______ places in the first intake, and the remainder were placed on a waiting list.",
        "options": ["were offered", "offered", "have offered", "offering"],
        "answer": 0,
        "explain": {
            "point": "主詞是接受動作的人 → 被動 were offered",
            "why": "真正的主詞是句首的 Only twelve of the eighty technicians，離空格很遠；他們是被提供名額的人，要被動。最近的 plant 才是提供者。",
            "wrong": [
                None,
                "plant offered places 局部通順；但主詞其實是 twelve",
                "主動完成式；技術員不是提供名額的一方",
                "分詞不能當主要動詞",
            ],
            "wrongMore": [
                None,
                "Davenholt Motors plant offered places 單看是完整的主動句，因為空格前最近的名詞是 plant（提供名額的一方）。但 plant 只是 at 的受詞；主詞是句首的 Only twelve of the eighty technicians。他們是申請人，被提供名額，要用被動 were offered。",
                None,
                None,
            ],
            "zh": "在申請 Davenholt Motors 工廠三年期學徒計畫的八十位技術員中，只有十二位在第一梯次獲得名額，其餘的人則被列入候補名單。",
            "vocab": [["apprenticeship", "學徒訓練"], ["intake", "（一梯次的）錄取名額"], ["waiting list", "候補名單"]],
        },
    },
    {
        "id": "g-voice-06", "type": "grammar", "format": "gap", "unit": "voice", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B",
        "stem": "Despite the eleven days it spent in the terminal yard, the refrigerated shipment cleared the port without ______ even once, a result that surprised the freight forwarder, who had expected customs officers to open every pallet.",
        "options": ["opening", "being opened", "having opened", "to be opened"],
        "answer": 1,
        "explain": {
            "point": "without + Ving 的邏輯主詞是主句主詞 → 被動 being opened",
            "why": "without 後面動作的主詞是主句的 the refrigerated shipment；貨物不會自己開箱，是被海關人員打開，所以用被動 being opened。",
            "wrong": [
                "without opening 是常見片語；但貨物自己不會打開",
                None,
                "完成式主動，動作者一樣不對",
                "介系詞 without 後面要接 Ving，不接 to V",
            ],
            "wrongMore": [
                "without opening even once 單看是順的常見說法。但 without 後面 Ving 的動作者要和主句主詞一致，這裡主詞是 the shipment，貨物不會自己打開什麼；動作者是句尾提到的 customs officers，所以貨物是「被打開」，要用被動。",
                None,
                None,
                None,
            ],
            "zh": "儘管在碼頭堆場放了十一天，這批冷藏貨物通關時一次也沒被開箱，這出乎貨運承攬業者的意料，他原本預期海關人員會打開每個棧板檢查。",
            "vocab": [["terminal yard", "碼頭堆場"], ["freight forwarder", "貨運承攬業者"], ["pallet", "棧板"], ["customs", "海關"]],
        },
    },
    # ------------------------------------------------------------ mandative
    {
        "id": "g-mandative-05", "type": "grammar", "format": "gap", "unit": "mandative", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "After two reported cargo-door failures, the aviation authority has demanded in a notice to all carriers that every airline operating more than fifty aircraft ______ a full inspection of its door seals within sixty days.",
        "options": ["completing", "to complete", "completed", "complete"],
        "answer": 3,
        "explain": {
            "point": "demand + that 子句 → 原形動詞",
            "why": "that 子句的主詞是 every airline，operating more than fifty aircraft 只是修飾語；demanded that 之後，動詞用原形 complete。",
            "wrong": [
                "像修飾 aircraft 的分詞；但 that 子句還缺動詞",
                "that 子句裡不接 to V",
                "過去式不合要求語氣，也和 within sixty days 的未來不合",
                None,
            ],
            "wrongMore": [
                "more than fifty aircraft completing a full inspection 單看讀得通，像是形容飛機的分詞片語。但 every airline operating … 是 that 子句的主詞，讀到空格為止還沒有動詞；要補謂語，demand 後面接原形 complete。",
                None,
                None,
                None,
            ],
            "zh": "兩起貨艙門故障通報之後，航空主管機關在發給各家業者的通知中要求，每家營運超過五十架飛機的航空公司，須在六十天內對其艙門密封條完成全面檢查。",
            "vocab": [["aviation authority", "航空主管機關"], ["carrier", "航空（運輸）業者"], ["seal", "密封條"]],
        },
    },
    {
        "id": "g-mandative-06", "type": "grammar", "format": "gap", "unit": "mandative", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D",
        "stem": "The tenants' association has asked, in a letter that the housing authority received on March 4, that no resident ______ evicted while the dispute over maintenance fees is still before the tribunal.",
        "options": ["being", "to be", "be", "been"],
        "answer": 2,
        "explain": {
            "point": "ask that + 主詞 + 原形（被動：be + p.p.）",
            "why": "asked 與 that 之間插了一段 in a letter …；that 子句的主詞是 no resident，動詞用原形 be，接 evicted 成被動。",
            "wrong": [
                "像分詞片語；但 that 子句缺定式動詞",
                "ask someone to be 眼熟；但這裡是 that 子句",
                None,
                "been 單獨不能當動詞",
            ],
            "wrongMore": [
                "no resident being evicted while the dispute … 單看是通順的分詞片語。但 asked 後面接的是 that 子句，no resident 是它的主詞，子句本身需要動詞；ask that 的子句用原形 be。",
                "ask someone to be evicted 的句型很常見，所以 to be 眼熟。但這裡 asked 後面是 that no resident …，no resident 已是 that 子句的主詞，後面不能再接 to V。",
                None,
                None,
            ],
            "zh": "房客協會在一封住宅主管機關於三月四日收到的信中要求，在維修費爭議仍待仲裁庭審理期間，不得驅逐任何住戶。",
            "vocab": [["evict", "驅逐（房客）"], ["maintenance fees", "維修費"], ["tribunal", "仲裁庭"]],
        },
    },
    # ------------------------------------------------------------ conditional
    {
        "id": "g-conditional-05", "type": "grammar", "format": "gap", "unit": "conditional", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "______ the print shop's scheduling manager, who had handled the autumn catalog for eleven years, been told about the switch to recycled paper stock, the first run would not have been rejected by the retailer.",
        "options": ["If", "Should", "Had", "Were"],
        "answer": 2,
        "explain": {
            "point": "過去相反假設的倒裝：Had + 主詞 + p.p.",
            "why": "主詞很長，關鍵的 been 到後面才出現；Had … been told 是 If … had been told 的倒裝，主句 would not have been rejected 也是過去相反假設。",
            "wrong": [
                "If the print shop's scheduling manager 一路都通；但 been 前沒有 had",
                "Should 後接原形，不接 been",
                None,
                "Were 後不接 been",
            ],
            "wrongMore": [
                "If the print shop's scheduling manager, who had handled the autumn catalog for eleven years 讀起來完全順，連關係子句裡都有 had handled。但到 been told 才發現 If 後面缺 had；If 句要有 had been told，省略 If 時 had 要移到句首，所以用 Had。",
                "Should + 主詞 + 原形（Should the manager be told）才是對的倒裝，表可能性不高的未來。這裡後面是 been told，是過去完成式的一部分，Should 接不上。",
                None,
                None,
            ],
            "zh": "如果當時負責秋季目錄已十一年的印刷廠排程經理，有被告知要改用再生紙，第一批印刷就不會被零售商退回了。",
            "vocab": [["scheduling manager", "排程經理"], ["paper stock", "紙材"], ["retailer", "零售商"]],
        },
    },
    {
        "id": "g-conditional-06", "type": "grammar", "format": "gap", "unit": "conditional", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D",
        "stem": "The Rivermark Hotel ______ its second tower a full year earlier if the construction permit that the city issued in 2021 had not been suspended pending a flood-risk review.",
        "options": ["would open", "had opened", "opened", "would have opened"],
        "answer": 3,
        "explain": {
            "point": "過去相反假設的結果子句：would have + p.p.",
            "why": "句尾的 if 子句是 had not been suspended，是過去相反的條件；主句要配 would have opened。a full year earlier 也指過去。",
            "wrong": [
                "would open 本身通順；但 if 子句是過去完成",
                "had opened 只能放在 if 子句裡",
                "簡單過去式不能當假設的結果子句",
                None,
            ],
            "wrongMore": [
                "would open its second tower a full year earlier 單看像第二類假設的結果子句。但句尾 if 子句是 had not been suspended（過去完成），條件是過去的相反事實，結果也要回到過去，用 would have opened。",
                None,
                None,
                None,
            ],
            "zh": "如果市府在 2021 年核發的施工許可，沒有因水患風險審查而被暫停，Rivermark 飯店的第二棟大樓本來可以早整整一年開幕。",
            "vocab": [["permit", "許可"], ["suspend", "暫停"], ["pending", "在…期間／等待…"]],
        },
    },
    # ------------------------------------------------------------ parallel
    {
        "id": "g-parallel-05", "type": "grammar", "format": "gap", "unit": "parallel", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D",
        "stem": "Under the revised travel policy, software engineers must either book flights through the approved agency, whose rates were renegotiated in January, or ______ written approval from their team lead before buying a ticket elsewhere.",
        "options": ["obtaining", "obtain", "to obtain", "obtained"],
        "answer": 1,
        "explain": {
            "point": "either A or B：A、B 形式要平行（book … or obtain）",
            "why": "must either book 定下了原形動詞的形式；插入 whose rates … 之後，or 帶出的第二個動詞要與 book 平行，用原形 obtain。",
            "wrong": [
                "or obtaining 局部像並列 Ving；但與 book 不平行",
                None,
                "must 之後接原形，不加 to",
                "過去式與 book 的形式不平行",
            ],
            "wrongMore": [
                "agency, whose rates were renegotiated in January, or obtaining … 單看像在並列一個動名詞片語。但 or 連接的是 must either book 後面的兩個動詞；book 是原形，所以 obtain 也要原形。",
                None,
                None,
                None,
            ],
            "zh": "依新修訂的差旅政策，軟體工程師要不就透過指定旅行社訂機票（該社費率已於一月重新議定），要不就先取得團隊主管的書面核准，才可向他處購票。",
            "vocab": [["renegotiate", "重新議定"], ["rate", "費率"], ["team lead", "團隊主管"]],
        },
    },
    {
        "id": "g-parallel-06", "type": "grammar", "format": "gap", "unit": "parallel", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B",
        "stem": "On graduation day, the university will close both the main library, which has stayed open around the clock since exams began on the third, ______ the three smaller campus libraries at 6 p.m.",
        "options": ["and", "as well as", "along with", "or"],
        "answer": 0,
        "explain": {
            "point": "both A and B：成對連接詞只能用 and",
            "why": "close 後面的 both 被長插入語 which has stayed open … 推得很遠；both 只能與 and 成對：both the main library and the three smaller campus libraries。",
            "wrong": [
                None,
                "意思像「和」；但 Both 不能配 as well as",
                "along with 是介系詞，接不上 Both",
                "Both 配 or 邏輯不合",
            ],
            "wrongMore": [
                None,
                "the main library … as well as the three smaller campus libraries 單看是通順的並列。但前面有 both，both 的第二項一定要用 and 連接；as well as 不能替代。",
                "Both the main library, along with the three smaller campus libraries 單看像「連同」的意思。但 along with 是介系詞，只能附加說明，不能與 Both 成對。",
                None,
            ],
            "zh": "畢業典禮當天，學校會在下午六點關閉主圖書館（自三號期末考開始後全天開放）和三間較小的校區圖書館。",
            "vocab": [["around the clock", "全天候"], ["graduation day", "畢業典禮日"]],
        },
    },
    # ------------------------------------------------------------ quantity
    {
        "id": "g-quantity-06", "type": "grammar", "format": "gap", "unit": "quantity", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D",
        "stem": "Although the new assembly line is already running, ______ of the newly ordered, custom-built testing equipment is still held up in customs, and two quality checks have had to be done by hand.",
        "options": ["many", "several", "much", "few"],
        "answer": 2,
        "explain": {
            "point": "不可數名詞 equipment 配 much of",
            "why": "中心名詞 equipment 在空格後很遠，是不可數名詞，後面的動詞也是單數 is，所以用 Much of。Many、Several、Few 只接可數複數。",
            "wrong": [
                "Many of the newly ordered 看似順；但 equipment 不可數",
                "several 只接可數複數",
                None,
                "few 只接可數複數",
            ],
            "wrongMore": [
                "Many of the newly ordered, custom-built 單看很順，像在接一個複數名詞。但中心名詞 equipment 在後面，而且不可數（沒有 equipments），後面的動詞 is 也是單數。",
                None,
                None,
                None,
            ],
            "zh": "雖然新的組裝線已經開始運轉，但新訂購、客製的測試設備大部分仍卡在海關，有兩項品質檢查只好以人工完成。",
            "vocab": [["assembly line", "組裝線"], ["custom-built", "客製的"], ["held up", "受阻、延誤"], ["customs", "海關"]],
        },
    },
    # ------------------------------------------------------------ compare
    {
        "id": "g-compare-06", "type": "grammar", "format": "gap", "unit": "compare", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "The monthly fee charged for permits in the city's older parking structures, most of which were renovated after 2020, is now almost as high as ______ for spaces in the new private garages.",
        "options": ["those", "that", "it", "them"],
        "answer": 1,
        "explain": {
            "point": "比較時用 that 代替前面的單數名詞（the fee）",
            "why": "被比較的是 The monthly fee（單數），as high as 後面用 that 代替它。插入語裡的 permits、structures 是複數，但不是被比較的對象。",
            "wrong": [
                "被 structures、permits 吸過去；但被比較的是單數 fee",
                None,
                "it 不能直接接 for 片語",
                "them 是受格，不能這樣代替主詞",
            ],
            "wrongMore": [
                "as high as those for spaces in the new private garages 單看很順，因為前面剛出現 permits、structures（複數）。但被比較的是 The monthly fee（單數），要用 that；those 只能代替複數的 fees。",
                None,
                None,
                None,
            ],
            "zh": "市內較舊停車場大樓（其中多數在 2020 年後已整修）的月票費用，現在幾乎和新的私人停車場車位的費用一樣高。",
            "vocab": [["permit", "許可證、停車證"], ["parking structure", "停車場大樓"], ["renovate", "整修"]],
        },
    },
    # ------------------------------------------------------------ participle
    {
        "id": "g-participle-08", "type": "grammar", "format": "gap", "unit": "participle", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D S",
        "stem": "Patients ______ at the Rosewood Clinic after 5 p.m., including those who have been referred by other practices, will be seen by the evening team rather than by their usual physician.",
        "options": ["arrive", "have arrived", "are arriving", "arriving"],
        "answer": 3,
        "explain": {
            "point": "名詞 + Ving 修飾名詞；主要動詞在後面",
            "why": "主要動詞是遠處的 will be seen；Patients 已經有動詞，空格不能再放一個定式動詞，要用分詞 arriving 修飾 Patients。",
            "wrong": [
                "Patients arrive at the Rosewood Clinic 單句很順；但 will be seen 已是主要動詞",
                "完成式也是定式動詞",
                "進行式也是定式動詞",
                None,
            ],
            "wrongMore": [
                "Patients arrive at the Rosewood Clinic after 5 p.m. 本身是完全通順的一句話。但這個句子的主要動詞是逗號後的 will be seen，一個句子不能有兩個主要動詞；空格要改成分詞 arriving 來修飾 Patients。",
                None,
                None,
                None,
            ],
            "zh": "下午五點後到 Rosewood 診所的病人，包括由其他診所轉介的病人，將由晚班團隊看診，而不是由他們平常的醫師看診。",
            "vocab": [["referred", "被轉介"], ["practice", "診所（執業單位）"], ["physician", "（內科）醫師"]],
        },
    },
    # ------------------------------------------------------------ relative
    {
        "id": "g-relative-07", "type": "grammar", "format": "gap", "unit": "relative", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "The hospital's charitable trust has agreed to donate its surplus infusion pumps to ______ the review panel decides has the strongest plan for putting them to use in rural clinics.",
        "options": ["whomever", "who", "whoever", "whom"],
        "answer": 2,
        "explain": {
            "point": "複合關係代名詞的格，由它自己的子句決定",
            "why": "to 後面看似要受格，但空格是後面 has the strongest plan 的主詞；the review panel decides 是插入語。主詞要主格 whoever。",
            "wrong": [
                "to whomever 局部像對的；但它是 has 的主詞",
                "介系詞 to 後面不接 who，也少了「任何人」的意思",
                None,
                "whom 是受格，不能當 has 的主詞",
            ],
            "wrongMore": [
                "to whomever 看起來很對：介系詞 to 後面用受格。但 whomever 的格不是由 to 決定，而是由它自己所在的子句決定；拿掉插入語 the review panel decides，剩下 whoever has the strongest plan，它是 has 的主詞，要用主格。",
                None,
                None,
                None,
            ],
            "zh": "醫院的慈善基金會同意，把剩餘的輸液幫浦捐給審查小組認定擁有最佳方案、能將其用於偏鄉診所的任何人。",
            "vocab": [["charitable trust", "慈善基金會"], ["surplus", "剩餘的"], ["infusion pump", "輸液幫浦"], ["review panel", "審查小組"]],
        },
    },
    # ------------------------------------------------------------ agree
    {
        "id": "g-agree-07", "type": "grammar", "format": "gap", "unit": "agree", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "Enclosed with the revised franchise agreement, which the hotel group will return to its owners on Friday, ______ the original signed floor plans for every property in the portfolio.",
        "options": ["is", "are", "has been", "being"],
        "answer": 1,
        "explain": {
            "point": "倒裝句的動詞，與動詞後面的真正主詞一致",
            "why": "Enclosed with … 倒裝在句首，真正的主詞在空格後：the original signed floor plans（複數），所以用 are。agreement、Friday 是單數，但不是主詞。",
            "wrong": [
                "被單數的 agreement 吸過去；但主詞在空格後",
                None,
                "單數形式，主詞是複數 plans",
                "being 不是定式動詞，句子會缺主要動詞",
            ],
            "wrongMore": [
                "Enclosed with the revised franchise agreement, which … on Friday, is 單看很順，因為空格前最近的名詞 agreement、Friday 都是單數。但這是倒裝句：Enclosed … 在前，主詞放在動詞之後，是 the original signed floor plans，複數，用 are。",
                None,
                None,
                None,
            ],
            "zh": "隨附於修訂後加盟合約（飯店集團將於週五寄還給業主）的，是集團旗下每一處物業的簽署版原始平面圖。",
            "vocab": [["enclosed", "隨附的"], ["franchise agreement", "加盟合約"], ["portfolio", "（旗下）資產組合"]],
        },
    },
    # ------------------------------------------------------------ prep
    {
        "id": "g-prep-10", "type": "grammar", "format": "gap", "unit": "prep", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "ldbs": "L D B S",
        "stem": "Every subcontractor working on the new data center is expected to adhere, in all its dealings with site staff and without exception, ______ the security protocols added to the master agreement last spring.",
        "options": ["to", "with", "by", "for"],
        "answer": 0,
        "explain": {
            "point": "動詞 + 介系詞：adhere to，中間被插入語隔開",
            "why": "決定介系詞的是 adhere，被 in all its dealings … and without exception 隔開；adhere 固定接 to。with 屬於 comply，by 屬於 abide。",
            "wrong": [
                None,
                "comply with 很熟；但 adhere 不接 with",
                "abide by 很熟；但 adhere 不接 by",
                "for 與 adhere 沒有搭配",
            ],
            "wrongMore": [
                None,
                "without exception, with the security protocols 單看通順，因為 comply with 同義又常見。但搭配是由前面的 adhere 決定，不是由空格附近的字決定；adhere 只接 to。",
                "abide by the protocols 是同義的真實搭配，所以 by 眼熟。但 adhere 與 abide 各有固定的介系詞，adhere 後面是 to，不是 by。",
                None,
            ],
            "zh": "每位參與新資料中心工程的分包商，在與現場人員的一切往來中，都必須無一例外地遵守去年春天加入主合約的安全規範。",
            "vocab": [["subcontractor", "分包商"], ["dealings", "往來、交涉"], ["protocols", "規範、協定"], ["master agreement", "主合約"]],
        },
    },
]
