# Grammar set B — second-stage review log

Scope: `items_grammar_b.py` (28 items: voice 3, agree 3, relative 3, pronoun 3, toing 3, compare 3, quantity 3, parallel 3, mandative 2, conditional 2).
Inputs: DESIGN.md §1, §5, §7 and the appendix; `review/solved_grammar_b.json` (blind solve agreed with the key on 28/28, no ambiguity flags; calibration judged the set slightly easy); the grammar reference page's `U.push` blocks for these ten units.

Result:
- **Step 1:** 4 items rewritten for difficulty and style (g-agree-01, g-pronoun-01, g-parallel-02, g-parallel-03). They are set to `reviewed: False` and need a round-2 blind review.
- **Step 2:** 14 explanation fields fixed in 9 unchanged items, plus 1 level change. No stem, option or answer of an unchanged item was touched.
- **Flags:** 24 items set to `reviewed: True`.
- **`v`:** stays 1 on every item because nothing in this set has been published yet, which matches the set A log. Bump it if any of these items is published before the rewrite.

## Step 1 — rewritten items (alignment with real Part 5)

| id | field | before → after | reason |
|---|---|---|---|
| g-agree-01 | stem | Every conference room on the fourth floor ______ a projector and a video camera. → The projectors in every conference room on the fourth floor ______ been replaced with newer models. | Calibrator: easier than real items, because no plural noun stood between the subject and the blank to attract a wrong verb form. Now the singular *every conference room … floor* sits right before the blank and pulls toward *has*, while the real subject, *projectors*, is ten words back. The rule is the reference page's 插入的修飾語 rule. I used this instead of the calibrator's *Each of the conference rooms …* for two reasons. First, several usage guides accept a plural verb after *each of + plural* in informal English, which would give a second defensible answer. Second, that sentence nearly repeats the reference page example *Each of the hotel rooms is equipped with…*. |
| g-agree-01 | options / answer | has, have, having, to have (key A = has) → have, has, having, to have (key A = have) | The key is now *have*. The options were reordered so the key stays at A. |
| g-agree-01 | level | 1 → 2 | The clue is far from the blank and a nearer noun attracts the wrong form. |
| g-agree-01 | explain (all) | every + 單數名詞 rule → 動詞跟真正的主詞一致，不跟介系詞片語裡的名詞; new why, wrong, zh, vocab | Rewritten for the new sentence. wrong[has] names the trap (*every conference room*). |
| g-pronoun-01 | options | it, its, **it's**, itself → it, its, **theirs**, itself | The brief called for a pronoun-form distractor instead of the contraction. *their* was rejected because *Venlow Logistics has updated their return policy* is acceptable in informal English and in British usage, which would give two defensible answers. *theirs* cannot come before a noun in any variety. It also tests 所有格 vs 所有代名詞 from the reference page. Key unchanged (B = its). |
| g-pronoun-01 | explain (all) | point: 名詞前用所有格 its；it's = it is / it has → 空格後面接名詞 → 用所有格 its（它的）; why, wrong, zh (自家的, 到貨後), vocab (+delivery) | The point no longer mentions *it's*. wrong[theirs] names why it fails here. Level stays 1. |
| g-parallel-02 | stem | Ms. Grant ______ approved the new marketing plan nor rejected it, saying she needed more time to review it. → The regional director has ______ approved the budget requests from the sales and marketing departments nor explained why they are on hold. | Calibrator: easy, because *nor* came only five words after the blank. Now *nor* comes ten words after the blank. The *and* in *sales and marketing* sits closer to the blank and pulls toward *both*, so every distractor fits the words next to the blank. Options unchanged; key unchanged (A = neither). |
| g-parallel-02 | explain (all) | new point, why, wrong, zh, vocab | wrong[both] explains why that *and* is not the partner. Level stays 2. |
| g-parallel-03 | stem | Ms. Ahn's duties include scheduling client meetings, ______ travel arrangements for the sales team, and updating the customer database. → Customers who want the extended warranty must register the product online within 30 days of purchase and ______ the original receipt. | Calibrator: easy, because gerunds on both sides of the blank gave the pattern away. Now the partner (*must register*) is ten words back. The words next to the blank (*of purchase and ___*) make *keeping* look right, and the answer is a base form. The old answer was Ving, so the item also no longer repeats the unit's Ving pattern. |
| g-parallel-03 | options / answer | make, to make, making, made (key C) → to keep, keeping, keep, kept (key C = keep) | New verb. Key kept at C. |
| g-parallel-03 | explain (all) | new point (and 連接的兩個動詞共用 must，都要用原形), why, wrong, zh, vocab | Rewritten. Level stays 2. |

