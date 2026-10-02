# Grammar book review: cross-chapter consistency (chapters 1-16)

Scope: all sixteen files in `chapters/` read as one book against `STYLE.md`. Each chapter has already had its own review (`review/grammar_review_01-04.md`, `05-08`, `09-12`, `13-16`); this file records only what a single-chapter review cannot see: references between chapters, rules stated in more than one place, terms, Chinese conventions, and names. No chapter file was edited.

## Result of `check.py` and `build.py`

- `python3 check.py`: all 16 chapters report `ok` (exit code 0).
- `python3 build.py`: `chapters 16 bytes 449941`, exit code 0. The rebuilt `grammar.html` is byte-identical to the committed one (md5 `cc1f41ac380690b7d5a8b3f466998ed3`), so the build changed nothing in the working tree.
- Every replacement below was applied to a scratch copy of the book (exact-match assertions on every `old` string, then `check.py` and `build.py` on the copy): all pass (`chapters 16`, exit code 0). After the replacements, a re-scan finds no surname used for both a man and a woman, no 小姐, no 核心名詞, no names written in characters, no bare `that 子句` outside the two headings that cannot carry markup, and no English question stem outside `<em>`.

## How to read this file

- Field paths are relative to the chapter file and 0-based, exactly as in the JSON (`sections[5]` is section n.6 on the page, where n is the chapter number). `10-conditional.json sections[2]` is section 10.3.
- **mustFix** = a wrong reference or a contradiction between chapters. **shouldFix** = inconsistency in terms, Chinese, names or formatting, or a gap a reader could fall into; each carries a priority (high / medium / low) to order the work.
- 'Replace `X` with `Y`' is a substring edit inside the named field and `X` occurs there exactly once unless a count is given. 'Replace every `X` with `Y` in …' lists every field that contains `X`; the list is exhaustive. 'Set the whole value' and 'append' are given in full. Replacement text uses the JSON markup (`<em>`, `<b>`); Chinese uses 「」, so nothing needs escaping.
- Edits within one issue do not overlap, and edits of different issues touch different substrings, so they can be applied in any order. The one dependency: the English question stems in X-S15 are given in their final form, after the renames of X-S18 (three of them contain a renamed surname).

## Summary

mustFix: 2. shouldFix: 20 (high 4, medium 3, low 13). The largest groups of fields are X-S15 (34 question stems) and the names in X-S13 / X-S18; every other issue is a handful of fields. X-M1 is one field; X-M2 is two fields plus one optional insertion.

| ID | Severity | Priority | Category | Files | What |
|---|---|---|---|---|---|
| X-M1 | mustFix | - | Contradiction (definition of 子句 / 有時態的動詞) | 16 | Chapter 16 calls a tenseless group a 'that 子句', against the clause rule of chapters 2 and 3 |
| X-M2 | mustFix | - | Wrong cross-reference (第 6 章) | 03 | Chapter 3 sends the reader to chapter 6 for a participle after a noun, which chapter 6 does not teach |
| X-S1 | shouldFix | low | Cross-reference | 13 | Chapter 13 points to chapter 11 for 'others', which chapter 11 does not teach |
| X-S2 | shouldFix | low | Cross-reference | 16 | Chapter 16 says chapter 4 teaches matching tenses across clauses; it teaches one case only |
| X-S3 | shouldFix | high | Contradiction risk / terms (time clause and condition clause) | 08, 10 | Chapters 8 and 10 restate chapter 4's present-for-future rule without the names 時間子句 / 條件子句; chapter 10 also loses the limit |
| X-S4 | shouldFix | low | Duplicated teaching (could be a pointer) | 13 | Chapter 13 re-teaches each / every and most of / some of from chapter 7 without saying so |
| X-S5 | shouldFix | medium | Terms (中心名詞) | 11, 13 | 中心名詞 is called 核心名詞 in chapters 11 and 13 |
| X-S6 | shouldFix | low | Terms (補充) | 08 | 補充 names two different ideas: an added point in chapter 8, a comma clause in chapter 9 |
| X-S7 | shouldFix | low | Terms (所有格 / 所有代名詞) | 11 | Chapter 11 files yours / ours / theirs / hers under 所有格, against its own table |
| X-S8 | shouldFix | low | Terms (chapter title vs STYLE.md) | 06 | Chapter 6's title drops the part of the STYLE.md title that tells the reader participles are here |
| X-S9 | shouldFix | medium | Chinese conventions (director) | 06, 16, 09 | 'director' is 總監 in chapters 1, 2, 5, 10 but 主任 in chapters 6 and 16 and 主管 in chapter 9 |
| X-S10 | shouldFix | low | Chinese conventions (project) | 08, 14 | 'project' is 專案 in chapters 9 and 10 but 計畫 in chapters 8 and 14 (where 計畫 also translates 'plan') |
| X-S11 | shouldFix | low | Chinese conventions (hotel guest / tenant) | 05, 06, 08, 13, 15, 16 | Hotel 'guests' are 房客 in chapters 5, 6, 8, 16 and 客人 in 13, 15, and chapter 16 uses 房客 for 'tenant' too |
| X-S12 | shouldFix | low | Chinese conventions (workshop) | 08, 10, 11 | 'workshop' is 研習 in chapters 8, 10, 11 and 工作坊 in chapters 14, 15 |
| X-S13 | shouldFix | high | Chinese conventions (personal names in Chinese lines) | 05, 06, 07, 08, 09, 10, 11, 12, 14, 16 | Chinese lines render some names in Chinese characters (one surname four ways); 小姐 appears five times where the book uses 女士 |
| X-S14 | shouldFix | low | Chinese conventions (`<em>` around names in Chinese lines) | 05, 06, 07, 08 | Names and places inside Chinese lines are wrapped in `<em>` in chapters 5–8 only |
| X-S15 | shouldFix | high | Chinese conventions (`<em>` around English) | 13, 14, 15, 16 | In chapters 13–16 every English question stem is plain text; in chapters 1–12 every one is inside `<em>` |
| X-S16 | shouldFix | low | Chinese conventions (`<em>` around English words in Chinese lines) | 03, 06, 11, 16 | 'that' in 'that 子句' and two tap-question words are bare English in chapters 3, 6, 11 and 16 |
| X-S17 | shouldFix | low | Chinese conventions (small items) | 09, 12, 10, 01, 14, 02 | Four one-line inconsistencies: App / app, 你 / 您 in a notice, filler 注意, a missing space before a name |
| X-S18 | shouldFix | high | Names (same surname, different people) | 03, 04, 05, 09, 11, 13, 14, 15 | Twelve surnames are used for a man in one chapter and a woman in another |
| X-S19 | shouldFix | medium | Names (companies) | 12, 04 | Two company names are one letter apart or share a first word with another company |
| X-S20 | shouldFix | low | Places (borderline real names; optional) | 15 | No real major city or well-known company appears in the chapters; one place name (Riverside) is a real mid-size city, optional |

File column shows chapter numbers.

## What was checked and found consistent

So that nothing here is re-checked: these were read across the whole book and need no change.

