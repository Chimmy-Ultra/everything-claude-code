# Grammar book review: chapters 1-4

Files reviewed: `chapters/01-pos.json`, `02-skeleton.json`, `03-clause.json`, `04-tense.json`.
Read first: `STYLE.md`, `check.py`, and the way `template.html` renders a chapter (body, then examples, then table, then quiz, then takeaway). Chapters 5-16 were searched for every cross-reference into chapters 1-4 so that the changes below do not break them (see the last section).

Method: every English sentence, Chinese translation, `<u>` mark, quiz option and `why` was read; every `tap` item was split on spaces and its index list checked by script; `python3 check.py` passes for all four files as they stand. All replacements below were applied to scratch copies of the four files and the copies also pass `check.py`. No chapter file was edited.

How to read this file:
- Field paths are relative to the chapter file and 0-based exactly as in the JSON (`sections[5]` is the sixth section, shown as n.6 on the page, n being the chapter number).
- **mustFix** = wrong, misleading as written, or a quiz without exactly one defensible answer. **shouldFix** = teaching gap, forward reference, unnatural wording, or polish; `high` marks the ones to do first.
- 'Replace X with' gives the complete new value of the field. 'Change' gives the exact fragment and its replacement. 'Insert after `list[n]`' and 'Append' add a new item; every index in this file refers to the ORIGINAL file, so apply insertions from the bottom of a list upwards, or apply them all against the original.
- Replacement text is in the same markup as the JSON (`<em>`, `<b>`, `<u>`); Chinese uses 「」, so no double quotes need escaping.

## Summary

| File | mustFix | shouldFix | Verdict in one line |
|---|---|---|---|
| 01-pos | 1 | 10 | Sound and well paced; one wrong word family (rely/reliability), one missing topic that chapter 2's first example runs into (same-shape words) |
| 02-skeleton | 1 | 9 | Best-built chapter; one false universal (prepositional phrases are always removable) that its own examples contradict |
| 03-clause | 1 | 7 | Accurate on the Ving / to V threshold; one false statement (subject = noun before the bracket), several missing pieces |
| 04-tense | 2 | 7 | Accurate examples, strong present-perfect section; two rules stated too broadly (when/if noun clauses, by + deadline) |

mustFix by chapter:
- 01-pos: 01-M1 The rely row is not a word family
- 02-skeleton: 02-M1 'Everything a preposition introduces can be removed' is false, and the chapter's own examples show it
- 03-clause: 03-M1 'The main clause's subject is the noun in front of the bracket' is false when that noun follows a preposition
- 04-tense: 04-M1 'when / if clauses take the present for the future' is false for when / if / whether noun clauses; 04-M2 The future-perfect takeaway reverses the body: 'by + future deadline' does not require will have + p.p.

Verified as correct (no change needed): all `tap` answers (01 sections[3].quiz[0] = [6]; 02 check[0] = [8], check[2] = [1], sections[1].quiz[0] = [2], sections[5].quiz[0] = [2, 8, 11], sections[6].quiz[0] = [1]; 03 check[4] = [8, 9], sections[3].quiz[0] = [5-10], sections[6].quiz[0] = [7]; 04 sections[2].quiz[0] = [9, 10], sections[7].quiz[0] = [7]), each with one defensible span and a `why` that states the method; every `choose` item has exactly one correct option; every English example sentence is grammatical, set in a business situation and uses invented names (the few places where the wording is not the most natural choice are listed below as shouldFix); `<u>` marks sit on the words the note names; no banned phrases, no claims about the test, a takeaway in every section, section quiz counts 7 / 7 / 8 / 9; Chinese is Taiwan usage (投影片, 簡報, 雲端硬碟, 介系詞, 稽核) apart from the items listed below (雇, 主任, name style); terms are used as in the STYLE.md table and are consistent across the four chapters (連綴動詞 and 助動詞 are introduced once and reused; section cross-references such as 第 5 節 and 第 4 節 point at the right sections).

---

## 01-pos.json

### 01-M1 [mustFix] The rely row is not a word family
- Where: `sections[6].table.rows[4]`
- Problem: The noun of *rely* is *reliance* (依賴). *Reliability* is the noun of *reliable* (可靠度). The row therefore mixes two families, and the section's own claim that the four words 'mean about the same' (`sections[6].body[2]`) is false for it: *our reliance on one supplier* and *our supplier's reliability* are different statements. A learner who stores rely → reliability will fill a *reliance* blank wrongly. *reliable* / *reliably* are already shown in the suffix table (`sections[5].table`) and in `sections[1].ex[0]`, so nothing is lost by swapping the row for a regular family.
- Replace `sections[6].table.rows[4]` with:
```
[
  "<em>differ</em>",
  "<em>difference</em>",
  "<em>different</em>",
  "<em>differently</em>"
]
```

### 01-S1 [shouldFix, high] Words with one shape and two jobs (report, increase, late, early, hard) are never mentioned
- Where: `sections[5].body[1]`, new paragraph after `sections[5].body[5]`, `sections[5].takeaway`
- Problem: The chapter's method is 'read the job from the position and the ending'. It never says that many everyday business words have one shape and two jobs: noun/verb (*report, increase, plan, order, offer, request, review, process*; the chapter itself uses *review* as verb and noun in `sections[4].ex[0]` and `ex[1]` without comment) and adjective/adverb (*late, early, fast, hard, daily, weekly, monthly*). Chapter 2 `sections[0].ex[1]` then uses *started late* with *late* as an adverb, straight after chapter 1 listed *late* as an adjective (`sections[0].table.rows[2]`) and described adverbs as 'adjective + -ly' (`sections[5].table`). Two pairs also change meaning (*hard / hardly*, *late / lately*), which is the usual reason an '-ly means adverb' habit goes wrong. Without this paragraph the learner has no way to read a shape that gives no clue. The new paragraph is the fifth exception, so `body[1]` changes from four to five.
- Replace `sections[5].body[1]` with: (now: `字尾只是線索。有四組例外要認得。`)
```
字尾只是線索。有五組例外要認得。
```
- Insert after `sections[5].body[5]` (it becomes `sections[5].body[6]`; later items shift down by one):
```
五，有些字形狀完全不變，同一個字可以當兩種詞性。名詞兼動詞：<em>report</em>、<em>increase</em>、<em>plan</em>、<em>order</em>、<em>offer</em>、<em>request</em>、<em>review</em>。<em>We will review the plan.</em> 裡的 <em>review</em> 是動詞，<em>The review is due on Friday.</em> 裡的 <em>review</em> 是名詞。形容詞兼副詞：<em>late</em>、<em>early</em>、<em>fast</em>、<em>hard</em>、<em>daily</em>、<em>weekly</em>、<em>monthly</em>。<em>The report is late.</em> 裡的 <em>late</em> 描述名詞 <em>report</em>，是形容詞；<em>The report arrived late.</em> 裡的 <em>late</em> 描述動作 <em>arrived</em>，是副詞。這種字從形狀看不出詞性，只能看位置。注意 <em>hard</em>（努力地）和 <em>hardly</em>（幾乎不）、<em>late</em>（遲）和 <em>lately</em>（最近）意思不一樣，不能因為有 <em>-ly</em> 就選它。
```
- Replace `sections[5].takeaway` with: (now: `字尾是線索，位置是證據；-ly 不一定是副詞，-al 和 -ive 也可能是名詞。`)
```
字尾是線索，位置是證據；<em>-ly</em> 不一定是副詞，<em>-al</em> 和 <em>-ive</em> 也可能是名詞，有些字（<em>report</em>、<em>late</em>）兩種詞性長得一樣，只能看位置。
```

### 01-S2 [shouldFix, high] The small words before a noun (a, the, our, this) have no name, and this is listed twice with two jobs
- Where: `sections[1].body[1]`, `sections[0].table.rows[6]`, `sections[7].body[3]`
- Problem: `sections[1].body[1]` lists *a, an, the, our, your, its, this* as '這類字' without a name, and none of the seven 詞性 covers them; a reader who forgot grammar will ask what *the* is. `sections[0].table.rows[6]` lists *this* as a 代名詞, while `sections[1]` treats it as a word that must be followed by a noun (*this report*), so the learner cannot tell which is meant. The pronoun row also says pronouns replace 'a noun mentioned before', which leaves out *we* and *you*, the pronouns a business reader sees most.
- Replace `sections[1].body[1]` with:
```
第一，名詞前面的小字：<em>a</em>、<em>an</em>、<em>the</em>（冠詞），<em>our</em>、<em>your</em>、<em>its</em>（所有格），<em>this</em>、<em>that</em>（後面接名詞時，意思是「這個」「那個」）。這些字不在七種詞性裡，但它們後面<b>一定</b>有一個名詞在等。中間可以夾形容詞（<em>the new budget</em>），但最後總要落在名詞上。<em>this</em> 單獨出現（<em>This is late.</em>）時才是代名詞。
```
- Replace `sections[0].table.rows[6]` with:
```
[
  "代名詞",
  "代替名詞：前面提過的人事物，或說話的人和聽的人",
  "<em>it</em>、<em>they</em>、<em>them</em>、<em>we</em>、<em>you</em>"
]
```
- Replace `sections[7].body[3]` with:
```
<b>代名詞</b>代替名詞，免得重複。<em>The client called. She wants a refund.</em> 裡的 <em>She</em> 就是 <em>the client</em>。<em>we</em>、<em>you</em> 則直接指說話的人和聽的人。代名詞的細節在第 11 章。
```

