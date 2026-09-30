# Grammar set A — second-stage review log

Scope: `items_grammar_a.py` (24 items: pos 6, tense 5, connect 5, prep 4, participle 4).
Inputs: DESIGN.md §1, §5, §7; `review/solved_grammar_a.json` (blind solve agreed with the key on 24/24, no ambiguity flags); the grammar reference page's `U.push` blocks for pos, tense, connect, prep and participle.

Result: 7 items changed (10 fields), 24 marked `reviewed: True`, 0 left unreviewed. No stem, option or answer was changed. `v` stays 1 because none of these items has been published yet.

## Changes

| id | field | before → after | reason |
|---|---|---|---|
| g-pos-04 | why | 後面用 who 接著說他來廠裡、提出建議，這是人做的事 → 後面的 who 只能指人，來廠裡、提出建議的也是人 | `recommended` is the main verb, not part of the who clause. The old wording put both verbs inside the who clause, and it did not state the deciding clue: who only refers to people. |
| g-pos-06 | level | 3 → 2 | The clue (`easier`) is directly after the blank. The difficulty is two rules working together: the make it + adjective pattern pulls toward `considerable`, but the adverb that modifies a comparative wins. That fits the level 2 definition. Level 3 means the whole sentence must be read, and this item does not need that. |
| g-tense-02 | wrong[0] | 現在簡單式講習慣或固定行程，不講此刻 → …，不講此刻正在做的事 | More precise. With stative verbs, the present simple does describe "now". What it cannot do is describe an action in progress. |
| g-tense-02 | wrong[3] | 現在完成式講到目前的結果，不配 at the moment → 現在完成式講已做到的結果，不表示此刻正在查 | "不配 at the moment" over-generalises ("At the moment we've received 30 replies" is fine). The real reason is that the sentence describes an action still in progress. |
| g-connect-03 | wrong[1] | 連接詞，後面要直接接子句，不能加逗號 → 連接詞，不能單獨夾在分號和逗號之間；因果也反了 | "不能加逗號" is too broad, because parenthetical commas after `because` are possible. The new wording names the actual structural slot, and also the reversed cause and effect. |
| g-connect-03 | wrong[2] | 介系詞，後面要接名詞，不能接逗號 → 介系詞，後面要接名詞，這裡接的是子句 | "不能接逗號" is not a grammatical reason. The concrete failure is that a clause follows. |
| g-connect-05 | wrong[3] | 意思對，但它是連接副詞，不能連接兩個子句 → 連接副詞，不能連接兩個子句；也該放在後一句開頭 | "意思對" is inaccurate. `Nevertheless` introduces the unexpected result (sales rose), not the concession clause, so it is wrong in this position as well as in structure. |
| g-prep-04 | wrong[2] | until 表示持續到那時，時間方向相反 → until 講到合併那時為止，但 has doubled 延續到現在 | "時間方向相反" was vague. The new wording names the clash with the present perfect in this sentence. |
| g-participle-01 | wrong[1] | 原形動詞或名詞，不能這樣修飾 price list → 原形動詞不能修飾名詞；當名詞也沒有 update price list 的說法 | "不能這樣修飾" did not give a reason. Nouns can modify nouns (the reference page's 名詞修飾名詞 rule), so the concrete point is that *update price list* is not an existing compound. |
| g-participle-01 | wrong[3] | 複數名詞或動詞，不能放在 the 和名詞之間 → 動詞不能修飾名詞；updates price list 也不是複合名詞 | Over-generalised: plural nouns do sit between *the* and a noun (the sales team, the savings account). |

## Items left unreviewed

None.

## Checked and left as is (for the record)

- Every `point` states the deciding rule, and every `why` applies that rule. The wording matches the reference page's terms (連綴動詞, 人和事的名詞, 時間和條件子句, 連接副詞, 分詞構句, 情緒動詞, by／until, for／during).
- `zh` and `vocab` are accurate for all 24 items. Minor wording alternatives (for example 帳務軟體 vs 計費軟體, 配送網) were judged acceptable in Taiwan usage and left alone.
- Borderline levels kept: g-connect-04 stays at 2 even though structure alone decides it. For Taiwanese learners, 「除非…否則」 in the meaning pulls toward `otherwise`, so structure and meaning have to be weighed against each other. g-prep-04 and g-tense-05 stay at 3, because the deciding clue is the verb tense at the far end of the sentence and every distractor works in other contexts.
- Level spread for this batch is now 10 / 10 / 4, against the 40 / 40 / 20 target for the whole bank.
- Names: Okafor, Haddad, Varga, Brenmoor Foods, Kessling Freight, Orvane Shipping, Tamsin Road and Westbrook returned no real-company match. Lisbon and Haverford are real places, which DESIGN.md allows.

## For the builder

- **Merriden Hotel (g-tense-05)** is one letter off the *Meriden Hotel*, a Grade II listed building in Meriden, West Midlands, UK. The spellings differ, so I did not change the stem. If you want zero overlap with real businesses, rename it and search the new name first. The stem and `zh` would both need the new name (the `zh` currently says Merriden 飯店).
- The blind reviewer's note still applies: g-tense-01 and g-tense-02 are easy (one obvious time marker). Set B or a later batch could add a present perfect vs simple past item without an explicit time adverb.