- **Cross-references.** All 147 `第 n 章`, 17 `第 n 節` and about 30 relative pointers (上一節, 下一節, 前兩節, 本章後面, 前半章, 第 6 章最後一節 and similar) were followed to the target. Every chapter number matches the STYLE.md table, and every in-chapter section number matches the real section order (02 `sections[6].body[0]` → `sections[5]`; 03 `sections[6].body[2]` and `sections[7].body[1]` → `sections[4]`; 04 `sections[0].body[3]` → `sections[3]`; 05 → sections 1, 3, 4, 6, 7; 06 `sections[4].body[4]` → `sections[1]`; 07 → sections 2 and 7; 08 `sections[6].body[4]` → `sections[2]`; 14 `sections[5].body[2]` → the table in `sections[4]`). The targets of the forward pointers exist (examples, all pairs were checked): 01 → 02 (有時態的動詞, 補語, 連綴動詞), 03, 06, 08, 11; 02 → 03, 04, 05, 06, 07, 13; 03 → 04, 06, 08, 09, 16; 04 → 03, 05, 07; 06 → 08, 16; 07 → 13; 08 → 10; 11 → 9, 12, 13; 13 → 7, 12; 14 → 6, 8, 10; 15 → 4, 6, 8; 16 → 3, 4, 5, 6, 7, 10. Exceptions are only X-M2, X-S1 and X-S2.
- **Definitions.** 有時態的動詞 (01 sections[4], 02 sections[1], 03, 06 sections[0], 08 sections[0]), 子句 and 片語 (STYLE §2, 02 sections[0] and [5], 03, 06 sections[6], 08), 中心名詞 (02 sections[5], 03 sections[6], 07 sections[1]) say the same thing everywhere; the one exception is chapter 16's tenseless clause (X-M1). 主要動詞 (02 sections[1]; used in 09 ×4 and 11) keeps its meaning.
- **When / if.** Chapter 4 teaches the present-for-future rule for time and condition clauses and limits it (04 sections[7].body[5]); chapters 8 and 10 never say 'every when / if clause' and every restatement is inside a time or condition context. (Naming only: X-S3.)
- **unless = if … not.** 08 sections[5].body[1]–[2] and 10 sections[6] give the same rule, the same caveat (reaction to something not happening) and the same example; each points to the other.
- **Agreement** (02 sections[6], 07, 09 sections[2].body[5], 11 sections[4] and [7], 13 sections[5]–[7], 14 sections[4]): skip the of-phrase and the inserted clause; the quantity-phrase exception (a number of / most of / some of); each, every, one of, either of; the number of vs a number of; there is / are; A and B vs A or B vs neither … nor; collective nouns, news, uncountables, people / police, Ving as a subject; the verb after who / which / that takes the number of the antecedent. No two chapters disagree. 02 `sections[6].body[3]` states 'the noun after a preposition is not the subject' as a bold rule and `body[4]` qualifies it in the next paragraph, which is how 07 sections[1].body[5] treats it too.
- **to as a preposition** (06 sections[3], 08 sections[8].body[2], 15 sections[6]): the same noun-test, compatible lists (look forward to, be committed to, in addition to, prior to, according to vs in order to, be able to, used to), and 06 / 16 agree that *suggest* takes Ving or a that-clause, never to V.
- **Other pairs checked, no conflict:** during / while / because / because of (01, 03, 08, 15); since / for (04, 15); by + deadline (04, 05, 15); passive and p.p. forms (04, 05, 06); *than I* (11, 12); *those of* (11, 12); British vs American handling of collective nouns and the base form (07, 11, 16); *ask / require + person + to V* (06) against *ask / require that* (16).
- **Terms:** 連綴動詞 (01, 02), 助動詞 (02, 05, 14), 及物 / 不及物 (05 introduces, 06 uses with a pointer), 先行詞 (09 only, 30 uses, no variants), 限定 / 補充 (09 only; see X-S6 for chapter 8), 冠詞 (01 only), 所有格 (01, 09, 11, 12; see X-S7), 連接副詞 (03, 08), 倒裝 (10, 14). No variant spellings of any STYLE.md §2 term were found (no 動名詞, 不定詞, 原型, 主句, 附屬, 介詞, 連詞).
- **Chinese:** no simplified characters; 僱 (nine uses, no 雇); 資料夾; 總監; 電子郵件; 軟體; 檔案; 筆電; 計程車; 線上; 週; 您 for letters to a reader. No mainland vocabulary (質量, 信息, 軟件, 視頻, 默認, 打印, 登錄, 網絡) anywhere.
- **Names and places:** every example name is invented; no real capital or large city and no well-known company remains (X-S20 lists the borderline ones). The `workbook` list of every chapter matches STYLE.md §3.

## mustFix

### X-M1 · mustFix · Chapter 16 calls a tenseless group a 'that 子句', against the clause rule of chapters 2 and 3

- **Category:** Contradiction (definition of 子句 / 有時態的動詞)
- **Files:** `16-mandative.json`
- **Problem:** Chapter 2 defines a clause as a group with its own subject and a 有時態的動詞 (02 sections[1]: the verb that 'marks time'), and chapter 3 turns that into a counting rule: '一句話裡有幾個有時態的動詞，就有幾個子句' (03 sections[4].body[0]). Chapter 16 calls the group after requested / recommended a 'that 子句' (lead, sections[0].body[0], table headers) and then says its verb carries no tense: 'sections[0].body[1]: 也就是不標任何時態', 'sections[3].body[1]: 這個句型的動詞沒有時態'. By the book's own test, `that Mr. Kim submit the report` has no tensed verb, so a reader who applies the chapter 3 count to *The manager requested that Mr. Kim submit the report.* gets one clause, while chapter 16 says there are two. Chapter 16 never says the rule bends here. One added sentence closes the gap without changing the chapter's teaching.
- **Replacement:**
  - `16-mandative.json` `sections[0].body[1]`: append to the end of the field: `這是第 2、3 章「子句裡有一個有時態的動詞」的特例：<em>submit</em> 沒有標時態，但它前面有自己的主詞 <em>Mr. Kim</em>，所以 <em>that Mr. Kim submit the report</em> 仍然是子句；整句有時態的動詞是 <em>requested</em>。`

### X-M2 · mustFix · Chapter 3 sends the reader to chapter 6 for a participle after a noun, which chapter 6 does not teach

- **Category:** Wrong cross-reference (第 6 章)
- **Files:** `03-clause.json`
- **Problem:** 03 `sections[2].body[4]` and `sections[2].ex[3]` use *the contract signed by both parties* (a past participle placed after the noun) as the example of a past participle that is not a finite verb, and body[4] adds '第 6 章會講'. Chapter 6 teaches participles only before a noun or after *be* (06 sections[5].body[0]: 'Ving 和 p.p. 也可以放在名詞前面或 be 後面') and as sentence-opening phrases (06 sections[6]). No section of chapter 6 shows a participle phrase after a noun, so the reader who follows the pointer finds nothing for this shape, and the example in chapter 3 stays unexplained. Two ways out. Option A (minimal, chapter 3 only) explains the shape in one clause where it is first used and keeps the pointer for participles in general. Option B (optional, in addition) gives the shape one short paragraph in chapter 6 so the pointer is fully true.
- **Replacement:**
  - `03-clause.json` `sections[2].body[4]`: replace `（<em>-ed</em> 的樣子，例如 <em>the contract signed by both parties</em> 裡的 <em>signed</em>，第 6 章會講）` with `（<em>-ed</em> 的樣子。放在名詞後面時，像 <em>the contract signed by both parties</em> 裡的 <em>signed</em>，意思是「被雙方簽署的那份合約」；分詞第 6 章會講）`
  - `03-clause.json` `sections[2].ex[3].note`: replace `<em>signed</em> 是過去分詞，不是有時態的動詞：這組字是片語。` with `<em>signed</em> 是過去分詞，放在名詞 <em>contract</em> 後面，說明是哪一份合約，不是有時態的動詞：<em>signed by both parties</em> 是片語。`
  - `06-verbforms.json` `sections[5].body`: insert a new item at index 4 (before the current item 4): `分詞也可以放在名詞後面，帶著自己後面的字一起說明這個名詞：<em>the contract signed by both parties</em>（被雙方簽署的合約）、<em>the staff attending the briefing</em>（出席說明會的員工）。選 <em>-ing</em> 還是 <em>-ed</em>，問題還是一樣：這個名詞是做，還是被做。這種寫法的作用和 <em>who</em>、<em>which</em> 帶頭的關係子句（第 9 章）一樣，只是沒有那個連接的字，也沒有有時態的動詞，所以是片語。`
