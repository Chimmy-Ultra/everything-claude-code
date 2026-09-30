# Final explanation check — items rewritten in review

Scope: the 15 rewritten grammar and vocab items (g-connect-01, -03, -04, g-prep-01, g-tense-01, g-agree-01, g-pronoun-01, g-parallel-02, -03, v-collocation-02, -05, v-synonym-01, -02, -03, -05) and all 14 listening items (26 questions).
Inputs: DESIGN.md §1, §3, §5, §7 and the appendix; the 多益文法考點 reference page (voice, tense, connect, agree, pronoun, prep, parallel units) for terminology; review/solved_*_round2.json, solved_vocab_round2.json and solved_listen_round3.json for the final blind answers and bands; log_vocab.md and revised_listen.json for the level conventions.

Result: **23 fields changed** in 16 items (15 explanation / translation / vocab fields and 8 levels). **No stem, option, answer, script `text`/`say`, evidence index or `accent` was changed, and none needed changing.** All 29 items are now `reviewed: True`. `v` stays 1 because nothing has been published yet.

## Changes

| id | field | before → after | reason |
|---|---|---|---|
| g-tense-01 | point | 明確的過去時間用過去式；主詞被動承受用被動 → 明確的過去時間用過去式；主詞承受動作又沒受詞用被動 | 「主詞被動承受用被動」is circular and names no test. Now uses the reference page's voice rule (subject receives the action, no object → passive), which is what `why` applies. |
| g-connect-04 | point | unless 表示例外：除非……，否則不…… → unless 引出例外條件：除非……，否則…… | 「否則不……」over-generalises: it implies the main clause of *unless* must be negative. |
| g-connect-04 | why | 前半句說隔天才出貨，後半句是付費選當日出貨，正好是「不隔天出貨」的例外條件，所以用 unless。 → 前半句是規則：三點後的訂單隔天才出貨；加價選當日出貨正是這條規則的例外，所以用 unless。 | 「「不隔天出貨」的例外條件」is convoluted and easy to read backwards. Now states the rule (after 3 p.m. → next day) and the exception (paid same-day) plainly. |
| g-connect-04 | wrong[3] (whether) | whether 引導副詞子句時要配 or not → whether 表「不論」時要配 or not；補上了句意也不通 | Only gave the structural reason. With *or not* added, the sentence says the order ships next day whether or not the customer pays for same-day shipping. That makes no sense, and it is the full reason whether fails here. |
| g-prep-01 | wrong[2] (since) | since 搭配完成式，講從過去延續到現在 → since 標的是「從那時起」的起點，不能表示截止期限 | Stated a general use of *since* rather than why it fails here: April 5 is a deadline, and *since* only marks a starting point. |
| g-pronoun-01 | point | 空格後面接名詞 → 用所有格 its（它的） → 所有格放在名詞前；單數的公司用 its（它的） | 「空格後面接名詞 → 用所有格」over-generalises (*We sent ___ brochures* needs *them*); the same kind of rule was already removed from g-relative-01. Now uses the reference wording 所有格放在名詞前 and says why *its* (singular company). |
| v-collocation-05 | why | 「在 A 和 B 之間取得平衡」固定說 strike a balance between A and B；pull、run、lift 都不和 balance 搭配。 → 「在 A 和 B 之間取得平衡」固定說 strike a balance between A and B；pull、run、lift 都沒有這個用法。 | Said run never collocates with *balance*, but *run a balance* (a card balance) exists, and `wrong[1]` says exactly that. Now says none of them can mean 取得平衡. |
| v-synonym-01 | wrong[1] (pension) | pension 是退休後才領的退休金 → pension 是退休後才領的退休金，不按合約抽成 | Only gave a definition and did not tie it to the stem (paid per contract signed). Now matches the other two `wrong` entries. |
| v-collocation-02 | level | 1 → 2 | Vocab `level` follows the calibrated band (log_vocab.md: easy 1 / medium 2 / hard 3). Round 2 rated it medium, since *come/go into effect* are live lures. |
| v-synonym-02 | level | 2 → 1 | Round 2 band: easy (two explicit cues rule out rents and donates). Same convention. |
| v-synonym-03 | level | 3 → 2 | Round 2 band: medium. The author's 'hard' was a self-estimate that log_vocab.md said round 2 should check. |
| v-synonym-05 | level | 3 → 2 | Round 2 band: medium (each distractor is refuted by its own cue, so elimination works). Same convention. |
| l-qr-02 | level | 3 → 2 | Listening `level` follows the calibrated band (revised_listen.json aligned l-qr-07/08 the same way). Round 2 band: medium. |
| l-qr-03 | level | 3 → 2 | Round 2 band: medium ('both distractors are easy to rule out on form, so this is medium rather than hard'). |
| l-conv-03 | level | 3 → 2 | Latest bands are medium / medium / easy (round 3 Q1, round 2 Q2–Q3). Every other conv/talk item takes the level of its hardest question, which here is medium. SUMMARY.md also states that no listening question was rated hard. |
| l-conv-04 | level | 3 → 2 | Round 2 bands: medium / medium / medium. Same rule. |
| l-conv-02 | transcriptZh[3] | 不好意思，我們星期五的外送司機中午才開始送。不過歡迎您提早過來拿。 → 不好意思，我們的司機星期五要到中午才開始外送。不過歡迎您提早過來拿。 | 「我們星期五的外送司機」 reads like 'our Friday driver'. The English means the driver does not start until noon on Fridays. Reordered for accuracy and natural Taiwan phrasing. |
| l-conv-02 | q1 vocab (I'm afraid) | ["I'm afraid", "恐怕（委婉拒絕）"] → ["I'm afraid", "恐怕（委婉帶出壞消息）"] | *I'm afraid* softens bad news in general, not only refusals; here it introduces the noon start, not a refusal. |
| l-conv-03 | q2 wrong[3] | 價格 Tom 看過了，他們正要跳過 → 價格頁 Tom 看過了，他們決定跳過 | 「他們正要跳過」 is unnatural and sounds in-progress. They have already agreed to skip that page (*we can skip the back page*). |
| l-conv-04 | transcriptZh[2] | 比較舊的，我已經用了四年。公司說今年春天會換新筆電，但我不抱什麼期望。 → 比較舊的，我已經用了四年。公司答應過今年春天要換新筆電，但我不抱什麼期望。 | *We were promised* means 答應過, not just 說. The Q1 key (*as promised*) depends on this word, so the translation has to carry it. |
| l-conv-04 | q2 wrong[2] | 同字陷阱：battery 出現過，但由男方送來 → 同字陷阱：電池下午才由男方送來，她現在換不了 | The question asks what she does *next*. The old entry did not say why this is not next. The new one says the battery only arrives this afternoon, so she cannot replace it now. |
| l-talk-01 | q0 why | 說要更換 those lifts → 改述成 installation of new elevators（lift＝elevator）。 → 承包商要 replace 東側的 lifts → 改述成 installation of new elevators（lift＝elevator）。 | *those lifts* means the east-side lifts in line 2 but the main-entrance lifts in line 4, and Q2's `why` explains the latter. Q1 now names the east-side lifts so the two explanations do not clash. |
| l-talk-01 | q0 wrong[3] | 聯想陷阱：只叫大家走樓梯，沒提到演習 → 聯想陷阱：走樓梯是施工期間的替代方式，不是演習 | 「只叫大家走樓梯」 misstates the talk, which says use the main-entrance lifts **or** the stairs. |

## Set to `reviewed: True` (29)

g-connect-01, g-connect-03, g-connect-04, g-prep-01, g-tense-01, g-agree-01, g-pronoun-01, g-parallel-02, g-parallel-03, v-collocation-02, v-collocation-05, v-synonym-01, v-synonym-02, v-synonym-03, v-synonym-05, l-qr-01, l-qr-02, l-qr-03, l-qr-04, l-qr-05, l-qr-06, l-qr-07, l-qr-08, l-conv-01, l-conv-02, l-conv-03, l-conv-04, l-talk-01, l-talk-02

No item was held back. The vocab items and l-conv-03 had no stem, option or answer problem. The final blind rounds agree with the key (vocab 6/6, listening round 3 3/3, grammar 5/5 and 4/4, listening round 2 26/26), and no item was flagged ambiguous or too close to a real test item.

## Checked and left as is

- **Point / why / wrong.** Each remaining `point` states the deciding rule or listening skill, and each `why` applies it to the item. For listening, each `why` gives the paraphrase (audio → option). All `wrong` entries are in option order with `None` at the answer.
- **Trap labels.** 同字陷阱 marks an option that reuses a heard word in a false statement (e.g. drive, present, trained, came in). 答錯問句類型 marks a response that answers a different question type (Yes to a wh-question, a time or person to a where-question, a place to an offer). 張冠李戴 marks only actions done by the other speaker (the woman hands out the boxes, the man books the room, the woman brings the printed copy, Nora is the organizer). The extra labels 聯想陷阱, 字面陷阱 and 曲解 are accurate where used.
- **zh / transcriptZh.** All other `zh`, `transcriptZh` lines and vocab glosses are accurate, natural Taiwan usage. Alternative wordings such as 看完 vs 審完 for *go over* were judged acceptable and left alone.
- **Listening metadata.** Every evidence index points at the line(s) holding the answer. Every line with digits, times, prices, an abbreviation (IT, 4B, p.m.) or *Wei* has a `say`. Lines whose times are written in words (nine thirty, half past eight, one o'clock) need none. `accent` matches the voices in all 14 items. `transcriptZh` has one entry per line.
- **Grammar levels kept.** Grammar `level` follows the §7 definitions, not the band, as in log_grammar_a/b.md (e.g. g-tense-05 medium → 3). g-tense-01 stays 3: two rules plus a clue at the far end and a present-tense lure in the tail, the same profile as g-tense-05. g-prep-01 stays 1: one rule, with the clue right before the blank. g-connect-01 and -03 and g-parallel-02 and -03 stay 2: two rules, or a clue far from the blank. The calibrator rated them easy.
- **Limits.** point ≤ 40, why ≤ 90 and wrong ≤ 45 hold for all 29 items. The longest are l-qr-01 why (89), l-conv-03 q2 why (89) and g-agree-01 wrong[1] (44).

## Verification

- A Python check over all 29 items tested imports, required fields, the limits, `wrong[answer] is None`, evidence in range, and that `transcriptZh` length equals the number of lines. It passed.
- A diff against HEAD confirms that only the fields in the table above (plus `reviewed`) changed.
- `build_page.py` (strict mode, no `--draft`), run on a scratch copy, now builds the whole bank (90 items) with no warnings or errors. That means every hand-written item is `reviewed: True` and every audio file exists.

## For the builder (non-blocking)

- Levels now give listening 3 / 11 / 0 across levels 1 / 2 / 3, matching SUMMARY.md's statement that no listening question was rated hard. Vocab is 7 / 13 / 4 (level 3: v-synonym-04, v-business-06, v-family-03, v-family-06). Both now match the calibrated distribution in SUMMARY.md.
- The v-synonym-05 calibrator notes that one cue per distractor 'feels somewhat engineered', and the v-collocation-05 calibrator notes 'no near-miss option'. Both are style notes. The keys are unique, so they do not block review.