### 01-S3 [shouldFix] A noun can stand in front of a noun; -ing / -ed words are often adjectives
- Where: new paragraph after `sections[1].body[1]`, new paragraph after `sections[2].body[1]`
- Problem: `sections[3].quiz[0].why` (*marketing team*) and `sections[5].ex[2]` (*a sales representative*) rely on 'a noun can describe another noun', but the chapter only says that a noun slot is introduced by *a / the / our* plus adjectives. A reader who has just learned 'the word in front of a noun is an adjective' will not know what *sales* is doing. *-ing / -ed* words in adjective position (*a growing market, an experienced manager, the attached file*) are very common in business writing and look like verbs in an adjective slot; one sentence and a pointer to chapter 6 is enough here.
- Insert after `sections[1].body[1]` (it becomes `sections[1].body[2]`; later items shift down by one):
```
名詞前面的字不一定是形容詞，也可以是另一個名詞：<em>sales team</em>（業務團隊）、<em>travel expenses</em>（差旅費）、<em>safety glasses</em>（護目鏡）。前面那個字在說明後面那個名詞，但它自己還是名詞。
```
- Insert after `sections[2].body[1]` (it becomes `sections[2].body[2]`; later items shift down by one):
```
<em>-ing</em> 和 <em>-ed</em> 結尾的字也常放在名詞前面當形容詞：<em>a growing market</em>、<em>an experienced manager</em>、<em>the attached file</em>。這類字第 6 章再講。
```

### 01-S4 [shouldFix] Adverbs: 'describe things other than nouns' is stated without exception, and the position list invites verb + adverb + object
- Where: `sections[3].body[0]`, `sections[3].body[2]`
- Problem: '副詞描述名詞以外的東西' has no exception. Adverbs also stand in front of numbers and quantity words (*approximately 200 employees, nearly all*), which chapter 13 `sections[7]` also meets (*almost 200 employees*). `body[2]` lists where an adverb goes but never says that it normally does not go between a verb and its direct object; *reviewed carefully the report* is a typical error for Chinese speakers, and the list reads as if 'after the verb' were allowed. `body[2]` also says 做事的人 and 動作 where STYLE §2 has 主詞 and 動詞.
- Replace `sections[3].body[0]` with:
```
副詞主要描述<b>名詞以外</b>的東西：動作怎麼做（<em>reviewed carefully</em>）、形容詞的程度（<em>very late</em>、<em>highly qualified</em>），或說話的人對整句話的態度（<em>Unfortunately, …</em>）。數字和數量字前面也常放副詞（<em>approximately 200 employees</em>、<em>nearly all</em>）。
```
- Replace `sections[3].body[2]` with:
```
常見的副詞位置：主詞和動詞中間（<em>She quickly replied.</em>）；<em>has</em>、<em>is</em>、<em>will</em> 和後面的動詞中間（<em>has finally arrived</em>）；形容詞前面（<em>extremely busy</em>）；句子開頭加逗號（<em>Fortunately, …</em>）；句尾（<em>She replied quickly.</em>）。副詞通常不放在動詞和受詞中間：不說 <em>She reviewed carefully the report.</em>，說 <em>She carefully reviewed the report.</em> 或 <em>She reviewed the report carefully.</em>。
```

### 01-S5 [shouldFix] Adjective section: 'two places' then a third, no test for linking verbs, pronouns left out
- Where: `sections[2].body[0]`, `sections[2].body[3]`, `sections[2].takeaway`
- Problem: `body[0]` says the adjective appears in 'two places'; `body[4]` then adds 'a third place', and the takeaway lists two. `body[3]` is the chapter's stated threshold, but it gives the learner no test they can run: 'doesn't do an action' is a judgement call (*She looked carefully at the report* is an action, with the same verb). It lists five verbs, while *look, sound, feel, get, prove* behave the same way, and chapter 2 already uses *look* and *sound*. A usable test is 'replace the verb with *is*'. 'Describes a noun' also leaves out pronouns (*She seems happy*).
- Replace `sections[2].body[0]` with: (now: `形容詞只做一件事：描述名詞。它出現在兩個地方。`)
```
形容詞只做一件事：描述名詞（或代名詞：<em>She seems happy.</em>）。它出現在三個地方，最常見的是前兩個。
```
- Replace `sections[2].body[3]` with:
```
第二種位置是門檻。很多人看到動詞後面，就想用副詞，因為「副詞修飾動詞」。可是 <em>remain</em>、<em>seem</em> 這類動詞並沒有在做什麼動作，它們只是把前面的名詞和後面的描述接起來，像一個等號。等號後面描述的是名詞，所以用形容詞。這種動詞叫<b>連綴動詞</b>，第 2 章講「補語」時會再看到。<em>look</em>（看起來）、<em>sound</em>（聽起來）、<em>feel</em>（感覺起來）、<em>get</em>（變得，<em>get better</em>）、<em>prove</em>（<em>prove useful</em>）也是同一類。怎麼測？把動詞換成 <em>is</em>，句子還通，後面就是形容詞：<em>The fees seem reasonable.</em> 換成 <em>The fees are reasonable.</em>，意思幾乎不變。同一個動詞也可能真的在做動作，例如 <em>She looked carefully at the report.</em>，換成 <em>is</em> 就不通，那時後面才是副詞。
```
- Replace `sections[2].takeaway` with: (now: `形容詞描述名詞：放在名詞前面，或放在 be、remain、seem、become 後面。`)
```
形容詞描述名詞：放在名詞前面，放在 <em>be</em>、<em>remain</em>、<em>seem</em>、<em>become</em> 後面，或放在 <em>make</em>、<em>keep</em>、<em>find</em>＋名詞的後面。
```

### 01-S6 [shouldFix] First takeaway does not follow from the section
- Where: `sections[0].takeaway`
- Problem: '中文不變形，所以讀英文時要特別看位置' is not what the section concluded. The body says the two clues are position and ending and that position wins when they disagree; it never says Chinese readers should look at position *because* Chinese does not change shape. This is the one sentence the reader keeps from the opening section.
- Replace `sections[0].takeaway` with: (now: `英文用字的形狀標出它的工作；中文不變形，所以讀英文時要特別看位置。`)
```
英文用字的形狀標出它的工作；判斷詞性，先看位置，再用字尾確認。
```

### 01-S7 [shouldFix] Use 主詞 / 動詞 (STYLE §2) instead of 做事的人 / 動作 / 主角; one 'why' narrows the noun to things
- Where: `check[0].why`, `check[1].why`, `sections[4].body[1]`, `sections[4].body[3]`
- Problem: STYLE §2 makes 主詞 and 動詞 the shared terms, and `sections[1].body[3]` introduces 主詞. The chapter nevertheless says 主角 (`check[0].why`), 做事的人 and 動作 (`check[1].why`, `sections[4].body[1]`). 做事的人 does not fit a thing as subject (*The review … takes a day*). `check[0].why` also limits the blank to 'the thing announced' (被宣布的那件事), but the blank could just as well be a person (*the winner was announced*). `sections[4].body[3]` says that if a verb is already present the remaining blanks are noun, adjective or adverb, and leaves out *to* + base form, Ving and p.p., which chapter 2 teaches as non-finite and which fill blanks in a sentence that already has a verb.
- Replace `check[0].why` with: (now: `空格前面是 <em>the</em>，<em>the</em> 後面一定要落在一個名詞上。這個名詞也是 <em>was announced</em> 的主角：被宣布的那件事。`)
```
空格前面是 <em>the</em>，<em>the</em> 後面一定要落在一個名詞上。這個名詞也是 <em>was announced</em> 的主詞：被宣布的人或事。
```
- Replace `check[1].why` with: (now: `句子已經有做事的人 <em>Ms. Okada</em> 和動作 <em>reviewed</em>，空格夾在中間，說明「怎麼審」。描述動作的是副詞（例如 <em>carefully</em>）。拿掉它，句子還是完整的。`)
```
句子已經有主詞 <em>Ms. Okada</em> 和動詞 <em>reviewed</em>，空格夾在中間，說明「怎麼審」。描述動作的是副詞（例如 <em>carefully</em>）。拿掉它，句子還是完整的。
```
- Replace `sections[4].body[1]` with:
```
動詞通常緊跟在主詞後面，而且會隨著時間變形：<em>approve</em>、<em>approves</em>、<em>approved</em>、<em>will approve</em>。這種會隨時間變化的動詞，第 2 章叫它「有時態的動詞」。
```
- Replace `sections[4].body[3]` with: (now: `判斷詞性時，先看句子有沒有動詞。還沒有，缺的很可能就是動詞；已經有了，其他空位通常是名詞、形容詞或副詞。`)
```
判斷詞性時，先看句子有沒有動詞。還沒有，缺的很可能就是動詞；已經有了，其他空位通常是名詞、形容詞或副詞（也可能是 <em>to</em>＋原形、Ving、p.p.，這幾種不算有時態的動詞，第 2 章會講）。
```