- **Note:** The third edit (06 `sections[5].body`, insert as the new item at index 4, i.e. after the current body[3] and before body[4]) is Option B and optional. If it is used, 06 `sections[5]` still has one idea (participles as adjectives), only a second position for them.

## shouldFix

### 1. Cross-references

### X-S1 · shouldFix (low) · Chapter 13 points to chapter 11 for 'others', which chapter 11 does not teach

- **Category:** Cross-reference
- **Files:** `13-quantity.json`
- **Problem:** 13 `sections[8].body[4]` says '`<em>others</em>` 是代名詞（第 11 章）'. Chapter 11 covers case forms, its/it's, -self forms, agreement, one/ones, those who and each other; *others* is not in it. The pointer is only right as a pointer to the part of speech, which chapter 1 teaches, and chapter 13 already points to chapter 1 for *almost* (sections[7].body[3]).
- **Replacement:**
  - `13-quantity.json` `sections[8].body[4]`: replace `<em>others</em> 是代名詞（第 11 章），` with `<em>others</em> 是代名詞（第 1 章），`

### X-S2 · shouldFix (low) · Chapter 16 says chapter 4 teaches matching tenses across clauses; it teaches one case only

- **Category:** Cross-reference
- **Files:** `16-mandative.json`
- **Problem:** 16 `sections[1].body[1]`: '一般的句子裡，第 4 章教你讓前後時態配合'. Chapter 4 has no section on tense matching; the only related passage is the *said that she had already paid* paragraph (04 sections[5].body[4]) plus the time-clause rule. The learner looking for a general rule will not find one. Point to the passage that exists.
- **Replacement:**
  - `16-mandative.json` `sections[1].body[1]`: replace `一般的句子裡，第 4 章教你讓前後時態配合；在這個句型裡，不要配合。` with `一般陳述事實的 that 子句，時態要和前面的動詞對得上（第 4 章的 <em>The client said that she had already paid the deposit.</em>）；在這個句型裡，不要配合。`

### 2. Contradictions and duplicated teaching

### X-S3 · shouldFix (high) · Chapters 8 and 10 restate chapter 4's present-for-future rule without the names 時間子句 / 條件子句; chapter 10 also loses the limit

- **Category:** Contradiction risk / terms (time clause and condition clause)
- **Files:** `08-connect.json`, `10-conditional.json`
- **Problem:** Chapter 4 (sections[7]) teaches the rule once, with the names 時間子句 and 條件子句 and the limit that `when` / `if` meaning 'what time' / 'whether' (after know, ask, tell, check) are noun clauses and keep *will* (04 sections[7].body[5]). Chapters 8 and 10 each restate the rule. None says 'every when / if clause', and every restatement sits in a time or condition context, so nothing is wrong as written. But 08 `sections[5].body[6]` and `sections[7].body[2]` say '照第 4 章的規則' without naming the clause type, and 10 `sections[2].body[2]` says 'if 子句也用現在式' and '這些表示時間的連接詞' with no pointer to the limit; 10 `sections[0].body[0]` opens with 'if 帶頭的子句 … 說的是「條件」', which is true of conditional clauses but not of every if-clause (the noun-clause *if* of 04 sections[7].body[5] is the exception). A learner who reads chapter 10 alone, or who meets *Please tell us if the order will arrive* later, has nothing that says the rule stops at time and condition clauses. Use the chapter 4 names everywhere and give chapter 10 the pointer.
- **Replacement:**
  - `08-connect.json` `sections[5].body[6]`: replace `講未來的條件時，<em>unless、if</em> 帶的子句照第 4 章的規則用現在式，不用 <em>will</em>：` with `<em>unless</em>、<em>if</em> 帶頭的是條件子句（第 4 章第 8 節）。講未來的事時，條件子句用現在式，不用 <em>will</em>：`
  - `08-connect.json` `sections[7].body[2]`: replace `時態照第 4 章的規則：這類句子講的常常是未來，主要子句用 <em>will</em>，<em>once、as soon as</em> 帶的子句卻用現在式：` with `<em>once</em>、<em>as soon as</em> 帶頭的是時間子句（第 4 章第 8 節）。這類句子講的常常是未來，主要子句用 <em>will</em>，時間子句卻用現在式：`
  - `10-conditional.json` `sections[0].body[0]`: replace `<em>if</em> 帶頭的子句是從屬子句（第 3 章），說的是「條件」；` with `<em>if</em> 帶頭、交代條件的子句叫條件子句（第 4 章第 8 節），是從屬子句（第 3 章），說的是「條件」；`
  - `10-conditional.json` `sections[2].body[2]`: replace `<em>when</em>、<em>before</em>、<em>as soon as</em> 這些表示時間的連接詞，後面的子句也一樣用現在式（第 4 章）。` with `<em>when</em>、<em>before</em>、<em>as soon as</em> 帶頭的時間子句也一樣，未來用現在式。<em>if</em> 放在 <em>ask</em>、<em>know</em> 這類動詞後面、當「是不是」用時，不是條件子句，未來照用 <em>will</em>。兩點都見第 4 章第 8 節。`

### X-S4 · shouldFix (low) · Chapter 13 re-teaches each / every and most of / some of from chapter 7 without saying so

- **Category:** Duplicated teaching (could be a pointer)
- **Files:** `13-quantity.json`
- **Problem:** The following topics are taught twice and the two versions agree (no contradiction found): each / every / one of (07 sections[2] and 13 sections[6]); a number of / the number of (07 sections[3] and 13 sections[5]); most of / some of / all of + noun (07 sections[1].body[5] and 13 sections[7]); neither … nor, either … or, A or B (07 sections[5] and 14 sections[4]); unless = if … not (08 sections[5] and 10 sections[6]); than I / than me (11 sections[1].body[4] and 12 sections[3].body[3]); preposition *to* (06 sections[3] and 15 sections[6]); during / while (08 sections[4] and 15 sections[4]); since / for (04 sections[3] and 15 sections[3]). Seven of the nine already carry a pointer (13 sections[5].body[1] → 7; 14 sections[4].body[0] → 7; 08 ↔ 10; 12 → 11; 15 → 4, 6, 8). The two that do not are 13 sections[6] and 13 sections[7]; a reader who has just done chapter 7 meets the same rule again and may wonder whether it changed. One sentence each makes it a deliberate second look.
- **Replacement:**
  - `13-quantity.json` `sections[6].body[0]`: replace `<em>each</em> 和 <em>every</em> 都是「每一個」。` with `第 7 章第 3 節講過 <em>each</em>、<em>every</em> 配單數動詞；這一節從後面接的名詞再看一次。<em>each</em> 和 <em>every</em> 都是「每一個」。`
  - `13-quantity.json` `sections[7].body[2]`: replace `動詞跟著 <em>of</em> 後面的名詞走：` with `動詞跟著 <em>of</em> 後面的名詞走（第 7 章第 2 節的例外）：`

### 3. Terms

### X-S5 · shouldFix (medium) · 中心名詞 is called 核心名詞 in chapters 11 and 13

