# English notes review: Part 7 three-document sets r-p7-01 to r-p7-05

Files reviewed: `en/items_read_b.json` (r-p7-01, r-p7-02, r-p7-03) and `en/items_read_c.json` (r-p7-04, r-p7-05), checked against `items_read_b.py` and `items_read_c.py` and the rules in `en/STYLE.md`. The notes files were not edited.

Conventions in this list
- `q[n]` and `gloss[n]` use the 0-based index of the array in the notes JSON (`q[0]` is the first question).
- Every replacement is the full new value of the field, as an English line and a Chinese twin.
- Replacements never mention option letters. The page shuffles the options for each session (`optionOrder` in `template.html`), so a letter in a note would point at the wrong option. The current notes already avoid letters; keep it that way.
- Every `<em>` quote in the replacement text was matched against the document text by script.

## What was checked and found sound

- All 25 keys were re-derived from the documents. Every note leads to its keyed answer and agrees with the Chinese explanation in the items file. Nothing needs a `_flags` entry.
- Every date, time and sum was recomputed and is right: r-p7-01 opening 8:30 + 15 min = 8:45, Room 112 at 11:00 (slot 10:45-12:00); r-p7-02 6 x ($468 + $226 + $134) = $4,968 against the $3,000 threshold, Sept 8 to Sept 25 = 17 days, ($226 - $189) x 6 = $222; r-p7-03 Nov 30 interview, Nov 21-25 away, Nov 26 e-mail; r-p7-04 34 x $26 = $884, $884 + $35 + $60 - $195 = $784, March 20 + 2 days = Saturday March 22; r-p7-05 lunch 12:45 -> 1:30, return 5:30 -> 6:15, offer open until Thursday June 12.
- Both NOT questions locate their confirmed options correctly. r-p7-02 q[0]: order form (quantities, order and required-by dates, special instructions) plus price list (unit prices, free-delivery row, Colors column). r-p7-05 q[4]: sister in review paragraph 1, wedges in paragraph 2, starving in paragraph 3, full refund only in e-mail paragraph 4.
- Every `<em>` quote in every point and why matches the document text exactly. The one exception is `carries` in r-p7-02 q[2].point, which is a named word pattern and is fine.
- Each English line and its Chinese twin agree on meaning, numbers and quoted words. The Chinese is natural Taiwan Traditional Chinese, with English terms and quotes kept in English.
- No line about a wrong option, no banned phrase, no exclamation mark; `python3 en/check.py` prints `ok` for both files.
- All word-card examples are 12 words or fewer, natural, and use the headword. Headwords, parts of speech and glosses fit the context, apart from the points below.

## mustFix

### 1. r-p7-03, q[4].why: a date relation the document does not support

Problem: the note says the exercise "arrives the day after he gets back". The e-mail says he is away "from November 21 to 25", so he is back on the 25th evening or the 26th, and the exercise arrives on the 26th. "The day after he gets back" can be wrong by a day. The note also names the advertisement's plan without saying where it is (STYLE asks for the place).

Replacement (EN):
The fourth paragraph of the advertisement planned the exercise for <em>the day of their interview</em>, but the third paragraph of the second e-mail changes this: <em>you will receive it by e-mail on November 26 and should send it back to me before your interview</em>. Its first paragraph sets the interview for <em>Monday, November 30</em>. In the third paragraph of the first e-mail, Mr. Reyes says <em>I will be away at a family wedding from November 21 to 25</em>. The exercise does not reach him until November 26, after his trip has ended, and it is due before the interview on the 30th. So he will do it just after he returns from traveling.

Replacement (ZH):
廣告第 4 段原本安排在 the day of their interview 做練習，但第二封 e-mail 第 3 段改了：you will receive it by e-mail on November 26 and should send it back to me before your interview。同一封信第 1 段把面試定在 Monday, November 30。第一封 e-mail 第 3 段，Reyes 先生說 I will be away at a family wedding from November 21 to 25。練習要到 11 月 26 日才寄到他手上，那時他的旅程已經結束，而且要在 30 日的面試前寄回。所以他會在旅行回來後不久完成。

