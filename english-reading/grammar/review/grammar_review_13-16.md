# Review of grammar chapters 13 to 16

Scope: `chapters/13-quantity.json`, `14-parallel.json`, `15-prep.json`, `16-mandative.json`, checked against `STYLE.md`. The reader is a Taiwanese adult (TOEIC 690, aiming for 785 to 860) who has forgotten most grammar. The chapter files were not edited.

How to read this file

- **mustFix**: a grammar error, a quiz item with more than one acceptable answer, a rule that is false or contradicts another chapter, or a gap the reader will fall into. **shouldFix**: an improvement to accuracy, clarity, consistency or style.
- Paths are written from the root of the chapter JSON, for example `sections[3].quiz[0]`. Indices are the current ones in the file.
- **Replace** means: set the field to the given value. **Insert** means: add the given value as a new list element at the stated index, so the elements from that index on move down by one (when two edits touch the same list, apply the replace edits first and the inserts last, highest index first). **Append** means: add the given text to the end of the existing string.
- Every replacement string was applied to a scratch copy of the chapters and run through `check.py`; all four files pass (tags, banned phrases, counts of examples, quizzes and check items).

| File | mustFix edits | shouldFix edits |
|---|---|---|
| 13-quantity.json | 9 | 12 |
| 14-parallel.json | 2 | 8 |
| 15-prep.json | 5 | 14 |
| 16-mandative.json | 9 | 10 |

## chapters/13-quantity.json

Checked and correct: Both tap items verified by splitting on spaces (advices = 6; number + is = 1 and 4, no second reasonable selection). Every other choose item has one answer except 13-01. Each/every/each of agreement, a number of / the number of, most / most of the, another / other, and the countable and uncountable claims (equipment, information, advice, furniture, luggage, feedback, merchandise, machinery, clothing, news) are correct. Spelling is American. No banned phrases and no test claims (check.py passes).

### 13-01 · mustFix · `sections[3].quiz[0]`

**Problem.** Two answers are defensible. 'A few people signed up for the workshop, so it was canceled' is grammatical and natural (a few can still be too few), so the stem does not force 'Few'. The why also overclaims ('A few ... 不會導出取消'). The body[3] trick (look at the second half) is only a tendency, so the item cannot rest on it. Replace the whole quiz item with a stem whose second half only fits 'A few'.

**Edit.** Replace the field value with:

```json
{
  "type": "choose",
  "q": "___ people signed up for the workshop, so we can hold it as planned.",
  "options": [
    "A few",
    "Few"
  ],
  "answer": 0,
  "why": "後半句是正面的結果（照原訂計畫舉行），表示報名的人「有一些、夠了」，用有 <em>a</em> 的 <em>A few</em>。<em>Few</em> 是「很少、幾乎沒有」，不會導出「可以照計畫舉行」。"
}
```

### 13-02 · mustFix · `sections[4].body[1]`

**Problem.** The test 'front can take two, so use fewer' contradicts the next paragraph: 'two minutes' and 'two dollars' also pass the test, yet 'less than 30 minutes' is right. Restate the test as counting people or things one by one.

**Edit.** Replace the field value with:

```
日常口語裡常聽到有人把 <em>less</em> 放在可數名詞前面，但正式的書面英文分得很清楚。寫報告或信件時先判斷名詞：如果它是一個一個數的人或東西（<em>two errors</em>、<em>two clients</em>），就用 <em>fewer</em>。
```

### 13-03 · mustFix · `sections[4].body[2]`

**Problem.** Only half of 'less than / fewer than' with numbers is taught. The reader is told that numbers take 'less than' and never meets 'fewer than 50 employees' (people or items counted one by one), the usual formal-writing form. Taught as written, the section leads to 'less than 50 employees'.

**Edit.** Replace the field value with:

```
有一個看起來像例外的地方：<em>than</em> 後面接數字的時候。數字後面是時間、金額、距離、重量，用 <em>less than</em>：<em>less than 30 minutes</em>、<em>less than $500</em>。這時英文把「30 分鐘」「500 元」看成一整個量，不是一分鐘一分鐘地數。數字後面是一個一個數的人或東西，還是用 <em>fewer than</em>：<em>fewer than 50 employees</em>、<em>fewer than ten complaints</em>。
```

### 13-04 · mustFix · `sections[4].ex[3]`

**Problem.** Add an example that shows 'fewer than + number + countable noun', so the section shows both halves of the 'than + number' rule (section has 3 examples; 4 is within the 1-5 limit).

**Edit.** Insert as a new element at `sections[4].ex[3]`:

```json
{
  "en": "<u>Fewer than</u> 50 employees attended the safety briefing.",
  "zh": "出席安全說明會的員工不到五十人。",
  "note": "員工是一個一個數的，數字前面用 <em>fewer than</em>；時間和金額的數字才用 <em>less than</em>。"
}
```

### 13-05 · mustFix · `sections[4].takeaway`

**Problem.** Takeaway repeats the incomplete rule (only time and money take 'than' after less). Bring it in line with the fixed body.

**Edit.** Replace the field value with:

```
能數的「比較少」用 <em>fewer</em>，不能數的用 <em>less</em>；數字前面，時間、金額這種一整個量用 <em>less than</em>，一個一個數的人或東西用 <em>fewer than</em>。
```

