# Grammar book review: chapters 5-8

Files reviewed: `chapters/05-voice.json`, `06-verbforms.json`, `07-agree.json`, `08-connect.json`.
Read first: `STYLE.md`, `chapters/02-skeleton.json`, `chapters/03-clause.json` (definitions of 有時態的動詞, 中心名詞, 片語, 子句, 主要/從屬子句, the "count the tensed verbs" rule), and the parts of chapter 4 that these chapters build on (p.p., tense names, time and conditional clauses). Chapters 13 and 16 were grepped to see what they already cover (uncountable nouns, `most of`, mandative `suggest that`).

Method: every English sentence, Chinese translation, `<u>` mark, quiz option and `why` was read; every `tap` item was split on spaces and the index list checked (8 tap items in total); `python3 check.py` passes for all four files (no format errors). No chapter file was edited.

How to read this file:
- Field paths are relative to the chapter file and 0-based exactly as in the JSON (so "section 3" in prose is `sections[2]`).
- **mustFix** = wrong, misleading, mistranslated, or a topic the review brief names that the book does not teach anywhere. **shouldFix** = teaching gap, unnatural wording, forward reference, or polish.
- Replacement text is given in the same markup as the JSON (`<em>`, `<b>`, `<u>`). Chinese uses 「」, so no double quotes need escaping inside JSON strings. "Replace X with Y" on a substring means a find-and-replace inside that field; "Replace the whole value" means the full string.
- Format limits from `check.py` and STYLE.md still apply after the fixes: `sections` 4-9, `ex` 1-5 per section, section quizzes 4-10 per chapter, `check` 3-5. Where a fix would break a limit I say so. 08 is already at the maximum for sections (9) and quizzes (10); sections[2], [3], [4], [5] there already have 5 examples.

## Summary

| File | mustFix | shouldFix | Verdict in one line |
|---|---|---|---|
| 05-voice | 0 | 9 | Accurate and slowly paced; only polish, one missing form (to be + p.p.), and one STYLE item (real place name) |
| 06-verbforms | 2 | 9 | Good structure; the -ing/-ed rule ("not time, only active/passive") is wrong for intransitive -ed, and `be used to` + base form is missing |
| 07-agree | 2 | 5 | Rules are correct; one mistranslation (兩位董事會), and collective nouns are not taught anywhere in the book |
| 08-connect | 2 | 10 | The framework is sound and every example is correct; two over-strong statements (so vs so that, `Even the store was busy`) and a reduced-clause paragraph that needs restructuring |

Verified as correct (no change needed):
- All 8 `tap` answers: 05 check[2] = [3,4,5]; 05 sections[3].quiz[1] = [2,3,4]; 06 sections[0].quiz[0] = [2]; 06 sections[6].quiz[1] = [4,5,6]; 07 check[4] = [1]; 07 sections[1].quiz[0] = [1]; 07 sections[4].quiz[0] = [4]; 08 sections[0].quiz[0] = [3]. None has a second reasonable selection.
- All `choose` items have exactly one correct option in both British and American formal written English (including `Each of the meeting rooms has`, `Neither the contract nor the invoices were`, `A number of customers have`).
- All example sentences are grammatical and natural; all `<u>` marks are on the intended words; all `mistakes` pairs are the same sentence in two versions.
- Cross-references between sections and chapters point to the right places (e.g. 05 sections[0] "第 6 節" = `sections[5]`; 08 sections[6] "第 3 節" = `sections[2]`).
- No banned phrases, no invented test claims, a takeaway in every section, term usage (子句, 片語, 連接詞, 介系詞, 連接副詞, to V, Ving, p.p., 原形, 時態) consistent with STYLE.md and chapters 2-4.

Cross-cutting items that appear in every chapter file (each is listed again under its file):
1. **Real place names** (Kaohsiung, Tainan, Osaka, Hsinchu, Tokyo, Singapore) break STYLE.md §1 "人名、公司名、地名都虛構"; chapters 1-3 use only invented places (Eastfield, Harbor City, Westbrook, Dalton). If the owner prefers real Asian cities, change the STYLE rule instead; either way it should be one decision.
2. **Answer-position pattern.** In 05, 6 of the 8 three-option items have the answer in the middle slot (index 1); in 08, 8 of 14 `choose` answers are index 1. A test-wise reader can guess. Concrete reorderings are given at the end of each file's section (05-S9, 06-S9, 08-S10). 07 is balanced (5 / 5).

---

## 05-voice.json

No mustFix items.

### 05-S1 [shouldFix] Tense labels differ from chapter 4's names
- Where: `sections[3].table.rows[0..5][0]`
- Problem: Chapter 4 (`sections[0].body[0]`) says the simple row is "直接叫現在式、過去式、未來式，這本書也這樣叫", and 05 itself says 現在完成式 elsewhere. The table uses 現在簡單 / 過去簡單 / 未來 / 現在進行 / 現在完成 / 過去完成, which are names the reader has not met.
- Replace the first cell of each row:
  - rows[0]: `現在簡單` -> `現在式`
  - rows[1]: `過去簡單` -> `過去式`
  - rows[2]: `未來` -> `未來式`
  - rows[3]: `現在進行` -> `現在進行式`
  - rows[4]: `現在完成` -> `現在完成式`
  - rows[5]: `過去完成` -> `過去完成式`

### 05-S2 [shouldFix] Passive after `to` (to be + p.p.) is missing
- Where: `sections[3].body[3]` and `sections[3].table.rows`
- Problem: The chapter teaches `be` + p.p. after modals but never after `to`, which is the common business form (`is expected to be completed`, `needs to be signed`). Chapter 6 does not cover it either. The learner will see `to be checked` and have no rule for it.
- Replace `sections[3].body[3]` (whole value) with:
```
<em>will、can、must、should</em> 和 to V 的 <em>to</em> 後面一律接原形，所以 <em>be</em> 保持原形：<em>will be checked</em>、<em>must be checked</em>、<em>needs to be checked</em>。
```
- Append one row to `sections[3].table.rows` (the table can take more rows; `ex` is not affected):
```
["加 <em>to</em>", "<em>The team needs to check the invoice.</em>", "<em>The invoice needs to be checked.</em>"]
```