### 2. r-p7-05, q[0].why: the note contradicts itself

Problem: the note first says the first paragraph "only asks passengers to read the information below", then ends "each paragraph changes something about Saturday's tour". The first paragraph changes nothing, so the last sentence is false and will confuse a learner. "Set against" is also harder than it needs to be.

Replacement (EN):
The first paragraph of the e-mail only asks passengers to <em>read the information below</em>, so the purpose is in the paragraphs after it. The second paragraph replaces the boat stop: <em>In its place, we will visit Hessle Farm Dairy</em>. It also moves lunch and the return later than the itinerary shows. The third paragraph moves the departure to <em>Bay 2</em>. The fourth gives other choices to passengers who prefer not to travel because of the change. Paragraphs two to four all tell passengers how Saturday's tour differs from the itinerary, so the e-mail was sent to announce changes to a trip.

Replacement (ZH):
e-mail 第 1 段只請旅客 read the information below，所以目的要看後面的段落。第 2 段替換了搭船那一站：In its place, we will visit Hessle Farm Dairy，午餐和回程也比行程表所列的時間晚。第 3 段把出發地點改到 Bay 2。第 4 段給因此不想去的旅客其他選擇。第 2 到第 4 段都在告訴旅客週六的行程和行程表哪裡不一樣，所以寫信是為了通知行程變動。

### 3. Five word cards cannot be tapped on the page

Problem: the page only underlines gloss words inside document paragraphs (`readCard` runs `glossify` on `paras`). Words that occur only in a table cell, a header line or a title are never underlined, so the card can never be opened. `check.py` does not catch this because it also searches table rows. Five cards are affected: `freight` (r-p7-01, program table only), `Height-adjustable` and `Mesh-back` (r-p7-02, price list table only), `surcharge` and `Balance due` (r-p7-04, invoice table only). The content of those five cards is correct. There are two ways to fix it: (a) swap each for a word that sits in a paragraph, as below (the word counts stay 7, 7 and 8, inside the 5-8 range); or (b) make `graphicTable` in `template.html` run `glossify` on its cells, after which the original five can stay. Option (a) needs no page change. Each replacement below was checked to occur in a paragraph, with an example of 12 words or fewer that uses the headword.

r-p7-01, gloss[0] (replaces `freight`). Occurs in the second e-mail, paragraph 1: "the cold-storage labeling workshop filled up last week". It is also the language that decides the "more applicants than places" question.
```json
{"w": "filled up", "hw": "fill up", "pos": "phr.", "zh": "額滿、被訂滿", "ex": "The evening class filled up in two days."}
```

r-p7-02, gloss[0] (replaces `Height-adjustable`). Occurs in the e-mail, paragraph 1: "Our crew will bring everything up to your floor".
```json
{"w": "crew", "hw": "crew", "pos": "n.", "zh": "工作小組、作業人員", "ex": "The crew arrived early to set up the stage."}
```

r-p7-02, gloss[1] (replaces `Mesh-back`). Occurs in the e-mail, paragraph 1: "does not expect to ship more until the middle of October".
```json
{"w": "ship", "hw": "ship", "pos": "v.", "zh": "出貨、寄送", "ex": "We ship all orders within two business days."}
```

r-p7-04, gloss[6] (replaces `surcharge`). Occurs in the web page, paragraph 3: "an additional $60 staffing charge", which is the evidence for the last question.
```json
{"w": "staffing charge", "hw": "staffing charge", "pos": "n.", "zh": "人員費用", "ex": "A staffing charge applies to weekend events."}
```

r-p7-04, gloss[7] (replaces `Balance due`). Occurs in the web page, paragraph 3: "25 percent of the estimated food cost".
```json
{"w": "estimated", "hw": "estimated", "pos": "adj.", "zh": "預估的", "ex": "The estimated cost includes delivery and tax."}
```

## shouldFix

### 4. r-p7-02, q[0].why: the total is stated, not shown; the labels are fragments

Problem: the note gives three unit prices and says "the total is $4,968", but the learner cannot see the quantity step, and NOT questions are exactly where the learner needs to check the sum. The labels "Over two weeks:" and "A time of day:" read like scraps of the option text.

