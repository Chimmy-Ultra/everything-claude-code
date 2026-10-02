# Round 7 reading items, Part 6 style (text completion), written under WRITING_RULES.md (sections 0, 3, 4, 6, 8).
# 4 documents, 4 blanks each (16 questions): r-p6-01 e-mail (elevator work), r-p6-02 memo (expense system),
# r-p6-03 news article (bakery second site), r-p6-04 letter (magazine price and format).
# Each document has exactly one sentence-insertion blank; the other three are word or phrase blanks. The learner's
# weak spots (connectors / prepositions, relative pronouns, conditionals) appear in every set: 01 unless, 02 As a
# result, 03 Until, 04 Unlike / who / Should. Word-form / collocation blanks: 02 late, 03 opportunity.
# All names of people, firms, products, streets and towns are invented. US spelling (elevator, center).
# `ldbs` on each question is the writer's self-test (WRITING_RULES 8.3) and is only a guide; the blind reviewer sets
# the final band and `level`. `level` stays 3 until then. reviewed stays False until the items pass a blind review.
# Self-test summary: easy 0, medium 4, hard 12. Answer positions over the 16 questions: A 4, B 4, C 4, D 4.
# Round-7 blind review: 16/16 keys matched, no mustFix; this version applies its shouldFix list and the coordinator's
# notes (r-p6-01 {3}/{4} reordered so the unless clue comes after the blank; r-p6-02 {4} is now a word-form blank;
# r-p6-03 capacity loophole closed; r-p6-04 salutation). Answer letters are unchanged.
# Writer's notes for each question (near-correct option, where the deciding clue is) are in review/round7_p6.json.