### 05-S3 [shouldFix] Table says the object is always gone in the passive
- Where: `sections[0].table.rows[3][2]`
- Problem: "已經搬去當主詞，動詞後面沒有了" is absolute; `sections[6]` later shows that give/offer/award keep one object (`Ms. Wu was offered the position`). The reader meets a rule, then a counter-example, with no pointer.
- Replace the whole value with:
```
已經搬去當主詞，動詞後面通常沒有了（<em>give、offer</em> 這類有兩個受詞的動詞，見第 7 節）
```

### 05-S4 [shouldFix] "時態由它決定" is imprecise for has been / will be
- Where: `sections[1].body[0]`
- Problem: Check[2] and `sections[3]` show `has been installed` and `will be introduced`, where the tense is carried by `has` / `will` plus the shape of `be`. "時態由它決定" (it = be) is only half true and the reader meets `has been` before it is explained.
- Replace the whole value with:
```
被動的動詞一定由兩個零件組成：<em>be</em> 和 p.p.（過去分詞）。<em>be</em> 可以是 <em>is、are、was、were、be、been、being</em> 任何一個樣子，時態靠它的形狀標出來（完成式、未來式前面還會多一個 <em>has</em>、<em>will</em> 這類助動詞，第 4 節會講）；p.p. 是 <em>approved、sent、written</em> 這種形式。
```

### 05-S5 [shouldFix] Four small wording fixes
- `sections[1].body[1]`: replace the substring `意思是樣品正在寄東西給客戶，說不通` with `意思是樣品當時正在寄東西給客戶，說不通`. (Past progressive: 「當時」.)
- `sections[1].ex[2].zh`: replace `所有發票都在 30 天內付款。` with `所有發票都會在 30 天內付清。`
- `check[2].why`: replace the substring `<em>been</em> 是 <em>be</em> 的完成式樣子` with `<em>been</em> 是 <em>be</em> 的 p.p.（完成式要用這個樣子）`.
- `sections[0].ex[2].zh`: replace `預算在星期一核准了。` with `預算在星期一獲得核准。`

### 05-S6 [shouldFix] Forward reference to `must be submitted`
- Where: `sections[2].ex[2].note`
- Problem: `must be submitted` appears in section 3, but `must` + `be` + p.p. is only taught in section 4.
- Replace the whole value with:
```
<em>by Friday</em> 是期限，不是做動作的人。判斷被動靠的是：表格不會自己繳交。<em>must be submitted</em> 裡的 <em>must be</em>，第 4 節會講。
```

### 05-S7 [shouldFix] Converse of "no object, no passive" is not stated
- Where: `sections[5].body[5]` (append a sentence at the end)
- Problem: The chapter says verbs without an object have no passive. A reader may infer that every verb with an object has one. A few state verbs do not (`The hotel has 120 rooms.`, `cost`, `resemble`).
- Append to `sections[5].body[5]`:
```
 反過來，後面有受詞也不保證有被動：表示擁有或狀態的 <em>have</em>（<em>The hotel has 120 rooms.</em>）、<em>cost</em>、<em>resemble</em> 通常不用被動。這類字不多，不確定時用主動。
```

### 05-S8 [shouldFix] Real place name
- Where: `sections[1].ex[1].en` and `.zh`
- Replace `en` with: `The annual meeting <u>is held</u> in Harbor City every June.`
- Replace `zh` with: `年會每年六月在海港市舉行。`

### 05-S9 [shouldFix] Answer positions: 6 of 8 three-option items have the answer in the middle
- Where: the `choose` items below. `why` texts refer to options by content, not by position, so reordering is safe.
- Reorder `options` and set `answer`:

| Path | New `options` | `answer` |
|---|---|---|
| `check[0]` | `["signed", "was signing", "was signed"]` | 2 |
| `sections[1].quiz[0]` | `["is prepared", "prepares", "is preparing"]` | 0 |
| `sections[2].quiz[0]` | `["The system sends a reminder every Monday.", "Mr. Kuo sent the reminders on Monday.", "The reminders are sent every Monday."]` | 2 |
| `sections[5].quiz[0]` | `["The meeting was taken place in Room 4.", "The meeting was took place in Room 4.", "The meeting took place in Room 4."]` | 2 |
| `sections[6].quiz[0]` | `["was given", "gave", "has given"]` | 0 |

### Verdict: 05-voice
The chapter is accurate and teaches at the right speed: the one threshold that matters (the passive subject is the active object) gets its own paragraph and is reused in section 6 (no object, no passive) and section 7 (two objects). `was sending` / `was sent` and `being` / `been` are both treated as separate thresholds with a contrast and a test. I found no grammar error, no mistranslation and no quiz with more or fewer than one correct answer; the `tap` items have a single clean selection. What remains is polish: use chapter 4's tense names in the table (05-S1), add `to be` + p.p. because it is the form business text uses most (05-S2), soften two absolute statements (05-S3, 05-S4), and replace the one real city name (05-S8). Ready to ship after those.

---

## 06-verbforms.json