### 13-06 · mustFix · `sections[7].body[3]`

**Problem.** 'almost 不能直接放在名詞前面' is false as a general statement: 'almost 200 employees', 'almost midnight', 'almost half the staff' are all fine. The real point is that almost cannot stand in for 'most' (the majority). Narrow the claim.

**Edit.** Replace the field value with:

```
<em>most</em> 也別跟 <em>almost</em> 搞混。<em>almost</em> 是副詞（第 1 章），意思是「幾乎」，它要修飾別的字，不能拿來當「大部分」直接放在名詞前面：要說 <em>almost all employees</em> 或 <em>almost every employee</em>，不能說 <em>almost employees</em>。<em>almost</em> 後面接數字是另一回事：<em>almost 200 employees</em> 是「將近兩百位員工」。
```

### 13-07 · mustFix · `sections[8].body[5]`

**Problem.** Pronoun use of 'the other' and the form 'the others' are never taught, yet ex[2] uses 'the other is next to the airport' with no noun (a jump), and the table says 'the other' is followed by a noun. 'the others' (the remaining ones) is the natural partner of 'others' and is missing from a section whose title lists the four words. Add one paragraph after body[4].

**Edit.** Insert as a new element at `sections[8].body[5]`:

```
<em>the other</em> 和 <em>others</em> 也可以單獨出現，後面不接名詞。<em>the other</em> 單獨用，指剩下的那一個：<em>one is near the port, and the other is next to the airport</em>。要指剩下的全部，用 <em>the others</em>：<em>Three of us went to the fair; the others stayed in the office.</em> <em>others</em> 沒有 <em>the</em>，是「其他的一些人或東西」，不特定；<em>the others</em> 有 <em>the</em>，是「剩下的全部」，範圍已經確定。
```

### 13-08 · mustFix · `sections[8].table.rows[2][1]`

**Problem.** Table cell says 'the other' is followed by a singular or plural noun, but the section's own ex[2] uses 'the other' alone. Make the cell cover both.

**Edit.** Replace the field value with:

```
名詞，或不接名詞（<em>the other</em>、<em>the others</em>）
```

### 13-09 · mustFix · `sections[8].table.rows[2][3]`

**Problem.** Add the standalone forms to the example cell, matching the new paragraph.

**Edit.** Replace the field value with:

```
<em>the other room</em>、<em>the other rooms</em>、<em>the others</em>
```

### 13-10 · shouldFix · `sections[8].takeaway`

**Problem.** Keep the takeaway consistent with the added 'the others'.

**Edit.** Replace the field value with:

```
<em>another</em> 是「再一個」，接單數；<em>the other</em>、<em>the others</em> 是「剩下的全部」；<em>others</em> 自己就是名詞，後面不再接名詞。
```

### 13-11 · shouldFix · `sections[1].table.rows[5][1]`

**Problem.** The column is headed '要數的時候' (how to count it), but 'some feedback' is not a way of counting. 'a piece of feedback' is standard and parallels the other rows.

**Edit.** Replace the field value with:

```
<em>a piece of feedback</em>
```

### 13-12 · shouldFix · `sections[0].body[3]`

**Problem.** Wrap the bare English terms in <em> (STYLE section 1). Content unchanged.

**Edit.** Replace the field value with:

```
判斷的方法：試著在名詞前面加 <em>two</em>。<em>two invoices</em> 可以，所以 <em>invoice</em> 可數；<em>two furnitures</em> 不行，所以 <em>furniture</em> 不可數。拿不準就查字典，字典會標 <em>[C]</em>（<em>countable</em>，可數）或 <em>[U]</em>（<em>uncountable</em>，不可數）。
```

### 13-13 · shouldFix · `sections[0].body[4]`

**Problem.** Threshold gap: many everyday nouns are both countable and uncountable with different meanings (room, paper, experience, time, business). The 'add two' test and the claim that uncountables never take 'a' will misfire on them, and the chapter itself uses 'experience' as uncountable (sections[3].ex[0], 'ten years of experience') without comment. One short paragraph after body[3].

**Edit.** Insert as a new element at `sections[0].body[4]`:

```
有些名詞兩種都有，意思不一樣。<em>a room</em> 是一間房（可數），<em>room</em> 是空間（不可數）：<em>There is no room for another desk.</em> <em>a paper</em> 是一份文件，<em>paper</em> 是紙。所以「加 <em>two</em>」的測試，要問在這個句子的意思下能不能數。
```

### 13-14 · shouldFix · `sections[0].body[2]`

**Problem.** '前面一定要有 a、the…' has real exceptions in fixed phrases (by car, at work, in person). One short hedge prevents a reader meeting 'by car' and concluding the book is wrong.

**Edit.** Append to the end of the existing value of this field:

```
少數固定說法是例外，例如 <em>by car</em>、<em>at work</em>、<em>in person</em>，先當成整塊記。
```

### 13-15 · shouldFix · `sections[5].h`

**Problem.** 'an amount of' is rare as a bare phrase; the examples and body use 'a large amount of' and 'the amount of'. Teach the form readers will actually meet.

**Edit.** Replace the field value with:

```
a number of、the number of、a large amount of
```