ITEMS = [
    # ------------------------------------------------------------------ r-p6-01  e-mail, elevator work
    # {1} insertion (C): only "one elevator at a time" fits P2's "the elevator that remains in service".
    # {2} it (A): singular, back to that one elevator; "them" is pulled by "two passenger elevators" / "the stairs".
    # {3} unless (B): the clue comes AFTER the blank: P3 opens the freight elevator to "these deliveries" 6-8 a.m.,
    #     so "even if" (a strict no-deliveries rule, believable when the blank is read) contradicts it.
    # {4} will be (D): the arrangement is for next week's work (e-mail March 9, work from March 16).
    # Revised after the round-7 blind review: the delivery sentence now comes before the freight-elevator sentence,
    # so the reader meets {3} before the clue; "During the work," was dropped from P2.
    {
        "id": "r-p6-01", "type": "read", "format": "p6", "unit": "p6", "level": 3,
        "source": "hand", "reviewed": True, "v": 1,
        "docs": [
            {
                "kind": "E-mail",
                "head": [["To", "All tenants, Harlow Court"], ["From", "Denise Okafor"], ["Date", "March 9"], ["Subject", "Elevator work, March 16-20"]],
                "title": None,
                "paras": [
                    "On Monday, March 16, technicians from Calloway Lift Services will begin replacing the control systems in Harlow Court's two passenger elevators. The work is expected to take five days. {1}",
                    "The elevator that remains in service will be busier than usual. Tenants on the second and third floors are therefore asked to use the stairs whenever possible and to leave {2} free for residents of the upper floors. Deliveries of furniture or other large items should be postponed {3} they are brought in through the loading dock early in the morning.",
                    "The freight elevator at the loading dock, which is normally used only by building staff, {4} open to tenants for these deliveries from 6 to 8 a.m. each weekday. If you have any questions, please call the management office at extension 210.",
                    "Denise Okafor, Property Manager, Harlow Court",
                ],
                "zh": [
                    "3 月 16 日星期一起，Calloway 電梯服務公司的技術人員將開始更換 Harlow Court 兩部客梯的控制系統。工程預計需時五天。兩部電梯會輪流停用，一次只停一部，先從東側那部開始。",
                    "仍在運轉的那部電梯會比平常繁忙。因此，請住在二樓和三樓的住戶盡量走樓梯，把它留給高樓層的住戶使用。家具或其他大型物品的送貨，除非是在清晨經由卸貨區送進來，否則請延後。",
                    "卸貨區的貨梯平常只供大樓員工使用，屆時每個平日上午 6 點到 8 點將開放給住戶收這類貨物。如有任何問題，請撥分機 210 聯絡管理室。",
                    "Harlow Court 物業經理 Denise Okafor",
                ],
            }
        ],
        "questions": [
            {
                "options": [
                    "Both elevators will therefore be out of service until March 20.",
                    "We will let you know the dates once they have been confirmed.",
                    "Only one elevator will be shut down at a time, starting with the east one.",
                    "We apologize in advance for closing the loading dock that week.",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "句子插入：插入句要讓下一段的 the elevator that remains in service（仍在運轉的那部電梯）有著落",
                    "why": "空格在第一段最後；線索在第二段。第二段第一句說 the elevator that remains in service will be busier than usual，第二句又請低樓層住戶把 it（單數）留給高樓層住戶——表示施工期間有一部客梯照常運轉。只有 C「一次只停一部，先從東側那部開始」能接上這個說法。",
                    "evidence": [[0, 0], [0, 1]],
                    "wrong": [
                        "接在「工程需時五天」後面最順，therefore 也像在順著前句下結論；但第二段說有一部 remains in service，兩部同時停用與此矛盾",
                        "說日期還沒確定；但第一段第一句已寫明 3 月 16 日星期一開工，主旨也寫了 3 月 16 到 20 日",
                        None,
                        "說要關閉卸貨區；但第二段說大型貨物可以在清晨經由卸貨區送進來，第三段也說卸貨區的貨梯會開放給住戶收貨",
                    ],
                    "wrongMore": [
                        "A 是最強的誘答：前一句說兩部電梯都要換控制系統、要做五天，「所以兩部都停到 3 月 20 日」是最直覺的推論，本段自己讀起來毫無問題。但插入句也要接得上後文。第二段一開頭就說 the elevator that remains in service will be busier than usual，接著請住戶 leave it free for residents of the upper floors——如果兩部同時停用，就沒有「仍在運轉的那部」，也沒有「它」可以讓給別人。要讀到第二段才能排除 A。",
                        None,
                        None,
                        "D 和主題有關（施工、卸貨區都在信裡），所以不像無關的句子那樣一眼可刪。但第二段說大型貨物可以 brought in through the loading dock early in the morning，第三段也說 The freight elevator at the loading dock … will be open to tenants for these deliveries——卸貨區不但沒關，還是施工期間的替代路線。",
                    ],
                    "vocab": [["tenant", "房客；住戶"], ["control system", "控制系統"], ["passenger elevator", "客梯"]],
                },
            },
            {
                "options": ["it", "them", "one", "theirs"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "代名詞：要回前一句找先行詞——施工期間只剩「一部」電梯，用單數 it",
                    "why": "空格指的是要「留給高樓層住戶用」的東西。前一句說 the elevator that remains in service（單數），第一段的插入句也說一次只停一部，所以施工期間能用的客梯只有一部，用 it。決定性線索在前一句的單數 the elevator 與第一段的「一次只停一部」。",
                    "evidence": [[0, 0], [0, 1]],
                    "wrong": [
                        None,
                        "第一段的 two passenger elevators 是複數，看起來可以用 them；但施工期間只有一部在運轉，而 them 若指 the stairs，又和「請走樓梯」自相矛盾",
                        "leave one free 像是「留一部給別人」；但要有兩部以上可選才能這樣說，施工期間能用的只有一部",
                        "所有格代名詞 theirs（他們的東西）放進去，變成把低樓層住戶自己的東西留給高樓層住戶，說不通",
                    ],
                    "wrongMore": [
                        None,
                        "them 是最容易誤選的：空格前最近的複數名詞是 the stairs，第一段又說大樓有 two passenger elevators，學生很自然把「電梯」想成複數。但 them 如果指 the stairs，句子變成「請走樓梯，並把樓梯留給高樓層住戶」，前後矛盾；如果指兩部電梯，又跟前一句的 the elevator that remains in service 和第一段「一次只停一部」矛盾——施工期間只剩一部可以留。",
                        "leave one free for … 本身是正確的說法（例如大樓有三部電梯，請大家留一部給搬貨）。但 one 的意思是「從幾部之中留一部」，前提是至少有兩部可用；這裡只剩一部在運轉，要整部讓給高樓層住戶，所以用 it 指那一部。",
                        None,
                    ],
                    "vocab": [["in service", "運轉中；可使用"], ["whenever possible", "盡可能"], ["resident", "住戶"]],
                },
            },
            {
                "options": ["even if", "unless", "because", "although"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "連接詞：unless（除非）——決定性線索在下一段：貨梯會開放給住戶收「這類貨物」",
                    "why": "讀到空格時，「施工期間大型家具一律延後」和「除非從卸貨區送，否則延後」都說得通。要讀到第三段：卸貨區的貨梯 will be open to tenants for these deliveries from 6 to 8 a.m. each weekday——these deliveries 就是前一句的大型家具送貨，而 6 點到 8 點就是本句的 early in the morning。既然清晨從卸貨區送進來是可以的，本句只能是「除非在清晨經由卸貨區送進來，否則延後」，用 unless。",
                    "evidence": [[0, 1], [0, 2]],
                    "wrong": [
                        "even if（即使）讀到空格時完全通，像一條「一律延後」的嚴格規定；但第三段說貨梯會在 6 點到 8 點開放給住戶收這類貨物，「即使清晨從卸貨區送也要延後」與此矛盾",
                        None,
                        "因果說不通：貨物從卸貨區送進來，不是要延後的理由",
                        "although 把「貨物是在清晨從卸貨區送進來的」當成已經發生的事實，而且同樣和第三段開放貨梯收這類貨物的安排矛盾",
                    ],
                    "wrongMore": [
                        "even if 是本題的近乎正確誘答：施工期間「大型貨物一律延後，即使從卸貨區送也一樣」是很常見的大樓規定，讀到空格這一句時沒有任何東西排除它。決定性線索在下一段：The freight elevator at the loading dock … will be open to tenants for these deliveries from 6 to 8 a.m. each weekday。these deliveries 指的就是大型家具的送貨，6 點到 8 點就是 early in the morning——管理室特地為這類貨物開了一個時段，所以信的意思只能是「除非在那個時段從卸貨區送，否則延後」。選 even if 等於說這個時段也不能用，跟第三段矛盾。",
                        None,
                        None,
                        "although 跟 even if 錯在同一個地方（和第三段矛盾），而且 although 後面接的是已經成立的事實：「雖然這些貨是清晨從卸貨區送進來的」——信寫的是下週要怎麼安排，這件事還沒發生。",
                    ],
                    "vocab": [["postpone", "延後"], ["furniture", "家具"], ["loading dock", "卸貨區；裝卸平台"]],
                },
            },
            {
                "options": ["has been", "was", "had been", "will be"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "時態：信裡描述的是下週施工期間的安排，用未來式",
                    "why": "這封 e-mail 寫於 3 月 9 日，施工 3 月 16 日才開始（第一段 will begin）。本句的 these deliveries 指第二段那些「要延後、或改在清晨送」的大型家具，也是施工期間才有的事；同一句的 which is normally used only by building staff 又說貨梯平常只給員工用。開放給住戶是配合施工的新安排，還沒發生，所以是 will be open。",
                    "evidence": [[0, 0], [0, 1], [0, 2]],
                    "wrong": [
                        "has been open 本句文法通；但這表示已經開放了一段時間，和「平常只給員工用」以及「施工下週才開始」矛盾",
                        "過去式表示以前開放過；但這是下週施工期間的安排",
                        "過去完成式要有一個更早的過去時間點，信裡沒有",
                        None,
                    ],
                    "wrongMore": [
                        "has been open to tenants … each weekday 單看本句可以讀成「每個平日都已經開放」。但同一句的 normally used only by building staff 說平常只給員工用，信的日期（3 月 9 日）和第一段又說施工下週一（3 月 16 日）才開始——開放給住戶收貨是為了施工才有的安排，現在還沒開始，所以用 will be。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["freight elevator", "貨梯"], ["normally", "平常；通常"], ["extension", "分機"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p6-02  memo, expense system
    # {1} As a result (D): "far fewer rejected claims" is a good result; "Nevertheless" is pulled by "rejected".
    # {2} still (B): the next sentence (auditors may ask to see the originals) rules out "no longer".
    # {3} insertion (A): "This earlier date" = the 5th; "in the month they are submitted" is the contrast for the
    #     next sentence's "the following month instead".
    # {4} late (C): word form. "late" is itself the adverb ("submitted late" = after the 5th); "lately" means
    #     "recently" and does not fit the deadline in the previous sentences.
    # Revised after the round-7 blind review: "see them" -> "see the originals"; {4} was a participle blank
    # ("submitted", judged easy) and is now a word-form blank.
    {
        "id": "r-p6-02", "type": "read", "format": "p6", "unit": "p6", "level": 3,
        "source": "hand", "reviewed": True, "v": 1,
        "docs": [
            {
                "kind": "Memo",
                "head": [["To", "All staff"], ["From", "Graham Petrosyan, Finance Director"], ["Date", "September 2"], ["Subject", "Changes to expense claims"]],
                "title": None,
                "paras": [
                    "As many of you know, the finance department has spent the summer testing Tallyway, an online system for reporting business expenses. Staff in the sales department, who used the system throughout the trial, reported far fewer rejected claims than they had with the paper forms. {1}, Tallyway will replace the paper forms for all employees starting October 1.",
                    "With Tallyway, receipts are simply photographed with a phone and attached to the claim. You will {2} need to keep the original receipts for six months. Our auditors may ask to see the originals during the annual review.",
                    "The new system also brings a change to the monthly deadline. Claims are currently accepted until the 15th of the following month; from October, they need to be submitted by the 5th. {3} Claims submitted {4} will be repaid the following month instead.",
                ],
                "zh": [
                    "如同許多同仁所知，財務部整個夏天都在試用 Tallyway，這是一套申報業務費用的線上系統。在試用期間全程使用這套系統的業務部同仁表示，被退回的申請比使用紙本表單時少了很多。因此，自 10 月 1 日起，Tallyway 將取代全體員工的紙本表單。",
                    "使用 Tallyway 時，只要用手機拍下收據、附在申請上即可。你仍然需要把收據正本保留六個月。我們的稽核人員在年度審查時可能會要求查看正本。",
                    "新系統也會改變每月的申報期限。目前申請可以在次月 15 日之前提出；從 10 月起，必須在 5 日之前提交。提前的期限能讓我們在申請提交的當月就撥款。逾期提交的申請，則改在下個月撥款。",
                ],
            }
        ],
        "questions": [
            {
                "options": ["Nevertheless", "Otherwise", "For example", "As a result"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "連接副詞：前一句是好結果，這一句是因此採取的行動 → As a result",
                    "why": "前一句說業務部試用時 reported far fewer rejected claims than they had with the paper forms（被退回的申請比用紙本時少很多）——這是正面的結果，所以「因此」全公司改用 Tallyway。要先看懂 far fewer rejected claims 是好消息（rejected 是負面字，但重點是 far fewer），才能排除 Nevertheless。",
                    "evidence": [[0, 0]],
                    "wrong": [
                        "本句單看也通（「儘管如此，還是要換系統」）；但前一句是好結果，不是要克服的問題",
                        "otherwise 是「否則；不然的話」，前面沒有可以接「否則」的條件或指示",
                        "這一句不是前一句的例子",
                        None,
                    ],
                    "wrongMore": [
                        "Nevertheless 是近乎正確誘答：「儘管如此，Tallyway 將取代紙本表單」文法完全對，而且前一句有 rejected 這個負面字，很容易讓人以為試用出了問題。但 far fewer rejected claims than they had with the paper forms 的意思是「被退回的申請比用紙本時少很多」——試用很成功。好結果之後接「所以全面採用」，用 As a result；Nevertheless 要前面先有不利的事實。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["trial", "試用；試行"], ["reject", "退回；駁回"], ["claim", "（費用）申請"]],
                },
            },
            {
                "options": ["no longer", "still", "not yet", "already"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "副詞：still（仍然）——下一句的稽核要求決定方向",
                    "why": "前一句說收據拍照上傳即可，很容易以為正本不用留了。但下一句 Our auditors may ask to see the originals during the annual review——稽核人員可能要看正本，所以正本「仍然」要保留，用 still。決定性線索在下一句。",
                    "evidence": [[0, 1]],
                    "wrong": [
                        "接在「拍照上傳即可」之後最自然；但下一句說稽核人員可能要看正本，不保留就沒有東西給他們看",
                        None,
                        "「還不需要保留」說不通：保留收據不是之後才開始的事",
                        "「已經需要保留」語意不通，already 不這樣和 will need 連用",
                    ],
                    "wrongMore": [
                        "no longer 是最強的誘答：系統改成拍照上傳，「不再需要把正本保留六個月」是最順的推論，本句文法也完全對。但下一句 Our auditors may ask to see the originals——如果正本不必保留，稽核人員要看什麼？所以這裡是「雖然上傳了照片，正本仍然要留」，用 still。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["receipt", "收據"], ["auditor", "稽核人員；審計員"], ["annual review", "年度審查"]],
                },
            },
            {
                "options": [
                    "This earlier date lets us repay claims in the month they are submitted.",
                    "This later date gives everyone more time to collect receipts.",
                    "Claims that arrive after that date will no longer be accepted.",
                    "Paper forms will continue to be accepted until the end of the year.",
                ],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "句子插入：This earlier date 要接上前一句的「5 日」，也要接上下一句的「改到下個月」",
                    "why": "前一句說期限從次月 15 日提前到 5 日，所以是 earlier date；下一句說逾期（submitted late）的申請 will be repaid the following month instead（改到下個月撥款）——instead 對照的就是 A 的「提交當月就撥款」。A 同時接上前後兩句。",
                    "evidence": [[0, 0], [0, 2]],
                    "wrong": [
                        None,
                        "5 日比 15 日早，不是 later date；期限提前也不會讓人多出時間",
                        "說逾期就不受理；但下一句說逾期的申請只是改到下個月撥款",
                        "說紙本可以用到年底；但第一段說 10 月 1 日起 Tallyway 就取代全體員工的紙本表單",
                    ],
                    "wrongMore": [
                        None,
                        "要先比日期：舊規定是次月 15 日前，新規定是 5 日前，新期限比較早。This later date 在文中指不到任何日期；「讓大家有更多時間收集收據」也和期限提前的方向相反。",
                        "C 接在「必須在 5 日前提交」之後非常自然（截止後不受理是常見規定），本句文法、語意都對。但下一句 Claims submitted late will be repaid the following month instead 說逾期的申請照樣撥款，只是晚一個月——和「不受理」矛盾。",
                        None,
                    ],
                    "vocab": [["deadline", "截止期限"], ["currently", "目前"], ["repay", "償還；撥還（款項）"]],
                },
            },
            {
                "options": ["lately", "lateness", "late", "latter"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "詞性：late 本身就是副詞（submitted late＝逾期提交）；lately 是另一個字，意思是「最近」",
                    "why": "空格修飾 submitted，要用副詞。late 既是形容詞也是副詞，submitted late 就是「逾期提交」。前文說期限是 5 日（they need to be submitted by the 5th），插入句說準時的申請當月撥款，所以這一句講的是過了期限才交的申請改到下個月撥款（instead 對照的是「當月」）。lately 雖然是 -ly 結尾，意思卻是 recently（最近），「最近提交的申請改到下個月撥款」和前文的期限規定接不起來。",
                    "evidence": [[0, 2]],
                    "wrong": [
                        "-ly 結尾，看起來像 late 的副詞，本句文法也通；但 lately 的意思是「最近」，和前文 5 日的期限無關",
                        "名詞，不能放在 submitted 後面修飾它",
                        None,
                        "latter（後者的）是形容詞，只能放在名詞前（the latter option），不能當副詞修飾 submitted",
                    ],
                    "wrongMore": [
                        "lately 是本題的陷阱：很多學生以為形容詞加 -ly 就是副詞，所以 late → lately。但 late 本身就能當副詞（arrive late、submitted late），lately 是另一個字，意思是 recently（最近）。Claims submitted lately will be repaid the following month instead 文法通，意思卻變成「最近交的申請改到下個月撥款」——前文才說期限是 5 日、準時交的申請當月撥款，instead 對照的是「逾期」，不是「最近」。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["the following month", "次月；下個月"], ["instead", "改為；取而代之"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p6-03  article, bakery second site
    # {1} insertion (B): the next sentence (narrow lot) explains why expanding was never an option; A "close Mill
    #     Road" reads well locally but P3/P4 keep Mill Road running.
    # {2} began (D): only the dateline (June 12) and "this autumn" rule out "will begin in March".
    # {3} Until (C): the new building has room for ALL pastry production, so Mill Road can keep some only before
    #     the new site reaches full capacity.
    # {4} opportunity (A): the previous sentence says no one will be required to move.
    # Revised after the round-7 blind review: "The plan is for it to take over all ..." became "The building has room
    # for all ..." (closes the "new site too small" reading that kept "Once" alive); "however" was dropped from
    # insertion options B and D so it appears only once in the article.
    {
        "id": "r-p6-03", "type": "read", "format": "p6", "unit": "p6", "level": 3,
        "source": "hand", "reviewed": True, "v": 1,
        "docs": [
            {
                "kind": "Article",
                "head": [],
                "title": "Corvell Bakeries to Open Second Production Site",
                "paras": [
                    "HADLEY CROSS (June 12) — Corvell Bakeries, which supplies more than sixty grocery stores in the region, will open a second production site in Southmere this autumn. Until now, everything the company sells has been baked at its original bakery on Mill Road in Hadley Cross.",
                    "Orders have nearly doubled since Corvell began supplying the Tolver Markets chain two years ago, and the Mill Road ovens now run around the clock. {1} The bakery sits on a narrow lot between a school and a row of houses.",
                    "Conversion work on the new site, a former furniture warehouse, {2} in March, and the bakery is due to open in October. The building has room for all of Corvell's pastry production, so Mill Road will eventually bake only bread. {3} the new site is running at full capacity, however, Mill Road will continue to bake some pastries, said operations director Paula Brandt.",
                    "Corvell expects to hire about forty bakers and drivers for Southmere. Brandt stressed that no current employee will be required to move. Mill Road staff will be given the {4} to transfer before the jobs are advertised.",
                ],
                "zh": [
                    "HADLEY CROSS（6 月 12 日）——為本地區六十多家雜貨店供貨的 Corvell 烘焙公司，今年秋天將在 Southmere 開設第二座生產基地。到目前為止，該公司販售的所有產品，都是在 Hadley Cross 磨坊路（Mill Road）的原始烘焙廠烘製的。",
                    "自從兩年前 Corvell 開始供貨給 Tolver Markets 連鎖超市以來，訂單幾乎翻倍，磨坊路的烤爐現在日夜不停地運轉。但擴建原本的烘焙廠從來就不是可行的選項。這座烘焙廠位在一所學校和一排住宅之間的狹長土地上。",
                    "新廠址是一座舊家具倉庫，改建工程已於 3 月開工，新烘焙廠預定 10 月啟用。這棟建築容得下 Corvell 所有的糕點生產，磨坊路最後只會做麵包。不過，營運總監 Paula Brandt 表示，在新廠全面運轉之前，磨坊路仍會繼續烘焙一些糕點。",
                    "Corvell 預計為 Southmere 新廠招募約四十名烘焙師傅和司機。Brandt 強調，現有員工都不會被要求調動。磨坊路的員工將在職缺公開招募之前，獲得調職的機會。",
                ],
            }
        ],
        "questions": [
            {
                "options": [
                    "The company plans to close the Mill Road bakery once the new site opens.",
                    "Expanding the original bakery was never an option.",
                    "For years, the company has split its baking between two sites.",
                    "The ovens are switched off every night.",
                ],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "句子插入：插入句要能被下一句「夾在學校和住宅之間的狹長土地」解釋，也不能和第三、四段矛盾",
                    "why": "前一句說訂單翻倍、烤爐日夜運轉；下一句說烘焙廠位在學校和住宅之間的狹長土地上——這是在解釋「為什麼不能在原址擴建」。B 正好接在中間：產能不夠，原址又沒辦法擴建，所以才要另開新廠（第一段）。A 說要關閉磨坊路的廠，要讀到第三、四段（磨坊路之後只做麵包、員工不必調動）才能排除。",
                    "evidence": [[0, 1], [0, 2], [0, 3]],
                    "wrong": [
                        "接在「烤爐日夜運轉」和「土地狹小」之間也讀得通；但第三段說磨坊路之後只做麵包，還會繼續烤一些糕點——它沒有要關",
                        None,
                        "說一直分兩處生產；但第一段說到目前為止所有產品都在磨坊路的原始烘焙廠烘製",
                        "說烤爐每晚關掉；和前一句的 run around the clock（日夜運轉）矛盾",
                    ],
                    "wrongMore": [
                        "A 是近乎正確誘答：放進空格後，下一句「烘焙廠夾在學校和住宅之間的狹長土地上」剛好像在說明為什麼要關廠，第二段自己讀起來很順。決定性線索在第三段：The building has room for all of Corvell's pastry production, so Mill Road will eventually bake only bread，以及 Mill Road will continue to bake some pastries；第四段也說現有員工不必調動。磨坊路會繼續營運，只是最後改成只做麵包。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["around the clock", "日夜不停地"], ["lot", "（一塊）土地；地段"], ["supply", "供貨給"]],
                },
            },
            {
                "options": ["will begin", "has begun", "had begun", "began"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "時態：要用報導日期（6 月 12 日）判斷 3 月已經過去",
                    "why": "句子本身只有 in March，沒說是哪一年的 3 月。第一段開頭的報導日期是 June 12，新廠 this autumn 開幕、本段又說 10 月啟用——所以改建工程是今年 3 月已經開始的事，用過去式 began。",
                    "evidence": [[0, 0], [0, 2]],
                    "wrong": [
                        "will begin in March … due to open in October 本句自己讀起來沒問題；但報導日期是 6 月 12 日，3 月已經過了",
                        "現在完成式不能和 in March 這種明確的過去時間連用",
                        "過去完成式要有一個更早的過去參照點；而且同一句的另一半是現在式 is due to open",
                        None,
                    ],
                    "wrongMore": [
                        "will begin 是近乎正確誘答：「3 月動工、10 月啟用」單看本句很順。但第一段開頭的 (June 12) 是報導日期，第一段也說新廠 this autumn 開幕；如果是明年 3 月才動工，就不可能今年秋天啟用。要先回第一段確認報導日期，才能判斷 3 月已經過去。",
                        "很多學生覺得「已經開始了」就該用 has begun；但英文的現在完成式不能接 in March、last year 這類明確的過去時間，要說 began in March，或不寫時間說 has already begun。",
                        None,
                        None,
                    ],
                    "vocab": [["conversion", "改建；改裝"], ["warehouse", "倉庫"], ["be due to", "預定（做某事）"]],
                },
            },
            {
                "options": ["Once", "Even though", "Until", "In case"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "連接詞：Until（在…之前一直）——要和前一句「新廠容得下所有糕點生產」對得上",
                    "why": "前一句說新廠的建築 has room for all of Corvell's pastry production，磨坊路最後只會做麵包。本句說磨坊路會繼續烤一些糕點——這只能是過渡期：在新廠全面運轉「之前」，所以用 Until。用 Once 就變成新廠全面運轉「之後」磨坊路還在烤糕點；但新廠容得下全部糕點生產，全面運轉後沒有理由再讓磨坊路烤，和前一句矛盾。",
                    "evidence": [[0, 2]],
                    "wrong": [
                        "Once … is running at full capacity 本句很順；但前一句說新廠容得下全部糕點生產、磨坊路最後只做麵包，全面運轉後磨坊路不會再烤糕點",
                        "even though 把「新廠正在全面運轉」當成事實；但新廠 10 月才啟用",
                        None,
                        "in case 是「以防」，「以防新廠全面運轉，磨坊路繼續烤糕點」說不通",
                    ],
                    "wrongMore": [
                        "Once 是近乎正確誘答：「新廠全面運轉之後怎樣」是這類報導最常見的說法，本句單看文法、語意都對；如果新廠容量不夠，「全面運轉後磨坊路仍要補烤一些糕點」也說得通。前一句把這條路關掉了：The building has room for all of Corvell's pastry production, so Mill Road will eventually bake only bread。新廠容得下全部糕點，全面運轉後就由新廠全包；磨坊路繼續烤糕點只可能發生在那之前，所以是 Until。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["full capacity", "全面運轉；滿載產能"], ["eventually", "最後、終究"], ["operations director", "營運總監"]],
                },
            },
            {
                "options": ["opportunity", "obligation", "instruction", "necessity"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "字彙：be given the opportunity to V（獲得…的機會）——前一句說沒有人會被要求調動",
                    "why": "前一句 Brandt stressed that no current employee will be required to move（現有員工都不會被要求調動），所以磨坊路員工得到的是「可以選擇」調職的機會，不是義務或指示。",
                    "evidence": [[0, 3]],
                    "wrong": [
                        None,
                        "「被賦予調職的義務」本句說得通；但前一句說沒有人會被要求調動",
                        "「接到調職的指示」同樣和前一句的「不會被要求調動」矛盾",
                        "necessity 不和 be given the … to V 搭配，意思也和前一句矛盾",
                    ],
                    "wrongMore": [
                        None,
                        "obligation 在本句單看是通的：公司開新廠、先調老員工過去支援，很合理。決定性線索在前一句 no current employee will be required to move——既然不強制，磨坊路員工拿到的只能是「可以選擇調職」的 opportunity。",
                        None,
                        None,
                    ],
                    "vocab": [["stress", "強調"], ["transfer", "調職；調動"], ["advertise", "公開招募（職缺）"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ r-p6-04  letter, magazine subscription
    # {1} Unlike (A): P1 says the printed copy often arrives a week late, so "Like" contradicts it.
    # {2} insertion (C): the next sentence's refund only makes sense if the new rate covers renewals; D ($96 print)
    #     is ruled out by P3 ($72 + $30).
    # {3} who (D): remove "our records show"; the gap is the subject of "have paid" (whom = hypercorrection).
    # {4} Should (B): "Would you prefer" reads as a question, but a comma and an imperative follow.
    # Revised after the round-7 blind review: the letter now opens with a salutation (its own paragraph, index 0), so
    # every evidence index moved up by one; "第一段" in the explanations means the first body paragraph.
    {
        "id": "r-p6-04", "type": "read", "format": "p6", "unit": "p6", "level": 3,
        "source": "hand", "reviewed": True, "v": 1,
        "docs": [
            {
                "kind": "Letter",
                "head": [["From", "The Packhouse Journal, Subscriber Services"], ["Date", "September 15"]],
                "title": None,
                "paras": [
                    "Dear Subscriber,",
                    "Many readers have told us that their printed copy of The Packhouse Journal often arrives a week or more after the first of the month. Our printing and postage costs have also risen sharply. Beginning with the January issue, we will therefore make two changes to your subscription.",
                    "First, the Journal will become a digital publication. {1} the printed magazine, the digital edition will reach you on the first of every month. Because it costs far less to produce, the annual subscription price will fall from $96 to $72. {2} Subscribers {3} our records show have already paid for next year will receive a refund of the difference.",
                    "Second, printed copies will be mailed only to readers who request them. {4} you prefer to keep receiving the magazine by mail, please check the box on the enclosed form and return it by November 30. The print option costs an extra $30 a year.",
                    "Lena Marsh, Subscriber Services, The Packhouse Journal",
                ],
                "zh": [
                    "親愛的訂戶：",
                    "許多讀者告訴我們，他們訂的《Packhouse Journal》紙本常常在每月 1 日之後一週甚至更久才送到。我們的印刷和郵寄成本也大幅上漲。因此，從一月號起，我們將對您的訂閱做兩項調整。",
                    "第一，本刊將改為數位出版。和紙本雜誌不同，數位版會在每月 1 日準時送到您手上。由於製作成本低得多，年度訂閱費將從 96 美元降為 72 美元。新費率適用於所有訂閱，包括已經續訂的訂閱。根據我們的紀錄，已經預付明年訂閱費的訂戶將獲退還差額。",
                    "第二，紙本只會寄給提出要求的讀者。如果您希望繼續以郵寄方式收到雜誌，請勾選隨函表格上的方框，並在 11 月 30 日前寄回。紙本選項每年另加 30 美元。",
                    "《Packhouse Journal》訂戶服務部 Lena Marsh",
                ],
            }
        ],
        "questions": [
            {
                "options": ["Unlike", "Like", "Despite", "Except for"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "介系詞：Unlike（和…不同）——要回第一段看紙本是不是每月 1 日送到",
                    "why": "第一段說讀者反映紙本 often arrives a week or more after the first of the month（常常晚一週以上才到）。本句說數位版會在每月 1 日送到——這和紙本「不同」，所以是 Unlike。本句單看，Like 和 Unlike 都通；要回第一段才知道紙本常遲到。",
                    "evidence": [[0, 1], [0, 2]],
                    "wrong": [
                        None,
                        "「和紙本一樣在 1 日送到」本句通順；但第一段說紙本常常晚一週以上才到",
                        "despite 表讓步，「儘管有紙本雜誌，數位版會在 1 日送到」說不通",
                        "except for 是「除了…之外（排除）」，放在句首不知道要排除什麼",
                    ],
                    "wrongMore": [
                        None,
                        "Like 是近乎正確誘答：Like the printed magazine, the digital edition will reach you on the first of every month 文法完全對，也很像在安撫讀者「一切照舊」。但信一開頭就說讀者抱怨紙本 often arrives a week or more after the first of the month——紙本並不是 1 日送到；數位版準時送到，正是它和紙本「不同」的地方。",
                        None,
                        None,
                    ],
                    "vocab": [["printed copy", "紙本"], ["postage", "郵資"], ["digital edition", "數位版"]],
                },
            },
            {
                "options": [
                    "Readers who have already renewed, however, will keep paying the old rate.",
                    "This is the first price increase in the magazine's history.",
                    "The new rate will apply to all subscriptions, including renewals.",
                    "The print edition will stay at its current price of $96.",
                ],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": True, "S": True, "band": "hard"},
                "explain": {
                    "point": "句子插入：要接得上前一句的降價，也要接得上下一句的「退還差額」",
                    "why": "前一句說年費從 96 美元降為 72 美元；下一句說已經預付明年訂閱費的訂戶會拿到 a refund of the difference（差額退款）——只有新費率也適用於已續訂的訂閱，才會有差額可退。C 正好把降價和退款接起來。",
                    "evidence": [[0, 2], [0, 3]],
                    "wrong": [
                        "說已續訂的讀者照舊價付費；但下一句說他們會拿到差額退款",
                        "說這是首次漲價；但前一句說價格從 96 美元降到 72 美元",
                        None,
                        "說紙本維持 96 美元；但第三段說紙本是在 72 美元之外每年另加 30 美元（共 102 美元）",
                    ],
                    "wrongMore": [
                        "A 是最強的誘答：降價之後補一句「已續訂者照舊價計算」是很常見的規定，接在前一句後面非常順。但下一句 Subscribers who our records show have already paid for next year will receive a refund of the difference——已經付了錢的人會拿回差額，表示新價格也適用於他們，和 A 正好相反。",
                        None,
                        None,
                        "D 接在「年費降到 72 美元」之後也讀得通（數位版降價、紙本維持原價）。但第三段說 The print option costs an extra $30 a year——紙本是在 72 美元之外另加 30 美元，共 102 美元，不是 96 美元。要讀到第三段並算一下才能排除。",
                    ],
                    "vocab": [["annual", "年度的；每年的"], ["refund", "退款"], ["difference", "差額"]],
                },
            },
            {
                "options": ["whom", "whose", "which", "who"],
                "answer": 3,
                "ldbs": {"L": True, "D": False, "B": True, "S": True, "band": "medium"},
                "explain": {
                    "point": "關係代名詞：拿掉插入語 our records show，空格是 have paid 的主詞 → who",
                    "why": "把插在中間的 our records show（根據我們的紀錄）拿掉，句子是 Subscribers ___ have already paid for next year will receive a refund——空格後面直接接動詞 have paid，所以空格是關係子句的主詞，用 who。",
                    "evidence": [[0, 2]],
                    "wrong": [
                        "whom our records show 看起來像受格（our records 是主詞）；但 our records show 是插入語，空格其實是 have paid 的主詞",
                        "whose 後面要接它所修飾的名詞（whose subscriptions …）；這裡接的是插入語 our records show",
                        "which 不用來指人（Subscribers）",
                        None,
                    ],
                    "wrongMore": [
                        "whom 是過度矯正的陷阱：空格後面緊接著 our records，看起來 our records 是主詞、空格是 show 的受詞，所以選 whom。但 show 後面真正的受詞是整個子句（[that] they have already paid …），our records show 只是插在中間的插入語。拿掉它：Subscribers who have already paid for next year will receive a refund——主詞要用 who。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["record", "紀錄"], ["subscriber", "訂戶"]],
                },
            },
            {
                "options": ["Would", "Should", "Had", "Were"],
                "answer": 1,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "條件句倒裝：Should you prefer … = If you prefer …，後面接祈使句",
                    "why": "逗號後面是祈使句 please check the box …，前面要是一個條件子句。Should + 主詞 + 原形動詞就是省略 if 的條件句（＝If you prefer …）。Would you prefer 是問句的形式，後面不能用逗號接祈使句。",
                    "evidence": [[0, 3]],
                    "wrong": [
                        "Would you prefer to keep receiving the magazine by mail 單看像禮貌的問句；但後面是逗號加祈使句 please check，不是問號",
                        None,
                        "Had 倒裝要接 p.p.（Had you preferred），而且是與過去事實相反的假設；這裡是對未來的一般條件",
                        "Were 倒裝要寫成 Were you to prefer；Were you prefer 不合文法",
                    ],
                    "wrongMore": [
                        "Would 是近乎正確誘答：Would you prefer to keep receiving the magazine by mail? 是很自然的禮貌問句，空格前後幾個字讀起來完全對。但這裡沒有問號，逗號後面直接接 please check the box——前半要是條件子句，只有 Should you prefer（＝If you prefer）可以。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["enclosed", "隨函附上的"], ["by mail", "以郵寄方式"], ["option", "選項"]],
                },
            },
        ],
    },
]
