# Grammar book review: chapters 9-12

Files reviewed: `chapters/09-relative.json`, `10-conditional.json`, `11-pronoun.json`, `12-compare.json`.
Read first: `STYLE.md`, and `chapters/03-clause.json` (definitions of 子句, 主要子句, 從屬子句, 關係子句 preview), plus the parts of chapters 4, 8, 13 that these chapters point to (time/conditional clauses, unless, another/others).

Method: every English sentence, Chinese translation, `<u>` mark, quiz option and `why` was read; every `tap` item was split on spaces and the index list checked; `python3 check.py` passes for all four files (no format errors). No chapter file was edited.

How to read this file:
- Field paths are relative to the chapter file, 0-based exactly as in the JSON (so "section 8" in prose is `sections[7]`).
- **mustFix** = wrong, misleading, or a quiz that does not have exactly one defensible answer. **shouldFix** = teaching gap, unnatural wording, forward reference, or polish.
- Replacement text is given in the same markup as the JSON (`<em>`, `<b>`, `<u>`). Chinese uses 「」 so no double quotes need escaping.
- Where a section already has 5 examples (the maximum), I say so and propose a paragraph only.

## Summary

| File | mustFix | shouldFix | Verdict in one line |
|---|---|---|---|
| 09-relative | 1 | 12 | Accurate and well sequenced; one false demonstration (omitting a subject relative pronoun), one missing topic (agreement inside the relative clause) |
| 10-conditional | 1 | 7 | Very solid core; one quiz distractor is arguably grammatical, and several absolute claims need the polite-request exception |
| 11-pronoun | 1 | 9 | Good; the its/it's test fails for it's = it has; pronoun case after than/as and each/everyone + their are missing |
| 12-compare | 1 | 6 | Good; the -ly rule contradicts the chapter's own "earlier"; two small gaps (of the two, than I) |

Verified as correct (no change needed): all `tap` answers (09 check[4] = [4]; 09 sections[3].quiz[0] = [3,4,5]; 11 check[3] = [1]; 11 sections[5].quiz[0] = [5]); the who/whom logic including "we believe" and "the director said"; that-after-comma and that-after-preposition rules; whose for things; the three conditional patterns and were for all persons; Should/Had/Were inversion forms; no banned phrases, no test-frequency claims, a takeaway in every section, quiz counts 10 / 10 / 8 / 9.

---

## 09-relative.json

### 09-M1 [mustFix] Demonstration of "who cannot be omitted" is itself a grammatical sentence
- Where: `sections[7].body[2]`, `sections[7].ex[3].en`, `sections[7].ex[3].zh`
- Problem: `The client called this morning is waiting in the lobby.` is not broken. It parses as a reduced passive relative clause (the client [who was] called this morning is waiting), meaning someone phoned the client. The text says the reader "接下去不通", which is false, and a learner who has done chapter 6 (分詞) can see it parses. The rule itself (a subject relative pronoun cannot be omitted) is correct; the demonstration must use a verb with no passive participle. `arrive` is intransitive, so deleting `who` gives a clearly broken sentence, and it ties back to chapter 3's "count the finite verbs" rule.
- Replace `sections[7].body[2]` with:
```
當主詞時不能省略。試試看：<em>The client who arrived this morning is waiting in the lobby.</em> 拿掉 <em>who</em>，變成 <em>The client arrived this morning is waiting in the lobby.</em> 一句話裡有兩個有時態的動詞（<em>arrived</em>、<em>is waiting</em>），中間沒有任何字把它們接起來，句子就壞了（第 3 章）。當主詞的關係代名詞，同時就是那個接句子的字，拿掉它就接不起來，所以不能省。
```
- Replace `sections[7].ex[3].en` with: `The client <u>who arrived this morning</u> is waiting in the lobby.`
- Replace `sections[7].ex[3].zh` with: `今天早上抵達的那位客戶正在大廳等候。`
- (`note` stays as is.)

### 09-S1 [shouldFix, high] Missing: the verb after a subject relative pronoun agrees with the antecedent
- Where: add after `sections[2].body[4]` (new `body[5]`) and add one example to `sections[2].ex` (currently 4, so one more fits).
- Problem: Neither chapter 7 nor chapter 9 says that the verb after subject `who/which/that` takes its number from the antecedent (an employee who works / employees who work). Chapter 11 only does it for `those who`. This is a standard source of errors in business writing.
- Add `sections[2].body[5]`:
```
關係代名詞當主詞時，後面的動詞要和先行詞的單複數一致（第 7 章）。<em>who</em>、<em>which</em>、<em>that</em> 自己沒有單複數，它代替誰，動詞就跟著誰：<em>an engineer who <b>designs</b> apps</em>（先行詞 <em>engineer</em> 是單數），<em>engineers who <b>design</b> apps</em>（先行詞 <em>engineers</em> 是複數）。
```
- Add to `sections[2].ex`:
```
{"en": "The <u>engineers</u> who design the app work in our Ashford office.", "zh": "設計這個 app 的工程師在我們的 Ashford 辦公室上班。", "note": "先行詞 <em>engineers</em> 是複數：<em>who</em> 後面用 <em>design</em>，不是 <em>designs</em>。"}
```