### 13-16 · shouldFix · `sections[5].body[2]`

**Problem.** Same fix as the heading: 'a large amount of' (or 'a small amount of') + uncountable noun + singular verb.

**Edit.** Replace the field value with:

```
不可數名詞不能用 <em>number</em>（數目），要用 <em>amount</em>（份量）：<em>a large amount of money</em>、<em>the amount of paperwork</em>。<em>a large amount of</em>（也可以是 <em>a small amount of</em>）後面接不可數名詞，動詞用單數。
```

### 13-17 · shouldFix · `sections[5].table.rows[3][1]`

**Problem.** Same fix in the table.

**Edit.** Replace the field value with:

```
<em>a large amount of</em>、<em>a great deal of</em>
```

### 13-18 · shouldFix · `sections[4].body[0]`

**Problem.** 'few 和 little 的比較級（第 12 章）' points to a chapter that only covers little to less and many/much to more; 'fewer' does not appear in chapter 12. Keep the cross-reference to the concept, not to fewer.

**Edit.** Replace the field value with:

```
「比較少」也分兩個字。<em>fewer</em> 接複數可數名詞（<em>fewer errors</em>、<em>fewer complaints</em>），<em>less</em> 接不可數名詞（<em>less paper</em>、<em>less time</em>）。<em>fewer</em> 是 <em>few</em> 的比較級，<em>less</em> 是 <em>little</em> 的比較級（比較級的觀念見第 12 章），所以分組跟上一節一模一樣。
```

### 13-19 · shouldFix · `check[0].why`

**Problem.** STYLE requires the why to teach the method. State how to tell that equipment is uncountable (the two-test) before giving the rule.

**Edit.** Replace the field value with:

```
<em>equipment</em> 是不可數名詞：<em>two equipments</em> 說不通，所以不加 <em>-s</em>，前面也不加 <em>a</em>。要一件一件數，就說 <em>a piece of equipment</em>。
```

### 13-20 · shouldFix · `sections[3].body[3]`

**Problem.** Present the 'look at the second half' trick as a clue only, so readers do not apply it as a rule.

**Edit.** Replace the field value with:

```
讀句子時可以看後半當線索：結果是正面的（可以開始、還來得及），通常是有 <em>a</em> 的；結果是負面的（取消、延期、很難），通常是沒有 <em>a</em> 的。這只是線索，真正的差別是說話的人覺得夠不夠。
```

### 13-21 · shouldFix · `lead`

**Problem.** '數量詞' is used in the lead and the title but never defined. Add a short gloss at first use.

**Edit.** Replace the field value with:

```
英文的名詞（第 1 章）分成兩種：可以一個一個數的，和不能數的。這個分類決定了前面能不能加 <em>a</em>、後面能不能加 <em>-s</em>、要用 <em>many</em> 還是 <em>much</em>、動詞用單數還是複數。這一章先教你判斷一個名詞屬於哪一種，再把 <em>each</em>、<em>few</em>、<em>most of</em>、<em>another</em> 這些放在名詞前面說明「多少」的數量詞，照「後面接什麼名詞」一個一個整理清楚。
```

## chapters/14-parallel.json

Checked and correct: All four tap items verified (small + comfortable. = 4 and 6; read = 7; fast + reliable. = 7 and 10; technicians + were = 5 and 6). Every choose item has one answer. The proximity rule for either/or and neither/nor is the standard answer in British and American writing. Both A and B is plural; neither/nor takes no extra 'not'; rather than takes parallel forms and instead of takes a noun or Ving; the claim that this book's examples use the serial comma holds (pattern search over the English fields of all 16 chapters). No banned phrases and no test claims.

### 14-01 · mustFix · `sections[5].body[1]`

**Problem.** Internal contradiction. This paragraph says a fronted 'not only' makes the clause invert, but the table in the previous section (sections[4].table.rows[3][2]) contains 'Not only the staff but also the director is ...', which begins with 'Not only' and does not invert (correctly: it joins two subjects, not two clauses). A reader who has forgotten grammar cannot tell which rule wins. Scope the rule to 'not only' followed by a full clause, and cite chapter 2 for auxiliary and chapter 10 so inversion is not read as the 'Should you need' kind only.

**Edit.** Replace the field value with:

```
注意前半的語序：不是 <em>the hotel is</em>，而是 <em>is the hotel</em>，動詞或助動詞（第 2 章）跑到主詞前面，像問句的樣子。這叫倒裝（第 10 章的 <em>Should you need …</em> 也是倒裝，這裡是另一種場合）。<em>not only</em> 這類否定的字放到句首、後面接的是一個完整子句時，那個子句要倒裝，英文固定這樣寫。不倒裝，寫成 <em>Not only the hotel is close to the station</em>，就是錯的。
```

### 14-02 · mustFix · `sections[5].body[2]`

**Problem.** Companion paragraph for the fix above: explains why 'Not only the staff but also the director is' needs no inversion. Insert after body[1].

**Edit.** Insert as a new element at `sections[5].body[2]`:

```
有一個情況要分清楚：上一節表裡的 <em>Not only the staff but also the director is …</em> 也是 <em>Not only</em> 開頭，卻沒有倒裝。差別在 <em>not only</em> 後面接什麼。那一句 <em>not only</em> 後面只有一個名詞（<em>the staff</em>），接著 <em>but also</em> 另一個名詞，連接的是兩個主詞，不是兩個子句，所以不倒裝。<em>not only</em> 後面接著主詞加動詞（<em>the hotel is</em>），連接的是兩個子句，才倒裝。
```

### 14-03 · shouldFix · `sections[5].body[2]`

**Problem.** Incomplete: only be-verbs and do/does/did are covered. Auxiliaries (will, can, has) simply move; a reader told to 'borrow do' may write 'Not only does the system will reduce'. State both cases.

**Edit.** Replace the field value with:

```
<em>be</em> 動詞和助動詞（第 2 章）可以直接搬到主詞前面：<em>the hotel is</em> 變成 <em>is the hotel</em>，<em>the system will reduce</em> 變成 <em>will the system reduce</em>。一般動詞沒有東西可以搬，就借 <em>do</em>、<em>does</em>、<em>did</em> 放到主詞前面，動詞回到原形：<em>the layout saved</em> 變成 <em>did the layout save</em>。
```

### 14-04 · shouldFix · `sections[5].ex[3]`

**Problem.** Add an example with an auxiliary (will) so the rule in the fix above is shown (section has 3 examples; 4 is within the limit).

**Edit.** Insert as a new element at `sections[5].ex[3]`:

```json
{
  "en": "<u>Not only will</u> the new system reduce costs, but it will also shorten delivery times.",
  "zh": "新系統不但會降低成本，還會縮短交貨時間。",
  "note": "助動詞 <em>will</em> 直接搬到主詞前面，<em>reduce</em> 維持原形。"
}
```

### 14-05 · shouldFix · `sections[5].ex[0].note`

**Problem.** Wrap the bare 'be' in <em>.

**Edit.** Replace the field value with:

```
<em>be</em> 動詞直接搬到主詞前面：<em>the hotel is</em> 變成 <em>is the hotel</em>。
```

### 14-06 · shouldFix · `sections[3].ex[4]`

**Problem.** 'online or at the counter' joins an adverb with a prepositional phrase. It is acceptable English, but this chapter teaches that the two sides must have the same form (section 0), and it asks the reader to check by splitting the sentence. The example works against its own rule. Use two 'by' phrases.

**Edit.** Replace the field value with:

```json
{
  "en": "<u>Whether</u> you pay by card <u>or</u> by bank transfer, you will receive a receipt.",
  "zh": "不管是刷卡還是轉帳付款，您都會拿到收據。"
}
```

### 14-07 · shouldFix · `sections[3].table.rows[4][2]`

**Problem.** Match the table example to the revised ex[4].

**Edit.** Replace the field value with:

```
<em>whether you pay by card or by bank transfer</em>
```

### 14-08 · shouldFix · `sections[3].quiz[0].q`

**Problem.** Same adverb plus prepositional-phrase mix in the stem ('online or at the front desk'). Use two prepositional phrases. The answer (either) is unchanged.

**Edit.** Replace the field value with:

```
You can submit the form ___ by email or at the front desk.
```

### 14-09 · shouldFix · `sections[2].quiz[1].q`

**Problem.** '點出跟 sign 共用同一個 to 的那個動詞' can be read as asking for 'sign' itself, since it too shares the 'to'. Say explicitly which word is wanted.

**Edit.** Replace the field value with:

```
<em>sign</em> 前面沒有 <em>to</em>，它借用前面某個動詞的 <em>to</em>。點出跟 <em>sign</em> 共用同一個 <em>to</em> 的另一個動詞（不要點 <em>sign</em> 自己）。
```

### 14-10 · shouldFix · `lead`

**Problem.** The lead says the chapter ends with subject-verb agreement after or/nor, but two more sections follow (not only inversion; rather than / instead of). Update the roadmap.

**Edit.** Replace the field value with:

```
用 <em>and</em>、<em>or</em>、<em>but</em> 把東西接在一起時，被接起來的每一項要是<b>同一種形式</b>：名詞配名詞、形容詞配形容詞、原形（第 6 章）配原形。這叫平行結構。<em>both … and</em>、<em>either … or</em> 這類成對的連接詞也一樣，而且前半決定後半。這一章教你先找出被接起來的是哪幾塊，再檢查它們長得一不一樣；接著講兩個主詞用 <em>or</em>、<em>nor</em> 接起來時，動詞要跟誰；最後講 <em>not only</em> 放在句首時的倒裝，以及 <em>rather than</em> 和 <em>instead of</em> 的差別。
```

## chapters/15-prep.json

Checked and correct: The tap item verified (Friday = 5). Every choose item has one answer. At/on/in, in versus within, for/since with the present perfect, during versus while (consistent with chapter 8), and according to versus in accordance with are correct. The fixed-phrase table is correct and lists no wrong preposition. No banned phrases and no test claims.

### 15-01 · mustFix · `sections[4].takeaway`

**Problem.** Wrong for two of the three words. 'They are all prepositions followed by a noun or Ving' is false for during and throughout: 'during completing the form' and 'throughout working' are not standard. It also contradicts chapter 8 (sections[4].body[1]: during takes only a noun) and this chapter's own table (during and throughout take a named event or period). Only prior to takes Ving. The STYLE glossary's generic 'preposition + noun or Ving' should not be copied onto during.