- **Category:** Terms (中心名詞)
- **Files:** `11-pronoun.json`, `13-quantity.json`
- **Problem:** Chapter 2 introduces 中心名詞 (02 sections[5].body[2]) and chapters 3 and 7 use it. Chapter 11 sections[4].body[3] and chapter 13 sections[5] (quiz q and why) say 核心名詞 for the same thing, with no pointer. Use the one term, and give chapter 11 the chapter 2 pointer (STYLE §2: remind where a term was taught).
- **Replacement:**
  - `11-pronoun.json` `sections[4].body[3]`: replace `要找的是核心名詞，不是離代名詞最近的那個字。` with `要找的是中心名詞（第 2 章），不是離代名詞最近的那個字。`
  - `13-quantity.json` `sections[5].quiz[0].q`: replace `這句主詞的核心名詞，和它的動詞。` with `這句主詞的中心名詞，和它的動詞。`
  - `13-quantity.json` `sections[5].quiz[0].why`: replace `主詞的核心是 <em>number</em>（數目）。` with `主詞的中心名詞是 <em>number</em>（數目）。`

### X-S6 · shouldFix (low) · 補充 names two different ideas: an added point in chapter 8, a comma clause in chapter 9

- **Category:** Terms (補充)
- **Files:** `08-connect.json`
- **Problem:** Chapter 9 sections[6] makes 限定 / 補充 the pair that names a relative clause without / with commas (eight uses of 補充 there). Chapter 8 sections[8], one chapter earlier, uses 補充 for the sentence relation 'one more point in the same direction' (in addition, moreover). Both uses are explained where they occur, but the reader has met 補充 as 'addition' before chapter 9 asks it to mean 'a clause you could remove'. Rename the chapter 8 label so 補充 belongs to chapter 9 only.
- **Replacement:**
  - `08-connect.json` `sections[8].body[1]`: replace `往同一個方向再加一點，是<b>補充</b>。` with `往同一個方向再加一點，是<b>追加</b>。`
  - `08-connect.json` `sections[8].body[2]`: replace `補充是前面還沒講的一組：` with `追加是前面還沒講的一組：`
  - `08-connect.json` `sections[8].ex[1].note`: replace `兩個優點，同一個方向：補充。` with `兩個優點，同一個方向：追加。`
  - `08-connect.json` `sections[8].table.rows[6][0]`: replace `補充` with `追加`
  - `08-connect.json` `sections[8].quiz[0].why`: replace `往同一個方向加，是補充：` with `往同一個方向加，是追加：`
  - `08-connect.json` `sections[8].takeaway`: replace `目的、補充）` with `目的、追加）`

### X-S7 · shouldFix (low) · Chapter 11 files yours / ours / theirs / hers under 所有格, against its own table

- **Category:** Terms (所有格 / 所有代名詞)
- **Files:** `11-pronoun.json`
- **Problem:** Chapter 11's table (sections[0]) names *my, your, her, our, their* 所有格 and *mine, yours, hers, ours, theirs* 所有代名詞. Section 3 then says 'the 所有格 of pronouns takes no apostrophe: its, yours, ours, theirs, hers' and the takeaway repeats it, so three of the five words listed are 所有代名詞 by the chapter's own table. Chapter 1, 9 and 12 use 所有格 in the table's narrow sense.
- **Replacement:**
  - `11-pronoun.json` `sections[2].body[0]`: replace `但代名詞的所有格<b>不加撇號</b>：` with `但代名詞的所有格和所有代名詞<b>都不加撇號</b>：`
  - `11-pronoun.json` `sections[2].takeaway`: replace `代名詞的所有格不加撇號；` with `代名詞的所有格和所有代名詞都不加撇號；`

### X-S8 · shouldFix (low) · Chapter 6's title drops the part of the STYLE.md title that tells the reader participles are here

- **Category:** Terms (chapter title vs STYLE.md)
- **Files:** `06-verbforms.json`
- **Problem:** STYLE.md §3 gives chapter 6 the title '動詞後面接什麼：to V、Ving、原形；分詞'; the file has '動詞後面接什麼'. Chapters 2 and 3 send the reader to chapter 6 for 過去分詞 (02 sections[1].body[2], 03 sections[2].body[4]), and the chapter list shows only the title. All other 15 titles match STYLE.md exactly. (If the shorter title is intended, change the STYLE.md row instead.)
- **Replacement:**
  - `06-verbforms.json` `title`: set the whole value to `動詞後面接什麼：to V、Ving、原形；分詞`

### 4. Chinese conventions

### X-S9 · shouldFix (medium) · 'director' is 總監 in chapters 1, 2, 5, 10 but 主任 in chapters 6 and 16 and 主管 in chapter 9

- **Category:** Chinese conventions (director)
- **Files:** `06-verbforms.json`, `16-mandative.json`, `09-relative.json`
- **Problem:** 01 sections[5].ex[1], 02 sections[4], 05 sections[2].ex[1] and 10 sections[5].ex[1] render *director* as 總監 (the convention the chapter 1–4 review set: 總監 for director). 06 sections[4].ex[0].zh and 16 sections[4].ex[3].zh say 主任, and 09 sections[3].quiz[0].why says 「主管說」 for *the director said*. 工地主任 for *site supervisor* (06 sections[0].ex[2]) is correct and stays.
- **Replacement:**
  - `06-verbforms.json` `sections[4].ex[0].zh`: replace `主任要我們重做銷售預測。` with `總監要我們重做銷售預測。`
  - `16-mandative.json` `sections[4].ex[3].zh`: replace `主任要求這份檔案不要分享給團隊以外的人。` with `總監要求這份檔案不要分享給團隊以外的人。`
  - `09-relative.json` `sections[3].quiz[0].why`: replace `「主管說」` with `「總監說」`

### X-S10 · shouldFix (low) · 'project' is 專案 in chapters 9 and 10 but 計畫 in chapters 8 and 14 (where 計畫 also translates 'plan')

- **Category:** Chinese conventions (project)
- **Files:** `08-connect.json`, `14-parallel.json`
- **Problem:** 09 sections[3].ex[1], ex[2] and 10 sections[8].ex[2] render *project* as 專案. 08 sections[0].ex[0]–ex[3] ('we finished the project on time') and 14 sections[6].ex[2] ('canceling the project') render it 計畫, which chapters 2 and 4 use for *plan* ('approve the plan'). Taiwan business usage separates the two; use 專案 for *project* throughout and keep 計畫 for *plan* / *program*.
- **Replacement:**
  - `08-connect.json`: replace every `完成了計畫` with `完成了專案` in `sections[0].ex[0].zh`, `sections[0].ex[1].zh`, `sections[0].ex[2].zh`, `sections[0].ex[3].zh`
  - `14-parallel.json` `sections[6].ex[2].zh`: replace `取消這個計畫` with `取消這個專案`

### X-S11 · shouldFix (low) · Hotel 'guests' are 房客 in chapters 5, 6, 8, 16 and 客人 in 13, 15, and chapter 16 uses 房客 for 'tenant' too

- **Category:** Chinese conventions (hotel guest / tenant)
- **Files:** `05-voice.json`, `06-verbforms.json`, `08-connect.json`, `13-quantity.json`, `15-prep.json`, `16-mandative.json`
- **Problem:** 16 sections[1].ex[3].zh uses 房客 for *tenant* ('房東堅持房客要付全額押金') and 16 sections[3].ex[2].zh uses the same word for hotel *guests* ('飯店請房客不要在陽台抽菸'), two different people in one chapter. Elsewhere hotel guests are 房客 (05, 06, 08) or 客人 (13, 15). Use 住客 for hotel guests everywhere; 房客 then means only the tenant.
- **Replacement:**
  - `05-voice.json` `sections[4].ex[0].note`: replace `房客要知道的是早餐。` with `住客要知道的是早餐。`
  - `06-verbforms.json` `check[3].why`: replace `房客是被弄得沮喪的人` with `住客是被弄得沮喪的人`
  - `08-connect.json` `sections[7].ex[2].zh`: replace `房客一抵達，` with `住客一抵達，`
  - `13-quantity.json` `sections[5].ex[0].zh`: replace `有好幾位客人要求延後退房。` with `有好幾位住客要求延後退房。`
  - `13-quantity.json` `sections[5].body[1]`: replace `（客人的數目增加了一倍）` with `（住客的數目增加了一倍）`
  - `13-quantity.json` `sections[5].body[1]`: replace `從「客人」變成「數目」` with `從「住客」變成「數目」`
  - `15-prep.json` `sections[7].ex[0].zh`: replace `大部分的客人偏好` with `大部分的住客偏好`
  - `16-mandative.json` `sections[3].ex[2].zh`: replace `飯店請房客不要` with `飯店請住客不要`