### 09-S2 [shouldFix] "we believe 不是子句的骨架" collides with chapter 3's definition of 子句
- Where: `sections[3].body[1]`
- Problem: Chapter 3 teaches that anything with a subject and a finite verb is a clause. `we believe` has both, so "它不是子句的骨架" confuses a learner who has just learned that rule. The accurate statement: it is an inserted short clause, and the relative clause's own subject is `who` and own verb is `is`.
- Replace with:
```
原因是 <em>we believe</em> 是插進來的一小段，意思是「我們認為」。它自己也有主詞和動詞，但它只是夾在中間的插入語，不是關係子句的骨架；關係子句真正的主詞是 <em>who</em>，真正的動詞是 <em>is</em>。把它劃掉：<em>the candidate ___ is the most qualified</em>，空格後面直接是動詞 <em>is</em>，缺主詞，答案是 <em>who</em>。
```

### 09-S3 [shouldFix, high] The "we believe" section never shows the case where whom is still correct after an inserted phrase
- Where: `sections[3].body[4]`; add `sections[3].ex[3]` (section has 3 examples, so one more fits).
- Problem: The section teaches "cross out the inserted phrase, usually find a missing subject". The learner can over-generalize to "after we believe, always who". The cross-out test cuts both ways: `The candidate whom we believe the committee will choose` keeps `whom`, because `choose` lacks an object. Also the last sentence of `body[4]` ("we interviewed 後面沒有 [動詞]") is imprecise: in `The candidate whom we interviewed will start in May`, a verb does follow `interviewed`. The real difference is the verb type: believe/think/say can take a whole clause as object; interview needs a person.
- Replace `sections[3].body[4]` with:
```
對照真的缺受詞的句子：<em>The candidate whom we interviewed yesterday …</em> <em>interview</em>（面試）後面一定要接一個人，<em>we interviewed</em> 後面少了那個人，這時才用 <em>whom</em>。<em>believe</em>、<em>think</em>、<em>say</em> 這類動詞不一樣：後面可以接一整件事（「我們認為這位應徵者最合格」），所以 <em>we believe</em> 後面可以直接接 <em>is</em>。如果插入語後面接的是另一個主詞，缺受詞的就是那個主詞的動詞，這時還是用 <em>whom</em>：<em>The candidate whom we believe the committee will choose …</em>（劃掉 <em>we believe</em>，剩 <em>whom the committee will choose</em>，<em>choose</em> 後面少了受詞）。
```
- Add to `sections[3].ex`:
```
{"en": "The candidate <u>whom</u> we believe the committee will choose starts in May.", "zh": "我們認為委員會會選上的那位應徵者，五月到職。", "note": "劃掉 <em>we believe</em> → <em>whom the committee will choose</em>：<em>choose</em> 後面少了受詞，用 <em>whom</em>。"}
```

### 09-S4 [shouldFix] "take place in a room" is not a verb that needs a preposition to take an object
- Where: `sections[5].body[0]`
- Problem: "有些動詞要帶介系詞才能接受詞：…take place in a room" is misleading. `in a room` is a place adjunct, not an object the verb requires. The section's own example `the room in which the interview will take place` is fine; the setup sentence is not.
- Replace with:
```
有些動詞要帶介系詞才能接受詞：<em>speak to</em> someone、<em>work for</em> a company。地點、時間的介系詞也一樣，後面的名詞是它的受詞：<em>in</em> a room、<em>on</em> Friday。這時關係代名詞是<b>介系詞的受詞</b>。例如：<em>This is the manager.</em> <em>We spoke to the manager.</em>
```

### 09-S5 [shouldFix] Stranded-preposition example: wrong field use, and a missed contrast with "that"
- Where: `sections[5].body[1]`, `sections[5].ex[2]`
- Problem 1: `ex[2].zh` holds a comment ("意思同上；介系詞留在句尾，語氣比較口語。") instead of a translation; the comment belongs in `note`.
- Problem 2: `whom ... to` mixes a formal relative pronoun with a colloquial stranded preposition. A more useful example shows the contrast the chapter relies on: when the preposition is stranded, `that` (or nothing) is fine; only the fronted `to whom` bans `that`. This is exactly the "that after a preposition" rule learners ask about.
- Replace `sections[5].body[1]` with:
```
接成一句有兩種放法。第一種，介系詞留在原位，在子句最後：<em>This is the manager whom we spoke to.</em> 這種放法，關係代名詞也可以用 <em>that</em>，或乾脆省略（第 8 節）：<em>the manager that we spoke to</em>、<em>the manager we spoke to</em>。第二種比較正式，介系詞跟著關係代名詞一起移到前面：<em>This is the manager to whom we spoke.</em>
```
- Replace `sections[5].ex[2]` with:
```
{"en": "Mr. Grant is the buyer <u>that</u> we sent the samples <u>to</u>.", "zh": "Grant 先生就是我們寄樣品過去的那位採購。", "note": "介系詞留在句尾，語氣比較口語，這時可以用 <em>that</em>。移到前面的 <em>to whom</em> 才不能用 <em>that</em>。"}
```