**Edit.** Replace the field value with:

```
<em>during</em> 接事件或時段的名稱，<em>throughout</em> 是從頭到尾，<em>prior to</em> 是正式的 <em>before</em>；三個都是介系詞，後面不能接子句。<em>during</em>、<em>throughout</em> 後面接名詞，<em>prior to</em> 可以接名詞或 Ving。
```

### 15-02 · mustFix · `sections[6].h`

**Problem.** Overgeneralization. As a heading it says every phrase-final 'to' is a preposition. 'in order to', 'be able to', 'be about to', 'be supposed to', 'have to' end in 'to' and take the base form. A reader with the heading as the rule will write 'in order to reducing costs'. Chapter 6 (sections[3]) presents this as 'some phrases'. Heading and body need the contrast.

**Edit.** Replace the field value with:

```
有些片語最後的 to 是介系詞，不是 to V
```

### 15-03 · mustFix · `sections[6].body[4]`

**Problem.** Add the contrast the heading needs: phrases ending in a to-V 'to'. Insert after body[3].

**Edit.** Insert as a new element at `sections[6].body[4]`:

```
不是所有以 <em>to</em> 結尾的片語都是這樣。<em>in order to</em>、<em>be able to</em>、<em>be about to</em>、<em>be supposed to</em>、<em>have to</em> 裡的 <em>to</em> 是 to V 的 <em>to</em>，後面接原形：<em>in order to reduce costs</em>。用上面的測試：<em>in order to the salary</em> 說不通，所以它的 <em>to</em> 是 to V。
```

### 15-04 · mustFix · `sections[6].takeaway`

**Problem.** Takeaway must carry the contrast too.

**Edit.** Replace the field value with:

```
<em>in addition to</em>、<em>prior to</em> 這類片語最後的 <em>to</em> 是介系詞，後面接名詞或 Ving；<em>in order to</em> 這類的 <em>to</em> 是 to V，後面接原形。
```

### 15-05 · mustFix · `sections[2].body[3]`

**Problem.** The decision rule 'look at the verb: one-time action means by, lasting state means until' fails for states that must be reached by a deadline: 'The room must be ready by 9 a.m.' (chapter 16 uses exactly this: 'be ready by 9 a.m.'), 'be available by', 'be open by'. A reader using the verb-type rule would pick until. The question form already used in body[1] and body[2] (latest time to finish vs how long it lasts) is the reliable test; make that the rule and show a state with by.

**Edit.** Replace the field value with:

```
換錯會怎樣？<em>Please submit the report until Friday.</em> 變成「請一直交報告，交到星期五為止」。交報告不是能持續的事，句子就說不通。判斷時不要只看動詞，直接問那個時間的作用：它是「最晚要完成的期限」（<em>by</em>），還是「這個狀態一直持續到那時才結束」（<em>until</em>）？同樣是狀態，<em>The room must be ready by 9 a.m.</em>（最晚九點要準備好）用 <em>by</em>，<em>The room will stay closed until 9 a.m.</em>（一直關到九點）用 <em>until</em>。
```

### 15-06 · shouldFix · `sections[6].body[3]`

**Problem.** Companion to the heading fix. Link to chapter 6, which already taught look forward to and listed be committed to, be used to, contribute to. Without the link this reads as new material, and the list of other phrases ending in prepositional 'to' is missing here.

**Edit.** Replace the field value with:

```
<em>look forward to</em> 也是同一個道理（第 6 章講過）：<em>We look forward to working with you.</em> 第 6 章列過的 <em>be committed to</em>、<em>be used to</em>、<em>contribute to</em>，後面接動作時也用 Ving。
```

### 15-07 · shouldFix · `sections[2].table.rows[1][0]`

**Problem.** The row is a tendency, not a rule (see the fix above).

**Edit.** Replace the field value with:

```
常搭配的動詞（只是傾向）
```

### 15-08 · shouldFix · `sections[2].table.rows[1][1]`

**Problem.** Add a state that takes by, matching the fixed body[3].

**Edit.** Replace the field value with:

```
<em>submit</em>、<em>pay</em>、<em>reply</em>、<em>finish</em>、<em>arrive</em>、<em>be ready</em>
```

### 15-09 · shouldFix · `sections[2].takeaway`

**Problem.** Takeaway should state the question test, not the verb-type shortcut.

**Edit.** Replace the field value with:

```
<em>by</em> 回答「最晚什麼時候要完成」，是期限；<em>until</em> 回答「一直持續到什麼時候」。
```

### 15-10 · shouldFix · `sections[0].body[4]`

**Problem.** '前面有 this、next、last、every 時，什麼介系詞都不加' is too broad: 'in this quarter', 'in the last year', 'in the next two weeks', 'for the last three years' keep their prepositions. The rule holds for the bare phrases (next Monday, last year, every morning). Say so.

**Edit.** Replace the field value with:

```
有兩個地方要特別看。第一，一天裡的時段一旦加上某一天，就變成「某一天」，改用 <em>on</em>：<em>in the morning</em>，但 <em>on Friday morning</em>，決定介系詞的是 <em>Friday</em>。第二，前面直接放 <em>this</em>、<em>next</em>、<em>last</em>、<em>every</em> 時，什麼介系詞都不加：<em>next Monday</em>、<em>last year</em>、<em>every morning</em>。這些字已經把時間定好位置了，不需要介系詞，寫成 <em>on next Monday</em> 是錯的。（前面還有 <em>the</em> 的說法是另一回事，例如 <em>in the next two weeks</em>。）
```

### 15-11 · shouldFix · `sections[0].table.rows[5][0]`

**Problem.** Match the table row to the narrowed rule.

**Edit.** Replace the field value with:

```
前面直接放 <em>this</em>、<em>next</em>、<em>last</em>、<em>every</em>
```

### 15-12 · shouldFix · `sections[0].body[3]`

**Problem.** 'at night' is the commonest exception to 'times of day take in' and is missing; business readers will meet it constantly (night shift, at night).

**Edit.** Replace the field value with:

```
<em>in</em> 接<b>比一天長的時段</b>，像一個範圍，事情發生在裡面：<em>in June</em>、<em>in 2027</em>、<em>in the third quarter</em>。一天裡的時段也用 <em>in</em>：<em>in the morning</em>、<em>in the afternoon</em>、<em>in the evening</em>。只有 <em>night</em> 例外，要說 <em>at night</em>。
```

### 15-13 · shouldFix · `sections[4].table.rows[1][2]`

**Problem.** '在那段期間裡的某時候' is contradicted by the chapter's own ex[0] ('keep your phone on silent during the presentation' means the whole presentation) and by body[2], which says only that during 'may be' just one moment. Say that during is neutral.

**Edit.** Replace the field value with:

```
在那段期間裡（可能是其中某個時候，也可能是整段）
```

### 15-14 · shouldFix · `sections[2].body[1]`

**Problem.** '星期五之前交' is ambiguous in Chinese about whether Friday itself is included; 'by Friday' includes Friday. Use 'at the latest'.

**Edit.** Replace the field value with:

```
<em>by</em> 回答「<b>最晚什麼時候要做完？</b>」它是期限，搭配做一次就完成的動作：交、付、回覆、抵達、完成。<em>Please submit the report by Friday.</em>（最晚星期五要交，星期三交也可以）
```

### 15-15 · shouldFix · `sections[2].ex[0].zh`

**Problem.** Same ambiguity: '六月三十日前' may read as excluding June 30.

**Edit.** Replace the field value with:

```
請在六月三十日（含）以前寄回簽好的合約。
```

### 15-16 · shouldFix · `sections[2].quiz[0].q`

**Problem.** The stem is odd: if the room is reserved until 3 p.m. there is no reason to 'leave before then'. Use a stem where only until fits and the logic is clear. The answer (until) is unchanged.

**Edit.** Replace the field value with:

```
The conference room is reserved for our team ___ 3 p.m., so no other group can use it before then.
```

### 15-17 · shouldFix · `sections[7].ex[1].zh`

**Problem.** '出倉' reads as Hong Kong or mainland usage; in Taiwan the natural phrase is '從倉庫出貨'.

**Edit.** Replace the field value with:

```
根據 Reyes 先生的說法，貨今天早上已經從倉庫出貨了。
```

### 15-18 · shouldFix · `check[4]`

**Problem.** The check is meant to test the chapter's thresholds so that a reader who passes may skip. The 'prepositional to + Ving' point (a whole section, and the one most likely to trip a reader) is not tested, so a reader could pass all four items and skip it. Add a fifth item (limit is 5).

**Edit.** Insert as a new element at `check[4]`:

```json
{
  "type": "choose",
  "q": "In addition to ___ the new hires, Ms. Hale manages the payroll.",
  "options": [
    "train",
    "training",
    "trained"
  ],
  "answer": 1,
  "why": "<em>in addition to</em> 整組是介系詞，最後的 <em>to</em> 後面放得進名詞（<em>in addition to the new hires</em>），所以接動作時用 Ving：<em>training</em>。"
}
```

### 15-19 · shouldFix · `sections[1].body[0]`

**Problem.** 'in + length of time = after that time' is true for statements about the future. With a past or completed sense it means how long something took ('finished in two hours'). Mark the scope.

**Edit.** Replace the field value with:

```
<em>in</em> 後面接一段時間長度，說的是未來的事時，意思是「從現在起，過了這段時間」，也就是「……之後」：<em>The renovation will be finished in about three weeks.</em>（大約三週後完工）。中文很容易把它想成「三週內」，但它說的是一個時間點：大約三週後。
```

## chapters/16-mandative.json

Checked and correct: Both tap items verified (include = 6; be + translated = 6 and 7). The base form is the correct answer in every item, and is acceptable in British formal writing; the problem is only that other options may also be acceptable there (16-01 to 16-07). The suggest/insist split, the 'suggest him to' error, 'not + base', and 'be' in the passive are all correct. Nothing in the chapter needs 'were'. No banned phrases and no test claims.

### 16-01 · mustFix · `check[0].q`