### X-S12 · shouldFix (low) · 'workshop' is 研習 in chapters 8, 10, 11 and 工作坊 in chapters 14, 15

- **Category:** Chinese conventions (workshop)
- **Files:** `08-connect.json`, `10-conditional.json`, `11-pronoun.json`
- **Problem:** The same English word is rendered two ways across five chapters: 研習 (08 sections[4].ex[0], ex[1]; 10 sections[6].ex[0]; 11 sections[1].ex[3]) and 工作坊 (14 sections[3].ex[3]; 15 sections[3].ex[3]). Use 工作坊 (the majority of Taiwan business writing for *workshop*).
- **Replacement:**
  - `08-connect.json` `sections[4].ex[0].zh`: replace `研習進行時，` with `工作坊進行時，`
  - `08-connect.json` `sections[4].ex[1].zh`: replace `研習期間，` with `工作坊期間，`
  - `10-conditional.json` `sections[6].ex[0].zh`: replace `否則不能參加研習。` with `否則不能參加工作坊。`
  - `11-pronoun.json` `sections[1].ex[3].zh`: replace `會主持研習。` with `會主持工作坊。`

### X-S13 · shouldFix (high) · Chinese lines render some names in Chinese characters (one surname four ways); 小姐 appears five times where the book uses 女士

- **Category:** Chinese conventions (personal names in Chinese lines)
- **Files:** `05-voice.json`, `06-verbforms.json`, `07-agree.json`, `08-connect.json`, `09-relative.json`, `10-conditional.json`, `11-pronoun.json`, `12-compare.json`, `14-parallel.json`, `16-mandative.json`
- **Problem:** The chapter 1–4 review fixed one convention for the whole book: the Chinese line keeps the Latin name ('Ruiz 女士', 'Park 女士'), titled 先生 / 女士. Chapters 5–16 were not searched against it. Names written in characters remain in eight chapters (29 occurrences, against 72 titled names written in Latin letters): 周 / 何 / 吳 / 林 (05), 高 / 阿部 (06), 陳 (07, 09, 14), 佐藤 (08), 李 (11), 金 (16, eight occurrences). The same name is therefore written two or more ways: Abe is 阿部先生 in 06 and Abe 先生 in 11; Chen is 陳女士 in 07 and 14 and 陳小姐 in 09; Lin is Lin 先生 in 04, 林先生 in 05, 林小姐 in 09 and 林女士 in 14. 小姐 is used five times (09 ×2, 10 ×2, 12 ×1); the other 49 uses of a title for a woman are 女士. (The Ms. Lin lines in 09 and 14 are covered by X-S18, which renames that person.) The book puts a space between a Chinese character and a Latin name ('寄給 Abe 先生', '我們 Westbrook 分店'), so where a Chinese character comes right before the name the replacement adds that space; each pair below shows the exact context, and the pairs are exhaustive for the field named.
- **Replacement:**
  - `05-voice.json`: `周女士` → `Chou 女士`: `sections[0].body[0]`: `是周女士` → `是 Chou 女士`; `sections[0].ex[0].zh`: `周女士` → `Chou 女士`; `sections[0].ex[1].zh`: `由周女士` → `由 Chou 女士`
  - `05-voice.json`: `林先生` → `Lin 先生`: `sections[2].body[2]`: `林先生` → `Lin 先生`; `sections[2].ex[1].zh`: `林先生` → `Lin 先生`
  - `05-voice.json`: `何女士` → `Ho 女士`: `sections[4].ex[2].zh`: `何女士` → `Ho 女士`
  - `05-voice.json`: `吳女士` → `Wu 女士`: `sections[6].body[0]`: `了吳女士` → `了 Wu 女士`; `sections[6].body[2]`: `吳女士` → `Wu 女士`; `sections[6].ex[0].zh`: `供吳女士` → `供 Wu 女士`; `sections[6].ex[1].zh`: `吳女士` → `Wu 女士`
  - `06-verbforms.json`: `高女士` → `Kao 女士`: `sections[0].ex[1].zh`: `高女士` → `Kao 女士`
  - `06-verbforms.json`: `阿部先生` → `Abe 先生`: `sections[4].ex[2].zh`: `阿部先生` → `Abe 先生`; `sections[4].ex[3].zh`: `阿部先生` → `Abe 先生`
  - `07-agree.json`: `陳女士` → `Chen 女士`: `sections[1].ex[3].zh`: `陳女士` → `Chen 女士`
  - `08-connect.json`: `佐藤女士` → `Sato 女士`: `sections[8].ex[2].zh`: `佐藤女士` → `Sato 女士`
  - `09-relative.json`: `陳小姐` → `Chen 女士`: `sections[0].ex[2].zh`: `陳小姐` → `Chen 女士`
  - `10-conditional.json`: replace every `Kato 小姐` with `Kato 女士` in `sections[3].ex[1].zh`
  - `10-conditional.json`: replace every `Ruiz 小姐` with `Ruiz 女士` in `sections[5].ex[1].zh`
  - `11-pronoun.json`: `李先生` → `Lee 先生`: `sections[1].ex[4].zh`: `給李先生` → `給 Lee 先生`
  - `12-compare.json`: replace every `Tran 小姐` with `Tran 女士` in `sections[7].ex[2].zh`
  - `14-parallel.json`: `陳女士` → `Chen 女士`: `sections[2].ex[3].zh`: `陳女士` → `Chen 女士`
  - `16-mandative.json`: `金先生` → `Kim 先生`: `sections[0].body[0]`: `道金先生` → `道 Kim 先生`; `求金先生` → `求 Kim 先生`; `sections[0].body[2]`: `對金先生` → `對 Kim 先生`; `sections[0].body[3]`: `金先生` → `Kim 先生`; `sections[0].ex[0].zh`: `道金先生` → `道 Kim 先生`; `sections[0].ex[1].zh`: `求金先生` → `求 Kim 先生`; `sections[6].ex[0].zh`: `求金先生` → `求 Kim 先生`; `sections[6].ex[1].zh`: `求金先生` → `求 Kim 先生`

### X-S14 · shouldFix (low) · Names and places inside Chinese lines are wrapped in `<em>` in chapters 5–8 only

