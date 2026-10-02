# Review: lessons/p6.json and lessons/p7-triple.json

Scope: every line of both lessons, read against lessons/STYLE.md, WRITING_RULES.md section 8 (including 8.0) and the reviewed lesson lessons/connect.json. Both files pass `lessons/check.py`. I also compared the lesson examples with the three Part 7 sets already in items_read_b.py (no Part 6 items exist in the bank yet, so nothing could be cross-checked there).

How to read this file: each issue gives the file, the field path, the problem, and an exact replacement. Where the field is an `[English, Chinese]` pair, both are given. Replacement lengths were counted by hand against the STYLE.md limits (lead 40, step 25, body 45, example 22, why 35, trap 40 words).

## mustFix summary

1. p6.json `lead`: states the workbook's own format choices ("most take a word or phrase; one takes a whole sentence", "often") as facts about the test. 8.0 says type counts are our settings.
2. p6.json `rules[0].ex[1]`: the tense is not forced. "has opened" (soft opening, ceremony later) is also acceptable, so the example does not show that the other sentence decides.
3. p7-triple.json `rules[4].ex[0]`: the example teaches "address = speak to / write an address on", which are exactly the two distractors of the bank item r-p7-03 (answer "deal with"). It gives that item away.
4. p7-triple.json `rules[4].ex[2]`: the Chinese gloss "處理" is the wrong sense for "covers sales", and the contrast "not hides" is artificial.
5. p7-triple.json `rules[5].body`: the NOT rule says to look for each option in the documents and pick the one you "cannot find". Correct options are reworded and wrong options can be contradicted rather than absent, so this misleads.

---

## lessons/p6.json

### P6-1 mustFix: lead
Problem: "Most take a word or phrase; one takes a whole sentence" is a count of question types. 8.0 supports "four blanks" (Questions 131-134) and the instruction line "A word, phrase, or sentence is missing", but its last bullet says how many of each type appear is our setting, not an official specification. "often in another sentence" is also a frequency claim; the difficulty described in 8.1 is the workbook's own judgment.
Replace with:
- EN: `One short business document with four blanks. A blank may need a word, a phrase or a whole sentence. The sentence with a blank may accept several options, so the deciding clue can be in another sentence or paragraph.`
- ZH: `一份簡短的商業文件，有四個空格。空格可能要填一個字、一個片語或一整句。有空格的句子可能接受好幾個選項，所以決定答案的線索可能在另一句或另一段。`

### P6-2 shouldFix: steps[0]
Problem: "the date" assumes every text has one. The 8.0 sample e-mail has only To / From / Subject. "寫的人" is colloquial.
Replace with:
- EN: `Read from the top, not just the sentence with the blank. Note any date, who is writing and what is changing.`
- ZH: `從頭讀，不要只讀有空格的那一句。注意文中有沒有日期，也注意是誰寫的、有什麼變動。`

### P6-3 shouldFix: steps[1]
Problem: teaching gap. 8.0 says the sample's first two blanks were word form and a fixed phrase, which are decided inside their own sentence. The step only says what to do when several options fit, so a learner may over-read. Add the "only one fits" case.
Replace with:
- EN: `For a word blank, try each option in its sentence. If only one fits, take it. If several fit, look before and after.`
- ZH: `字詞空格：把每個選項放進句子試試。只有一個通就選它；好幾個都通，就往前後找線索。`