### 06-M1 [mustFix] "分詞本身不表示時間 ... 只看主動被動" is misleading and the rule fails for -ed of intransitive verbs
- Where: `sections[5].body[2]` and `sections[5].takeaway`
- Problem: (a) The paragraph says `the attached file` is not 「已經附上」. The ordinary reading of `attached` is exactly that the file has been attached; the sentence denies what the reader sees. (b) The rule "名詞自己做用 -ing，被做用 -ed，只看主動被動" has no place for -ed on an intransitive verb, which is active and completed: `increased demand`, `a retired manager`, `fallen leaves`. A learner who has just been told "名詞自己做就用 -ing" will reject `increased demand` and will not know that `increased` and `increasing` are both correct with different meanings (已經增加 vs 正在增加). This is the same intransitive / transitive split that chapter 5 teaches, so the fix is short.
- Replace `sections[5].body[2]` (whole value) with:
```
分詞不像有時態的動詞那樣標出過去、現在、未來。<em>the attached file</em> 不會因為「明天才附」就換個樣子，它只表示檔案和「附上」之間是被動的關係。所以選 <em>-ing</em> 還是 <em>-ed</em>，先問主動還是被動，不問時間。只有一類要多想一步：不及物動詞（第 5 章）沒有被動，它們的 <em>-ed</em> 放在名詞前面，意思是「已經……了」，是名詞自己做完了這個動作：<em>increased demand</em>（需求已經增加了）、<em>a retired manager</em>（已經退休的經理）。同一個動詞的 <em>-ing</em> 是「正在……」：<em>rising prices</em>（正在上漲的價格）。這類字不多，遇到時兩種形式都可能是對的，意思不同。
```
- Replace `sections[5].takeaway` (whole value) with:
```
名詞自己正在做，用 <em>-ing</em>；被做，用 <em>-ed</em>；感覺的字，讓人有感覺的事物用 <em>-ing</em>，有感覺的人用 <em>-ed</em>。
```

### 06-M2 [mustFix] `be used to` + base form ("被用來做") is missing and the text implies it is wrong
- Where: `sections[3].body[3]`, `sections[3].body[4]`, `sections[3].ex`
- Problem: The section lists `be used to` among the phrases whose `to` is a preposition and ends with "只差一個 be，to 的身分就不同". But `be used to` + base form is a very common business pattern with a different meaning: `This tool is used to measure humidity.` (`used` is the p.p. of `use`; `to measure` is a purpose to V). A reader who trusts the section will mark `is used to track` as an error. The section needs the contrast, with the test of who the subject is.
- Replace `sections[3].body[3]` (whole value; the list sits inside one `<em>`) with:
```
這樣的片語有：<em>look forward to、be committed to、be dedicated to、be used to</em>（習慣於）<em>、be accustomed to、contribute to、object to、in addition to</em>。
```
- Replace `sections[3].body[4]` (whole value) with:
```
要特別分清楚的一組：<em>used to</em> + 原形，是「以前曾經」，現在不再這樣；<em>be used to</em> + Ving，是「習慣於」。只差一個 <em>be</em>，<em>to</em> 的身分就不同。另外還有一種 <em>be used to</em> 後面接原形，意思是「被用來做」：<em>This tool is used to measure humidity.</em> 這裡的 <em>used</em> 是 <em>use</em> 的 p.p.（第 5 章的被動），<em>to measure</em> 是「用來做什麼」的 to V。分辨方法：主詞是人，通常是「習慣於」，後面接 Ving；主詞是工具、系統、方法，通常是「被用來」，後面接原形。
```
- Add one example to `sections[3].ex` (it has 4, so 5 is the maximum):
```json
{"en": "This software <u>is used to track</u> shipments.", "zh": "這套軟體是用來追蹤貨物的。", "note": "主詞是軟體，不是人。這個 <em>is used to</em> 是「被用來做」，後面接原形；和 <em>is used to handling</em>（習慣於）不同。"}
```

### 06-S1 [shouldFix] Passive of `make` (be made to) is missing
- Where: `sections[4]` (new paragraph after `body[3]`, plus one table row)
- Problem: Section 2 teaches that the passive keeps `to` (`was asked to`), and section 5 teaches `make` + 人 + 原形. The step in between, `We were made to redo the slides` (the bare infinitive gets its `to` back), is not taught, so a learner will write `were made redo`. `let` and `have` (人 + 原形) have no such passive; `be allowed to` is the way to say it.
- Insert as new `sections[4].body[4]`:
```
<em>make</em> 變成被動時，<em>to</em> 會跑出來：<em>The director made us redo the sales forecast.</em> 的被動是 <em>We were made to redo the sales forecast.</em>，和 <em>ask → be asked to</em> 同一個道理（第 2 節）。<em>let</em> 和 <em>have</em>（人 + 原形）沒有這樣的被動；要說「被允許」，用 <em>be allowed to</em>。
```
- Append to `sections[4].table.rows`:
```json
["<em>make</em>（被動）", "<em>be made</em> + to V", "<em>We were made to redo the slides.</em>"]
```
- `sections[4].ex` already has 5 examples; do not add one. (The old `body[4]`, the `have` + 東西 + p.p. paragraph, becomes `body[5]`.)

### 06-S2 [shouldFix] be + Ving can be a progressive or an adjective
- Where: `sections[5].body[0]` and a new paragraph after it
- Problem: (a) "Ving 和 p.p. 除了放在動詞後面" lumps the Ving after `consider` / `finish` (which the book never names) with participles. (b) `The results were surprising.` looks like the past progressive the reader learned in chapter 4 and in 05 (`was sending`). The section never says why it is an adjective.
- Replace `sections[5].body[0]` (whole value) with:
```
Ving 和 p.p. 也可以放在名詞前面或 <em>be</em> 後面，當形容詞用。這時它們叫<b>分詞</b>：Ving 是現在分詞，p.p. 是過去分詞。
```
- Insert as new `sections[5].body[1]` (everything after shifts by one):
```
<em>be</em> 後面接 Ving，有時是進行式（第 4 章），有時是形容詞。<em>The results were surprising.</em> 的 <em>surprising</em> 是形容詞：前面放得進 <em>very</em>（<em>very surprising</em>），意思是「令人意外的」，不是「正在使人意外」。
```