### 01-S8 [shouldFix, small] Two section quizzes: one repeats a check item, one has a word that can be read as a verb
- Where: `sections[2].quiz[0]`, `sections[4].quiz[0]`
- Problem: `sections[2].quiz[0]` is the same item as `check[2]` (*seem* + *clear* / *reasonable*). A reader who missed `check[2]` and then read the section is re-tested with the same pattern; vary the verb (*remain*) so the quiz shows the rule carries over. `sections[4].quiz[0]` uses *errors*, which is a noun here but can be read as a verb (*the system errors out*), so an adverb option can be argued; *mistakes* has no verb reading.
- Replace `sections[2].quiz[0]` with:
```
{
  "type": "choose",
  "q": "<em>Our prices remain ___ in the Asian market.</em> 空格放哪一個？",
  "options": [
    "competitive",
    "competitively",
    "competition"
  ],
  "answer": 0,
  "why": "<em>remain</em> 是連綴動詞，後面描述的是 <em>prices</em>（價格仍然有競爭力），要用形容詞 <em>competitive</em>。價格不等於「競爭」，所以不是名詞 <em>competition</em>。"
}
```
- Replace `sections[4].quiz[0].q` with: (now: `<em>The new software ___ errors in our monthly reports.</em> 這句缺的是哪一種詞性？`)
```
<em>The new software ___ mistakes in our monthly reports.</em> 這句缺的是哪一種詞性？
```
- Replace `sections[4].quiz[0].why` with: (now: `前面有 <em>The new software</em>，後面有 <em>errors</em>，中間卻沒有任何動作。缺的是動詞，例如 <em>reduces</em>（減少）。`)
```
前面有 <em>The new software</em>，後面有 <em>mistakes</em>，中間卻沒有任何動作。缺的是動詞，例如 <em>reduces</em>（減少）。
```

### 01-S9 [shouldFix, small] Suffix table gives only the American -ize spelling
- Where: `sections[5].table.rows[3][1]`
- Problem: STYLE §1 line 17 asks for American spelling in examples but requires the answers to be right in British and American formal English. A learner who meets *organise, finalise* in a British text will think the suffix is missing from the table.
- Replace `sections[5].table.rows[3][1]` with: (now: `<em>-ize</em>、<em>-ify</em>、<em>-en</em>`)
```
<em>-ize</em>（英式拼 <em>-ise</em>）、<em>-ify</em>、<em>-en</em>
```

### 01-S10 [shouldFix, small] Chinese wording, and English words left outside <em> (STYLE §1)
- Where: `sections[5].ex[1].zh`, `sections[2].ex[2].zh`, `sections[7].ex[2].zh`, `check[2].why`, `sections[1].takeaway`, `sections[7].takeaway`
- Problem: (1) *the director's approval* → 主任 is a small-unit title in Taiwan business usage; for an approval chain 總監 reads naturally (the same word is used for *director* in chapter 2). (2) 還算合理 weakens *remain reasonable even in summer*. (3) 看完 adds 'finished reading', which *reviewed … overnight* does not say. (4) STYLE §1 says English words inside Chinese take `<em>`; two takeaways and one `why` leave them bare (*a、the、your*; *because*; *seem*).
- Replace `sections[5].ex[1].zh` with: (now: `這份提案需要主任的核准。`)
```
這份提案需要總監的核准。
```
- Replace `sections[2].ex[2].zh` with: (now: `這家飯店的價格即使在夏天也還算合理。`)
```
這家飯店的價格即使在夏天也依然合理。
```
- Replace `sections[7].ex[2].zh` with: (now: `Ochoa 女士寄來投影片，團隊連夜看完了。`)
```
Ochoa 女士寄來投影片，團隊連夜審閱了。
```
- In `check[2].why`: `不是在說「怎麼 seem」` → `不是在說「怎麼 <em>seem</em>」`
- Replace `sections[1].takeaway` with: (now: `a、the、your 這類字和介系詞的後面，都在等一個名詞。`)
```
<em>a</em>、<em>the</em>、<em>your</em> 這類字和介系詞的後面，都在等一個名詞。
```
- Replace `sections[7].takeaway` with: (now: `小字的詞性決定後面接什麼：介系詞接名詞，because 這類連接詞接一整句話。`)
```
小字的詞性決定後面接什麼：介系詞接名詞，<em>because</em> 這類連接詞接一整句話。
```

### Verdict, chapter 1
Chapter 1 is close to ready. The pacing suits a reader who has forgotten grammar: it starts from why English changes shape, ranks position above suffix, and gives the one real threshold (a linking verb takes an adjective) its own paragraph with the equals-sign picture. Examples are natural business English, translations are accurate, the single tap item has one defensible answer, and the check items test position rather than vocabulary. One item must change before release: the *rely / reliability* row is not a word family, and the section's claim that family members 'mean about the same' is false for it (01-M1). The most useful additions are small: say that many words keep one shape for two jobs (*report, increase, late, early, hard*), because chapter 2's first example (*started late*) otherwise contradicts what the reader just learned (01-S1), and name the small words before a noun (*a, the, our, this*) so that *this* is not listed as both a pronoun and a noun-marker (01-S2). Everything else is wording: use 主詞/動詞 consistently, soften 'adverbs never describe nouns', and put English words in `<em>` in the takeaways.

---

## 02-skeleton.json

### 02-M1 [mustFix] 'Everything a preposition introduces can be removed' is false, and the chapter's own examples show it
- Where: `sections[5].body[1]`, `sections[5].body[2]`, new paragraph after `sections[5].body[2]`, `sections[5].ex`, `sections[5].takeaway`, `sections[4].body[2]`
- Problem: The section teaches that every string introduced by a preposition is a removable accessory ('拿掉之後，句子的文法還是完整的'; takeaway '介系詞那一串都是配件'). That is false for two common patterns, and the chapter's own material contradicts it: `check[2]` (*belong to Mr. Becker*: remove it and *The boxes belong.* is left) and `sections[6].ex[1]` (*The list of approved vendors is on the shared drive*: remove it and *The list … is.* is left). Verb + preposition (*belong to, depend on, reply to, apply for, comply with*) and *be* + place or time (*is on the shared drive, is at 3 p.m., is based in Taipei*) need their prepositional phrase. A reader who strips every preposition phrase will 'find' skeletons that are not sentences. `sections[4]` (補語) also never says that *be* can be followed by a place or time, so the 'is on the shared drive' pattern has no home in the chapter.
- Replace `sections[5].body[1]` with:
```
其他的字多半是<b>修飾語</b>：形容詞（<em>new</em>）、副詞（<em>carefully</em>）、介系詞帶頭的一組字（<em>of our Westbrook branch</em>、<em>for next year</em>）。它們補充細節，拿掉之後，句子的文法還是完整的。
```
- Replace `sections[5].body[2]` with: (now: `找骨架的方法，就是一件一件拿掉：先拿掉副詞，再拿掉介系詞帶頭的那一串，再拿掉名詞前面的形容詞。剩下拿不掉的，也就是一拿掉句子就倒的，就是主詞、動詞、受詞或補語。`)
```
找骨架的方法，就是一件一件拿掉：先拿掉副詞，再拿掉介系詞帶頭的那一串（有兩種拿不掉，見下一段），再拿掉名詞前面的形容詞。剩下拿不掉的，也就是一拿掉句子就倒的，就是主詞、動詞、受詞或補語。
```
- Insert after `sections[5].body[2]` (it becomes `sections[5].body[3]`; later items shift down by one):
```
有兩種介系詞那一串拿不掉。一是動詞離不開它：<em>belong to</em>、<em>depend on</em>、<em>reply to</em>、<em>apply for</em>。拿掉 <em>to Mr. Becker</em>，<em>The boxes belong.</em> 就不成句。二是 <em>be</em> 後面說地點或時間：<em>The agenda is on the shared drive.</em>、<em>The meeting is at 3 p.m.</em>。拿掉就剩 <em>The agenda is.</em>，不成句。判斷方法不變：拿掉之後句子倒了，就留著。
```
- Append to `sections[5].ex`:
```
{
  "en": "The <u>agenda</u> <u>is</u> <u>on the shared drive</u>.",
  "zh": "議程放在共用雲端硬碟上。",
  "note": "<em>on the shared drive</em> 說明 <em>is</em> 的地點，拿掉就剩 <em>The agenda is.</em>，所以要留下。"
}
```
- Replace `sections[5].takeaway` with: (now: `形容詞、副詞、介系詞那一串都是配件；拿掉就倒的，才是骨架。`)
```
形容詞、副詞和多數介系詞那一串是配件；拿掉就倒的，才是骨架。
```
- Replace `sections[4].body[2]` with:
```
補語可以是形容詞（<em>The report is late.</em>），也可以是名詞（<em>Ms. Park is the new director.</em>）。<em>be</em> 後面也可以接地點或時間（<em>The meeting is at 3 p.m.</em>），這一組字同樣拿不掉。拿掉補語，句子就倒：<em>The report is.</em> 不成句。
```

