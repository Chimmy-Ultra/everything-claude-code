# Round 3: fixes and explanation check

Inputs: DESIGN.md §1, §3, §5, §7 and both appendices; review/round3_grammar.json, round3_vocab.json and round3_listen.json (44 new or changed ids); review/consult2_solved.json (independent blind review: 52/52 keys agree, mustFix empty); the 多益文法考點 page for terminology (Ving, to V, p.p., 原形, 連接副詞).

Result: **8 items had their stem or options changed** and go back to blind review (`review/round3_fixed.json`). **25 explanation fields** were changed: 17 in those 8 items and 8 in items that keep their stem. **17 levels** now follow the blind band. **36 items** are `reviewed: True`; the 8 reblind items stay `False`. No answer index, audio script (`text`/`say`), evidence index or `accent` changed, and nothing in `audio/` was touched. `v` was not bumped because none of these versions has been published yet; this follows log_final_explanations.md.

## Step 1: review fixes (stem or options changed → reblind)

| id | what changed | explanation fields rewritten |
|---|---|---|
| g-prep-05 | Option D: `on behalf of` → `in exchange for`. `on behalf of` is the key of g-prep-07, so one item no longer rules out an option in another. | wrong[3] |
| g-connect-06 | Stem: "accept deliveries after 6 p.m." → "after that time", so it matches "staffed only until 5 p.m.". The provided that / unless test is unchanged. | why, zh (六點 → 五點) |
| g-mandative-03 | Option A: `checks` → `checking`. The British covert-mandative reading (indicative "checks") can no longer defend a second answer. The new lure is "recommend + Ving". | point, why, wrong[0], wrongMore[0] |
| v-synonym-02 | Option A: `rents` → `returns`. `rents` was marginally defensible; `returns` is clearly wrong (the equipment belongs to IT, and the staff are the ones who return it). | point, wrong[0], wrongMore removed (it only explained rents) |
| g-tense-06 | Stem: "straight out of university" → "straight out of college" (American register). | none needed (zh 大學一畢業 still fits) |
| g-pos-06 | Stem: "so the front desk no longer handles" → "so the receptionists no longer handle". | zh (櫃台 → 接待人員) |
| g-pos-07 | Stem: "without calling the front desk for directions" → "without calling ahead for directions". | why, wrongMore[0], zh, vocab (first-time visitor → call ahead) |
| v-family-07 | Stem: "the front-desk staff" → "the reception staff". | zh, vocab (front desk → reception staff) |

l-talk-01 still says "the front desk". Its script was left alone because the audio is already recorded, so "front desk" now appears in that one item only.

Levels of the reblind items were left as they were, for the new blind review to set. Their consultant-review bands were: g-prep-05 medium (level 1), g-connect-06 medium (3), g-mandative-03 hard (3; likely lower now that the -s lure is gone), v-synonym-02 easy (2), g-tense-06 medium (3), g-pos-06 easy (2), g-pos-07 easy (2), v-family-07 easy (2).

## Step 2: explanation check (items whose stem was not changed)

| id | field | before → after | reason |
|---|---|---|---|
| g-pos-08 | why | 「後面整句沒有別的動詞」 → 「缺主要動詞（would pay 屬於 that 子句）」 | The sentence does contain a verb (would pay), so the old wording was imprecise. The rule is that the main clause has no finite verb. |
| g-prep-06 | zh | 「把…下滑的主因歸於」 → 「把…的下滑大多歸因於」 | The stem says *most of the drop*, not "the main cause". |
| g-prep-07 | zh | 「在 10 月 14 日我們的年度頒獎晚宴上」 → 「於 10 月 14 日在本會的年度頒獎晚宴上」 | Smoother word order for a formal letter. |
| g-relative-04 | zh | 「三位它認為最有資格…的人選」 → 「三位人選…；委員會認為他們最有資格…」 | 「它認為」 is unnatural in Chinese. |
| v-collocation-09 | vocab | `parking lot` → `lot`（parking lot 的簡稱） | The stem says "the lot on Carver Street". |
| v-synonym-09 | why | 「其他三個受詞要是人」 → 「其他三個的受詞是被免除的人」 | States the actual contrast: the object is what is freed, not the fee. |
| v-business-07 | wrongMore[1] | 「是分期付款不是退款」 → 「是先付的訂金，不是退款」 | A deposit plus a balance is not an installment plan. |
| l-conv-06 q1 | wrong[2] | 「張冠李戴：115 是女方要去的合約那場」 → 「同字陷阱：115 是合約那場，他去的是下一場」 | The woman never says she is going. The trap is hearing "contracts". |

The following were checked and left unchanged: point/why rule and application, wrong/wrongMore reasons with None at the key, zh/transcriptZh, vocab glosses, evidence indexes, and `say` on every line with digits, times or Ms. (l-qr-09, l-talk-01, l-talk-03). This covers g-tense-02, g-voice-02, g-connect-03, g-participle-01, g-participle-05, g-agree-04, g-quantity-04, g-compare-04, g-toing-01, g-toing-04, g-pronoun-04, g-conditional-03, v-synonym-04, v-family-01, v-collocation-07, v-collocation-08, v-synonym-07, v-synonym-08, v-business-08, v-family-08, l-qr-03, l-qr-09 to l-qr-12, l-conv-05, l-conv-06 (q0 and q2), l-talk-01 and l-talk-03.

## Levels from the consultant-review band (easy 1 / medium 2 / hard 3; conv/talk take their hardest question's band)

| id | level |
|---|---|
| g-tense-02 | 2 → 1 |
| g-connect-03 | 2 → 1 |
| g-pos-08 | 2 → 1 |
| g-quantity-04 | 2 → 1 |
| g-compare-04 | 1 → 2 |
| g-conditional-03 | 1 → 2 |
| g-toing-04 | 2 → 3 |
| v-synonym-04 | 3 → 2 |
| v-collocation-08 | 3 → 2 |
| v-synonym-09 | 3 → 2 |
| v-business-08 | 3 → 2 |
| v-synonym-07 | 2 → 3 |
| v-business-07 | 2 → 1 |
| v-family-08 | 1 → 2 |
| l-qr-09 | 3 → 2 |
| l-qr-11 | 3 → 2 |
| l-conv-06 | 3 → 2 (bands easy / medium / medium) |

The other 19 non-reblind items already matched their band.

## Check

A Python check ran over all 123 items and found 0 errors. It covered:
- imports through content.py
- required fields and unit/level values
- one blank and 4 distinct options per gap item
- the answer range
- wrong/wrongMore shape, with None at the key
- limits: point ≤ 40, why ≤ 90, wrong ≤ 45
- vocab pairs
- transcriptZh length
- audio files present
- `say` on lines with digits, `$`, titles or abbreviations
- evidence in range
- graphic rows
- unique ids
- reviewed = True for the 36 round-3 items and False for the 8 reblind ids

## Not done (outside this round's fix list)

- **Too easy:** consult2 shouldFix says g-tense-02, g-participle-01, g-toing-01, g-prep-07, v-business-07 and v-family-01 are too easy. They are untouched; their levels now say so.
- **v-business-07 setting:** the editor note says a logistics firm receiving part of a purchase price reads oddly; a supplier would read better.
- **Topic overlap:** v-collocation-09 (parking garage closed on Saturday) overlaps l-qr-10. The reviewer said to vary it only if convenient.