### 06-S3 [shouldFix] Verb lists are thin; `suggest` rule is stated too narrowly
- Where: `sections[1].body[2]` (new paragraph after it) and `sections[1].body[3]`
- Problem: The chapter's whole job is "which verb takes what", yet `want`, `need`, `manage`, `afford`, `fail`, `promise`, `admit`, `deny`, `mind`, `delay`, `involve` are absent. Also `suggest` "只接 Ving（或 that 子句）" leaves out `suggest` + noun, and the last sentence about "一眼就看得出來" is a claim about readers.
- Insert as new `sections[1].body[3]`:
```
上面是代表，不是全部。接 to V 的還有 <em>want、need、intend、manage、afford、fail、promise、prepare、arrange</em>；接 Ving 的還有 <em>admit、deny、mind、delay、risk、imagine、involve、quit</em>。
```
- In the old `body[3]` (now `body[4]`), replace the substring `但 <em>suggest</em> 只接 Ving（或 that 子句，第 16 章）。這種錯不會讓人看不懂，卻是一眼就看得出來的文法錯誤。` with `但 <em>suggest</em> 後面不接 to V，要接 Ving（或名詞、that 子句，第 16 章）。這種錯不會讓人看不懂，但在正式的商業文件裡是明顯的文法錯誤。`

### 06-S4 [shouldFix] Two over-broad statements about the second verb
- Where: `sections[0].body[2]` and `sections[0].takeaway`
- Problem: (a) "to 後面只能接原形" is said before the reader learns in section 4 that some `to` is a preposition. (b) The takeaway "其他動詞都要換成 to V、Ving 或原形" ignores `and` (chapter 2: `approved the budget and sent it`) and clauses.
- Replace the substring `<em>to</em> 後面只能接原形` in `sections[0].body[2]` with `to V 的 <em>to</em> 後面只能接原形`.
- Replace `sections[0].takeaway` (whole value) with:
```
一個子句只有一個有時態的動詞；第二個動作如果沒有用 <em>and</em> 或連接詞接進來，就要換成 to V、Ving 或原形。
```

### 06-S5 [shouldFix] Same Chinese for two different sentences
- Where: `sections[4].ex[2].zh` and `sections[4].ex[3].zh`
- Problem: Both read 「阿部先生請助理訂了一張六人桌。」 The `note` says the English differs; the Chinese should show it. `asked ... to book` does not say the booking was done.
- Replace `sections[4].ex[2].zh` with: `阿部先生交代助理訂了一張六人桌。`
- Replace `sections[4].ex[3].zh` with: `阿部先生請助理訂一張六人桌。`

### 06-S6 [shouldFix] Lead undersells the last section
- Where: `lead`
- Replace the substring `最後兩節講 Ving 和 p.p. 當形容詞用時怎麼選。` with `最後兩節講 Ving 和 p.p. 當形容詞用時怎麼選，以及放在句首的分詞片語。`

### 06-S7 [shouldFix] 「被設在那裡」 is not natural Chinese for `located`
- Where: `check[4].why` and `mistakes[4].why`
- Replace the substring `飯店是被設在那裡，所以用 p.p.。` in `check[4].why` with `飯店「位於」那裡，英文把它看成被安置在那裡的一方，所以用 p.p.。`
- Replace the substring `飯店是被設在那裡，用 p.p.。` in `mistakes[4].why` with `飯店是被安置在那裡（也就是位於那裡），用 p.p.。`

### 06-S8 [shouldFix] Real place names
- `check[0].q`: replace `in Tainan` with `in Eastfield`.
- `sections[3].ex[3].en`: replace `our Osaka branch` with `our Dalton branch`; `sections[3].ex[3].zh`: replace `我們的大阪分公司` with `我們的 Dalton 分公司`.

### 06-S9 [shouldFix] Answer positions (two-option items: 5 of 7 have index 1)
- Mild, but easy: reorder `check[4]` to `["Located", "Locating"]` with `answer` 0, and `sections[3].quiz[0]` to `["providing", "provide"]` with `answer` 0.

### Verdict: 06-verbforms
The chapter's architecture is right: it starts by showing why the second verb must lose its tense (building on chapter 2), then gives one section per rule with a concrete threshold (to as a preposition with a noun test, make/let/have vs allow/ask/get, restore-to-a-sentence for sentence-initial participles) and a dangling-participle example that shows the meaning breaking. The `look forward to`, `let us leave`, `suggest hiring`, `bored` and `Located near` explanations are all correct, and the tap on `Designed for small offices` has one clean selection. Two things must change before release: the -ing/-ed paragraph teaches a rule ("只看主動被動，不看時間") that fails for intransitive -ed and contradicts how `attached` actually reads (06-M1), and the `to` section implies `be used to` always takes Ving, which will make the learner distrust the very common `is used to` + base form (06-M2). The remaining items add the passive of `make`, a few more verbs for the lists, and polish. With those fixes the chapter is ready.

---

## 07-agree.json

### 07-M1 [mustFix] Mistranslation: 「兩位董事會」
- Where: `sections[5].ex[3].zh`
- Problem: `two board members` is 兩位董事; 董事會 is the board as a body. 「兩位董事會」 is also not Chinese. `along with` / `as well as` is 連同, which is the whole point of the contrast with `and`; and `is attending the opening` reads as 「將出席開幕式」.
- Replace the whole value with:
```
執行長連同兩位董事，將出席開幕式。
```