### 02-S1 [shouldFix, high] 'A noun after a preposition is never the subject' needs a pointer to the quantity phrases
- Where: `sections[6].body[3]`, new paragraph after `sections[6].body[3]`, `sections[6].takeaway`
- Problem: The sentence is bold in `body[3]` and is the takeaway. As a statement about structure it holds, but the learner will turn it into an agreement rule, and for *a number of employees are …*, *some of the budget is …*, *most of the rooms have …* the verb follows the noun after *of*. Chapter 7 `sections[3].body[4]` and chapter 13 `sections[7]` state this as an exception to this chapter's method, so the first exposure is a reversal. One paragraph that points forward is enough; the detail stays in chapters 7 and 13. `body[3]` also calls the error 錯在結構, which is vaguer than 'the wrong noun was taken as the subject'.
- In `sections[6].body[3]`: `錯在結構。` → `錯在找錯了主詞。`
- Insert after `sections[6].body[3]` (it becomes `sections[6].body[4]`; later items shift down by one):
```
有一類片語要小心：<em>a number of</em>、<em>some of</em>、<em>most of</em>、<em>all of</em>、<em>half of</em>，這種只在說「多少」的片語。動詞要看 <em>of</em> 後面的名詞：<em>A number of employees are …</em>、<em>Some of the budget is …</em>。這是第 7 章和第 13 章的內容；這一章處理的是 <em>report on …</em>、<em>list of …</em> 這種前面的名詞才是重點的情況。
```
- Replace `sections[6].takeaway` with: (now: `介系詞後面的名詞不會是主詞；劃掉介系詞那一串，剩下的才是。`)
```
介系詞後面的名詞通常不是主詞；劃掉介系詞那一串，剩下的才是。<em>a number of</em>、<em>some of</em> 這類數量片語例外，第 7 章會講。
```

### 02-S2 [shouldFix] 中心名詞 is used before it is defined
- Where: `check[2].q`, new paragraph after `sections[5].body[1]`, `sections[6].body[0]`
- Problem: 中心名詞 appears in `check[2].q` and in `sections[5].quiz[0].q` but is defined only in `sections[6].body[0]` (STYLE §5 item 4: no term before it is explained). The check item needs no term. For the section quiz, define the word where the 'remove the accessories' method first leaves a core word, and let `sections[6].body[0]` point back.
- Replace `check[2].q` with: (now: `點出主詞的中心名詞（一個字）。`)
```
點出主詞（只點最核心的那一個字）。
```
- Insert after `sections[5].body[1]` (it becomes `sections[5].body[2]`; later items shift down by one):
```
修飾語拿掉之後，主詞和受詞各會剩下一個核心的字，叫<b>中心名詞</b>：<em>manager</em> 是主詞的中心名詞，<em>budget</em> 是受詞的中心名詞。下面用拿掉修飾語的方法把它們找出來。
```
- Replace `sections[6].body[0]` with: (now: `主詞常常不是一個字，而是一長串：<em>The report on the new branches</em>。這一串裡，只有一個字是核心：拿掉其他字它還在，句子講的就是它。這個字叫<b>中心名詞</b>。`)
```
主詞常常不是一個字，而是一長串：<em>The report on the new branches</em>。這一串裡，只有一個字是核心：拿掉其他字它還在，句子講的就是它。這個字就是第 6 節說的<b>中心名詞</b>。
```

### 02-S3 [shouldFix] 'One finite verb per clause' contradicts its own first fix
- Where: `sections[2].body[0]`, `sections[2].quiz[0].why`
- Problem: The title and takeaway say a clause holds one finite verb, and the first fix is *and*, which puts two finite verbs in one stretch. The quiz `why` makes the clash explicit ('同一個子句要放兩個，中間要有 and'). Chapter 3 `sections[4].body[0]` then needs an 'exception' sentence to repair it. The accurate statement is: two finite verbs need something joining them, and with *and* the second verb shares the first one's subject.
- Replace `sections[2].body[0]` with: (now: `反過來也成立：一個子句裡，只放<b>一個</b>有時態的動詞。`)
```
反過來也成立：一個子句裡，只放<b>一個</b>有時態的動詞。要放第二個，中間一定要有東西把它接進來。
```
- Replace `sections[2].quiz[0].why` with: (now: `<em>picked up</em> 和 <em>delivered</em> 都是有時態的動詞。同一個子句要放兩個，中間要有 <em>and</em> 接起來。`)
```
<em>picked up</em> 和 <em>delivered</em> 都是有時態的動詞。兩個有時態的動詞之間，一定要有東西接起來：這裡用 <em>and</em>，兩個動詞共用主詞 <em>The courier</em>。
```

### 02-S4 [shouldFix] Definition of 有時態的動詞: '跟著主詞走', the Workbook's 主要動詞, and the direction of the time-change test
- Where: `sections[1].body[0]`, `sections[1].body[3]`
- Problem: (a) '而且跟著主詞走' is not true of most finite verbs: *approved, will approve, must approve* do not change with the subject. Agreement is chapter 7. (b) 'The Workbook 說的「主要動詞」，指的就是它' is imprecise. In the Workbook 主要動詞 is the finite verb of the main clause, so in *The consultant who visited us has sent …* both *visited* and *has sent* are finite, but only *has sent* is the 主要動詞 (chapter 3 makes this distinction). (c) The test says 'change the sentence to 昨天 or 明天' but a past sentence cannot be changed to yesterday; say 'change to the other time'. *must* has no other time form, so the test cannot be run on it.
- Replace `sections[1].body[0]` with: (now: `動詞有好幾種樣子，但不是每一種都撐得起一個句子。撐得起句子的，是<b>有時態的動詞</b>：它標出時間（現在、過去、未來），而且跟著主詞走。The Workbook 說的「主要動詞」，指的就是它。`)
```
動詞有好幾種樣子，但不是每一種都撐得起一個句子。撐得起句子的，是<b>有時態的動詞</b>：它標出時間（現在、過去、未來）。有些有時態的動詞還會跟著主詞變，例如 <em>approves</em>，第 7 章再講。The Workbook 說的「主要動詞」，指的是主要子句裡那個有時態的動詞（主要子句見第 3 章）。
```
- In `sections[1].body[3]`: `把句子改成「昨天」或「明天」。` → `把句子換成另一個時間：現在的句子改成「昨天」，過去的句子改成「明天」。`
- In `sections[1].body[3]`, change:
```
所以這句有時態的動詞是 <em>wants</em>。
→
所以這句有時態的動詞是 <em>wants</em>。<em>must</em> 沒有別的時間形狀，直接當作和後面原形合成一組的助動詞。
```

### 02-S5 [shouldFix] Linking-verb list is short; the note on 'started late' does not name the part of speech
- Where: `sections[4].body[1]`, `sections[0].ex[1].note`
- Problem: `body[1]` stops at *look* and *sound*. *feel*, *get* (*get better*) and *prove* (*prove useful*) behave the same way and appear in business writing. `sections[0].ex[1].note` calls *late* a 配件 without naming it, and chapter 1 taught *late* as an adjective; say 'adverb' and point back (works together with 01-S1).
- Replace `sections[4].body[1]` with:
```
會帶補語的動詞不多：<em>be</em>（<em>is</em>、<em>are</em>、<em>was</em>、<em>were</em>）、<em>become</em>、<em>remain</em>、<em>stay</em>、<em>seem</em>、<em>appear</em>、<em>prove</em>，還有當「看起來」的 <em>look</em>、當「聽起來」的 <em>sound</em>、當「感覺起來」的 <em>feel</em>，以及當「變得」的 <em>get</em>（<em>get better</em>）。它們叫<b>連綴動詞</b>：把主詞和描述連起來。
```
- Replace `sections[0].ex[1].note` with: (now: `<em>late</em> 是配件，拿掉後 <em>The meeting started.</em> 仍然完整。`)
```
<em>late</em> 在這裡是副詞，說明 <em>started</em> 怎麼開始（有些字的形容詞和副詞長得一樣，第 1 章）。拿掉後 <em>The meeting started.</em> 仍然完整。
```

### 02-S6 [shouldFix] Two over-generalisations in the 受詞 section
- Where: `sections[3].body[3]`, `sections[3].body[4]`
- Problem: `body[3]` 'verbs that take an object do not take a preposition' will be over-applied: *reply to, depend on, apply for, wait for* are verb + preposition and need it. `body[4]` 'only verbs followed by an object can become passive' ignores prepositional passives (*be dealt with, be looked into*); 'mainly' is accurate and costs nothing.
- In `sections[3].body[3]`, change:
```
中間沒有 <em>with</em>、<em>about</em>。
→
中間沒有 <em>with</em>、<em>about</em>。另有一批動詞本身就要介系詞，要一個一個認：<em>reply to</em>、<em>depend on</em>、<em>apply for</em>、<em>wait for</em>。
```
- Replace `sections[3].body[4]` with: (now: `動詞有沒有受詞，第 5 章會用到：只有後面接受詞的動詞，才能改成被動。`)
```
動詞有沒有受詞，第 5 章會用到：能改成被動的，主要是後面接受詞的動詞。
```

### 02-S7 [shouldFix] Missing: the empty subject it, and verbs with two objects
- Where: new paragraph after `sections[0].body[2]`, new paragraph after `sections[3].body[1]`
- Problem: (a) `sections[0].body[2]` says English cannot drop the subject (unlike Chinese) but gives no way out for 下雨了 / 三點了; the learner needs *It rained all day.* / *It is 3 p.m.* (chapter 11 treats pronouns, so one sentence is enough here). (b) The 受詞 section shows one object per verb. *send us a quote, give the client a call, offer them a discount* have two, and chapter 5 (passive) needs the learner to know that.
- Insert after `sections[0].body[2]` (it becomes `sections[0].body[3]`; later items shift down by one):
```
沒有東西可以當主詞的時候，英文放一個沒有意思的 <em>it</em>：<em>It rained all day.</em>、<em>It is 3 p.m.</em>。中文說「下雨了」「三點了」，英文不能只說 <em>Rained all day.</em>。
```
- Insert after `sections[3].body[1]` (it becomes `sections[3].body[2]`; later items shift down by one):
```
有些動詞可以接兩個受詞：先「給誰」，再「給什麼」。<em>The firm sent us a quote.</em> 裡，<em>us</em> 和 <em>a quote</em> 都是受詞：寄給誰？<em>us</em>。寄了什麼？<em>a quote</em>。
```