g-parallel-01 (both … and) is kept unchanged as the unit's easy item.

## Step 2 — explanation fixes in unchanged items

| id | field | before → after | reason |
|---|---|---|---|
| g-voice-01 | why | 識別證是被發放的一方，空格後直接接 to all employees，沒有受詞，所以用被動 will be distributed。 → 識別證是被發放的一方，後面沒有受詞，要用被動；by the end of next week 是未來，所以用 will be distributed。 | The old why justified the passive but not *will*. Option D (*distributed*) is ruled out partly by the future time phrase, so the why now names it. |
| g-voice-01 | wrong[1] | 主動進行式，後面同樣缺受詞 → 主動進行式，識別證不會自己發放，後面也缺受詞 | 同樣 pointed back to wrong[0]. The page lists the learner's wrong choice first, so each entry must stand alone. |
| g-voice-01 | wrong[3] | 當過去式主動用，缺受詞，也對不上 next week → 少了 be 就不是被動；當過去式又缺受詞、對不上 next week | A learner who picks *distributed* usually reads it as 被發放, a passive p.p. without *be*. The old entry covered only the past-tense reading. |
| g-voice-02 | wrong[3] | raise 的主動進行式，後面同樣缺受詞 → raise 的完成進行式是主動，後面缺受詞 | 同樣 was a cross-reference. *have been raising* is the perfect progressive, not simply 進行式. |
| g-voice-03 | wrong[1] | 同樣是主動，給假的是董事會，不是她 → 主動表示她給出假期，但給假的是董事會 | Removed the 同樣 cross-reference. |
| g-agree-02 | wrong[2] | have 配複數主詞；usually 講常態也不用完成式 → have 要配複數主詞，這裡的主詞是單數的動名詞片語 | Over-generalised: *usually* can go with the present perfect (*I have usually found…*). The real reason is agreement. |
| g-relative-01 | point | 空格後直接接名詞 → 所有格 whose → 名詞屬於先行詞、後面子句完整 → 所有格 whose | Over-generalised: a relative can be followed directly by a noun that is the clause subject (*the software which engineers designed*). *whose* is decided by possession plus a complete clause. |
| g-relative-01 | why | 空格後面直接接名詞 subscriptions，意思是「顧客的訂閱」，要用所有格 whose。 → subscriptions expire this month 已是完整子句，subscriptions 是顧客的訂閱，所以用所有格 whose。 | Applies the corrected rule to this sentence. |
| g-relative-01 | wrong[0] | who 後面要直接接動詞，這裡接的是名詞 → who 要補子句缺的主詞或受詞，但後面子句已完整 | Over-generalised: *who* is also followed by subject + verb when it is an informal object (*the people who we met*). The concrete failure here is that the clause has no gap. |
| g-compare-01 | wrong[3] | is 後面要接形容詞，more cheaply 是副詞 → 這裡 is 後面要用形容詞描述 shipping，more cheaply 是副詞 | Over-generalised: *is* can be followed by nouns, prepositional phrases and adverbs of place. Here it needs an adjective describing the subject. |
| g-compare-03 | level | 3 → 2 | One lexical rule (*superior to*) with the clue right before the blank. That does not fit level 3 (要讀完整句). Calibrator: medium. |
| g-quantity-01 | why | information 是不可數名詞，前面只能用 much；… → information 是不可數名詞，選項中只有 much 能接；… | 「只能用 much」 read as absolute (*any, some, a lot of, little* also work). The claim holds only among the options. |
| g-quantity-02 | why | 空格後面是 of the applicants，能接 of the 加複數名詞的只有 Most → …，選項中能接 of the 加複數名詞的只有 Most | Same issue: *many of, several of, all of the* also exist. |
| g-quantity-03 | why | …，只能用接不可數名詞的 a great deal of。 → …，選項中只有 a great deal of 接不可數名詞。 | Same issue: *much, a lot of, a large amount of* also exist. |
| g-quantity-03 | wrong[1] | many 接可數複數；不可數要用 much → many 只接可數複數名詞，equipment 不可數 | The old entry implied *ordered much new laboratory equipment*, which is unnatural in an affirmative sentence. |