### 07-M2 [mustFix] Collective nouns (and nouns whose shape misleads) are not taught anywhere in the book
- Where: new section inserted as `sections[6]` (before the Ving section, which becomes `sections[7]`; the chapter then has 8 sections)
- Problem: The review brief lists collective nouns as an agreement rule; `team`, `committee`, `department`, `company`, `board` as subjects, and `news` / `information` / `equipment`, are among the most common agreement traps in business writing. A grep of all 16 chapters finds no coverage of collective nouns; chapter 13 only says that uncountable nouns take a singular verb, without ever attaching it to agreement practice. The chapter's own lead says "難的是找到真正的主詞", but here the subject is found and the learner still cannot decide singular or plural.
- Dialect note: American usage treats collective nouns as singular; British usage may use plural when the members are in focus. The text and quizzes therefore teach the singular, which is acceptable in both, and the quiz uses `its` so only `has` is possible in both varieties.
- Insert as new `sections[6]` (JSON checked to parse; passes the tag, balance and banned-phrase checks):
```json
{
  "h": "團體、news、information：形狀和單複數不一定對得上",
  "body": [
    "前面都是先找主詞，再數它是一個還是好幾個。有幾類名詞，形狀會騙人。",
    "<b>集合名詞</b>是一個單數的字，指一群人：<em>team、committee、department、company、board</em>。把這群人當成一個團體來講時，動詞用單數：<em>The committee has approved the plan.</em> 英式英文有時把重點放在一個個成員身上，改用複數（<em>The committee have …</em>）；正式書面和商業文件用單數，英式、美式都能接受，本書的題目也以單數為準。",
    "<b>字尾有 -s 的單數名詞</b>：<em>news</em> 看起來像複數，其實是單數名詞，動詞用 <em>is</em>：<em>The news is encouraging.</em>",
    "<b>不可數名詞</b>（第 13 章）：<em>information、equipment、advice、furniture</em> 沒有複數形，當主詞時用單數：<em>The information on the website is out of date.</em> 中文的「資訊」「設備」常常指好幾樣東西，所以特別容易順手寫成 <em>are</em>。",
    "反過來，<em>people</em> 和 <em>police</em> 沒有 -s，講的卻是好幾個人，用複數：<em>The police are investigating the theft.</em>"
  ],
  "ex": [
    {"en": "The marketing <u>department</u> <u>has</u> moved to the fourth floor.", "zh": "行銷部已經搬到四樓了。", "note": "<em>department</em> 是一個單位，當成一個團體，用單數。"},
    {"en": "The <u>news</u> from our Eastfield office <u>is</u> encouraging.", "zh": "我們 Eastfield 辦公室傳來的消息令人振奮。", "note": "<em>news</em> 是單數名詞；<em>from our Eastfield office</em> 劃掉。"},
    {"en": "The <u>information</u> on the website <u>is</u> updated every Monday.", "zh": "網站上的資訊每週一更新。", "note": "<em>information</em> 不可數，沒有複數形，用單數。"}
  ],
  "quiz": [
    {"type": "choose", "q": "<em>The information on our website ___ updated every Monday.</em> 空格要填哪一個？", "options": ["is", "are"], "answer": 0, "why": "<em>information</em> 是不可數名詞，沒有複數形，當主詞用單數 <em>is</em>。<em>on our website</em> 是介系詞片語，劃掉。中文的「資訊」可以指很多東西，但英文只看這個字的形狀和類別。"},
    {"type": "choose", "q": "<em>The committee ___ announced its decision.</em> 空格要填哪一個？", "options": ["has", "have"], "answer": 0, "why": "<em>committee</em> 是集合名詞，這裡當成一個團體；後面的 <em>its</em> 也是單數，所以用 <em>has</em>。"}
  ],
  "takeaway": "名詞的形狀不一定等於單複數：一個團體、<em>news</em>、不可數名詞用單數；<em>people</em>、<em>police</em> 用複數。"
}
```
- This brings the section quizzes to 10 (the maximum). The cross-reference in 07-S1 below ("見第 7 節") refers to this section.

### 07-S1 [shouldFix] "兩邊都有 -s，就錯了" is absolute
- Where: `sections[0].body[2]`
- Problem: The rule about -s on the noun vs -s on the verb is correct for ordinary plurals, but `The news requires ...` has -s on both sides and is correct. A reader who memorizes "兩邊都有 -s 就錯" will later doubt `news`.
- Replace the substring `寫成 <em>The clients requires</em>，兩邊都有 <em>-s</em>，就錯了。` with `寫成 <em>The clients requires</em>，名詞已經是複數，動詞又加了代表單數的 <em>-s</em>，就錯了。（<em>news</em> 這類本身是單數的字，見第 7 節。）`

### 07-S2 [shouldFix] `either of`, `neither of`, and -one / -body words are missing from the "一個" section
- Where: `sections[2]` (heading, new `body[3]`, table row, one example, takeaway)
- Problem: `Neither of the printers is working` and `Everyone has received ...` are the same pattern as `each of` and are among the commonest agreement items; the chapter teaches `neither ... nor` but not `neither of`.
- Replace `sections[2].h` with: `each、every、one of、either of：都是「一個」`
- Insert as new `sections[2].body[3]`:
```
<em>either of</em>、<em>neither of</em> 和 <em>each of</em> 一樣，主詞是 <em>either</em>、<em>neither</em>，動詞用單數：<em>Either of the two dates is fine with me.</em> 字尾是 <em>-one</em>、<em>-body</em> 的字也是「一個一個看」：<em>everyone、everybody、someone、anyone、no one</em>，動詞用單數：<em>Everyone has received the new schedule.</em>
```
- Append to `sections[2].table.rows`:
```json
["<em>either of / neither of the</em>", "複數（<em>either of the dates</em>）", "單數"]
```
- Append to `sections[2].ex` (3 -> 4):
```json
{"en": "<u>Either</u> of the two dates <u>is</u> fine with me.", "zh": "這兩個日期我都可以。", "note": "主詞是 <em>either</em>（兩個裡面任何一個），劃掉 <em>of the two dates</em>，動詞用單數。"}
```
- Replace `sections[2].takeaway` with:
```
<em>each、every、one of、either of、neither of</em> 講的都是「一個」，動詞用單數；<em>one of</em> 後面的名詞卻要用複數。
```