### 09-S6 [shouldFix] `<u>` marks and one translation do not point at the lesson
- Where: `sections[5].ex[0]`, `sections[4].ex[0]`, `sections[4].ex[1]`, `sections[4].ex[2]`
- Problem: Section 6 teaches `in which`, but `ex[0]` underlines the antecedent `room`. Section 5 teaches `whose + noun`, but `ex[0]` and `ex[2]` underline the antecedent while `ex[1]` underlines `whose` alone. Also `sections[5].ex[0].zh` ("面試會在這個房間進行") drops "This is".
- Replace:
```
sections[5].ex[0].en: This is the room <u>in which</u> the interview will take place.
sections[5].ex[0].zh: 這就是面試會舉行的那個房間。
sections[4].ex[0].en: We called the client <u>whose order</u> was delayed.
sections[4].ex[1].en: Employees <u>whose contracts</u> end in June should contact Human Resources.
sections[4].ex[1].note (add): <em>whose contracts</em> = <em>the employees' contracts</em>。
sections[4].ex[2].en: The company <u>whose software</u> we use has opened an office in Harlow Bay.
```

### 09-S7 [shouldFix] Forward references to whose and to omission before they are taught
- Where: `sections[2].quiz[0].options[2]`, `sections[2].table` (所有格 column), `sections[6].table.rows[3][0]`
- Problem: Section 3's quiz offers "…空格後面接的是一個屬於先行詞的名詞", which is the `whose` idea, taught two sections later; the table's 所有格 column and section 7's omission row do the same. Previewing is acceptable in a table, but a quiz option should not depend on an untaught idea, and STYLE asks for one idea per section.
- Replace `sections[2].quiz[0].options` with: `["缺主詞", "缺受詞"]` (answer stays `1`).
- Append to `sections[2].body[4]`: ` 表格最右邊那一欄的 <em>whose</em>，兩節之後再講。`
- Replace `sections[6].table.rows[3][0]` with: `當受詞的關係代名詞能不能省略（下一節）`

### 09-S8 [shouldFix] "a faster delivery date" is not natural business English
- Where: `sections[8].body[1]`, `sections[8].ex[0]`
- Problem: Dates are "earlier", not "faster"; "a faster delivery" would be natural, "a faster delivery date" is not.
- In `sections[8].body[1]` replace `a faster delivery date` with `an earlier delivery date`.
- Replace `sections[8].ex[0].en` with: `<u>What</u> the client wants is an earlier delivery date.`
- Replace `sections[8].ex[0].zh` with: `客戶想要的是更早的交貨日期。`

### 09-S9 [shouldFix] Mistranslation of "spoke to"
- Where: `sections[7].ex[2].zh`
- Problem: "我們聯絡的那位經理" translates "contacted", not "spoke to".
- Replace with: `我們談過話的那位經理今天下午會回您電話。`

### 09-S10 [shouldFix] "whose 後面一定緊接一個名詞" reads as "no adjective allowed"
- Where: `sections[4].body[1]`
- Replace with:
```
<em>whose</em> 是 <em>his</em>、<em>her</em>、<em>its</em>、<em>their</em> 的關係代名詞版本，所以後面一定接一個名詞（中間可以有形容詞，如 <em>whose new order</em>），而且這個名詞屬於先行詞：<em>whose order</em> 是那位客戶的訂單。名詞前面不加 <em>the</em> 或 <em>a</em>，就像不會說 <em>her the order</em>。
```

### 09-S11 [shouldFix, low] Restrictive "which" in every thing-example, while the chapter itself says American writing prefers "that"
- Where: `sections[2].ex[2]`, `sections[2].ex[3]` (also `sections[0].ex[1]`, `sections[1].ex[1]` if wanted)
- Problem: `sections[6].body[4]` correctly says that for restrictive clauses "美式書面比較常用 that". Yet six of the restrictive thing-examples use `which`. All are acceptable, but the examples should not be the less common choice every time. Section 3's subject/object demonstration does not depend on which word is used, so switch these two.
- Replace:
```
sections[2].ex[2].en: The app <u>that crashed yesterday</u> has been fixed.
sections[2].ex[2].note: 事物當主詞：<em>that</em>（<em>which</em> 也可以）。
sections[2].ex[3].en: The app <u>that we launched last week</u> already has 2,000 users.
sections[2].ex[3].note: 事物當受詞，還是 <em>that</em>（<em>which</em> 也可以）。
```