### 02-S8 [shouldFix, small] Tap check: cost looks like a verb
- Where: `check[0].why`
- Problem: In *The cost of the repairs to the elevators surprised everyone.* both *cost* and *repairs* can be verbs in other sentences, and the `why` does not say why they are not here. The method the chapter teaches (a noun follows *The*) should be visible.
- Replace `check[0].why` with:
```
<em>surprised</em> 是唯一會隨時間變的動詞（改成現在就是 <em>surprises</em>）。<em>cost</em> 前面有 <em>The</em>，是名詞；<em>of the repairs to the elevators</em> 是介系詞帶頭的配件，裡面沒有動詞。
```

### 02-S9 [shouldFix] Chinese: name style, 主任, 雇, 開幕, 你/您, 動手腳
- Where: `lead`, `check[3].why`, `sections[0].ex[2].zh`, `sections[1].ex[2].zh`, `sections[3].ex[0].zh`, `sections[4].body[3]`, `sections[4].ex[1].zh`, `sections[4].ex[2].zh`, `sections[4].ex[2].note`, `sections[4].ex[3].zh`
- Problem: (1) Names: this chapter writes 太田先生 and 朴女士, while chapters 1, 3 and 4 keep Latin names (Ruiz 女士, Novak 先生) and chapter 4 uses 林先生 and 韓女士. Pick one convention for the whole book; Latin names keep the English spelling visible next to the sentence and avoid guessing a Chinese reading (*Han* could be 韓 or 한). The replacements below use Latin names; chapter 4 has matching entries (04-S7). (2) *director* → 主任 is a small-unit title in Taiwan business usage; use 總監. (3) 雇 is the mainland standard form; Taiwan usage (and 勞動基準法) writes 僱. (4) 開幕 is for a shop or an event; an office 啟用. (5) 你的申請 / 你摘要: chapters 1 and 4 use 您 in business sentences; make the example lines consistent. (6) 動手腳 means 'tamper with' in Taiwan Mandarin; the lead means 'make changes on'.
- In `lead`: `動手腳` → `做變化`
- In `check[3].why`: `朴女士` → `Park 女士`
- In `sections[0].ex[2].zh`: `開幕` → `啟用`
- In `sections[1].ex[2].zh`: `你的申請` → `您的申請`
- In `sections[3].ex[0].zh`: `太田先生` → `Ota 先生`
- In `sections[4].body[3]` (2 occurrences): `朴女士` → `Park 女士`
- In `sections[4].body[3]` (3 occurrences): `主任` → `總監`
- In `sections[4].ex[1].zh`: `朴女士` → `Park 女士`
- In `sections[4].ex[1].zh`: `主任` → `總監`
- In `sections[4].ex[2].zh`: `朴女士` → `Park 女士`
- In `sections[4].ex[2].zh`: `雇` → `僱`
- In `sections[4].ex[2].note`: `朴女士` → `Park 女士`
- In `sections[4].ex[3].zh`: `你摘要` → `您摘要`

### Verdict, chapter 2
Chapter 2 is the best built of the four. The finite-verb test (change the time and see what moves), the 'is the subject equal to what follows?' test that separates object from complement, and the three-step search for the head noun are concrete and checkable, and every tap item has exactly one answer. It is not release-ready because one rule is stated as a universal and is false: prepositional phrases are not always removable (*belong to Mr. Becker*, *is on the shared drive*), and the chapter's own `check[2]` and `sections[6].ex[1]` are counter-examples (02-M1); a reader who follows the method will 'find' skeletons that are not sentences. The statement that a noun after a preposition is never the subject also needs a one-paragraph pointer to *a number of / some of / most of* before chapter 7 reverses it (02-S1), 中心名詞 is used in a check item and a section quiz before it is defined (02-S2), and the 'one finite verb per clause' wording contradicts its own first fix (02-S3). The remaining items tidy the definition of 有時態的動詞 and the Workbook's 主要動詞, add the empty subject *it* and two objects, and fix Chinese consistency (Latin names, 總監, 僱, 啟用).

---

## 03-clause.json

### 03-M1 [mustFix] 'The main clause's subject is the noun in front of the bracket' is false when that noun follows a preposition
- Where: `sections[6].body` (whole list), `sections[6].ex[0]`, `sections[6].ex[2]`, `sections[6].takeaway`
- Problem: `body[3]` says the subject of the main clause is the noun in front of the bracket. For *The report on the branches [that opened last year] is late.* the noun in front of the bracket is *branches*; the subject is *report*. This is exactly the trap chapter 2 trains the reader to avoid, and chapter 7 builds on it. The paragraph also never says where the bracket ends, which the tap quiz and `check[4]` need. The replacement block below fixes this and, in the same pass, makes four smaller changes: (a) *who / which / that* can be the subject of their own clause (*who called this morning*: 誰打電話？ *who*), which the section's own definition of 子句 needs (chapter 9 `sections[0]` teaches it in full); (b) the that-clause-as-object paragraph (`body[5]`, `ex[2]`) moves out, because it is a second idea in a section titled 'preview of chapter 9' (see 03-S5; chapter 16 points here for 'that 子句 (第 3 章)', so the content must stay in this chapter); (c) *hired a supplier* → *chose* (*hire* is for people; the original is understandable but not idiomatic); (d) '書信和口語裡' is dropped: omitting *that* is common in formal writing too, so the register claim is unsupported.
- Replace `sections[6].body` with:
```
[
  "子句不一定掛在句子的前面或後面，也可以<b>夾在句子裡面</b>，描述一個名詞。",
  "<em>The supplier raised its prices.</em> 是一句話。想說是哪一家供應商，可以把一個子句塞在 <em>supplier</em> 後面：<em>The supplier <b>that we chose last spring</b> raised its prices.</em>。<em>that we chose last spring</em> 有主詞 <em>we</em>、有動詞 <em>chose</em>，是子句；它不能單獨成句，是從屬子句。",
  "這時一句話裡有兩個有時態的動詞：<em>chose</em> 屬於裡面的子句，<em>raised</em> 屬於主要子句。把它們接起來的字是 <em>that</em>，就是第 5 節說的「每多一個子句，多一個連接的字」。這種跟在名詞後面、用 <em>who</em>、<em>which</em>、<em>that</em> 帶頭、描述名詞的子句，叫<b>關係子句</b>，第 9 章完整講。",
  "帶頭的字有時自己就是子句的主詞。<em>The client who called this morning wants a full refund.</em> 裡，<em>who called this morning</em> 問「誰打電話？」，答案就是 <em>who</em>。<em>who</em>、<em>which</em>、<em>that</em> 後面直接接動詞的時候，都是這樣。",
  "讀長句的方法：看到 <em>who</em>、<em>which</em>、<em>that</em> 緊跟在名詞後面，先把它帶出的子句括起來，括號外面剩下的就是主要子句。括號到哪裡結束？括號裡的子句有自己的動詞（<em>called</em>），再往後出現的下一個有時態的動詞（<em>wants</em>），就是主要子句的動詞，括號在它前面結束。主詞通常是括號前面那個名詞；但如果那個名詞在介系詞後面，主詞還是第 2 章找到的中心名詞：<em>The report on the branches [that opened last year] is late.</em> 裡，括號前面是 <em>branches</em>，主詞卻是 <em>report</em>。",
  "這個 <em>that</em> 常常被省略：<em>The supplier we chose last spring raised its prices.</em>。連接的字看不見了，但子句還在：<em>we chose</em> 仍然是主詞＋有時態的動詞。什麼時候可以省，第 9 章再講。"
]
```
- Replace `sections[6].ex[0]` with:
```
{
  "en": "The supplier <u>that we chose last spring</u> raised its prices.",
  "zh": "我們去年春天選定的那家供應商漲價了。",
  "note": "括起底線部分，剩下 <em>The supplier raised its prices.</em>"
}
```
- Delete `sections[6].ex[2]`.
- Replace `sections[6].takeaway` with: (now: `名詞後面的 who、which、that 帶出一個子句；把它括起來，剩下的就是主要子句。`)
```
名詞後面的 <em>who</em>、<em>which</em>、<em>that</em> 帶出一個子句；把它括起來，剩下的就是主要子句。
```

### 03-S1 [shouldFix, high] and / but / or / so clauses are never classified, and the 'cover the introducing word' method fails on them
- Where: new paragraph after `sections[3].body[4]`
- Problem: `sections[3]` says clauses come in two kinds and gives a method for finding the main clause: cover the introducing word and the clause it introduces. `sections[4]` then lists *and, but, so* together with *because, although, when, if, who* as 'connecting words'. For *The truck was late, so the meeting started …* the learner cannot tell which clause is main, and the cover-it method returns only one of the two. Both clauses are main clauses (each stands as a sentence without *so*). Chapter 8 and chapter 14 depend on this distinction.
- Insert after `sections[3].body[4]` (it becomes `sections[3].body[5]`; later items shift down by one):
```
<em>and</em>、<em>but</em>、<em>or</em>、<em>so</em> 接起來的兩個子句，是兩個<b>主要子句</b>：<em>The truck was late, so the meeting started without the samples.</em> 拿掉 <em>so</em>，兩邊各自還是完整的一句話。這和 <em>because</em>、<em>although</em> 不一樣：<em>because the truck was late</em> 沒有主要子句就站不住。所以「把帶頭的字和它帶出的子句蓋住」這個方法，只用在從屬子句（<em>because</em>、<em>although</em>、<em>when</em>、<em>if</em>、<em>who</em>）。
```