**Problem.** British handling. The stem '選正式書面的寫法' does not exclude the other options in British formal writing. British writers use 'should + base form' and also the plain indicative after recommend, suggest, essential and similar words ('recommended that each team reviews'), and the indicative is not confined to informal British writing. The stem must say which standard decides the item. Use the American formal standard, which excludes the indicative, and which the correct answer also satisfies in British formal writing (the base form is accepted there). Same fix for the six other stems below.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：Our director recommended that each team ___ its budget by May 1.
```

### 16-02 · mustFix · `check[1].q`

**Problem.** Same fix (stem names the standard).

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：It is essential that every guest ___ a photo ID at check-in.
```

### 16-03 · mustFix · `check[2].q`

**Problem.** Same fix. In British formal writing 'does not sign' (indicative) and 'should not sign' (not offered) are both seen.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：Our lawyer recommended that the company ___ the contract until the terms are revised.
```

### 16-04 · mustFix · `check[3].q`

**Problem.** Same fix. 'is made' is the British indicative form.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：The contract requires that the payment ___ made in full before delivery.
```

### 16-05 · mustFix · `sections[1].quiz[0].q`

**Problem.** Same fix.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：Last year, the auditors recommended that the firm ___ its records every quarter.
```

### 16-06 · mustFix · `sections[2].quiz[0].q`

**Problem.** Same fix. 'It is important that each team member reviews the agenda' is the form British writers most often produce with 'important'.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法，哪一句對？
```

### 16-07 · mustFix · `sections[3].quiz[0].q`

**Problem.** Same fix.

**Edit.** Replace the field value with:

```
依美式正式書面英文的標準寫法選：The supervisor asked that the new technician ___ the machine without training.
```

### 16-08 · mustFix · `sections[6].body[2]`

**Problem.** Companion to the stem change, and the current text is also inaccurate: 'the examples and questions of this book all use the no-should form' is contradicted by sections[6].ex[1] in this chapter. The paragraph must explain why the stems name the American standard, so the reader is not confused when a British text writes should or the indicative.

**Edit.** Replace the field value with:

```
這一章其他的例句和題目，都用不加 <em>should</em> 的原形寫法，因為它在美式和英式的正式書面英文裡都通用。題目裡寫「依美式正式書面英文的標準寫法」，是為了排除上面兩種英式的寫法。讀到加 <em>should</em> 的句子，或直接用一般現在式的句子，知道意思跟原形一樣就好。
```

### 16-09 · mustFix · `sections[6].body[2]`

**Problem.** British handling is incomplete. The section offers 'should + base' as the only British alternative and omits the plain indicative ('requested that Mr. Kim submits'), which British writers do use. Say so, with the book's decision. Insert after body[1].

**Edit.** Insert as a new element at `sections[6].body[2]`:

```
英式英文裡也有人在這種子句裡直接用一般的現在式，例如 <em>requested that Mr. Kim submits the report</em>。這種寫法美式正式書面英文不用，而原形的寫法在美式和英式的正式書面英文裡都能用，所以這本書教原形。
```

### 16-10 · shouldFix · `lead`

**Problem.** '正式的書面英文讓子句裡的動詞用原形' presents the base form as the only formal choice. Say it is the American standard and also accepted in British formal writing.

**Edit.** Replace the field value with:

```
<em>The manager requested that Mr. Kim submit the report.</em> 這句的 <em>submit</em> 沒有 <em>-s</em>，也沒有跟著 <em>requested</em> 變成過去式，但它不是打錯。表示要求、建議、必要的字後面接 that 子句（第 3 章）時，美式正式書面英文讓子句裡的動詞用原形（第 6 章），英式正式書面英文也通用這個寫法，不管主詞是誰、時間是什麼時候。這一章講哪些字會帶出這個句型、為什麼要用原形，以及否定和被動怎麼寫。
```

### 16-11 · shouldFix · `mistakes[0].why`

**Problem.** 'submits' is called simply wrong. Under the chapter's own standard it is wrong; in British usage it is common. State the standard.

**Edit.** Replace the field value with:

```
要求的 that 子句用原形，主詞是單數也不加 <em>-s</em>。英式文字裡常見 <em>submits</em>，但這一章採用的是美式正式書面英文的標準寫法。
```

### 16-12 · shouldFix · `mistakes[2].why`

**Problem.** Same: 'are attached' is a British indicative.

**Edit.** Replace the field value with:

```
在這個句型裡，<em>be</em> 動詞一律用原形 <em>be</em>；被動是 <em>be</em> + p.p.。<em>are attached</em> 在英式文字裡常見，但不是美式正式書面英文的標準寫法。
```

### 16-13 · shouldFix · `sections[2].body[4]`

**Problem.** Important pattern missing: the passive 'It is recommended / required / requested / suggested that ...' is the usual form in notices, policies and emails, and it takes the base form after 'that'. The chapter covers adjectives and nouns but not this. Insert after body[3].

**Edit.** Insert as a new element at `sections[2].body[4]`:

```
公告和規定裡常見被動的說法：<em>It is recommended that all employees attend the briefing.</em>、<em>It is required that every visitor sign in.</em> 這裡的 <em>It is recommended / required / requested / suggested that</em> 跟形容詞的句型一樣，後面的 that 子句用原形。
```

### 16-14 · shouldFix · `sections[2].ex[4]`

**Problem.** Add an example for the passive pattern (section has 4 examples; 5 is within the limit).

**Edit.** Insert as a new element at `sections[2].ex[4]`:

```json
{
  "en": "It is <u>recommended</u> that all employees <u>attend</u> the safety briefing.",
  "zh": "建議所有員工參加安全說明會。"
}
```

### 16-15 · shouldFix · `sections[1].body[1]`

**Problem.** '第二個看起來像打錯的地方是時態' dangles: tense was already raised in section 0 (body[0], body[1]), and no 'first' is named here. Drop the counting.

**Edit.** Replace the field value with:

```
這些動詞自己可以是現在式、過去式或未來式，但 that 子句裡永遠是原形，不跟著變：<em>recommends that she apply</em>、<em>recommended that she apply</em>、<em>will recommend that she apply</em>。一般的句子裡，第 4 章教你讓前後時態配合；在這個句型裡，不要配合。
```

### 16-16 · shouldFix · `sections[0].body[4]`

**Problem.** '假設語氣' is used without a chapter pointer (STYLE section 2: remind where a term was taught). It is chapter 10.

**Edit.** Replace the field value with:

```
有些文法書把這個句型放在「假設語氣」（第 10 章）底下，寫成「要求、建議 + that + 主詞 + (should) + 原形」。叫什麼名字不重要，重要的是動詞的形式：原形。
```

### 16-17 · shouldFix · `sections[2].ex[1].zh`

**Problem.** 'important' is translated as '必須', which is stronger than the English; 'important' says it matters.

**Edit.** Replace the field value with:

```
每位新進員工都務必完成安全課程。
```

### 16-18 · shouldFix · `sections[2].ex[2].zh`

**Problem.** 'layout' is rendered '格局' in chapter 14 (sections[5].ex[1]) and '配置' here. Use one term for the book.

**Edit.** Replace the field value with:

```
新的格局顯然省時間。
```

### 16-19 · shouldFix · `sections[4].body[0]`

**Problem.** Wrap the bare 'be 動詞' in <em> (STYLE section 1). The same applies to sections[4].body[1], sections[4].takeaway, sections[4].quiz[0].why and mistakes[2].why, where 'be 動詞' or 'be' appears outside <em>.

**Edit.** Replace the field value with:

```
<em>is</em>、<em>am</em>、<em>are</em>、<em>was</em>、<em>were</em> 的原形是 <em>be</em>。所以在這個句型裡，<em>be</em> 動詞一律寫成 <em>be</em>：<em>It is essential that the room be ready by 9 a.m.</em>，不是 <em>is ready</em>。
```

## Verdicts

**13-quantity.json.** The chapter is accurate and teaches in a sound order: the countable test comes first, and the quantity words are then sorted by what noun follows. The contrast pairs are well chosen, the examples are natural and the translations are correct. Four mustFix items stand between it and release. The few / a few quiz has a defensible second answer. The 'less than' rule is half taught, with no 'fewer than 50 employees', and its 'add two' test contradicts its own exception. The statement that 'almost' cannot stand before a noun is false as written. And 'the other' is used as a pronoun, and 'the others' is missing, in a section whose title promises both. The shouldFix items (feedback row, nouns that are both countable and uncountable, 'an amount of', the chapter 12 cross-reference) are small. Ready once the four mustFix items are applied.

**14-parallel.json.** The chapter is accurate and paced well. The take-apart-and-test method for parallel forms and the three-paragraph treatment of shared to / will are the right slow handling of the threshold, and the quizzes each have one answer. There is one mustFix: the table in section 4 contains 'Not only the staff but also the director is', which begins with 'Not only' without inversion, while section 5 says a fronted 'not only' inverts. The rule needs scoping to 'not only' followed by a full clause. The shouldFix items are examples that join an adverb to a prepositional phrase against the chapter's own rule, the missing auxiliary case in inversion, an out-of-date roadmap in the lead, and one tap question that can be read two ways. Ready once the mustFix item is applied.

**15-prep.json.** The time-preposition half is clear and the 'size of the time' idea works. The fixed-phrase half is honest that there is no rule to derive. Three mustFix items need action. The during / throughout / prior to takeaway says all three take a noun or Ving, which is wrong for during and throughout and contradicts chapter 8. The heading of section 7 says the 'to' at the end of a phrase is a preposition, which is false for in order to, be able to and similar phrases, and the section has no contrast. And the by / until verb-type heuristic fails for states reached by a deadline ('ready by 9 a.m.'), which chapter 16 itself uses. The shouldFix items are the scope of this/next/last, 'at night', Chinese glosses that leave 'by June 30' ambiguous, the 'during' table cell, a fifth check item for 'to + Ving', and one Hong Kong style word. Not ready until the three mustFix items are applied.

**16-mandative.json.** The content is accurate for standard American formal English, and the teaching order is right for this reader: the odd-looking sentence first, then why, then the verbs, adjectives, negatives and be, then the suggest / insist exceptions. Every example and tap index checks out. The one mustFix is British handling. The stems say only 'formal written', which does not exclude the plain indicative or 'should' in British formal writing, and section 6 offers only 'should' as the British alternative. Name the standard in the seven stems, and rewrite section 6 so it states that the indicative also occurs in British writing and why the book teaches the base form. The passive 'It is recommended that' pattern is the main thing missing. Ready once the mustFix items are applied.