Replacement (EN):
Three options are confirmed. Free delivery: the order form has 6 each of DK-160, CH-40 and ST-02. On the price list, one of each costs <em>$468</em> + <em>$226</em> + <em>$134</em> = $828, so six of each is 6 × $828 = $4,968. The price list's last row says delivery is <em>free on orders of $3,000 or more</em>. Ordered more than two weeks early: the order form's order date is <em>September 8</em> and its required-by date is <em>September 25</em>, seventeen days later. A delivery time: its special instructions say <em>Deliveries must arrive before 9:00 A.M.</em> The graphite option is the one that is not true. The graphite item on the order is ST-02, and the price list gives its colors as <em>White, graphite</em>. The DK-160 desk comes in <em>White, oak, graphite</em>, and CH-40 only in <em>Black</em>. No item on the order is offered only in graphite, so this option is the answer.

Replacement (ZH):
三個選項都能確認。免運：訂購單上 DK-160、CH-40、ST-02 各 6 件。價目表上三種各一件是 $468 + $226 + $134 = $828，六組就是 6 × $828 = $4,968。價目表最後一行說 free on orders of $3,000 or more。提早兩週以上下單：訂購單的下單日是 September 8，最晚需要日是 September 25，相隔十七天。指定送達時間：特別指示寫 Deliveries must arrive before 9:00 A.M.。不成立的是石墨灰那一項：訂單上的石墨灰是 ST-02，價目表上它的顏色是 White, graphite；DK-160 是 White, oak, graphite，CH-40 只有 Black。訂單裡沒有任何一項只出石墨灰，所以這個選項就是答案。

### 5. r-p7-02, q[2].why: "carry means stock" leaves the answer word undefined

Problem: for this learner "stock" as a verb is the harder word. The note shows the structure well but ends on a bare synonym.

Replacement (EN):
The second paragraph of the e-mail offers <em>the same model without the headrest, which we carry in the color you chose</em>. The subject <em>we</em> is the seller, the object is a chair model, and <em>in the color you chose</em> says which version the seller has. So <em>carry</em> means stock: the seller keeps this chair available to sell.

Replacement (ZH):
e-mail 第 2 段提供 the same model without the headrest, which we carry in the color you chose。主詞 we 是賣家，受詞是一款椅子，in the color you chose 說的是賣家有哪個顏色。所以 carry 等於 stock：賣家備有這款椅子可以賣。

### 6. r-p7-04, q[2].why: no paragraph named, and the "more main dishes" step is implied

Problem: "On the web page" gives no paragraph (STYLE asks to say where). The step from "plus a second hot main course" to "more main dishes than January" is left for the learner; the web page says the Harvest Package has "one hot main course", so one clause closes it.

Replacement (EN):
The first paragraph of the e-mail says the January lunch was <em>the Harvest Package</em>. The second paragraph says colleagues <em>have asked for dessert and coffee</em> and asks for <em>the package that includes them</em>. In the second paragraph of the web page, only the Banquet Package has <em>a dessert table and coffee service</em>, and it is the Harvest Package <em>plus a second hot main course</em>, so it has two hot main courses and the Harvest Package has one. The invoice's first row, <em>34 guests at $26.00</em>, matches the Banquet price. So this lunch had more main dishes than the one in January.

Replacement (ZH):
e-mail 第 1 段說一月那次是 the Harvest Package。第 2 段說同事 have asked for dessert and coffee，所以要 the package that includes them。網頁第 2 段中，只有 Banquet Package 有 a dessert table and coffee service，而它是 Harvest Package plus a second hot main course，也就是兩道熱的主菜，Harvest 只有一道。發票第一行 34 guests at $26.00 也正是 Banquet 的價錢。所以這次的主菜比一月多。

### 7. r-p7-05, q[3].why: the link from "dropped" to the boat stop is thin

Problem: the e-mail never says "dropped". The learner has to see that the dairy visit replaces the boat stop, and the note leaves that out. Adding the "In its place" quote makes the three-document chain complete (review "dropped", e-mail "in its place", itinerary "cruise").