### 09-S12 [shouldFix, small] Two wording slips
- `check[3].why`: "只能用 which（事物）或 who（人）" leaves out whom/whose. Replace with: `逗號後面的關係子句是補充說明，不能用 <em>that</em>。先行詞 <em>office</em> 是事物，用 <em>which</em>。`
- `sections[3].takeaway`: "通常會發現" hedges a rule that is deterministic once the condition is met. Replace with: `空格後面是 <em>we think</em>、<em>we believe</em> 這類短語、再接一個動詞時，先劃掉短語，就會發現缺的是主詞。`

### Verdict, chapter 9
This is a careful chapter, and the threshold points are taught slowly: relative pronoun as connector plus pronoun, subject versus object slot, the inserted "we believe/the director said", whose, preposition fronting, comma versus that, omission. The who/whom rules, the ban on that after a comma or preposition, whose for things, and the omission conditions are all stated correctly, and every tap and choose item has exactly one answer. The chapter uses chapter 3's terms consistently. The one mustFix is a demonstration that does not demonstrate (09-M1). The most valuable additions are the agreement note (09-S1) and the contrast example for whom after an inserted phrase (09-S3), because the chapter otherwise nudges learners toward "after we believe, always who". The remaining items are wording, underline conventions, and two forward references.

---

## 10-conditional.json

### 10-M1 [mustFix] A quiz distractor is a grammatical sentence, and the `why` overclaims
- Where: `sections[2].quiz[0]` (options and why)
- Problem: Option 3 `If the client approved the design, we will start next week.` is grammatical as an open past condition (the speaker does not yet know whether the client approved). The `why` says the past tense "是「不是真的」的訊號，會和 will 互相矛盾", which is false in general (`If the invoice was sent on Monday, it should have arrived`). A learner who knows open past conditions can legitimately pick it, so the item does not have exactly one defensible answer. Adding `tomorrow` to all three options makes option 3 impossible and keeps the lesson (no `will` in the if-clause).
- Replace `sections[2].quiz[0]` with:
```
{
  "type": "choose",
  "q": "下面哪一句是對的？",
  "options": [
    "If the client will approve the design tomorrow, we will start next week.",
    "If the client approves the design tomorrow, we will start next week.",
    "If the client approved the design tomorrow, we will start next week."
  ],
  "answer": 1,
  "why": "<em>tomorrow</em> 是未來，主要子句用 <em>will</em>，表示這是可能發生的條件。這時 <em>if</em> 子句用現在式 <em>approves</em>，不用 <em>will</em>（第一句）。過去式 <em>approved</em> 講的是過去，不能配 <em>tomorrow</em>（第三句）。"
}
```

### 10-S1 [shouldFix, high] Absolute "would only in the main clause / two signals fight" needs the polite-request exception
- Where: `sections[3].body[2]`, `sections[4].body[3]`, `mistakes[1].why`
- Problem: Business letters are full of `If you have any questions, I would be happy to help` and `I would appreciate it if you could/would reply by Friday`. The chapter says a present `if` clause with `would` is two signals fighting, and that `would` belongs only in the main clause. Both are true for hypotheticals but a reader of real correspondence will meet counter-examples on day one. Scope the claims and name the exception.
- Replace `sections[3].body[2]` with:
```
沒有一起退會怎樣？<em>If we have more staff, we would open on Sundays.</em> 前半的現在式說「有可能」，後半的 <em>would</em> 說「不是真的」，兩個訊號打架，讀的人不知道你到底有沒有人手。兩半要一起退。有一種常見的例外是客氣的口氣：<em>If you have any questions, I would be happy to help.</em> 這裡的 <em>would</em> 不是在假設，只是把話說得比 <em>will</em> 客氣。信裡的 <em>I would appreciate it if you could reply by Friday.</em> 也一樣：<em>if</em> 子句裡的 <em>could</em>（或 <em>would</em>）是在客氣地請求，不是在假設。
```
- Replace `sections[4].body[3]` with:
```
兩個常見的錯。一是在過去不真的 <em>if</em> 子句裡也放 <em>would</em>（<em>If we would have known</em>）；<em>would</em> 只放在主要子句。二是 <em>would have</em> 後面忘了用 p.p.（<em>would have change</em>）；<em>would have</em> 後面一定是 p.p.：<em>changed</em>、<em>sent</em>、<em>written</em>。
```
- Replace `mistakes[1].why` with: `過去不真的 <em>if</em> 子句不放 <em>would</em>，<em>would</em> 只放在主要子句。這種 <em>if</em> 子句用 <em>had</em> + p.p.。`