### 03-S2 [shouldFix, high] Past-participle phrases are left out of the 'looks like a verb but is not' section
- Where: `sections[2].h`, `sections[2].body[4]`, `sections[2].ex`, `sections[2].takeaway`
- Problem: The section is 'the threshold of the chapter' and teaches that Ving and to V do not make a clause. A past participle looks like a finite verb after a noun just as much: in *the contract signed by both parties*, *the contract signed* looks like subject + past-tense verb. Chapter 2 `sections[1].body[2]` already warns that '-ed 的樣子有時也不算', but this chapter's test ('只找到 Ving 或 to V，就是片語') and takeaway do not cover it, so a reader applying the test will call *signed by both parties* a clause. Chapter 6 teaches the participle in full; here the reader only needs to know it does not count.
- Replace `sections[2].h` with: (now: `Ving 和 to V 不算：最容易看錯的地方`)
```
Ving、to V 和過去分詞不算：最容易看錯的地方
```
- Replace `sections[2].body[4]` with: (now: `檢查的方法：在那組字裡找有時態的動詞。只找到 Ving 或 to V，就是片語。`)
```
檢查的方法：在那組字裡找有時態的動詞。只找到 Ving、to V，或過去分詞（-ed 的樣子，例如 <em>the contract signed by both parties</em> 裡的 <em>signed</em>，第 6 章會講），就是片語。
```
- Append to `sections[2].ex`:
```
{
  "en": "The contract <u>signed by both parties</u> is in the folder.",
  "zh": "雙方簽署的合約放在資料夾裡。",
  "note": "<em>signed</em> 是過去分詞，不是有時態的動詞：這組字是片語。這句有時態的動詞是 <em>is</em>。"
}
```
- Replace `sections[2].takeaway` with: (now: `Ving 和 to V 看起來像動作，但不是有時態的動詞；只有它們的一組字是片語。`)
```
一組字裡如果只有 Ving、to V 或過去分詞，沒有有時態的動詞，就是片語。
```

### 03-S3 [shouldFix] 'Nothing or a comma between two clauses is wrong' leaves out the semicolon
- Where: `sections[4].body[1]`
- Problem: The rule 'every extra clause needs a connecting word' is the chapter's key rule. Two main clauses can also be joined by a semicolon, which the chapter itself uses in `body[5]` for *however / therefore* ('前面要用句號或分號'). Say so once so that the rule and the later sentence agree.
- In `sections[4].body[1]`, change:
```
（只有 <em>that</em> 這類字在某些位置可以省略，這一章最後一節和第 9 章會提到。）
→
（兩個主要子句之間也可以用分號，第 8 章會用到。<em>that</em> 這類字在某些位置可以省略，這一章後面和第 9 章會提到。）
```

### 03-S4 [shouldFix] '句子其實就是子句' and '誰簽的？沒說'
- Where: `sections[1].body[1]`, `sections[2].body[1]`, `check[2].why`
- Problem: (a) '第 2 章講的「句子」，其實就是子句' is followed by 'a sentence can have several clauses'; the two sentences contradict each other. (b) '這組字裡也沒有主詞，誰簽的？沒說' is not true as a reading of *After signing the contract, Mr. Novak called his team*: the doer is stated, in the main clause. What is true is that the group of words has no subject of its own.
- Replace `sections[1].body[1]` with:
```
第 2 章講的只有一個子句的句子，就是一個子句。一句話可以只有一個子句（<em>The truck was late.</em>），也可以有好幾個（<em>The truck was late, so the meeting started without the samples.</em>）。
```
- In `sections[2].body[1]`: `這組字裡也沒有主詞，誰簽的？沒說。` → `這組字裡也沒有自己的主詞：簽的人沒寫在這組字裡，要回頭看主要子句才知道。`
- Replace `check[2].why` with: (now: `<em>signing</em> 是 Ving，不是有時態的動詞，而且這組字裡沒有主詞（誰簽的？沒說）。所以是片語。`)
```
<em>signing</em> 是 Ving，不是有時態的動詞，而且這組字裡沒有自己的主詞（簽的人要回頭看主要子句才知道）。所以是片語。
```

### 03-S5 [shouldFix] Give the that-clause-as-object its own section
- Where: new `sections[7]` (appended; the chapter then has 8 sections and 9 quizzes, within STYLE §4 limits)
- Problem: `sections[6]` is titled 'preview of chapter 9' but its last paragraph and `ex[2]` teach a different idea (a clause filling the object slot). STYLE §1: one idea per section. Chapter 16's lead refers to 'that 子句（第 3 章）', and chapter 4 uses *We expect that the parts will arrive*, so the content must remain in chapter 3; it needs a home of its own, with a quiz. (Text in 03-M1 already removes it from `sections[6]`.)
- Append to `sections`:
```
{
  "h": "子句也可以當受詞：that 子句",
  "body": [
    "有些動詞後面接的對象，不是一個名詞，而是一整句話。<em>Ms. Moreau confirmed that the order shipped on Monday.</em>：確認了什麼？確認了 <em>that</em> 後面那一整個子句。它站在受詞的位置（第 2 章），所以整個 <em>that</em> 子句就是 <em>confirmed</em> 的受詞。",
    "這句有兩個有時態的動詞：<em>confirmed</em> 屬於主要子句，<em>shipped</em> 屬於 <em>that</em> 子句，把它們接起來的就是 <em>that</em>（第 5 節的規則）。這個 <em>that</em> 沒有「那個」的意思，只是連接的字。它和前一節的關係子句不同：關係子句描述前面的名詞，<em>that</em> 子句本身就是動詞要的那個對象。第 4 章的 <em>We expect that the parts will arrive</em> 和第 16 章的「that 子句」，都是這一種。"
  ],
  "ex": [
    {
      "en": "Ms. Moreau confirmed <u>that the order shipped on Monday</u>.",
      "zh": "Moreau 女士確認訂單已在週一出貨。",
      "note": "整個 <em>that</em> 子句是 <em>confirmed</em> 的受詞。"
    },
    {
      "en": "The auditors reported <u>that the records were complete</u>.",
      "zh": "稽核人員回報，紀錄都很完整。",
      "note": "<em>reported</em> 屬於主要子句；<em>were</em> 屬於 <em>that</em> 子句。"
    }
  ],
  "quiz": [
    {
      "type": "choose",
      "q": "<em>The manager said that the shipment left on Friday.</em> 這句有幾個子句？",
      "options": [
        "一個",
        "兩個",
        "三個"
      ],
      "answer": 1,
      "why": "有兩個有時態的動詞（<em>said</em>、<em>left</em>），就是兩個子句：主要子句 <em>The manager said</em>，加上 <em>that</em> 帶出的 <em>that the shipment left on Friday</em>。"
    }
  ],
  "takeaway": "<em>that</em> 帶出的子句可以整個當動詞的受詞；有幾個有時態的動詞，就有幾個子句。"
}
```

### 03-S6 [shouldFix] The opening check ends on a chapter-9 preview and never tests counting clauses
- Where: `check[4]`
- Problem: `check[4]` (main-clause verb with a relative clause in the middle) belongs to the last section, which is a preview of chapter 9. The check is supposed to test the chapter's thresholds; the count-the-verbs / one-connecting-word rule (`sections[4]`) is the idea chapters 8 and 9 rest on and is absent from it. The tap item stays as the quiz of `sections[6]`, so nothing is lost.
- Replace `check[4]` with:
```
{
  "type": "choose",
  "q": "哪一句是對的？",
  "options": [
    "The shipment was late, the store opened on time.",
    "The shipment was late, but the store opened on time."
  ],
  "answer": 1,
  "why": "有兩個有時態的動詞（<em>was</em>、<em>opened</em>），就是兩個子句，中間要有一個連接的字。只有逗號接不起來；加上 <em>but</em> 才行。"
}
```

### 03-S7 [shouldFix, small] Chinese and English polish: 雇, 才到, 'keep your phone on silent'
- Where: `sections[0].ex[1].zh`, `sections[0].ex[2].zh`, `sections[5].ex[0].zh`, `sections[5].ex[1].zh`, `sections[5].ex[2].en`, `sections[5].ex[3].en`
- Problem: (1) 樣品下午才到 adds 'late', which *arrived in the afternoon* does not say. (2) 雇 → 僱 (Taiwan standard; see 02-S9). (3) *keep your phone on silent* is British-leaning; *silence your phone* is neutral and keeps the *during* + noun / *while* + clause contrast intact.
- Replace `sections[0].ex[1].zh` with: (now: `樣品下午才到。`)
```
樣品是下午到的。
```
- In `sections[0].ex[2].zh`: `雇` → `僱`
- In `sections[5].ex[0].zh`: `雇` → `僱`
- In `sections[5].ex[1].zh`: `雇` → `僱`
- Replace `sections[5].ex[2].en` with: (now: `Please keep your phone on silent <u>during</u> the presentation.`)
```
Please silence your phone <u>during</u> the presentation.
```
- Replace `sections[5].ex[3].en` with: (now: `Please keep your phone on silent <u>while</u> Ms. Bauer is presenting.`)
```
Please silence your phone <u>while</u> Ms. Bauer is presenting.
```