Replacement (EN):
The first paragraph of the review says she booked mainly for <em>the stop I had been looking forward to for months</em>, and that Thornfield wrote <em>to say it had been dropped</em>. The second paragraph of the e-mail shows which stop was dropped: <em>The boat that serves the island tea house on Lindell Water has been taken out of service</em>, and <em>In its place, we will visit Hessle Farm Dairy</em>. The itinerary's third row describes the boat stop as a <em>Forty-minute cruise to the island tea house</em>, and the e-mail's fourth paragraph says <em>some of you chose this tour for the lake</em>. What she most looked forward to was a trip on a lake.

Replacement (ZH):
評論第 1 段說她報名主要是為了 the stop I had been looking forward to for months，而 Thornfield 來信 to say it had been dropped。e-mail 第 2 段說明取消的是哪一站：The boat that serves the island tea house on Lindell Water has been taken out of service，而且 In its place, we will visit Hessle Farm Dairy。行程表第三行說這一站是 Forty-minute cruise to the island tea house，e-mail 第 4 段也說 some of you chose this tour for the lake。所以她最期待的是遊湖。

### 8. r-p7-05, q[4].why: "wedges" is the one unknown word and is left unexplained

Problem: the note quotes "I bought two wedges to take home" as "buying a product" without saying what wedges are. A learner who does not know the word cannot see why this option is confirmed. The word card exists, but the note should stand alone.

Replacement (EN):
The review confirms three options. Traveling with a relative: <em>My sister and I booked this tour</em> (first paragraph). Buying a product: <em>I bought two wedges to take home</em> (second paragraph); the wedges are pieces of cheese from the dairy stop. Being hungry before a meal: <em>By the time we sat down at the inn, most of us were starving</em> (third paragraph). A full refund appears only in the fourth paragraph of the e-mail, for passengers who cancel. Ms. Quaye writes <em>We decided to go anyway</em>, and she mentions <em>my voucher</em>, not a refund. So receiving a full refund is not mentioned in the review.

Replacement (ZH):
評論確認了三個選項。和親人同行：My sister and I booked this tour（第 1 段）。買了商品：I bought two wedges to take home（第 2 段）；wedges 是在酪農場那一站買的幾塊起司。用餐前很餓：By the time we sat down at the inn, most of us were starving（第 3 段）。全額退款只出現在 e-mail 第 4 段，是給取消行程的人的。Quaye 女士寫 We decided to go anyway，她提到的是 my voucher，不是退款。所以評論沒有提到拿到全額退款。

### 9. r-p7-01, gloss[2] (`transfer`): the Chinese gloss is clumsy for this context

Problem: "轉換、改換（到別處）" is awkward. In the e-mail the word means moving a ticket from one session to another.

Replacement (gloss object; English fields unchanged, Chinese gloss changed):
```json
{"w": "transfer", "hw": "transfer", "pos": "v.", "zh": "改到、轉到（另一場）", "ex": "Can I transfer my booking to the evening class?"}
```

## Verdict

The five notes are strong. All 25 answer keys are right, each note reaches its key through the right document and place, every cross-document date, time and sum is correct, every quote matches the document text, and the English and Chinese twins agree and read naturally. The plain-English level suits a TOEIC 690 reader and the STYLE rules are followed. Two content errors need fixing before release: r-p7-03 q[4] claims the exercise arrives "the day after he gets back", which the dates do not establish, and r-p7-05 q[0] ends by saying "each paragraph" changes the trip right after saying the first paragraph does not. One functional problem also needs fixing: five word cards (r-p7-01 `freight`, r-p7-02 `Height-adjustable` and `Mesh-back`, r-p7-04 `surcharge` and `Balance due`) sit only in table cells, which the page never underlines, so the learner can never open them. Swap them for the paragraph words given above, or have the page gloss table cells. The shouldFix items add the missing arithmetic in the r-p7-02 NOT note, define "stock" and "wedges", name a paragraph, and complete the "dropped" chain in r-p7-05; none changes an answer. With the mustFix items applied the set is ready.