- **Category:** Chinese conventions (`<em>` around names in Chinese lines)
- **Files:** `05-voice.json`, `06-verbforms.json`, `07-agree.json`, `08-connect.json`
- **Problem:** In chapters 1–4 and 9–16 a Latin name or place inside a Chinese line is plain text ('Ruiz 女士', 'Westbrook 分店'; some 70 cases). In chapters 5, 6, 7 and 8 eleven fields wrap it in `<em>`, so the page shows the same kind of word in two colours (the template colours `<em>` with the accent colour). Majority rule: plain text. (05 `sections[6].ex[3].zh` is handled by X-S18 because the name also changes there.)
- **Replacement:**
  - `05-voice.json` `sections[4].ex[3].zh`: replace `<em>Delmont Foods</em>` with `Delmont Foods`
  - `05-voice.json` `sections[6].quiz[0].why`: replace `<em>Tan</em> 女士` with `Tan 女士`
  - `06-verbforms.json` `sections[3].ex[1].zh`: replace `<em>Halden Foods</em>` with `Halden Foods`
  - `06-verbforms.json` `sections[3].ex[2].zh`: replace `<em>Ruiz</em>` with `Ruiz`
  - `06-verbforms.json` `sections[3].ex[3].zh`: replace `<em>Holt</em>` with `Holt`
  - `06-verbforms.json` `sections[3].ex[3].zh`: replace `<em>Dalton</em>` with `Dalton`
  - `06-verbforms.json` `sections[6].ex[0].zh`: replace `<em>Larkfield</em>` with `Larkfield`
  - `06-verbforms.json` `sections[6].ex[1].zh`: replace `<em>Kestrel</em>` with `Kestrel`
  - `07-agree.json` `sections[5].ex[0].zh`: replace `<em>Westbrook</em>` with `Westbrook`
  - `07-agree.json` `sections[6].ex[1].zh`: replace `<em>Eastfield</em>` with `Eastfield`
  - `08-connect.json` `sections[3].ex[3].zh`: replace `<em>Ng</em>` with `Ng`

### X-S15 · shouldFix (high) · In chapters 13–16 every English question stem is plain text; in chapters 1–12 every one is inside `<em>`

- **Category:** Chinese conventions (English words in Chinese / formatting)
- **Files:** `13-quantity.json`, `14-parallel.json`, `15-prep.json`, `16-mandative.json`
- **Problem:** In chapters 1–12 all 113 `choose` stems that contain an English sentence wrap it in `<em>` (e.g. `<em>The ___ was announced at the morning meeting.</em> 空格要放哪一種詞性？`). In chapters 13–16 thirty-four `choose` stems are the bare sentence (`We don't have ___ information about the new supplier yet.`), so the page shows them in the Chinese font and body colour, while `template.html` renders `<em>` in the English font and accent colour (`em,.en{font-family:var(--en)…}`, `em{color:var(--accent)}`) and every other chapter shows its stems that way. STYLE.md §1 asks for `<em>` on English inside Chinese. Wrap each stem; in chapter 16 the Chinese lead-in `依美式正式書面英文的寫法選：` stays outside. Values below are final (they include the X-S18 renames in 15 `check[2].q`, `check[4].q` and `sections[4].quiz[0].q`).
- **Replacement:** set the whole value of each field to the value shown.

| File | Field | New value |
|---|---|---|
| `13-quantity.json` | `check[1].q` | `<em>We don't have ___ information about the new supplier yet.</em>` |
| `13-quantity.json` | `check[2].q` | `<em>Each of the new interns ___ a laptop.</em>` |
| `13-quantity.json` | `check[3].q` | `<em>There were ___ errors in this month's report than in last month's.</em>` |
| `13-quantity.json` | `check[4].q` | `<em>We have two meeting rooms. Room A is booked, so please use ___ one.</em>` |
| `13-quantity.json` | `sections[2].quiz[0].q` | `<em>How ___ luggage are you bringing on the trip?</em>` |
| `13-quantity.json` | `sections[3].quiz[0].q` | `<em>___ people signed up for the workshop, so we can hold it as planned.</em>` |
| `13-quantity.json` | `sections[4].quiz[0].q` | `<em>The new air conditioners use ___ electricity than the old ones.</em>` |
| `13-quantity.json` | `sections[6].quiz[0].q` | `<em>Each of the new laptops ___ with a two-year warranty.</em>` |
| `13-quantity.json` | `sections[8].quiz[0].q` | `<em>Some clients pay online; ___ pay by bank transfer.</em>` |
| `14-parallel.json` | `check[1].q` | `<em>Please sign the form, ___ a copy, and return it to the HR office.</em>` |
| `14-parallel.json` | `check[2].q` | `<em>The hotel offers both free breakfast ___ an airport shuttle.</em>` |
| `14-parallel.json` | `check[3].q` | `<em>Neither the manager nor her assistants ___ available on Friday.</em>` |
| `14-parallel.json` | `sections[1].quiz[0].q` | `<em>Our goals this year are to cut costs, to improve customer service, and ___ sales in Asia.</em>` |
| `14-parallel.json` | `sections[2].quiz[0].q` | `<em>The technician will inspect the machine and ___ a report by Friday.</em>` |
| `14-parallel.json` | `sections[3].quiz[0].q` | `<em>You can submit the form ___ by email or at the front desk.</em>` |
| `14-parallel.json` | `sections[6].quiz[0].q` | `<em>Ms. Ward called the supplier instead of ___ another email.</em>` |
| `15-prep.json` | `check[0].q` | `<em>The new branch opens ___ March 3.</em>` |
| `15-prep.json` | `check[1].q` | `<em>Please submit your expense report ___ Friday.</em>` |
| `15-prep.json` | `check[2].q` | `<em>Mr. Dunmore has worked in the downtown office ___ 2021.</em>` |
| `15-prep.json` | `check[3].q` | `<em>Ms. Novak is ___ the new training program.</em>` |
| `15-prep.json` | `check[4].q` | `<em>In addition to ___ the new hires, Ms. Fraser manages the payroll.</em>` |
| `15-prep.json` | `sections[2].quiz[0].q` | `<em>The conference room is reserved for our team ___ 3 p.m., so no other group can use it before then.</em>` |
| `15-prep.json` | `sections[3].quiz[0].q` | `<em>Our company has used this supplier ___ more than ten years.</em>` |
| `15-prep.json` | `sections[4].quiz[0].q` | `<em>Mr. Voss answered several emails ___ the training session.</em>` |
| `15-prep.json` | `sections[5].quiz[0].q` | `<em>Mr. Diallo thanked the volunteers ___ the hotel's management.</em>` |
| `15-prep.json` | `sections[6].quiz[0].q` | `<em>In addition to ___ free Wi-Fi, the hotel offers a free airport shuttle.</em>` |
| `15-prep.json` | `sections[7].quiz[0].q` | `<em>___ the weather forecast, the storm will reach the coast tonight.</em>` |
| `16-mandative.json` | `check[0].q` | `依美式正式書面英文的寫法選：<em>Our director recommended that each team ___ its budget by May 1.</em>` |
| `16-mandative.json` | `check[1].q` | `依美式正式書面英文的寫法選：<em>It is essential that every guest ___ a photo ID at check-in.</em>` |
| `16-mandative.json` | `check[2].q` | `依美式正式書面英文的寫法選：<em>Our lawyer recommended that the company ___ the contract until the terms are revised.</em>` |
| `16-mandative.json` | `check[3].q` | `依美式正式書面英文的寫法選：<em>The contract requires that the payment ___ made in full before delivery.</em>` |
| `16-mandative.json` | `sections[1].quiz[0].q` | `依美式正式書面英文的寫法選：<em>Last year, the auditors recommended that the firm ___ its records every quarter.</em>` |
| `16-mandative.json` | `sections[3].quiz[0].q` | `依美式正式書面英文的寫法選：<em>The supervisor asked that the new technician ___ the machine without training.</em>` |
| `16-mandative.json` | `sections[5].quiz[0].q` | `<em>The latest sales figures suggest that the campaign ___ working.</em>` |

### X-S16 · shouldFix (low) · 'that' in 'that 子句' and two tap-question words are bare English in chapters 3, 6, 11 and 16