### Verdict, chapter 3
Chapter 3 teaches its threshold, that Ving and to V do not make a clause, slowly and correctly, and the phrase/clause pairs, the count-the-finite-verbs rule and the *despite / although*, *during / while* contrasts are accurate and well chosen. One statement is wrong: 'the main clause's subject is the noun in front of the bracket' fails when that noun follows a preposition (*The report on the branches [that opened last year] is late*), which is the trap chapter 2 trains against and chapter 7 builds on (03-M1; the rewritten block also fixes where the bracket ends and that *who / which / that* can be the clause's own subject). The rest are additions rather than corrections: *and / but / or / so* clauses are never classified and the cover-it method fails on them (03-S1), past-participle phrases are missing from the 'looks like a verb but is not' section (03-S2), the semicolon is missing from the one-connecting-word rule (03-S3), and the that-clause-as-object paragraph needs its own section, which must stay in this chapter because chapter 16 points here (03-S5). The opening check ends with a chapter-9 preview item instead of testing clause counting (03-S6).

---

## 04-tense.json

### 04-M1 [mustFix] 'when / if clauses take the present for the future' is false for when / if / whether noun clauses
- Where: `sections[7].body[2]`, new paragraph after `sections[7].body[4]`, `sections[7].ex`, `sections[7].takeaway`
- Problem: `body[2]` ('看它是不是 when、once、if 這類帶頭的。是，裡面就不用 will') and the takeaway ('when、once、as soon as、until、if 帶頭的子句，未來的事用現在式') cover every clause that starts with *when* or *if*. But *when* ('what time') and *if* ('whether') also start noun clauses after *know, ask, tell, wonder, find out, check*; there *will* stays: *Please tell us when the order will arrive.*, *We need to know if the vendor will deliver on time.* A reader who applies the rule as written will 'correct' these to the present tense. Chapter 4 already handles the *that* case in `body[4]`; this is the parallel case for *when / if*, and the Workbook's own lessons carry the same limit. Chapters 8 and 10 repeat the rule and should carry the same caveat.
- In `sections[7].body[2]`, change:
```
看它是不是 <em>when</em>、<em>once</em>、<em>if</em> 這類帶頭的。
→
看它是不是 <em>when</em>、<em>once</em>、<em>if</em> 這類帶頭的，而且是在交代時間或條件。
```
- Insert after `sections[7].body[4]` (it becomes `sections[7].body[5]`; later items shift down by one):
```
<em>when</em> 和 <em>if</em> 還有另一種用法：當「什麼時候」「是不是」，放在 <em>know</em>、<em>ask</em>、<em>tell</em>、<em>wonder</em>、<em>find out</em>、<em>check</em> 這類動詞後面，整個子句是動詞的受詞（第 3 章）。這種子句不是在交代時間或條件，未來照樣用 <em>will</em>：<em>Please tell us when the order will arrive.</em>、<em>We need to know if the vendor will deliver on time.</em> 分辨的方法：把 <em>when</em> 換成「在……的時候」、<em>if</em> 換成「如果」，句子還通，就是時間或條件子句，不用 <em>will</em>；要換成「什麼時候」「是不是」才通，就用 <em>will</em>。
```
- Append to `sections[7].ex`:
```
{
  "en": "Please let us know when the shipment <u>will arrive</u>.",
  "zh": "請告訴我們貨什麼時候會到。",
  "note": "<em>when</em> 是「什麼時候」，整個子句是 <em>let us know</em> 的受詞，不是時間子句，未來照用 <em>will</em>。"
}
```
- Replace `sections[7].takeaway` with: (now: `when、once、as soon as、until、if 帶頭的子句，未來的事用現在式；will 只放在主要子句。`)
```
<em>when</em>、<em>once</em>、<em>as soon as</em>、<em>until</em>、<em>if</em> 帶頭、交代時間或條件的子句，未來的事用現在式；<em>will</em> 只放在主要子句。
```

### 04-M2 [mustFix] The future-perfect takeaway reverses the body: 'by + future deadline' does not require will have + p.p.
- Where: `sections[6].takeaway`, new paragraph after `sections[6].body[2]`
- Problem: `body[1]` says the future perfect 'almost always' carries a future deadline, which is right. The takeaway reverses it: 'by＋未來的期限，用 will have＋p.p.'. But *We will ship the orders by Friday.* and *The parts will arrive by Monday.* are ordinary, and *Please submit the form by Friday.* takes the imperative. The takeaway is the one sentence the reader keeps, so a wrong takeaway is worse than a wrong body paragraph. The summary table row `sections[8].table.rows[6]` is under a 通常用 header and is acceptable once this paragraph exists.
- Insert after `sections[6].body[2]` (it becomes `sections[6].body[3]`; later items shift down by one):
```
有 <em>by</em>＋期限，不一定要用未來完成式。<em>We will ship the orders by Friday.</em> 只說「最晚週五出貨」；<em>We will have shipped the orders by Friday.</em> 把重點放在「到週五時已經出完了」。兩句都對。
```
- Replace `sections[6].takeaway` with: (now: `by＋未來的期限，用 will have＋p.p.：到那時已經做完。`)
```
未來完成式幾乎總帶著一個未來的期限；有 <em>by Friday</em> 不一定非用它，只說「最晚週五做」時，<em>will</em>＋原形也行。
```

### 04-S1 [shouldFix, high] Past progressive appears in the table and is relied on by chapter 5, but is never explained
- Where: `sections[2].h`, new paragraph after `sections[2].body[3]`, `sections[2].ex`
- Problem: `sections[0].table` lists *was approving*, and chapter 5 `sections[1].body[1]` says '變成過去進行式（第 4 章）' as if chapter 4 had taught it. Chapter 4 never shows what it is for. The *when / while* pairing (a long action in progress, interrupted by a short one) is the part a business reader meets. The chapter is at the 9-section maximum, so the paragraph goes at the end of the past-tense section and the heading widens.
- Replace `sections[2].h` with: (now: `過去式：已經結束的時間`)
```
過去式，和過去進行式
```
- Insert after `sections[2].body[3]` (it becomes `sections[2].body[4]`; later items shift down by one):
```
過去式有一個伴：過去進行式（<em>was</em>／<em>were</em>＋Ving），說過去某一刻事情正在進行。常和一個短的過去動作放在一起：<em>The phone rang while we were reviewing the contract.</em> 審合約是進行中的長動作，用 <em>were reviewing</em>；電話響是打斷它的短動作，用過去式 <em>rang</em>。
```
- Append to `sections[2].ex`:
```
{
  "en": "The phone rang while we <u>were reviewing</u> the contract.",
  "zh": "我們正在審合約時，電話響了。",
  "note": "過去進行式：過去那一刻還在進行。"
}
```

### 04-S2 [shouldFix, high] Past perfect: the reported-speech use is missing
- Where: new paragraph after `sections[5].body[3]`, `sections[5].ex`
- Problem: `sections[5].body[2]` says the past perfect needs a past reference point and lists other past actions, *by the time*, and *by last Friday*. A very common real use is after a past verb of saying or learning (*said / told / learned / found that … had …*): *The client said that she had already paid the deposit.* A reader who has only this chapter will write *said that she already paid* and be unable to say why a native speaker prefers the other.
- Insert after `sections[5].body[3]` (it becomes `sections[5].body[4]`; later items shift down by one):
```
還有一個很常見的用法：說話或得知的動詞是過去式，後面 <em>that</em> 子句講更早的事，就用 <em>had</em>＋p.p.：<em>The client said that she had already paid the deposit.</em>（客戶說她已經付過訂金了）。<em>said</em> 就是那個過去的參考點，付款發生在更早。
```
- Append to `sections[5].ex`:
```
{
  "en": "The client said that she <u>had</u> already <u>paid</u> the deposit.",
  "zh": "客戶說她已經付過訂金了。",
  "note": "<em>said</em> 是過去的參考點；付款更早：<em>had paid</em>。"
}
```

### 04-S3 [shouldFix] Lead promises six tenses, the body teaches seven; 'nine in all' ignores the perfect progressive; unsupported frequency claims
- Where: `lead`, `sections[0].body[0]`, `sections[0].body[3]`
- Problem: `lead` says the chapter explains six tenses; `sections[0].body[3]` says '這一章就講這七種' (six bold plus the present progressive), and the chapter also teaches *be going to* and the present for the future. `body[0]` says 3 × 3 = 'a total of nine', but the chapter itself then mentions *have been waiting* (perfect progressive), which the usual tables count, giving twelve. '商業英文天天用到' (lead) and '商業書信和會議裡用得最多的' (`body[3]`) are frequency claims with no source; STYLE §1 asks for none about the test and the same spirit applies.
- Replace `lead` with:
```
中文說「核准了」「正在核准」「已經核准」，靠的是多加一個字；英文把時間和樣子都做進動詞的形狀裡：<em>approved</em>、<em>is approving</em>、<em>has approved</em>。這一章先給你整張時態表，再把最基本的七種講清楚：現在式、現在進行式、過去式、現在完成式、未來式、過去完成式、未來完成式。第 5 章的被動語態，就是把這一章的每一種時態，再套上一層 <em>be</em>＋p.p.。
```
- Replace `sections[0].body[0]` with: (now: `英文的時態由兩個部分組成。<b>時間</b>：過去、現在、未來。<b>樣子</b>：簡單、進行、完成。三乘三，一共九種。簡單的那一列通常直接叫現在式、過去式、未來式，這本書也這樣叫。`)
```
英文的時態由兩個部分組成。<b>時間</b>：過去、現在、未來。<b>樣子</b>：簡單、進行、完成。三乘三，得到九種。（完成和進行還可以合在一起，例如 <em>have been waiting</em>，所以常見的教材會列到十二種；這一章只看九種裡的七種。）簡單的那一列通常直接叫現在式、過去式、未來式，這本書也這樣叫。
```
- Replace `sections[0].body[3]` with:
```
九種不用一次學會。這一章先講表中粗體的六種，再加上現在進行式，共七種；其他的先認得形狀就好。完成和進行合在一起的樣子（<em>have been waiting</em>），表示一直持續到某個時間點，第 4 節會順帶提到。
```