## Checked and left as is (for the record)

- **Rules and reasons:** every other `point`/`why` pair states the deciding rule and applies it correctly. Every other `wrong` entry names a concrete reason tied to this sentence. `wrong[answer]` is `None` everywhere.
- **Terminology:** the wording matches the reference page's terms (授與動詞, 插入的修飾語, 所有代名詞, 介系詞 to, 使役動詞, 原形, 否定詞開頭的倒裝).
- **g-conditional-02:** stays in `conditional`. The reference page's 否定詞開頭的倒裝 rule covers *Not until … did*.
- **`zh` and `vocab`:** accurate. Minor alternatives were judged fine and left alone: g-voice-03's sabbatical glossed 「（帶薪）長假」 (sabbaticals are usually paid), newsletter 電子報, and g-mandative-02's 分享.
- **Borderline levels kept:**
  - g-voice-03 and g-agree-03 stay at 3. Active *granted* fits the object right after the blank. *Neither* pulls toward a singular verb. In both, the decision needs the whole subject or the *by* phrase.
  - g-pronoun-03 stays at 2. Its meaning clue (*Mr. Patel's request*) is far from the blank.
  - g-conditional-01 stays at 2. The calibrator called it hard, but it is two interacting rules.
- **Unit counts:** unchanged: voice 3, agree 3, relative 3, pronoun 3, toing 3, compare 3, quantity 3, parallel 3, mandative 2, conditional 2.
- **Answer letters:** A 7 / B 7 / C 7 / D 7, the same as before.
- **Levels:** now 10 / 13 / 5 (36% / 46% / 18%), against the 40 / 40 / 20 target.
- **Names:** Venlow Logistics, Tarrow Freight, Brenvale Foods, Halvern Medical, Dorvan (X5 tablet) returned no real-company match. Dunmore, Leeds and Linden Falls are place names, which DESIGN.md allows. The three new stems use no names.
- **Checks:**
  - My structural check passed: fields, unit counts, stem 12–25 words, one blank, 4 distinct options, limits, `wrong[answer] is None`, reviewed flags.
  - `build_page.py`'s item checks report only the expected "not reviewed yet" for the four rewritten items.
  - I solved each rewritten item with the key hidden and the options shuffled. Every one had a single defensible answer, and it matched the key.

## For the builder

- **Round-2 blind review** of the four rewritten items (DESIGN appendix step 4):
  - Generate: `python review/make_blind.py items_grammar_b g-agree-01,g-pronoun-01,g-parallel-02,g-parallel-03` writes `review/blind_grammar_b_round2.json`.
  - Compare: `python review/compare.py items_grammar_b _round2`.
  - Set `reviewed: True` only if the blind answers match.
- **Venlow Logistics (g-pronoun-01)** is one letter off **Venlo**, a Dutch city known as a logistics hub. That is a place, not a company, and no business named "Venlow Logistics" turned up, so I left it. Renaming it would change a stem, so do that before round 2 if you want zero overlap.
- **Hard items:** the set still has only 5 level-3 items. The calibrator's broader note stands: a real Part 5 set has more hard items whose deciding clue is far from the blank. g-agree-01 and the two parallel rewrites move in that direction, but I labelled them level 2 because that is honest.
- **g-mandative-02:** the calibrator marked it harder than real items and said it is fine to keep as a deliberately hard item. It is unchanged.