### 07-S3 [shouldFix] The `most of` exception sits in the wrong section
- Where: `sections[3].body[4]`, `sections[3].ex[2]`, `sections[3].ex[3]`; receiving paragraph in `sections[1]`
- Problem: `sections[3]` is about `the number of` / `a number of`. The `most of / some of / all of / half of` paragraph and its two examples are an exception to the 劃掉-the-of-phrase method taught in `sections[1]`, and STYLE.md says each section answers one question. It also makes the reader meet "動詞要看 of 後面的名詞" before `a number of`, which is a different logic.
- Delete `sections[3].body[4]`, `sections[3].ex[2]`, `sections[3].ex[3]` (the section keeps 2 examples).
- Append as new `sections[1].body[5]` (the section already has 4 examples; the two sentences are inline, so no example is added):
```
「劃掉 <em>of</em> 片語」有一個例外：前面是數量的時候，像 <em>most of、some of、all of、half of</em>，動詞要看 <em>of</em> 後面的名詞。<em>Most of the budget has been spent.</em>（預算，一筆，用單數）；<em>Most of the rooms have been booked.</em>（房間，好幾間，用複數）。這類數量詞在第 13 章細講。
```

### 07-S4 [shouldFix] 「和」 hides the point of `along with`
- Where: `sections[1].ex[3].zh`
- Replace `陳女士和她的兩位助理正在參加商展。` with `陳女士連同她的兩位助理，正在參加商展。`

### 07-S5 [shouldFix] Real place names
- `sections[0].quiz[0].options[2]`: replace `The manager is in Tokyo this week.` with `The manager is in Eastfield this week.`
- `sections[5].ex[0].en`: replace `in Hsinchu` with `in Westbrook`; `sections[5].ex[0].zh`: replace `新竹` with `Westbrook`.

### Verdict: 07-agree
The rules that are taught are correct and are taught the right way round: the chapter opens with where agreement is visible at all (so the learner knows when to worry), builds the 劃掉 method on chapter 2's 中心名詞, and gives each of `each of`, `one of`, `the number of`, `there are`, `neither ... nor` and Ving subjects its own threshold with a one-line test; the tap items select exactly one word and the `a number of` vs `the number of` test (swap in `many`) is a good method. The `neither ... nor` proximity rule and the `as well as` contrast with `and` are accurate. One item must be fixed outright: the translation 「兩位董事會」 (07-M1). The other must-fix is a gap, not an error: collective nouns, `news`, and the uncountable `information` / `equipment` are not covered here or in chapter 13 in agreement terms (07-M2); the ready-to-paste section brings the chapter to 8 sections and 10 quizzes. The rest is placement and polish (the `most of` exception, `either of`, one absolute statement, place names). Ready after these.

---

## 08-connect.json

### 08-M1 [mustFix] "只有 so、沒有 that，是結果，不是目的" is false as a general rule
- Where: `sections[6].ex[3].note`, `sections[6].body[4]`, `sections[6].takeaway`
- Problem: Purpose `so` without `that` is ordinary in business and everyday writing: `Please arrive early so we can start on time.` `We left early so we could catch the train.` The note and takeaway state the opposite as a rule ("只有 so 是「所以」"). The reader who trusts this will misparse `so you can ...` as a result. The reliable cues are the comma before `so` and what follows: a result `so` has a comma and a fact that already happened; a purpose `so` has no comma and a clause with can / could / will / would.
- Replace `sections[6].ex[3].note` (whole value) with:
```
<em>so</em> 前面有逗號，後面是已經發生的事（搭了計程車），是結果，不是目的。
```
- Replace `sections[6].body[4]` (whole value) with:
```
還要分清楚 <em>so that</em> 和 <em>so</em>。<em>so that</em> 是目的（為了），<em>so</em> 是結果（所以，第 3 節）。<em>We left early so that we could catch the train.</em> 是為了趕上火車才早走，有沒有趕上不知道；<em>We left early, so we caught the train.</em> 是早走了，結果趕上了。口語和一般書信裡，目的的 <em>so that</em> 常把 <em>that</em> 省掉：<em>We left early so we could catch the train.</em> 這時看兩個線索：結果的 <em>so</em> 前面有逗號，後面是已經發生的事；目的的 <em>so</em> 前面通常沒有逗號，後面的子句帶 <em>can、could、will、would</em>。
```
- Replace `sections[6].takeaway` (whole value) with:
```
目的：<em>so that</em> 接子句，可以換主詞；<em>in order to</em> 接原形；前面有逗號、後面是已經發生的事的 <em>so</em> 才是「所以」。
```

### 08-M2 [mustFix] `Even the store was busy, ...` 不成立 is not true
- Where: `sections[3].body[3]`
- Problem: `Even the store was busy` is a grammatical clause meaning 「連商店都很忙」 (`even` is a focus adverb here). It fails as a concessive 「儘管商店很忙」, not as English. Calling it 「不成立」 will be contradicted the first time the reader meets `Even the CEO was surprised`. State what it means instead.
- Replace `sections[3].body[3]` (whole value) with:
```
兩個小地方：<em>in spite of</em> 有 <em>of</em>，<em>despite</em> 沒有，<em>despite of</em> 是錯的。<em>even</em> 單獨不是「儘管」的連接詞：<em>Even the store was busy, …</em> 會被讀成「連商店都很忙」，不是「儘管商店很忙」。要表示讓步，要說 <em>Even though the store was busy, …</em>。
```