### 10-S2 [shouldFix, high] Missing: if + present, present (rules and policies)
- Where: add a paragraph after `sections[2].body[0]` and one example to `sections[2].ex` (currently 3, so one more fits).
- Problem: Policy and system statements (`If an order exceeds $500, shipping is free`) use present + present, not `will`. The chapter only offers `will` (or can/may) in the main clause, so a reader meeting this pattern has nothing to hang it on.
- Add new paragraph after `sections[2].body[0]`:
```
規則和政策也常用 <em>if</em>：兩半都用現在式，說的是「只要……就會……」，每一次都這樣，不是某一次的事。<em>If an invoice is overdue, the system sends a reminder automatically.</em> 要說某一次、還沒發生的事，才用 <em>will</em>：<em>If the invoice is overdue next week, we will call the client.</em>
```
- Add to `sections[2].ex`:
```
{"en": "If an invoice <u>is</u> overdue, the system <u>sends</u> a reminder automatically.", "zh": "只要帳款逾期，系統就會自動寄出催繳提醒。", "note": "規則：兩半都是現在式，不用 <em>will</em>。"}
```

### 10-S3 [shouldFix] "一看動詞的時態，就知道…" is too absolute
- Where: `sections[0].body[3]`
- Problem: A past-tense `if` verb is not always "not real" (open past conditions). The reliable signal is the pairing with the main clause (`will` / `would` / `would have`). Fix the sentence so it teaches the pairing, which is also what the chapter does from section 2 on.
- Replace with:
```
中文兩種都可以說「如果」，再靠「要是」「早知道」這類字眼和語氣表達。英文則一定要在<b>動詞</b>上表現出來：看 <em>if</em> 子句和主要子句的動詞形式（<em>will</em>、<em>would</em>、<em>would have</em>……），就知道說話的人覺得這件事有可能，還是知道它不是真的。這也是為什麼讀錯動詞，就會把意思整個讀反。
```

### 10-S4 [shouldFix] unless: "就是 if … not" needs a limit, and `body[3]` does not make a point
- Where: `sections[6].body[0]`, `sections[6].body[3]` (the same wording is in chapter 8; this is the place to state the limit)
- Problem: `unless` means "except if". It cannot replace `if … not` when the main clause is a reaction to the negative event (`We will be upset if the shipment does not arrive`). `body[3]` ("換句話說的時候要小心意思") does not say what to be careful about.
- Replace `sections[6].body[0]` with:
```
<em>unless</em> 的意思是「除非」，大致等於 <em>if … not</em>。<em>Unless you register by Friday, you cannot attend.</em> = <em>If you do not register by Friday, you cannot attend.</em>
```
- Replace `sections[6].body[3]` with:
```
<em>unless</em> 說的是「照這樣進行，除非出現這個例外」。<em>We will ship the order on Monday unless the parts arrive late.</em> 零件沒晚到，就星期一出貨；零件晚到，就不一定是星期一。如果要說的是「沒發生這件事，就糟了」，用 <em>if … not</em> 比較自然：<em>We will be upset if the shipment does not arrive.</em> 換成 <em>unless the shipment arrives</em> 就不自然。
```

### 10-S5 [shouldFix, small] Third conditional main clause: could have / might have
- Where: `sections[4].body[1]` (section 4 mentions could/might only for the present type)
- Append to `sections[4].body[1]`: ` 主要子句也可以用 <em>could have</em>（本來就能）、<em>might have</em>（本來可能會）加 p.p.。`

### 10-S6 [shouldFix] Two Chinese slips
- `lead`: "一種講不是真的事" is clipped. Replace the first sentence with: `<em>if</em> 的句子有兩種：一種講有可能發生的事，一種講假設、不是事實的事。` (rest of the lead unchanged)
- `check[0].why`: "是在講現在「不是真的」事" lacks 的. Replace with: `<em>if</em> 子句用過去式 <em>had</em>、主要子句用 <em>would</em>，是在講現在「不是真的」的情況：事實和句子相反，預算其實不夠大。這裡的 <em>had</em> 不是過去時間。`

### 10-S7 [shouldFix, optional] Label 「真的條件」 reads as "genuine/true condition"
- Where: `sections[0].h`, `sections[0].body[1]`, `sections[3].body[3]`, `sections[7].body[2]` and about a dozen more (the label appears on 17 lines of the file).
- Problem: 「不真的條件」 is understandable and consistently used, but 「真的條件」 is unidiomatic Taiwan Chinese (it sounds like "a true condition"). If the book keeps the pair, define it once with the plain meaning ("有可能發生的條件／假想的條件"); if you prefer a global change, use 有可能的條件 for 真的條件 and 假想的條件 for 不真的條件, and keep the explanatory phrase 「這不是真的」 where it is.

### Verdict, chapter 10
The core is accurate and well paced. "Step back one tense" is taught from first principles, the threshold that a backshifted past tense is not past time gets its own paragraph, the if-clause-never-takes-will point is explained, were is correctly given for all persons, the mixed conditional is handled with "each half on its own time", and the inversion section correctly limits the forms to Should/Had/Were, fixes the following verb form for each, bans `if` plus inversion, and teaches restoring the `if` clause. The English examples are natural and the Chinese is accurate. The single mustFix is a quiz item (10-M1) that has a second defensible answer. The most useful additions are the polite-request exception (10-S1) and the present-present pattern (10-S2), both of which appear constantly in the business correspondence the book targets. Optional: a one-line mention of the second mixed type (present state, past result: `If we were better prepared, we would have won the contract`).