### P6-4 shouldFix (minor): steps[2]
Problem: "any sentence after it" then "connect to both" is inconsistent when nothing follows the blank (the 8.0 sample's sentence blank is the last sentence of the body).
Replace with:
- EN: `For the sentence blank, read the sentence before it and the one after it, if there is one. The right option must connect to each.`
- ZH: `句子空格：讀它前一句；如果後面還有句子，也讀後一句。正確的選項要和讀到的每一句都接得上。`

### P6-5 shouldFix: rules[0].body
Problem: "the date of the letter" again assumes a date line exists (see P6-2). The tense clue may also come from a sentence after the blank.
Replace with:
- EN: `A sentence with no time word may accept several tenses. Check the date line, if there is one, and words like last week or next month in nearby sentences.`
- ZH: `沒有時間詞的句子可能好幾個時態都通。如果有日期欄就看日期，也看附近句子裡的 last week、next month 這類字。`

### P6-6 shouldFix: rules[0].ex[0]
Problem: the English is correct and natural, but only the answer is marked. The rule is about finding the time clue in another sentence, so mark the clue too. (Chinese unchanged.)
Replace the English with:
- EN: `Thank you for attending <em>last Thursday's</em> workshop. The slides we <em>presented</em> are now on the staff website.`

### P6-7 mustFix: rules[0].ex[1]
Problem: "The ceremony is set for June 3" does not fix the opening date. A memo dated May 10 could say "The new branch has opened on Harbor Road. The ceremony is set for June 3" (soft opening, ceremony later), so "will open" is not clearly the only right tense. The example must remove that reading.
Replace with:
- EN: `Memo, <em>May 10</em>: The new branch <em>will open</em> on Harbor Road. Its first day of business is <em>June 3</em>.`
- ZH: `五月十日的備忘錄：新分行將在 Harbor Road 開幕，第一天營業是六月三日。`

### P6-8 shouldFix (minor): rules[2].body
Problem: "what happens if not" is clumsy, and the relations are listed in the same order as the adverbs but never tied to them. Tie them.
Replace with:
- EN: `Several linking adverbs can follow a full stop. Decide the relation first: opposite (however), result (as a result), extra point (in addition), replacement (instead) or 'if not' (otherwise).`
- ZH: `好幾個連接副詞都能放在句號後。先判斷兩句的關係：相反（however）、結果（as a result）、補充（in addition）、取代（instead）、「不這樣做的話」（otherwise）。`

### P6-9 shouldFix: rules[3].ex[1] (Chinese only)
Problem: "請看看板上" reads as "看看" plus "板上" and "看板" is also a common word (signboard), so the first reading stumbles. "目前的菜色" is a little vague for "current dishes".
Replace the Chinese with:
- ZH: `我們的午餐菜單每週更換，請查看告示板上目前供應的菜色。`

### P6-10 shouldFix: rules[4].body
Problem: "The right sentence often refers to…" is a frequency claim about the test (STYLE.md: no "often"-type claims; 8.1 calls its descriptions our judgment). Make it a conditional rule, which is also what the learner uses on the page.
Replace with:
- EN: `If an option refers to something already said (these changes, the same discount, this request), that thing must appear before the blank and match in number.`
- ZH: `如果選項指回已經提過的事（these changes、the same discount、this request），那件事必須在空格前出現，單複數也要一致。`

### P6-11 shouldFix: rules[4].ex[1]
Problem: "applies to guests they bring" is clipped; "any guests they bring" is the natural wording. The Chinese "會員上所有課程" is stiff.
Replace with:
- EN: `Members receive a discount on all classes. <em>The same discount applies to any guests they bring.</em>`
- ZH: `會員參加所有課程都享有折扣，他們帶來的來賓也適用同樣的折扣。`

### P6-12 shouldFix: rules[5].body
Problem: "To place an order" needs something to order, not a "service". The Chinese "服務" repeats the error.
Replace with:
- EN: `If a sentence follows the blank, read it too. If it opens with Until then, For this reason or To place an order, the inserted sentence must supply the time, the reason or the thing to order.`
- ZH: `空格後如果還有句子，也要讀。若它以 Until then、For this reason、To place an order 開頭，插入句就必須交代那個時間、理由，或要訂的東西。`

### P6-13 shouldFix: pairs[1]
Problem: this pair repeats rules[0].ex[0] almost word for word (Thank you for attending last week's / last Thursday's session, the slides we presented). One of the 2-4 pair slots is wasted on the same scenario. Replace the pair with a different tense clue (the wrong version is clearly wrong: "begins on June 1" is a future plan).
Replace pairs[1] with:
- right: `Renovation of the lobby begins on June 1. During the work, guests will enter through the side door.`
- wrong: `Renovation of the lobby begins on June 1. During the work, guests entered through the side door.`
- why EN: `Begins on June 1 puts the renovation in the future, so the guests' route is a future plan. Entered would describe something already done.`
- why ZH: `begins on June 1 把整修放在未來，所以房客走哪個門是未來的安排。entered 描述的是已經發生的事。`

### P6-14 shouldFix (minor): lists[0].items[6] and lists[1].items[1] (Chinese only)
Problem: "在那時" does not say whether the time is past or future ("當時" past, "屆時" future). "因為這個原因" reads as a literal "because of this reason"; "基於這個原因" is the usual wording.
Replace with:
- lists[0].items[6] ZH: `當時、屆時`
- lists[1].items[1] ZH: `基於這個原因`

### P6-15 shouldFix: traps[0]
Problem: "only the sentence before shows which relation is true" is not accurate. The relation holds between the previous sentence and the sentence with the blank, so both are needed.
Replace with:
- EN: `Choosing the linking adverb that sounds most natural in its own sentence. Many fit after a full stop; only the two sentences read together show which relation is true.`
- ZH: `選了在本句裡聽起來最自然的連接副詞。很多都能放在句號後，要把前後兩句合起來讀，才看得出真正的關係。`

### P6-16 shouldFix (minor): traps[1]
Problem: "as the meaning of it or they" is awkward English.
Replace with:
- EN: `Assuming it or they refers to the nearest noun. Check the noun against the verb: a request is forwarded, a policy takes effect.`
- ZH: `以為 it 或 they 指的是最近的名詞。要用動詞檢查：被轉交的是申請，生效的是規定。`

### P6-17 shouldFix: traps[2]
Problem: 8.1 lists three ways a same-topic distractor fails: it points to something not yet introduced, it contradicts a detail, or it breaks the link between the sentences around the blank. The trap omits the third.
Replace with:
- EN: `Picking an inserted sentence because it is on topic. A wrong option can match the topic but mention something not yet introduced, clash with a date or name, or break the link with the sentences around it.`
- ZH: `因為和主題相關就選了插入句。錯誤選項可能主題相同，卻提到還沒出現的東西、和日期或人名衝突，或切斷了和前後句的銜接。`

### P6-18 shouldFix: traps[3]
Problem: "the date line" again assumes one exists (see P6-2), and "earlier paragraphs" ignores clues that come after the blank (the corrected example in P6-7 uses a later sentence).
Replace with:
- EN: `Choosing a tense from the blank's sentence alone. Look at any date line and the time words in nearby sentences and paragraphs.`
- ZH: `只看空格那一句就決定時態。要看有沒有日期欄，以及前後句、前後段裡的時間詞。`

---

## lessons/p7-triple.json

### P7-1 shouldFix (minor): steps[0] (Chinese only)
Problem: "寫的人" is colloquial for the sender or author of a document.
Replace the Chinese with:
- ZH: `先略讀每份文件的種類、日期和寄件人或作者，記下每份提供什麼：計畫、變更、訂單或評論。`

### P7-2 shouldFix (minor): steps[1]
Problem: "or two" contradicts the lead, which says some answers need two or three documents.
Replace with:
- EN: `Read the question and decide where to look: one document, or two or three that share a name, date or product.`
- ZH: `讀題目，決定去哪裡找：一份文件，或是有共同人名、日期、產品的兩三份。`

### P7-3 shouldFix: rules[0].body
Problem: "news the writer wants the reader to act on" does not work, because news is not acted on. The Chinese "要讀者處理的…消息" has the same problem.
Replace with:
- EN: `Why was the e-mail sent? Find the request or news the writer actually wants to give the reader. Thanks, background and small details are true but are not the purpose.`
- ZH: `Why was the e-mail sent? 找出寫信的人真正要提出的請求，或要傳達的消息。致謝、背景和小細節雖然屬實，卻不是目的。`

### P7-4 shouldFix: rules[0].ex[0]
Problem: "Corvale" is already the plant town in bank item r-p7-01 (reusing an invented place name across lesson and item makes them look linked). "a quote on fifty office chairs" is acceptable but "quote for" is the standard collocation.
Replace with:
- EN: `We met at last week's trade fair in Lanmoor. <em>I am writing to ask for a quote</em> for fifty office chairs.`
- ZH: `我們上週在 Lanmoor 的商展見過面。我寫信是想詢問五十張辦公椅的報價。`

### P7-5 shouldFix (optional): rules[2].body
Problem: the rule says "a later e-mail" but never says how to tell which document is later. Documents are not always given in time order, so the dates decide.
Replace with:
- EN: `A schedule or ad gives the plan. A later e-mail may move the date, change the room or replace a speaker. Questions about what actually happens need the latest version. Check the dates to see which is later.`
- ZH: `時程表或廣告給的是原計畫。後來的 e-mail 可能改日期、換會議室或換講者。問實際情況的題目要用最新的版本，所以要看日期，確定哪一份比較晚。`

### P7-6 shouldFix (optional): rules[4].body
Problem: first step is missing. 8.0 and the lesson's own wording list say the question names the paragraph, so tell the learner to go there before testing options. "The word has several meanings" also reads as a fact about every word question; "may" is accurate.
Replace with:
- EN: `Find the word in the paragraph the question names. It may have several meanings, and the one you know best may be a trap. Put each option in place of the word and read the sentence again.`
- ZH: `到題目指定的那一段找出這個字。它可能有好幾個意思，你最熟的那個可能就是陷阱。把每個選項換進句子裡，重讀一次。`

### P7-7 mustFix: rules[4].ex[0]
Problem: the bank item r-p7-03 (Ferrow Logistics advertisement) asks about "address" in paragraph 2 ("address any problems with deliveries") with options deal with / speak formally to / write a destination on / greet, and the answer is "deal with". This example teaches the two best distractor meanings, "speak to" and "write an address on", so a learner who has read the lesson can eliminate them before reading the item. Use a polysemous word that no bank item uses. Note that "run" and "carry" are the other two word-question targets in the bank (r-p7-01, r-p7-02), so avoid those too.
Replace with:
- EN: `The bank will <em>extend</em> a loan to the firm. Here it means offer, not make longer.`
- ZH: `銀行將提供這家公司一筆貸款。這裡的 extend 是「提供」，不是「延長」。`

### P7-8 mustFix: rules[4].ex[2]
Problem: the Chinese gloss "涵蓋、處理" gives 處理 (handle, process), which is the wrong sense for "the report covers sales" and would mislead. In English, "deals with" is a weak paraphrase and the contrast "not hides" is artificial: nobody reads "covers sales" as "hides sales". The meaning a learner actually falls back on is "put something over". Also, the two earlier examples use bare verb forms after "means" (speak to, obey), so "deals with / hides" is inconsistent.
Replace with:
- EN: `The report <em>covers</em> sales in all three regions. Here it means include, not put something over.`
- ZH: `這份報告涵蓋三個地區的銷售。這裡的 covers 是「涵蓋、包含」，不是「蓋住」。`

### P7-9 mustFix: rules[5].body
Problem: "Look for each option in the documents. The three you find are wrong; the one you cannot find is the answer." Two ways this misleads. (a) Per 8.2 the correct options are reworded, so a learner searching for the option's words will "not find" an option the documents do support and pick the wrong answer. (b) A wrong option can be contradicted in the text (stated as not offered), in which case the learner does find the words but the option is still the NOT answer.
Replace with:
- EN: `What is NOT mentioned? Check each option against the documents, looking for the idea, not the exact words. The three that the documents confirm are wrong; the one they never confirm, or contradict, is the answer. The details may be spread over two documents.`
- ZH: `What is NOT mentioned? 逐一拿每個選項去文件裡核對，找的是意思，不是一模一樣的字。文件有證實的三個是錯的；文件沒有證實、甚至說相反的那個才是答案。這些細節可能分散在兩份文件裡。`

### P7-10 shouldFix: rules[6].body
Problem: "The answer is reworded" states as a fact that the correct option is always reworded. 8.2's rewording distance is a design choice for this workbook. Hedge it.
Replace with:
- EN: `What is indicated or suggested about someone? The answer may be reworded but must follow from the text. An option that is only possible, or that is true of another person, is wrong.`
- ZH: `What is indicated / suggested about…? 答案可能經過改寫，但必須由文字推得出來。只是「有可能」的選項，或其實是在講別人的選項，都是錯的。`

### P7-11 shouldFix (minor): rules[6].ex[0] (Chinese only)
Problem: "run our office" means manage it. "負責" only says responsible for, which is weaker than the inference "has management experience" needs.
Replace the Chinese with:
- ZH: `原文：Osei 先生自 2019 年起負責管理我們的 Brenton 辦公室。可推得：他有管理經驗。推不出：他打算退休。`

### P7-12 shouldFix (minor): pairs[1].why
Problem: "the row above it" refers to a table row, but the pair shows the price list inline in brackets, so no row is visible.
Replace with:
- EN: `The e-mail names the mid-size van. $120 comes from the small van, the first one listed.`
- ZH: `e-mail 指定的是中型廂型車。120 美元是用最先列出的小型車價格算出來的。`

### P7-13 shouldFix: lists[0] (Typical question wordings)
Problem: (a) items[4] Chinese is clumsy ("沒有被提到是"). (b) 8.0 lists the stems that appear in the sample: "According to the advertisement, why …?", "Who most likely is …?", "What will … most likely do …?". The list has none of these, and "Who most likely is" is a type a learner should recognise. (The list holds 8 items; adding three stays under the 12 maximum.)
Replace items[4] with:
- EN: `What is NOT mentioned as a benefit of membership?`
- ZH: `文中沒有提到哪一項是會員的好處？`
Append these three items:
- EN: `According to the notice, what must customers do?` / ZH: `根據公告，顧客必須做什麼？`
- EN: `Who most likely is Mr. Osei?` / ZH: `Osei 先生最可能是什麼身分？`
- EN: `What will Ms. Kato most likely do on Friday?` / ZH: `Kato 女士星期五最可能做什麼？`

### P7-14 shouldFix (optional): lists[1] (Words that signal a change)
Problem: the list lacks "postponed", one of the most common change words in notices, and "revised". items[7] "replaces" has the same Chinese as items[4] "instead of" (取代); give it a different gloss.
Replace items[7] with:
- EN: `replaces` / ZH: `取代、改為`
Append:
- EN: `has been postponed until` / ZH: `已延後到`
- EN: `revised` / ZH: `修訂過的`

---

## Checked and left alone

- p6 rules[0] to [5], every other example: English is correct and natural, and each one shows its rule. In particular rules[1].ex[0] ("It" = policy, decided by "takes effect", with "Monday" as the nearest noun), rules[2].ex[0] and ex[1], rules[3].ex[0], and rules[5].ex[0] and ex[1].
- p6 pairs[0], [2], [3]: the "wrong" versions are clearly wrong, and the `why` lines are accurate. Chinese twins are accurate.
- p7 rules[1], [3] and all other examples: each shows its rule, and the arithmetic and date comparisons are correct (May 17 is after May 15; $80 x 2 = $160; $60 x 2 = $120; Group B is 10:30).
- p7 pairs[0], [2], [3]: sound. The distractor "moved into" for "settled" (pairs[2]) is a stretch as a dictionary sense but matches the example given in 8.2 and is plainly wrong in the sentence.
- Omitting line numbers in the word-question wording ("paragraph 2", no "line 3") is consistent with the decision recorded in 8.0. The 8.0 sample does give a line number, so the learner will see one on the printed test; the lesson does not claim otherwise, so no change is needed.
- "full stop" in p6 matches the reviewed lesson connect.json, so I left it.
- Style: no praise, no "Let's", no exclamation marks, no emoji, no "Remember" or "Note that" in either file. No percentages, frequency figures or official rules beyond the points listed in P6-1 and P6-10 (the soft "often"). "five questions", "three related documents" and "four blanks" are all visible in the 8.0 sample.

## Overall verdict

Both lessons are close to ready. The English is correct and natural almost everywhere, the Chinese twins are accurate and read as Taiwan Traditional Chinese, the tone follows STYLE.md, and the rules match the item design in section 8 without borrowing any official statistics. Five items need fixing before they ship: the p6 lead presents the workbook's own blank-type counts and a frequency as facts about the test, the p6 "will open" tense example is not forced by its clue, the p7 "address" example gives away the distractors of a live bank item, the p7 "covers" example has a wrong Chinese gloss and an artificial contrast, and the p7 NOT rule tells the learner to hunt for exact words when correct options are reworded and wrong ones can be contradicted. The remaining shouldFix items are mostly small: the date-line assumption (the 8.0 sample e-mail has none), a duplicated tense scenario between a rule example and a pair, a missing "only one option fits" step for word-form and fixed-phrase blanks, a few loose or clumsy phrasings, and a few stems and change words worth adding to the p7 lists. With the replacements above applied, I would expect both lessons to pass a second read without further changes.