### 08-S1 [shouldFix, high] The shortened-clause paragraph needs restructuring; it contradicts the chapter's own test as written
- Where: `sections[4].body[4]` and `sections[4].body[5]` (replace both with the three paragraphs below, in this order); then update the table and takeaway in 08-S5
- Problem: (a) `while driving` is introduced as a clause, but it has no tensed verb and no subject, so chapter 3's and this chapter's own test ("找有時態的動詞") would call it a phrase and demand a preposition. The paragraph says "其實這是子句的縮短" but never says that this is the one place where the test fails, or how to tell it apart from `after signing` (a preposition + Ving, chapter 3). (b) The paragraph packs five ideas into one block. (c) "兩個主詞不同就不能縮" is right for ordinary clauses but business text is full of the fixed exceptions `if necessary`, `when possible`, `unless otherwise stated` (the omitted subject is `it`). (d) The `before / after / until / since` paragraph should come first, so that the exception can refer to it. This is the "shortened adverbial clauses" topic in the brief.
- New `sections[4].body[4]`:
```
再看 <em>before、after、until、since</em>：它們<b>兩種身分都有</b>。<em>after the meeting</em> 是介系詞 + 名詞；<em>after the meeting ended</em> 是連接詞 + 子句（<em>ended</em> 是有時態的動詞）。這幾個字正好說明本章的原則：判斷時看後面接什麼，不是看這個字本身。
```
- New `sections[4].body[5]`:
```
有一個寫法看起來像例外：<em>Please do not use your phone while driving.</em> <em>while</em> 後面直接接 Ving，好像變成了介系詞。其實這是子句的縮短：從屬子句的主詞和主要子句的主詞是同一個時，可以把主詞和 <em>be</em> 一起拿掉。<em>while you are driving</em> 縮成 <em>while driving</em>，<em>while</em> 還是連接詞，只是後面的子句變短了。這是「找有時態的動詞」這個測試會失靈的地方：縮短以後，裡面找不到有時態的動詞，看起來像片語。分辨的方法看帶頭的字：<em>after、before</em> 本來就有介系詞的身分，接 Ving 照上一段處理（<em>after signing</em>）；<em>while、when、once</em> 沒有介系詞的身分，後面接 Ving 或 p.p.，就是縮短的子句。
```
- New `sections[4].body[6]`:
```
<em>when、once</em> 也常這樣縮：<em>When filling out the form, …</em>、<em>Once approved, …</em>。第 6 章最後一節的分詞片語，前面加上這些字，就是這種寫法；選 Ving 還是 p.p.，一樣把它還原成完整的子句，看主詞是做還是被做。兩個主詞不同就不能縮：<em>While driving, the phone rang.</em> 變成「電話在開車」。少數固定說法是例外，被省略的主詞是沒有實際意思的 <em>it</em>，已經當成慣用語：<em>if necessary、when possible、unless otherwise stated</em>。
```

### 08-S2 [shouldFix] No quiz item tests the shortened clause; add one, remove an overlapping one
- Where: `sections[0].quiz[1]` (remove) and `sections[4].quiz` (add)
- Problem: The chapter is at the 10-quiz cap, so a new item has to replace one. `sections[0].quiz[1]` ("___ the late delivery ... 空格後面接的是什麼？") repeats what `check[0]` and `sections[0].quiz[0]` already test; it is the one to drop.
- Delete `sections[0].quiz[1]`.
- Append to `sections[4].quiz` (checked: one correct option; `meanwhile working` is a linking adverb with no clause to follow, `while worked` has `work` as an object-less p.p.):
```json
{"type": "choose", "q": "<em>Please wear a helmet ___ on the construction site.</em> 空格要填哪一個？", "options": ["while worked", "while working", "meanwhile working"], "answer": 1, "why": "戴安全帽的是 <em>you</em>，<em>you</em> 也是做 <em>work</em> 這個動作的人，所以還原成 <em>while you are working</em>，主動，用 Ving，<em>while</em> 是連接詞，後面的子句縮短了。<em>worked</em> 是 p.p.，表示被做，不合。<em>meanwhile</em> 是連接副詞，要開新句子，不能接在句中。"}
```

### 08-S3 [shouldFix, high] `as a result` vs `as a result of`, and `due to` + Ving
- Where: `sections[2].body` (new paragraph after `body[4]`), `sections[2].body[4]`, `sections[2].table.rows[0][2]`
- Problem: `as a result` (連接副詞, 後面是結果) and `as a result of` (介系詞, 後面是原因) differ by one `of` and have opposite direction, the same trap as `in addition` / `in addition to` which the chapter does cover (section 9). It is also the pair most likely to be mixed up with `because of` under time pressure. In `body[4]`, "due to 後面也只能接名詞" is inconsistent with the chapter's own rule that a preposition takes a noun or Ving (`due to being late` is fine).
- Insert as new `sections[2].body[5]` (the old `body[5]`, the `since` paragraph, becomes `body[6]`; `ex` is at its 5-example maximum, so no example is added):
```
<em>as a result</em> 和 <em>as a result of</em> 只差一個 <em>of</em>，方向卻相反。<em>as a result</em> 是連接副詞，後面是結果：<em>The road was closed. As a result, the truck took another route.</em> <em>as a result of</em> 是介系詞，後面是原因：<em>The truck took another route as a result of the road closure.</em>
```
- In `sections[2].body[4]`, replace the substring `<em>due to</em> 後面也只能接名詞。` with `<em>due to</em> 後面也不接子句，只接名詞（或 Ving）。`
- Replace `sections[2].table.rows[0][2]` with: `<em>because of、due to、owing to、as a result of</em>`
- Replace `sections[8].table.rows[1][2]` with the same value.

### 08-S4 [shouldFix] `and / but / so` are not "從屬子句" makers
- Where: `sections[0].body[1]`
- Problem: "連接詞把這個子句掛到主要子句上，讓它變成從屬子句" is true of `although` / `because` but not of `and`, `but`, `so`, which the chapter later calls 連接詞 too (sections 2, 3, 4, 7). Nothing tells the reader that these join two clauses that can each stand alone and must sit between them, while `although` / `because` clauses can be moved to the front. That difference is also what the 「能不能搬動」 test in `sections[1]` rests on.
- Replace the last sentence of `sections[0].body[1]`, `連接詞把這個子句掛到主要子句上，讓它變成從屬子句（第 3 章）。`, with:
```
<em>although</em> 這類連接詞把這個子句掛到主要子句上，讓它變成從屬子句（第 3 章）。<em>and、but、so</em> 比較特別：它們把兩個子句並排接起來，兩邊都還能單獨成句，而且只能站在兩個子句中間；<em>although</em>、<em>because</em> 帶頭的子句則可以搬到句首。
```