---

## 11-pronoun.json

### 11-M1 [mustFix] The its / it's test fails for it's = it has, and contradicts the chapter's own example
- Where: `sections[2].body[1]`, `sections[2].quiz[0].why`
- Problem: The method says "把它換成 it is 唸一次，通順就是 it's，不通就是 its". For `It's been a busy quarter` (this chapter's own `ex[1]`, and the `It's been a long week` in the same paragraph), the full form is `it has`; `It is been a busy quarter` is not "通順", so a learner following the method would call it `its`. The method must test both expansions.
- Replace `sections[2].body[1]` with:
```
最容易搞混的是 <em>its</em> 和 <em>it's</em>。<em>it's</em> 是 <em>it is</em> 或 <em>it has</em> 的縮寫：<em>It's late.</em>、<em>It's been a long week.</em> 判斷方法：把它換成 <em>it is</em> 或 <em>it has</em> 唸一次，有一個通順，就是 <em>it's</em>；兩個都不通，就是 <em>its</em>。<em>The hotel has renovated it is lobby</em> 不通，<em>it has lobby</em> 也不通，所以是 <em>its lobby</em>。
```
- Replace `sections[2].quiz[0].why` with: `把 <em>it's</em> 換成 <em>it is</em> 或 <em>it has</em>：<em>lost it is connection</em>、<em>lost it has connection</em> 都不通。這裡要的是「它的連線」，所有格 <em>its</em>，不加撇號。`

### 11-S1 [shouldFix, high] Missing: pronoun case after than / as (and the same logic after prepositions)
- Where: add after `sections[1].body[3]` (that section already has 5 examples, so add a paragraph only).
- Problem: The chapter teaches case by position and the "remove the other person" test, but never covers comparisons (`longer than I / than me`), which is the other place case decisions come up in formal writing. Chapter 12 has no pointer either (see 12-S3). The same "restore the omitted verb" idea is the method.
- Add:
```
<em>than</em>、<em>as</em> 後面的代名詞，要把省略的動詞補回來再選格。<em>Ms. Diaz has worked here longer than I.</em> 補回去是 <em>longer than I have</em>，<em>I</em> 是補回來的 <em>have</em> 的主詞，所以用主格。口語裡常聽到 <em>than me</em>，正式書面用 <em>I</em>。<em>The new hire is as experienced as she.</em> 同理，補回去是 <em>as she is</em>。
```

### 11-S2 [shouldFix] Missing: each / everyone / someone and his or her / their
- Where: add after `sections[4].body[0]`.
- Problem: Section 5 teaches agreement of the pronoun with its antecedent but not the common case where the antecedent is a singular, gender-unspecified noun. Chapter 13 covers each/every for verbs, not for the following pronoun.
- Add:
```
代替 <em>each employee</em>、<em>everyone</em>、<em>someone</em> 這種不指定性別的單數時，書面英文有兩種寫法：<em>his or her</em>（比較保守），或 <em>their</em>（現代英文愈來愈常見，但比較保守的公文仍用 <em>his or her</em>）。最不會出問題的做法，是把句子改成複數：<em>All employees must submit their timesheets by Friday.</em>
```

### 11-S3 [shouldFix] "帶撇號的都是縮寫，不是所有格" contradicts `body[0]`
- Where: `sections[2].body[2]`
- Problem: `body[0]` of the same section says nouns take `'s` for possession (`the company's website`). The last sentence of `body[2]` then says anything with an apostrophe is a contraction. Scope it to the pronoun pairs.
- Replace with:
```
同樣的配對還有 <em>their</em>／<em>they're</em>（= <em>they are</em>）、<em>your</em>／<em>you're</em>（= <em>you are</em>），以及第 9 章的 <em>whose</em>／<em>who's</em>。這幾組裡，帶撇號的都是縮寫，不是所有格；名詞的 <em>'s</em>（<em>the company's website</em>）才是所有格。
```

### 11-S4 [shouldFix] Table cell and one check explanation
- Where: `sections[0].table.rows[4][3]`, `check[0].why`
- Problem 1: `it` has no stand-alone possessive pronoun; "（不常用）" implies a rare form exists. Replace the cell with: `（沒有這個形式）`
- Problem 2: `check[0].why` uses 受格 before section 1 defines it. Replace with: `先把 <em>Mr. Okafor and</em> 拿掉：<em>send the schedule to ___</em>。介系詞 <em>to</em> 後面要用受詞的形式（受格）<em>me</em>。<em>myself</em> 只在主詞也是「我」的時候用。`

### 11-S5 [shouldFix] Reflexive section: takeaway overgeneralizes, and the "myself" error is better shown in its common form
- Where: `sections[3].takeaway`, `sections[3].body[3]` (last sentence)
- Problem: "主詞和受詞是同一個人才用 -self" ignores the emphatic and `by oneself` uses taught in the same section. The closing sentence of `body[3]` ("這種錯誤常出現在想寫得正式一點的郵件裡") is an unsupported frequency claim; the common real-world form of the error is `Mr. Lee and myself`.
- Replace `sections[3].takeaway` with: `當受詞時，主詞和受詞是同一個人才用 <em>-self</em>；不是同一個人，用一般的受格。<em>-self</em> 也可以放在句尾，強調「本人親自」。`
- Replace the last sentence of `sections[3].body[3]` with: `兩個人連在一起時也一樣：<em>Please send the agenda to Mr. Lee and myself</em> 是錯的，句子的主詞是省略掉的 <em>you</em>，要寫 <em>to Mr. Lee and me</em>。<em>myself</em> 聽起來比較正式，所以容易被誤用；傳統文法視為錯誤，正式書面一律用 <em>me</em>。`

### 11-S6 [shouldFix, small] "後面緊接一個名詞" reads as "no adjective allowed"
- Where: `sections[1].body[1]` (first sentence)
- Replace the first sentence with: `後面接一個名詞、表示「誰的」，用所有格：<em>their office</em>、<em>her report</em>，中間有形容詞也一樣（<em>her annual report</em>）。`

### 11-S7 [shouldFix] A quiz where both options are grammatical and the sentence alone is ambiguous
- Where: `sections[8].quiz[0].q`
- Problem: `The two sales teams compete with themselves every quarter` is grammatical (each team against its own past record). The `why` relies on the reader assuming rivalry. Add the disambiguating phrase.
- Replace `q` with: `<em>The two sales teams compete with ___ for the same clients every quarter.</em> 空格填哪一個？` (options, answer, why unchanged)

### 11-S8 [shouldFix] Taiwan usage: 文件夾
- Where: `sections[6].ex[1].zh`
- Replace with: `這些資料夾太小了，有大一點的嗎？`

### 11-S9 [shouldFix, small] one/ones: "另一個" is slightly too narrow, and those who has a natural plural noun alternative
- Where: `sections[6].body[0]`, `sections[7].body[2]`
- `sections[6].body[0]`: `one` stands for "a countable item of that kind", not always "another" (`the lighter one` in `ex[2]`). Replace the second sentence with: `<em>it</em> 代替的是<b>同一個</b>東西；<em>one</em> 代替的是同一種東西裡的<b>一個</b>，不是前面講的那一個本身。`
- `sections[7].body[2]`: add the noun route. Replace with: `不能說 <em>them who</em> 或 <em>they who</em>。想用名詞開頭，可以說 <em>people who</em>、<em>employees who</em>（也是複數）；要說單數，用 <em>anyone who</em>，配單數動詞：<em>Anyone who needs a parking pass …</em>`

### Verdict, chapter 11
A clear, well-ordered chapter. The five forms are laid out in a table and then taught by position, the "remove the other person" method for Ms. Diaz and me is correct, the reflexive and each other sections give contrasts rather than definitions, the antecedent-finding method ("filter by number, then by meaning") is sound, and the examples are natural business sentences. The single mustFix (11-M1) is a method that gives the wrong answer for one of the chapter's own examples. The chapter should also cover pronoun case after than/as (11-S1) and each/everyone with their (11-S2), since "pronoun case in comparisons" is a standard formal-writing trap and is not taught anywhere in the book. The rest is wording and scope-limiting.

---

## 12-compare.json

### 12-M1 [mustFix] The -ly rule contradicts "earlier" used elsewhere in the chapter
- Where: `sections[1].body[1]`
- Problem: The paragraph says -y words change y to i (easier, busiest), then says "以 -ly 結尾的副詞也用 more". `early` is an adverb ending in -ly, and its forms are `earlier / earliest`; the chapter itself uses `The earlier you register` in section 7 (`sections[6]`). Read as written, the rule predicts `more early`, and `quickly` also ends in -y, so the order of the two rules is ambiguous. Limit the y-to-i rule to adjectives and name the exception.
- Replace with:
```
兩個音節的字：以 <em>-y</em> 結尾的形容詞，把 <em>y</em> 改成 <em>i</em> 再加 <em>-er</em>、<em>-est</em>：<em>easy</em> → <em>easier</em>、<em>busy</em> → <em>busiest</em>。其他兩個音節的字大多用 <em>more</em>、<em>most</em>：<em>more modern</em>、<em>more careful</em>。以 <em>-ly</em> 結尾的副詞也用 <em>more</em>：<em>more quickly</em>、<em>more carefully</em>。例外是 <em>early</em>（形容詞和副詞都一樣）：<em>earlier</em>、<em>earliest</em>，第 7 節的 <em>The earlier you register</em> 就是這個字。
```

### 12-S1 [shouldFix] Quiz sentence drops the verb that `body[1]` says must be there
- Where: `sections[6].quiz[0]`
- Problem: `sections[6].body[1]` says each half is "the + comparative, then a subject and verb". The quiz sentence `The more you order, ___ the price per unit.` leaves the second half without a verb, which contradicts that and makes the sentence less natural.
- Replace `q` with: `<em>The more you order, ___ the price per unit gets.</em> 空格填哪一個？`
- Replace `why` with: `前半是 <em>the more</em>，後半也要「<em>the</em> + 比較級」放在最前面：<em>the lower</em>，後面再接主詞和動詞（<em>the price per unit gets</em>）。少了 <em>the</em> 或用最高級都不成句型。`
- (options and answer unchanged)

### 12-S2 [shouldFix] Missing: "the + comparative + of the two"
- Where: add after `sections[7].body[1]` (section already has 5 examples, so paragraph and quiz only); the chapter currently has 9 quizzes, so one more fits.
- Problem: The chapter teaches "superlative for three or more" but never what to use for exactly two (`the cheaper of the two`), a common error and the reason `check[3]`'s distractor `the larger` exists.
- Add paragraph:
```
只有<b>兩個</b>東西在比的時候，不用最高級，用「<em>the</em> + 比較級 + <em>of the two</em>」：<em>Plan A is the cheaper of the two plans.</em>（兩個方案中比較便宜的那個）。三個以上才用最高級：<em>the cheapest of the four plans</em>。
```
- Add quiz to `sections[7].quiz`:
```
{"type": "choose", "q": "<em>We compared two suppliers, and Norvel is the ___ of the two.</em> 空格填哪一個？", "options": ["more reliable", "most reliable"], "answer": 0, "why": "只有兩個東西比，用「<em>the</em> + 比較級」：<em>the more reliable</em>。<em>most</em> 要三個以上才用。"}
```

### 12-S3 [shouldFix] Missing: pointer for pronoun case after than
- Where: add as `sections[3].body[3]` (after the "than 可以省略" paragraph).
- Problem: `than` is the preposition-or-conjunction where pronoun case is decided (see 11-S1). Chapter 12 never says so.
- Add:
```
<em>than</em> 後面如果是代名詞，要把省略的動詞補回來再選格：<em>Ms. Diaz has worked here longer than I (have).</em> 正式書面用主格 <em>I</em>（第 11 章）。
```

### 12-S4 [shouldFix, small] "very 只能修飾原級" is too strong
- Where: `check[4].why`
- Problem: `very` also modifies superlatives (`the very best`), which the chapter's last section covers. The claim needed here is only that `very` does not go before a comparative.
- Replace with: `比較級前面要加強，用 <em>much</em>、<em>far</em>、<em>even</em>。<em>very</em> 修飾的是原級（<em>very light</em>），不放在比較級前面。`

### 12-S5 [shouldFix, small] Cross-reference to chapter 9 for the superlative range clause
- Where: `sections[7].ex[3].note` (currently absent)
- Add `note`: `<em>we have ever received</em> 是省略了 <em>that</em> 的關係子句（第 9 章），說明 <em>order</em>。`

### 12-S6 [shouldFix] The check does not test the chapter's main threshold
- Where: `check[0]` (it only tests "than takes a comparative", which the item's own stem gives away)
- Problem: Section 4's threshold ("compare like with like: those of / that of") is not in the check, and the check is supposed to reflect the chapter's thresholds.
- Replace `check[0]` with:
```
{"type": "choose", "q": "<em>Our response times are shorter than ___ of most competitors.</em> 空格填哪一個？", "options": ["those", "that", "them"], "answer": 0, "why": "比的是「我們的回覆時間」和「大多數競爭對手的回覆時間」，兩邊要同一類。<em>times</em> 是複數，用 <em>those</em> 代替 <em>the response times</em>；單數才用 <em>that</em>。"}
```

### Verdict, chapter 12
A tidy, accurate chapter. The three levels, the partner words (than, as...as, the + range), the ban on `more` plus `-er`, `very` versus `much/far/even`, `one of the` plus a plural noun, and `in` versus `of` for superlative ranges are all correct and taught with contrasts. The comparison-of-like-with-like threshold (`those of` / `that of`) gets a proper paragraph. The single mustFix (12-M1) is a spelling-rule paragraph that conflicts with an example the chapter itself relies on. The gaps are small: the two-item case (`of the two`), pronoun case after `than` (shared with chapter 11), and a check item for the like-with-like threshold. Chinese is natural and consistent with STYLE.md.

---

## Cross-chapter notes (no change needed in these files, listed so the other chapters stay consistent)
- Chapter 3 `sections[6].ex[1]` and chapter 9 both use `The client who called this morning ...`; chapter 3 only uses it as a relative clause (nothing is deleted), so it is fine there. Only chapter 9's omission demonstration (09-M1) needs the verb change.
- Chapter 8 `sections[5]` says "unless 就是 if … not" with the same caveat missing as in 10-S4; consider one matching sentence there.
- Chapter 7 does not cover verb agreement inside a relative clause; if 09-S1 is not adopted in chapter 9, it should go in chapter 7.