- **Category:** Chinese conventions (`<em>` around English words in Chinese lines)
- **Files:** `03-clause.json`, `06-verbforms.json`, `11-pronoun.json`, `16-mandative.json`
- **Problem:** STYLE.md §1: English words inside Chinese text take `<em>`. Elsewhere the book writes '`<em>that</em>`' (e.g. 03 sections[7].body[0] and [1], 04 sections[7].body[4]); 03 sections[7].body[1] once, 06 (three fields) and 16 (twenty-one fields) leave *that* bare in the phrase 'that 子句'. 11 check[3].q and sections[5].quiz[0].q leave *it* / *they* bare in '點出 it 代替的那個名詞'. (The English question stems of 16 are separate: X-S15.) In each field listed, replace every `that 子句` with `<em>that</em> 子句`; the field lists below are exhaustive. Chapter titles and section headings (`title`, `sections[n].h`, e.g. 16 `title`, 03 `sections[7].h`) are excluded on purpose: `template.html` inserts them with `textContent`, so a tag there would print literally, and every heading in the book keeps its English bare.
- **Replacement:**
  - `03-clause.json`: replace every `that 子句` with `<em>that</em> 子句` in `sections[7].body[1]`
  - `06-verbforms.json`: replace every `that 子句` with `<em>that</em> 子句` in `sections[1].body[4]`, `sections[1].quiz[0].why`, `mistakes[1].why`
  - `16-mandative.json`: replace every `that 子句` with `<em>that</em> 子句` in `lead`, `check[0].why`, `check[1].why`, `sections[0].body[0]`, `sections[0].body[1]`, `sections[0].body[2]`, `sections[0].table.head[1]`, `sections[0].table.head[2]`, `sections[0].takeaway`, `sections[1].body[1]` ×2, `sections[1].quiz[0].why`, `sections[1].takeaway`, `sections[2].body[3]`, `sections[2].body[4]`, `sections[2].quiz[0].why`, `sections[3].quiz[0].why`, `sections[4].body[2]`, `sections[4].quiz[0].q`, `sections[4].quiz[0].why` ×2, `sections[6].body[2]`, `mistakes[0].why`
  - `16-mandative.json` `sections[0].body[4]`: replace `「要求、建議 + that + 主詞 + (should) + 原形」` with `「要求、建議 + <em>that</em> + 主詞 + (<em>should</em>) + 原形」`
  - `11-pronoun.json` `check[3].q`: replace `點出 it 代替` with `點出 <em>it</em> 代替`
  - `11-pronoun.json` `sections[5].quiz[0].q`: replace `點出 they 代替` with `點出 <em>they</em> 代替`

### X-S17 · shouldFix (low) · Four one-line inconsistencies: App / app, 你 / 您 in a notice, filler 注意, a missing space before a name

- **Category:** Chinese conventions (small items)
- **Files:** `09-relative.json`, `12-compare.json`, `10-conditional.json`, `01-pos.json`, `14-parallel.json`, `02-skeleton.json`
- **Problem:** (a) 'App' is capitalised in 13 sections[7].ex[3].zh and written 'app' in 09 sections[2].ex[0], ex[2], ex[3], ex[4] and 12 sections[5].ex[1] (Chinese lines); use 'App'. (b) 10 sections[6].ex[0].zh is a notice to attendees and says 你; the book's other notices and letters to a reader use 您 (01, 02, 04, 08, 09, 10 sections[2].ex[2], 14, 15). (c) The chapter 5–8 review removed the filler 注意 from chapter 8 (08-S8, STYLE.md §1); the same filler remains at 01 sections[5].body[6] and 14 sections[5].body[1]. (d) 02 `check[3].why` is the only place in the book where a Latin name touches a Chinese character with no space ('就是Park 女士本人'); everywhere else the book writes '就是 Park 女士'.
- **Replacement:**
  - `09-relative.json` `sections[2].ex[0].zh`: replace `設計這個 app 的` with `設計這個 App 的`
  - `09-relative.json` `sections[2].ex[2].zh`: replace `那個 app 已經` with `那個 App 已經`
  - `09-relative.json` `sections[2].ex[3].zh`: replace `推出的 app 已經` with `推出的 App 已經`
  - `09-relative.json` `sections[2].ex[4].zh`: replace `設計這個 app 的` with `設計這個 App 的`
  - `12-compare.json` `sections[5].ex[1].zh`: replace `更新後的 app 比` with `更新後的 App 比`
  - `10-conditional.json` `sections[6].ex[0].zh`: replace `除非你在星期五前報名` with `除非您在星期五前報名`
  - `01-pos.json` `sections[5].body[6]`: replace `只能看位置。注意 <em>hard</em>` with `只能看位置。<em>hard</em>`
  - `14-parallel.json` `sections[5].body[1]`: replace `注意前半的語序：` with `前半的語序：`
  - `02-skeleton.json` `check[3].why`: replace `就是Park 女士本人` with `就是 Park 女士本人`

### 5. Names and places

### X-S18 · shouldFix (high) · Twelve surnames are used for a man in one chapter and a woman in another