### 04-S4 [shouldFix] Time-word pairings stated without 'usually'; now / currently also go with state verbs
- Where: `sections[1].body[2]`, `sections[1].body[3]`
- Problem: 'every day … 搭現在式. now、currently、at the moment、this week 搭現在進行式' is stated as fact, while `sections[8].body[1]` says the pairings are 'typical, not absolute'. *now* and *currently* also go with the simple present for state verbs (*We currently have 40 employees. We now offer next-day delivery.*), which is ordinary company-announcement English. The stative paragraph that follows is the right place to say so.
- In `sections[1].body[2]`: `<em>each month</em> 搭現在式。` → `<em>each month</em> 通常搭現在式。`
- In `sections[1].body[2]`: `<em>this week</em> 搭現在進行式。` → `<em>this week</em> 搭動作動詞時，通常用現在進行式。`
- In `sections[1].body[3]`: `<em>own</em>、<em>contain</em>。` → `<em>own</em>、<em>contain</em>、<em>have</em>（擁有）。`
- In `sections[1].body[3]`, change:
```
不說 <em>We are needing more chairs.</em>
→
不說 <em>We are needing more chairs.</em>。這類動詞就算前面有 <em>now</em>、<em>currently</em>，也用現在式：<em>We currently have 40 employees.</em>
```

### 04-S5 [shouldFix] 'by the time + past → had + p.p.' is stated without 'usually'
- Where: `sections[6].body[3]`, `sections[6].table.head[1]`
- Problem: *By the time we arrived, the shop was closed.* is ordinary English with a state in the main clause; the paragraph and the table header say the main clause 'uses' *had* + p.p. for *by the time* + past, and *will have* + p.p. for *by the time* + present. The Workbook's lessons already carry 'usually' for exactly this pairing. The same applies to the future version (*By the time the auditors arrive, we will be ready*).
- Replace `sections[6].body[3]` with:
```
<em>by the time</em> 有兩種搭法，看它後面的子句是現在式還是過去式。<em>by the time</em>＋現在式（講未來），主要子句通常用 <em>will have</em>＋p.p.。<em>by the time</em>＋過去式，主要子句通常用 <em>had</em>＋p.p.；主要子句是狀態時，用過去式也很自然：<em>By the time we arrived, the shop was closed.</em>
```
- Replace `sections[6].table.head` with:
```
[
  "by the time 後面",
  "主要子句（通常）",
  "例子"
]
```

### 04-S6 [shouldFix, small] '否定和問句用 did' does not apply to be
- Where: `sections[2].body[3]`
- Problem: The rule is stated for all verbs; with *be* the negative is *was not*, never *did not be*. A reader who just forgot grammar over-applies rules.
- Replace `sections[2].body[3]` with:
```
一般動詞的否定和問句用 <em>did</em>。<em>did</em> 已經標出過去，後面的動詞回到原形：<em>We did not receive the invoice.</em>，不是 <em>did not received</em>。<em>be</em> 動詞不用 <em>did</em>：<em>The invoice was not late.</em>
```

### 04-S7 [shouldFix] Chinese: 雇, name style, two stiff future-perfect translations, an airport 'Gate', bare English in takeaways
- Where: `sections[3].body[0]`, `sections[3].body[2]`, `sections[3].ex[0].zh`, `sections[3].ex[1].zh`, `sections[3].ex[2].zh`, `sections[3].ex[3].zh`, `sections[3].quiz[1].q`, `sections[6].ex[1].zh`, `sections[6].ex[2].zh`, `sections[1].ex[2].en`, `sections[2].takeaway`, `sections[4].takeaway`, `sections[5].takeaway`
- Problem: (1) 雇 → 僱 (see 02-S9). (2) 林先生 / 韓女士 → Latin names, matching the other chapters (see 02-S9). (3) 將已經開了 and 我們會已經…整理好 are word-for-word renderings of *will have opened / will have organized* that no one says. (4) An airport shuttle leaves from a door or a stop, not a *Gate* (gates are for flights). (5) Three takeaways leave English words outside `<em>` (STYLE §1); the takeaways of `sections[6]` and `sections[7]` are replaced under 04-M2 and 04-M1.
- In `sections[3].body[0]`: `雇` → `僱`
- In `sections[3].body[2]` (2 occurrences): `雇` → `僱`
- In `sections[3].ex[0].zh`: `雇` → `僱`
- In `sections[3].ex[1].zh`: `雇` → `僱`
- In `sections[3].ex[2].zh`: `林先生` → `Lin 先生`
- In `sections[3].ex[3].zh`: `林先生` → `Lin 先生`
- In `sections[3].quiz[1].q`: `韓女士` → `Han 女士`
- Replace `sections[6].ex[1].zh` with: (now: `到年底時，公司將已經開了五家新店。`)
```
到年底，公司將已開出五家新店。
```
- Replace `sections[6].ex[2].zh` with: (now: `等稽核人員到的時候，我們會已經把所有收據整理好。`)
```
等稽核人員到的時候，我們就已經把所有收據整理好了。
```
- In `sections[1].ex[2].en`: `Gate 3` → `Door 3`
- Replace `sections[2].takeaway` with: (now: `有明確的過去時間（yesterday、ago、last、in 2021），就用過去式。`)
```
有明確的過去時間（<em>yesterday</em>、<em>ago</em>、<em>last …</em>、<em>in 2021</em>），就用過去式。
```
- Replace `sections[4].takeaway` with: (now: `講未來最穩的是 will＋原形；已經排好的行程也可以用現在進行式。`)
```
講未來最穩的是 <em>will</em>＋原形；已經排好的行程也可以用現在進行式。
```
- Replace `sections[5].takeaway` with: (now: `兩件過去的事，比較早的那一件用 had＋p.p.。`)
```
兩件過去的事，比較早的那一件用 <em>had</em>＋p.p.。
```

### Verdict, chapter 4
Chapter 4 has accurate examples and is strongest where it matters: the past versus present-perfect threshold gets a full section built on the closed-door / looking-back picture, minimal pairs (*worked here for five years* versus *has worked here for five years*), an explanation of why *have hired … last year* is wrong, and two quizzes. Two statements need correcting. The time/condition-clause section tells the reader that every *when* or *if* clause takes the present for the future, which fails for *when / if* noun clauses (*Please tell us when the order will arrive*) that appear in ordinary business emails (04-M1), and the future-perfect takeaway reverses the body, since *by Friday* does not require *will have* (04-M2). Smaller inconsistencies: the lead promises six tenses and the body teaches seven, 'nine in all' ignores the perfect progressive, and *by the time* + past is stated without 'usually' (04-S3, 04-S5). Past progressive is in the table and is cited by chapter 5 but never explained (04-S1), and the past perfect lacks its reported-speech use (04-S2). Fix the two mustFix items and the chapter is sound.

---

## Cross-chapter notes (no change needed in these files, listed so the other chapters stay consistent)
- Chapter 16 `lead` and chapter 4 `sections[7].body[4]` both rely on 'that 子句' being taught in chapter 3. 03-M1 and 03-S5 keep that content in chapter 3; do not delete the that-clause paragraph, only move it.
- Chapter 7 `sections[3].body[4]` and chapter 13 `sections[7]` already state the *a number of / some of / most of / all of / half of* exception to chapter 2's 'strike the of-phrase' method. 02-S1 only adds a pointer, so the wording there (most of, some of, all of, half of) is kept the same.
- Chapter 5 `sections[1].body[1]` cites '過去進行式（第 4 章）'. 04-S1 makes that citation true.
- Chapter 8 `sections[5].body[5]` and `sections[7].body[2]`, and chapter 10 `sections[2].body[2]`, restate chapter 4's time/condition-clause rule ('用現在式，不用 will'). Once 04-M1 is adopted, each of them should say 'time or condition clause' (not every *when* / *if* clause).
- Chapter 9 `sections[0].body[1]` and `body[2]` teach that *who* is the relative clause's own subject, and chapter 9 `sections[0].body[5]` already uses the 'treat the relative clause as a bracket' reading. 03-M1 only adds the same idea in one sentence so that chapter 3 is not silent when it says a clause 'has its own subject and verb'; the two chapters now agree on the bracket method.
- Chapter 7 `sections[1].body[0]` and `body[2]` use 中心名詞 and 'the method of chapter 2'. 02-S2 only moves the definition earlier within chapter 2; the term and its meaning do not change.
- Chinese conventions found in chapters 1-4 that should be fixed book-wide, not only here: Latin names in Chinese lines (02-S9, 04-S7), 僱 not 雇, 總監 for *director*, 您 in letters, and `<em>` around English words in takeaways. A search of chapters 5-16 for 雇, 主任 and 朴 / 林 / 韓 / 太田 is worth running once.