### 08-S5 [shouldFix] `since` missing from the two-identity list; `prior to` and `afterward` appear in the closing table without being taught
- Where: `sections[4].table.rows[3][0]`, `sections[4].takeaway`, `sections[8].table.rows[4]`
- Problem: Chapter 3 lists `before, after, until, since` as words with both identities; this chapter drops `since` (it only appears in `sections[2]`). In the final table, `prior to` and `afterward` have never been taught, and `before / after / until` (the best examples of the "look at what follows" rule) are missing from the time row.
- Replace `sections[4].table.rows[3][0]` with: `<em>before、after、until、since</em>`
- In `sections[4].takeaway`, replace the substring `<em>before、after、until</em> 兩種都行，看後面。` with `<em>before、after、until、since</em> 兩種都行，看後面。`
- Replace `sections[8].table.rows[4]` (the whole row) with:
```json
["時間", "<em>while、when、once、as soon as</em>，以及 <em>before、after、until、since</em>", "<em>during、upon</em>，以及 <em>before、after、until、since</em>", "<em>meanwhile、in the meantime</em>"]
```

### 08-S6 [shouldFix] "兩個主詞不同，只能用 so that" ignores `in order for X to V`
- Where: `sections[6].body[3]`
- Problem: `in order for the tour to start on time` is grammatical and appears in formal text. Saying "只能用 so that" will be contradicted. The point (plain `in order to` cannot take a new subject) stands.
- In `sections[6].body[3]`, replace the substring `只能用 <em>so that</em>。` with `要用 <em>so that</em>（比較正式的 <em>in order for the tour to start on time</em> 也可以，這本書不細講）。`

### 08-S7 [shouldFix] `upon request` does not mean 一……就
- Where: `sections[7].body[3]` and `sections[7].ex[3].zh`
- Problem: The section is about 「一……就」. `upon request` is 「應要求」, not 一……就, so a reader mixes two meanings of `upon`. `upon completion` (一完成) fits, and is a very common notice phrase.
- In `sections[7].body[3]`, replace the substring `<em>upon request</em>（應要求）` with `<em>upon completion</em>（一完成）`.
- `sections[7].ex[3].zh`: replace `我們就會寄電子郵件和您聯絡。` with `我們就會以電子郵件與您聯絡。`

### 08-S8 [shouldFix] Three small wording points
- `sections[8].body[2]`: replace the substring `注意 <em>in addition</em> 和 <em>in addition to</em> 只差一個 <em>to</em>` with `<em>in addition</em> 和 <em>in addition to</em> 只差一個 <em>to</em>` ("注意" is the kind of filler STYLE.md §1 rules out).
- `sections[1].body[1]`: after `等於兩個完整的句子只靠一個逗號黏在一起，文法上是錯的。` add ` 這種錯叫 comma splice（逗號接句）。` so the reader recognises the name elsewhere.
- `sections[4].quiz[0].q`: replace `celebrated with dinner` with `celebrated over dinner` (more natural).

### 08-S9 [shouldFix] Real place names
- `sections[4].body[1]`: replace `東京` with `海港市`, and each `in Tokyo` / `while I was in Tokyo` with `in Harbor City` / `while I was in Harbor City` (three occurrences: `during I was in Tokyo`, `during my stay in Tokyo`, `while I was in Tokyo`).
- `mistakes[3]`: replace `Singapore` with `Harbor City` in `wrong`, `right` and `why` (`During I was in Harbor City, I visited two clients.` / `While I was in Harbor City, ...` / `during my stay in Harbor City`).

### 08-S10 [shouldFix] Answer positions: 8 of 14 `choose` answers are index 1
- Reorder `options` and set `answer` (all `why` texts refer to options by content). The new `sections[4].quiz[1]` from 08-S2 already puts the answer at index 1.

| Path | New `options` | `answer` |
|---|---|---|
| `check[0]` | `["Although", "However", "Despite"]` | 2 |
| `check[2]` | `["The flight was delayed; therefore, we missed the meeting.", "The flight was delayed, therefore we missed the meeting.", "The flight was delayed therefore, we missed the meeting."]` | 0 |
| `check[3]` | `["while", "meanwhile", "during"]` | 2 |
| `sections[1].quiz[0]` | `["Our office will be closed on Monday, therefore, orders will ship on Tuesday.", "Our office will be closed on Monday, therefore orders will ship on Tuesday.", "Our office will be closed on Monday. Therefore, orders will ship on Tuesday."]` | 2 |
| `sections[2].quiz[0]` | `["Because", "As a result", "Because of"]` | 1 |
| `sections[6].quiz[0]` | `["so that", "because", "in order to"]` | 2 |
| `sections[7].quiz[0]` | `["Once", "Upon", "As soon as"]` | 1 |
| `sections[8].quiz[0]` | `["Moreover", "However", "Otherwise"]` | 0 |

After these changes the 14 items split 6 / 4 / 4 across positions 0 / 1 / 2.

### Verdict: 08-connect
This is the strongest of the four chapters and it is careful where the brief says it must be: the single decision rule (look at what follows: tensed verb means 連接詞, noun or Ving means 介系詞, new sentence means 連接副詞) is stated up front, tested on the right thresholds (`despite` + clause, `during` + clause, `because of` + clause, comma + `however`), repeated in the same table shape in every section, and then reversed in the last section (form first, meaning second). The punctuation rule for linking adverbs is correct and the 「能不能搬動」 test is a good second check; `unless` + a negative, `without` + clause, `upon you arrive`, `although ... but` and the tense rule in `once` / `unless` clauses are all handled accurately. I read every example, translation and option: all English is correct, every quiz has exactly one answer, and I found no comma-splice or punctuation error. Two statements must be changed because they overreach: `so` without `that` is not always a result (08-M1), and `Even the store was busy` is not ungrammatical (08-M2). The main structural weakness is the shortened-clause paragraph in the `while / during` section (08-S1), where the chapter's own test fails and the paragraph does not say so; a quiz for it is needed too (08-S2), and `as a result of` is the most valuable missing item (08-S3). Ready after these.