- **Category:** Names (same surname, different people)
- **Files:** `03-clause.json`, `04-tense.json`, `05-voice.json`, `09-relative.json`, `11-pronoun.json`, `13-quantity.json`, `14-parallel.json`, `15-prep.json`
- **Problem:** STYLE.md says names are invented; the book also reuses surnames freely across chapters, which is fine, but the same surname with Mr. in one chapter and Ms. in another reads as one person whose sex changes. Twelve surnames do this: Novak (Ms. Novak in 10, 11, 15; Mr. Novak in 03 (six fields)); Grant (Ms. Grant in 03, 15; Mr. Grant in 09 (four fields)); Hale (Mr. Hale in 01, 10; Ms. Hale in 15 (three fields)); Lee (Mr. Lee in 07, 11, 13; Ms. Lee in 04, 15); Lin (Mr. Lin in 04, 05; Ms. Lin in 09, 14); Abe (Mr. Abe in 06, 11; Ms. Abe in 04); Diaz (Ms. Diaz in 11, 12; Mr. Diaz in 04, 05, 15); Ito (Ms. Ito in 11, 16; Mr. Ito in 15); Kato (Ms. Kato in 10; Mr. Kato in 15); Okafor (Mr. Okafor in 11; Ms. Okafor in 13); Park (Ms. Park in 02, 09; Mr. Park in 11, 14); Tan (Ms. Tan in 05; Mr. Tan in 15). The fix renames the minority side (the side with fewer fields; Kato and Okafor are 2 against 2, so the later chapter is renamed), which keeps the number of edited fields small. New surnames were checked against every name already in the book (none collides) and are plain surnames, not places or companies. Chinese lines follow the English (X-S13 convention: Latin name + 先生 / 女士, with the same spacing rule: the pairs show the exact context). Ms. Lin's two Chinese forms (林小姐 in 09, 林女士 in 14) are renamed here, so they are not in X-S13; 05 `sections[6].ex[3].zh` also loses its `<em>` here.
- **Replacement** (one group per surname; the renamed side is the one with fewer fields, later chapter on a tie):
  - **Novak** (Ms. Novak in 10, 11, 15; Mr. Novak in 03 (six fields))
    - `03-clause.json`: replace every `Mr. Novak` with `Mr. Brandt` in `sections[2].body[2]` ×2, `sections[2].ex[0].en`, `sections[2].ex[1].en`, `sections[2].ex[1].note`
    - `03-clause.json`: replace every `Novak 先生` with `Brandt 先生` in `sections[2].ex[0].zh`, `sections[2].ex[1].zh`
  - **Grant** (Ms. Grant in 03, 15; Mr. Grant in 09 (four fields))
    - `09-relative.json`: replace every `Mr. Grant` with `Mr. Lowell` in `sections[5].ex[1].en`, `sections[5].ex[2].en`
    - `09-relative.json`: replace every `Grant 先生` with `Lowell 先生` in `sections[5].ex[1].zh`, `sections[5].ex[2].zh`
  - **Hale** (Mr. Hale in 01, 10; Ms. Hale in 15 (three fields))
    - `15-prep.json`: replace every `Ms. Hale` with `Ms. Fraser` in `check[4].q`, `sections[6].ex[0].en`
    - `15-prep.json`: replace every `Hale 女士` with `Fraser 女士` in `sections[6].ex[0].zh`
  - **Lee** (Mr. Lee in 07, 11, 13; Ms. Lee in 04, 15)
    - `04-tense.json`: replace every `Ms. Lee` with `Ms. Ellis` in `check[0].q`, `check[1].q`
    - `15-prep.json`: replace every `Ms. Lee` with `Ms. Ellis` in `mistakes[3].wrong`, `mistakes[3].right`
  - **Lin** (Mr. Lin in 04, 05; Ms. Lin in 09, 14)
    - `09-relative.json`: replace every `Ms. Lin` with `Ms. Rowan` in `sections[6].body[3]`, `sections[6].ex[2].en`
    - `09-relative.json`: `林小姐` → `Rowan 女士`: `sections[6].ex[2].zh`: `林小姐` → `Rowan 女士`
    - `14-parallel.json`: replace every `Ms. Lin` with `Ms. Rowan` in `sections[0].body[2]` ×5, `sections[0].ex[0].en`
    - `14-parallel.json`: `林女士` → `Rowan 女士`: `sections[0].body[2]`: `林女士` → `Rowan 女士`; `sections[0].ex[0].zh`: `林女士` → `Rowan 女士`
  - **Abe** (Mr. Abe in 06, 11; Ms. Abe in 04)
    - `04-tense.json`: replace every `Ms. Abe` with `Ms. Jansen` in `sections[6].quiz[0].q`
  - **Diaz** (Ms. Diaz in 11, 12; Mr. Diaz in 04, 05, 15)
    - `04-tense.json`: replace every `Mr. Diaz` with `Mr. Caldwell` in `check[3].q`
    - `04-tense.json`: replace every `Diaz 先生` with `Caldwell 先生` in `check[3].options[0]`
    - `05-voice.json`: replace every `Mr. Diaz` with `Mr. Caldwell` in `sections[6].ex[3].en`
    - `05-voice.json`: replace every `<em>Diaz</em> 先生` with `Caldwell 先生` in `sections[6].ex[3].zh`
    - `15-prep.json`: replace every `Mr. Diaz` with `Mr. Caldwell` in `sections[4].body[1]`
  - **Ito** (Ms. Ito in 11, 16; Mr. Ito in 15)
    - `15-prep.json`: replace every `Mr. Ito` with `Mr. Dunmore` in `check[2].q`
  - **Kato** (Ms. Kato in 10; Mr. Kato in 15)
    - `15-prep.json`: replace every `Mr. Kato` with `Mr. Keane` in `mistakes[1].wrong`, `mistakes[1].right`
  - **Okafor** (Mr. Okafor in 11; Ms. Okafor in 13)
    - `13-quantity.json`: replace every `Ms. Okafor` with `Ms. Odell` in `sections[1].ex[1].en`
    - `13-quantity.json`: replace every `Okafor 女士` with `Odell 女士` in `sections[1].ex[1].zh`
  - **Park** (Ms. Park in 02, 09; Mr. Park in 11, 14)
    - `11-pronoun.json`: replace every `Mr. Park` with `Mr. Sandoval` in `sections[8].body[0]`, `sections[8].ex[0].en`, `mistakes[4].wrong`, `mistakes[4].right`
    - `11-pronoun.json`: replace every `Park 先生` with `Sandoval 先生` in `sections[8].body[0]` ×2, `sections[8].ex[0].zh`
    - `14-parallel.json`: replace every `Mr. Park` with `Mr. Sandoval` in `sections[2].ex[2].en`
    - `14-parallel.json`: replace every `Park 先生` with `Sandoval 先生` in `sections[2].ex[2].zh`
  - **Tan** (Ms. Tan in 05; Mr. Tan in 15)
    - `15-prep.json`: replace every `Mr. Tan` with `Mr. Voss` in `sections[4].quiz[0].q`

### X-S19 · shouldFix (medium) · Two company names are one letter apart or share a first word with another company

- **Category:** Names (companies)
- **Files:** `12-compare.json`, `04-tense.json`
- **Problem:** (a) *Kestrel Logistics* (01 sections[2].ex[0]; 06 sections[6].ex[1]) and *Kestra Logistics* (12 sections[3].quiz[0], four places) are the same word minus one letter, and both are logistics firms; a reader will take them for one company or a typo. (b) *Halden Bank* (04 mistakes[1]) and *Halden Foods* (06 sections[3].ex[1]) share the first word and appear two chapters apart. Rename the later, single-use one in each pair. Optional (c): *Delmont Foods* (05 sections[4].ex[3]) sounds very close to the real brand Del Monte Foods; if the book wants zero resemblance, rename it as shown.
- **Replacement:**
  - `12-compare.json`: replace every `Kestra Logistics` with `Tessel Logistics` in `sections[3].quiz[0].options[0]`, `sections[3].quiz[0].options[1]`, `sections[3].quiz[0].why` ×2
  - `04-tense.json`: replace every `Halden Bank` with `Tallis Bank` in `mistakes[1].wrong`, `mistakes[1].right`
- **Note:** Optional (c): in 05-voice.json `sections[4].ex[3].en` and `.zh`, replace `Delmont Foods` with `Corvane Foods`.

### X-S20 · shouldFix (low) · No real major city or well-known company appears in the chapters; one place name (Riverside) is a real mid-size city, optional

- **Category:** Places (borderline real names; optional)
- **Files:** `15-prep.json`
- **Problem:** Checked every capitalised name in all sixteen chapters. No real capital or major city remains (the chapter 5–8 review replaced Tokyo and Singapore with *Harbor City*). The place names now in use are *Harbor City*, *Westbrook*, *Eastfield*, *Dalton*, *Harlow Bay*, *Eastgate*, *Harbor Point*, *Larkfield* and *Riverside*; several of these are also the names of small real towns or districts, none that a Taiwanese reader would know, so I left them. *Riverside* is the one a reader could recognise (a California city of over 300,000) and appears four times in chapter 15 (`sections[3].ex[0]` and `ex[1]`, en and zh); optional rename shown. Company names (*Kestrel*, *Nordline*, *Northgate Logistics*, *Norvel*, *Brightline Foods*, *Halden*, *Delmont*) are generic coinages; I cannot rule out a small real firm with the same name, and no search was run. Separate from the chapters: STYLE.md §4's `tap` example sentence still says 'our Tokyo office'; STYLE.md is not a chapter, but the rule it states ('地名都虛構') is broken by its own example. Suggested STYLE.md edit: `Tokyo office` → `Westbrook office` (the answer indexes in that example do not change).
- **Replacement:**
  - `15-prep.json`: replace every `Riverside` with `Ferngate` in `sections[3].ex[0].en`, `sections[3].ex[0].zh`, `sections[3].ex[1].en`, `sections[3].ex[1].zh`

## Notes for whoever applies this

- Re-run `python3 check.py` and `python3 build.py` after applying. Both pass on a scratch copy with every replacement above applied, including the optional ones (X-M2 option B, X-S19 (c), X-S20).
- The renames in X-S18 and X-S19 change names inside `why` and `options` text as well as examples; the substring rules above already cover those fields (they are listed). Tap-question answer indexes are unaffected: no rename touches a `tap` sentence.
- Left alone because they are choices, not errors: the book uses both 星期五 and 週五 / 每週 (both are Taiwan usage); 分店 / 分公司 / 分行 for *branch* vary with context (the one doubtful case, 14 `sections[2].ex[1].zh` 分行, sits in a payment sentence and reads as a bank; 分店 would fit the rest of the book).
