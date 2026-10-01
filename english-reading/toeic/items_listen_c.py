# Round 5 listening items, written under WRITING_RULES.md (sections 2, 3, 5, 6, 7.1).
# 5 qr (Part 2 style), 2 conv (Part 3 style; l-conv-10 has three named speakers), 1 talk (Part 4 style).
# Scripts are in US English even when a British voice reads them. All content is original; names of people,
# firms and places are invented.
# `ldbs` on each question is the writer's self-test (WRITING_RULES 3.4: L local / D distance / B belief /
# S two steps) and its band; the blind reviewer sets the final band and `level`. `level` here is the highest
# self-test band in the item (easy 1, medium 2, hard 3).
# reviewed stays False until the items pass a blind review and every mp3 has been heard.
# Scenes (new against l-qr-01..17, l-conv-01..08, l-talk-01..04): airline rebooking, awards-dinner seating,
# factory inspection, interview schedule, car rental, dental-clinic reminders, agency demo video, hotel banquet room.

ITEMS = [
    # ------------------------------------------------------------------ qr (Part 2)
    # l-qr-18  qr-wh, self-test medium. Condition: the morning departure has been canceled.
    # near-correct: (A) "The morning one, at ten." names a flight (form-correct) but is the canceled one.
    # (B) answers a seat preference (right topic, wrong question). Key (C) is a direct answer.
    {
        "id": "l-qr-18", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-18", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "af_sarah", "text": "Which flight is Mr. Brandt taking to the sales meeting, now that the morning departure has been canceled?",
                 "say": "Which flight is Mister Brandt taking to the sales meeting, now that the morning departure has been canceled?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "The morning one, at ten.", "say": "The morning one, at ten o'clock."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "He prefers an aisle seat."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "The one that leaves right after lunch."},
            ],
        },
        "transcriptZh": [
            "既然早上那班被取消了，Brandt 先生要搭哪一班飛機去參加業務會議？",
            "早上那班，十點的。",
            "他喜歡坐走道的位子。",
            "午餐後馬上起飛的那一班。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
            "explain": {
                "point": "Which 問句帶條件：用條件刪掉矛盾的答案",
                "why": "問早班取消後搭哪一班 → 回 the one that leaves right after lunch（午餐後的那班）：指出另一班，不是已取消的 morning。",
                "evidence": [3],
                "wrong": ["形式對情境錯：指出的正是被取消的早班", "答錯問句類型：講座位偏好，不是哪一班", None],
                "wrongMore": ["Which 問句回 The morning one 形式完全對；但問句後半 the morning departure has been canceled 已經說早班沒了。", None, None],
                "vocab": [["departure", "出發班次"], ["cancel", "取消"], ["aisle seat", "走道座位"]],
            },
        }],
    },
    # l-qr-19  qr-wh, self-test hard. Condition: the list "has doubled from a hundred".
    # near-correct: (A) "The list is still a hundred." repeats the figure but contradicts "has doubled".
    # (C) repeats chairs. Key (B) is indirect: the replies are not in yet, so the count is not fixed.
    {
        "id": "l-qr-19", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-19", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "bm_lewis", "text": "How many chairs should we set up for the awards dinner, now that the guest list has doubled from a hundred?"},
                {"file": "a.mp3", "who": "W", "voice": "bf_emma", "text": "The list is still a hundred."},
                {"file": "b.mp3", "who": "W", "voice": "bf_emma", "text": "The final replies aren't due until Friday."},
                {"file": "c.mp3", "who": "W", "voice": "bf_emma", "text": "The chairs are stacked in the storage room."},
            ],
        },
        "transcriptZh": [
            "既然頒獎晚宴的賓客名單已經從一百人加倍了，我們要擺幾張椅子？",
            "名單還是一百人。",
            "最後的回覆要到星期五才截止。",
            "椅子都疊放在儲藏室裡。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "How many 問句：答案可以是「人數還沒定」",
                "why": "問名單從一百人加倍後要擺幾張椅子 → 回 final replies aren't due until Friday：回覆還沒收齊，人數還沒確定。",
                "evidence": [2],
                "wrong": ["形式對情境錯：說的是加倍前的一百人", None, "同字陷阱：重複 chairs，答的是椅子放哪裡"],
                "wrongMore": ["How many 問句回一個數字，形式完全對；但問句說名單已從一百人加倍，A hundred 是舊數字，不夠用。", None, None],
                "vocab": [["set up", "布置、擺設"], ["guest list", "賓客名單"], ["replies", "回覆（出席與否）"]],
            },
        }],
    },
    # l-qr-20  qr-yesno, self-test hard. Condition: inspectors arrive on Friday.
    # near-correct: (B) "Yes" + repeats factory; (C) "No" is a form-correct opening but the inspectors are due
    # Friday, not last week. Key (A) is indirect: not even shipped, so No.
    {
        "id": "l-qr-20", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-20", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "Will the replacement parts reach the factory before the inspectors arrive on Friday?"},
                {"file": "a.mp3", "who": "W", "voice": "af_bella", "text": "The supplier hasn't even shipped them yet."},
                {"file": "b.mp3", "who": "W", "voice": "af_bella", "text": "Yes, the factory is fully staffed."},
                {"file": "c.mp3", "who": "W", "voice": "af_bella", "text": "No, the inspectors were here last week."},
            ],
        },
        "transcriptZh": [
            "替換零件會在檢查員星期五來之前送到工廠嗎？",
            "供應商甚至還沒把零件寄出來。",
            "會，工廠的人手很充足。",
            "不會，檢查員上星期就來過了。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 0,
            "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
            "explain": {
                "point": "Yes/No 問句：用「根本還沒出貨」暗示答案是 No",
                "why": "問零件會不會在週五前到 → 回 hasn't even shipped them yet（還沒出貨）：等於說不會在檢查員來之前到。",
                "evidence": [1],
                "wrong": [None, "同字陷阱：Yes 加上重複 factory，答的是人手", "形式對情境錯：No 後面說檢查員上週來過，但問句說他們週五才到"],
                "wrongMore": [
                    None,
                    "Yes 接得上 Will … 問句，又重複 factory；但後半講人手充足，沒有說零件會不會到。",
                    "No 也是合理的開頭；但問句說 the inspectors arrive on Friday，是還沒發生的事，上週來過的說法與它矛盾。",
                ],
                "vocab": [["replacement parts", "替換零件"], ["inspector", "檢查員"], ["ship", "出貨、寄出"]],
            },
        }],
    },
    # l-qr-21  qr-yesno, self-test easy (the batch's easy qr). Direct key; the others comment on the candidates / answer where.
    {
        "id": "l-qr-21", "type": "listen", "format": "qr", "unit": "qr-yesno", "level": 1,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-qr-21", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "W", "voice": "bf_emma", "text": "Do you have the schedule for next week's interviews?"},
                {"file": "a.mp3", "who": "M", "voice": "bm_george", "text": "The candidates were very impressive."},
                {"file": "b.mp3", "who": "M", "voice": "bm_george", "text": "In the second-floor meeting room."},
                {"file": "c.mp3", "who": "M", "voice": "bm_george", "text": "Yes, I'll e-mail it to you right now."},
            ],
        },
        "transcriptZh": [
            "你有下週面試的時程表嗎？",
            "那些應徵者都很出色。",
            "在二樓的會議室。",
            "有，我現在就用電子郵件寄給你。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 2,
            "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
            "explain": {
                "point": "Do you have 問句：直接回 Yes",
                "why": "問有沒有下週面試的行程表 → 回 Yes, I'll e-mail it to you：有，而且馬上寄。另外兩個回答的是應徵者的評價和地點。",
                "evidence": [3],
                "wrong": ["答非所問：講的是應徵者的評價，不是有沒有時程表", "答錯問句類型：講的是地點，不是有沒有時程表", None],
                "wrongMore": [None, None, None],
                "vocab": [["schedule", "時程表"], ["candidate", "應徵者"], ["impressive", "令人印象深刻的"]],
            },
        }],
    },
    # l-qr-22  qr-indirect, self-test medium. near-correct: (A) "Yes" + a return time (form-correct, answers
    # a different question); (C) repeats location. Key (B) is indirect: it depends on the branch.
    {
        "id": "l-qr-22", "type": "listen", "format": "qr", "unit": "qr-indirect", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-qr-22", "gapMs": 900,
            "lines": [
                {"file": "q.mp3", "who": "M", "voice": "am_michael", "text": "Is there an extra charge if I return the car to a different location?"},
                {"file": "a.mp3", "who": "W", "voice": "af_sarah", "text": "Yes, you can return it any time before six.", "say": "Yes, you can return it any time before six o'clock."},
                {"file": "b.mp3", "who": "W", "voice": "af_sarah", "text": "That depends on which branch you choose."},
                {"file": "c.mp3", "who": "W", "voice": "af_sarah", "text": "Our downtown location opens at seven.", "say": "Our downtown location opens at seven o'clock."},
            ],
        },
        "transcriptZh": [
            "如果我把車還到別的地點，要另外收費嗎？",
            "有，你六點以前隨時可以還車。",
            "要看你選哪一間分店。",
            "我們市中心的據點七點開門。",
        ],
        "questions": [{
            "q": None, "options": None, "answer": 1,
            "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
            "explain": {
                "point": "Yes/No 問句：可以回「看情況」",
                "why": "問換地點還車有沒有額外費用 → 回 That depends on which branch you choose：要看選哪一間分店，不是單純 Yes 或 No。",
                "evidence": [2],
                "wrong": ["形式對情境錯：Yes 後面講還車時限，沒回答費用", None, "同字陷阱：重複 location，講的是開門時間"],
                "wrongMore": ["Yes 接得上 Is there … 問句；但後面說的是 return it any time before six，在講時限，沒有提到收不收費。", None, None],
                "vocab": [["extra charge", "額外費用"], ["depends", "取決於"], ["branch", "分店"]],
            },
        }],
    },

    # ------------------------------------------------------------------ conv (Part 3)
    # l-conv-09  conv-topic. W = practice manager (bf_emma), M = Daniel (am_eric). Nobody says "reduce no-shows";
    # the topic has to be assembled from lines 1-3. Q2 asks for the function of the reception-desk remark.
    # Q3: Monday is the trial, Thursday is the owner meeting.
    {
        "id": "l-conv-09", "type": "listen", "format": "conv", "unit": "conv-topic", "level": 2,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-09", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Daniel, I went through last quarter's numbers. About one patient in six didn't show up for an appointment."},
                {"file": "02.mp3", "who": "M", "voice": "am_eric", "text": "That's a lot of empty chairs. We only phone people the day before, and half of them never answer."},
                {"file": "03.mp3", "who": "W", "voice": "bf_emma", "text": "A text message would reach more of them. The software company says patients can even confirm by replying."},
                {"file": "04.mp3", "who": "M", "voice": "am_eric", "text": "What would it cost, though? The owner already turned down a new reception desk this year."},
                {"file": "05.mp3", "who": "W", "voice": "bf_emma", "text": "It's a small monthly fee, and it would free up Mia's afternoons for other work. Each no-show costs us more than that."},
                {"file": "06.mp3", "who": "M", "voice": "am_eric", "text": "Mia would love that. Does it work with our current scheduling program?"},
                {"file": "07.mp3", "who": "W", "voice": "bf_emma", "text": "They say it does, but I'd like to see it running first. They're offering a free two-week trial."},
                {"file": "08.mp3", "who": "M", "voice": "am_eric", "text": "Then let's start the trial on Monday. I'll bring it up with the owner at Thursday's meeting."},
                {"file": "09.mp3", "who": "W", "voice": "bf_emma", "text": "Good idea. I'll tell the company to set it up."},
            ],
        },
        "transcriptZh": [
            "Daniel，我看了上一季的數字。大約每六位病患就有一位沒有來看診。",
            "那空了不少椅子。我們只在前一天打電話，而且一半的人都不接。",
            "傳簡訊可以聯絡到更多人。軟體公司說病患甚至可以直接回覆來確認。",
            "不過要花多少錢？老闆今年已經拒絕買一張新的櫃檯了。",
            "每個月的費用不高，而且 Mia 的下午就有空做別的事。每個沒來的人讓我們損失的比這還多。",
            "Mia 一定會很高興。它能配合我們現在的排程軟體嗎？",
            "他們說可以，但我想先看到它實際運作。他們提供兩週的免費試用。",
            "那我們星期一就開始試用。星期四開會時我會跟老闆提這件事。",
            "好主意。我會請那家公司來設定。",
        ],
        "questions": [
            {
                "q": "What are the speakers mainly discussing?",
                "options": ["Hiring more reception staff", "Replacing the clinic's scheduling program", "Ways to reduce the number of people who miss their visits", "Whether to buy a new reception desk"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "主旨題：把問題和對策串起來",
                    "why": "第一句 didn't show up 是問題，接著 A text message would reach more of them 是對策 → 合起來是改述成減少沒來的人數。",
                    "evidence": [0, 1, 2],
                    "wrong": ["沒有人提到雇人：Mia 只是省下時間做別的事", "同字陷阱：scheduling program 出現過，但只問它能不能配合", None, "提到但不是問的：櫃檯是他說明預算的例子"],
                    "wrongMore": [
                        None,
                        "scheduling program 確實出現，但那是男方問新服務能不能跟它搭配，換掉程式沒有人提。",
                        None,
                        "reception desk 確實出現，但那是老闆已經拒絕的事，男方拿來說明預算態度，不是討論的主題。",
                    ],
                    "vocab": [["no-show", "沒到的人"], ["reception desk", "櫃檯"]],
                },
            },
            {
                "q": "Why does the man mention the reception desk?",
                "options": ["To hint that the boss is reluctant to pay", "To request a replacement desk", "To complain about the waiting area", "To recommend hiring more staff"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "意圖題：提這件事是為了暗示別的（老闆不想花錢）",
                    "why": "他問 What would it cost，再說 the owner already turned down a new reception desk → 暗示老闆不願花錢。",
                    "evidence": [3],
                    "wrong": [None, "字面陷阱：他不是要買桌子，而是拿它當例子", "沒有人提到候診區", "沒有人提到雇人"],
                    "wrongMore": [None, "reception desk 是他提到的東西，所以這個選項最像；但那是老闆已經拒絕的事，他只是用它說明預算態度，沒有要求換桌子。", None, None],
                    "vocab": [["turn down", "拒絕"], ["cost", "花費"]],
                },
            },
            {
                "q": "What does the man say he will do at Thursday's meeting?",
                "options": ["Begin a two-week trial", "Watch the software run", "Contact the software company", "Present the idea to management"],
                "answer": 3,
                "ldbs": {"L": True, "D": True, "B": False, "S": False, "band": "medium"},
                "explain": {
                    "point": "對準題目問的那一天和那個人",
                    "why": "試用是 on Monday；I'll bring it up with the owner at Thursday's meeting 才是星期四的事 → 向管理層提出想法。",
                    "evidence": [7],
                    "wrong": ["時間錯置：試用從星期一開始，不是星期四", "張冠李戴：想先看軟體運作的是女方", "張冠李戴：要請軟體公司設定的是女方", None],
                    "wrongMore": [
                        "start the trial 在同一句出現，很容易選；但後面的 Monday 才是它的日期，星期四要做的是 bring it up with the owner。",
                        None,
                        None,
                        None,
                    ],
                    "vocab": [["bring up", "提出（話題）"], ["trial", "試用"]],
                },
            },
        ],
    },
    # l-conv-10  conv-intent, three speakers: W = Rosa (bf_emma, UK), M1 = Tom (am_michael, US), M2 = Gareth (bm_george, UK).
    # Rosa names both men in line 1; Tom (line 2) addresses her as "Rosa". Gareth is named in line 6, Tom in line 8.
    # Q1 is the batch's easy conv question. Q2: the quote is idiomatic ("belongs in a museum" = very old); (A) is the
    # literal reading. Q3: Rosa proposes eight, Gareth objects (eight thirty), settles on eight forty-five, Rosa agrees.
    {
        "id": "l-conv-10", "type": "listen", "format": "conv", "unit": "conv-intent", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "mixed",
        "audio": {
            "dir": "audio/l-conv-10", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "bf_emma", "text": "Tom, Gareth, thanks for staying late. Our presentation for the client is at nine tomorrow, and I'm worried about the demo video."},
                {"file": "02.mp3", "who": "M1", "voice": "am_michael", "text": "Rosa, it plays fine on my laptop. The trouble is the projector in their boardroom, which only accepts an older file type."},
                {"file": "03.mp3", "who": "M2", "voice": "bm_george", "text": "I saw that projector last spring. It belongs in a museum."},
                {"file": "04.mp3", "who": "W", "voice": "bf_emma", "text": "So can we convert the video tonight?"},
                {"file": "05.mp3", "who": "M1", "voice": "am_michael", "text": "I can, with free software. It takes about two hours to run, though, so I'd have to start it before I leave."},
                {"file": "06.mp3", "who": "W", "voice": "bf_emma", "text": "Please do. Gareth, I'd like you to test the new file on their projector before we start. Could you be there at eight?"},
                {"file": "07.mp3", "who": "M2", "voice": "bm_george", "text": "The building doesn't open until eight thirty, I'm afraid. How about eight forty-five, in the lobby?"},
                {"file": "08.mp3", "who": "W", "voice": "bf_emma", "text": "That works. The presentation is at nine, so we'll have fifteen minutes. Tom, text me when the conversion finishes tonight."},
                {"file": "09.mp3", "who": "M1", "voice": "am_michael", "text": "Will do. I'll start it as soon as we're done here."},
            ],
        },
        "transcriptZh": [
            "Tom、Gareth，謝謝你們留下來加班。我們明天九點要對客戶簡報，我擔心示範影片。",
            "Rosa，它在我的筆電上播得很順。問題出在他們會議室的投影機，它只接受比較舊的檔案格式。",
            "我去年春天看過那台投影機。它根本該放進博物館。",
            "那我們今晚可以把影片轉檔嗎？",
            "可以，用免費軟體就行。不過它要跑大約兩小時，所以我離開前就得先開始。",
            "麻煩你了。Gareth，我想請你在我們開始前，用他們的投影機測試新檔案。你八點能到那裡嗎？",
            "恐怕不行，那棟大樓八點半才開門。八點四十五分在大廳碰面如何？",
            "可以。簡報九點開始，所以我們會有十五分鐘。Tom，轉檔完成時今晚傳訊息給我。",
            "沒問題。我們談完我就開始。",
        ],
        "questions": [
            {
                "q": "What is Rosa worried about?",
                "options": ["Whether a video will play properly", "Whether the software will cost too much", "Whether the file conversion will take too long", "Whether the building will open early enough"],
                "answer": 0,
                "ldbs": {"L": False, "D": False, "B": False, "S": False, "band": "easy"},
                "explain": {
                    "point": "問題題：worried about 後面就是答案",
                    "why": "Rosa 在開頭說 I'm worried about the demo video，Tom 接著說投影機只收舊格式 → 她擔心影片播不順。",
                    "evidence": [0, 1],
                    "wrong": [None, "方向相反：Tom 說用免費軟體就行", "張冠李戴：兩小時轉檔是 Tom 說的作業時間，不是 Rosa 擔心的事", "張冠李戴：大樓八點半才開門是 Gareth 提到的，不是 Rosa 擔心的事"],
                    "vocab": [["demo", "示範"], ["worried", "擔心"]],
                },
            },
            {
                "q": "What does Gareth imply when he says, \"It belongs in a museum\"?",
                "options": ["The projector should be donated to a museum", "The projector is badly out of date", "The client displays old equipment in the boardroom", "He saw the projector at a museum last spring"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "引句題：belongs in a museum 是說太舊",
                    "why": "前一句說投影機只收 an older file type，Gareth 接著說 It belongs in a museum → 不是真的放博物館，而是說它老舊過時。",
                    "evidence": [1, 2],
                    "wrong": ["字面陷阱：照字面讀成要把它捐給博物館", None, "語境矛盾：沒有人說客戶會陳列舊設備", "同字陷阱：重複 museum、last spring，但他看的是客戶會議室的投影機"],
                    "wrongMore": [
                        "belongs in 照字面是「應該放在」；但這是誇張的說法，前一句已經說它只收舊格式，意思是太老了。",
                        None,
                        None,
                        "I saw that projector last spring 的 that projector 指前一句客戶會議室裡的那台，不是在博物館看到的。",
                    ],
                    "vocab": [["boardroom", "董事會議室"], ["file type", "檔案格式"], ["belongs in a museum", "老舊過時（俚語）"]],
                },
            },
            {
                "q": "When will Gareth most likely test the new file at the client's building?",
                "options": ["At eight o'clock", "At eight thirty", "At a quarter to nine", "At nine o'clock"],
                "answer": 2,
                "ldbs": {"L": True, "D": True, "B": False, "S": True, "band": "hard"},
                "explain": {
                    "point": "跨說話者：提議、修正、同意，問最後的時間",
                    "why": "Rosa 提議 eight；Gareth 說 eight thirty 才開門，改 eight forty-five；Rosa 回 That works → 八點四十五。",
                    "evidence": [5, 6, 7],
                    "wrong": ["提到但不是問的：八點是 Rosa 原本的提議，被 Gareth 否決", "時間錯置：八點半只是大樓開門的時間", None, "時間錯置：九點是簡報開始的時間"],
                    "wrongMore": [
                        "Could you be there at eight 是第一次提議；但 Gareth 接著說大樓八點半才開，並改成八點四十五，Rosa 同意。",
                        "The building doesn't open until eight thirty 是限制條件，不是約好的時間；他提議的是之後的八點四十五。",
                        None,
                        "The presentation is at nine 是簡報開始的時間，測試要在那之前完成；Rosa 還說 we'll have fifteen minutes。",
                    ],
                    "vocab": [["convert", "轉檔、轉換"], ["lobby", "大廳"]],
                },
            },
        ],
    },

    # ------------------------------------------------------------------ talk (Part 4)
    # l-talk-05  talk-next. Voicemail from a hotel events coordinator. Q1 purpose; Q2 the drawback after "but";
    # Q3 sequence: look over the plan (line 5) comes before ordering (Thursday) and before calling back (line 7).
    {
        "id": "l-talk-05", "type": "listen", "format": "talk", "unit": "talk-next", "level": 3,
        "source": "hand", "reviewed": True, "v": 1, "accent": "us",
        "audio": {
            "dir": "audio/l-talk-05", "gapMs": 500,
            "lines": [
                {"file": "01.mp3", "who": "W", "voice": "af_sarah", "text": "Hello, Mr. Alvarez, this is Priya Nair at the Linden Hotel, calling about your retirement dinner on the twentieth.",
                 "say": "Hello, Mister Alvarez, this is Priya Nair at the Linden Hotel, calling about your retirement dinner on the twentieth."},
                {"file": "02.mp3", "who": "W", "voice": "af_sarah", "text": "The Garden Room is no longer available, because a pipe burst there on Sunday."},
                {"file": "03.mp3", "who": "W", "voice": "af_sarah", "text": "I can offer you the Skyline Room on the top floor instead, at the same price. It's bigger, but it has no built-in microphone system."},
                {"file": "04.mp3", "who": "W", "voice": "af_sarah", "text": "Our audio company can supply one, but they need your order by Thursday."},
                {"file": "05.mp3", "who": "W", "voice": "af_sarah", "text": "Before you order anything, please look over the floor plan I e-mailed this morning."},
                {"file": "06.mp3", "who": "W", "voice": "af_sarah", "text": "I'll hold the Skyline Room until Friday. After that, I'll have to offer it to another client."},
                {"file": "07.mp3", "who": "W", "voice": "af_sarah", "text": "Please call me back at the front desk once you've seen the plan."},
            ],
        },
        "transcriptZh": [
            "Alvarez 先生您好，我是 Linden 飯店的 Priya Nair，打來是為了您二十號的退休晚宴。",
            "Garden 廳已經不能使用了，因為星期天那裡有一根水管破裂。",
            "我可以改提供頂樓的 Skyline 廳給您，價格一樣。它比較大，但沒有內建的麥克風系統。",
            "我們的音響公司可以提供一套，但他們需要您在星期四前下單。",
            "在您訂任何東西之前，請先看一下我今天早上用電子郵件寄出的平面圖。",
            "我會替您保留 Skyline 廳到星期五。之後我就得把它提供給別的客戶了。",
            "看過平面圖後，請打櫃檯的電話給我。",
        ],
        "questions": [
            {
                "q": "Why is the speaker calling?",
                "options": ["To confirm a payment for the dinner", "To suggest another venue for an event", "To arrange repairs to a banquet room", "To recommend an audio company"],
                "answer": 1,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "目的題：原因和提議串起來看",
                    "why": "no longer available 後接 I can offer you the Skyline Room instead → 提議另一個場地。",
                    "evidence": [1, 2],
                    "wrong": ["沒有人提到付款", None, "提到但不是問的：水管破裂是房間不能用的原因", "提到但不是問的：音響公司是之後的附帶建議"],
                    "wrongMore": [
                        None,
                        None,
                        "a pipe burst 確實出現，但那是 Garden Room 不能用的原因；她打電話是來提供另一個房間，不是安排維修。",
                        "audio company 出現在第四句，是配合新房間的附帶資訊，不是來電的目的。",
                    ],
                    "vocab": [["offer", "提供"], ["no longer available", "不再能使用"]],
                },
            },
            {
                "q": "What is mentioned as a drawback of the Skyline Room?",
                "options": ["It has to be booked by Thursday", "It was damaged by a burst pipe", "It is smaller than the original room", "It does not come with sound equipment"],
                "answer": 3,
                "ldbs": {"L": True, "D": False, "B": True, "S": False, "band": "medium"},
                "explain": {
                    "point": "缺點題：but 後面才是缺點",
                    "why": "She says the room is bigger, but it has no built-in microphone system → 改述成沒有附音響設備。",
                    "evidence": [2],
                    "wrong": ["時間錯置：星期四是音響公司要訂單的期限", "張冠李戴：水管破裂的是 Garden Room", "方向相反：她說 Skyline 廳比較大", None],
                    "wrongMore": [
                        "Thursday 確實出現，但那是 they need your order by Thursday，指音響公司；Skyline 廳是保留到 Friday。",
                        "a pipe burst 確實出現，但發生在 Garden Room，Skyline 廳沒有受損。",
                        None,
                        None,
                    ],
                    "vocab": [["burst", "爆裂"], ["built-in", "內建的"]],
                },
            },
            {
                "q": "What does the speaker ask the listener to do first?",
                "options": ["Review the layout of a room", "Call the hotel's front desk", "Place an order with the audio company", "Let the hotel know by Friday"],
                "answer": 0,
                "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
                "explain": {
                    "point": "順序題：before、once 決定先做哪一件",
                    "why": "Before you order anything 先 look over the floor plan；once you've seen it 才 call → 先看平面圖。",
                    "evidence": [4, 6],
                    "wrong": [None, "順序錯置：打電話要等 once you've seen the plan 之後", "順序錯置：下單要等看過平面圖之後（Before you order）", "時間錯置：星期五是她替他保留房間的期限"],
                    "wrongMore": [
                        None,
                        "她確實請他打電話給 front desk，所以很像；但那是 once you've seen the plan，要在看完平面圖之後。",
                        "by Thursday 是音響公司的期限；但她說 Before you order anything，先看平面圖才輪到下單。",
                        "Friday 是 I'll hold the Skyline Room until Friday，是她保留房間的期限，她沒有要他在星期五前通知。",
                    ],
                    "vocab": [["floor plan", "平面圖"], ["hold", "保留"]],
                },
            },
        ],
    },
]
