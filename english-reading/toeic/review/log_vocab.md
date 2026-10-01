# Vocabulary set — second-stage review log

Scope: `items_vocab.py` (24 items: collocation 6, synonym 6, business 6, family 6).
Inputs: DESIGN.md §1, §5, §7 and the appendix; `review/solved_vocab.json`. The blind solve agreed with the key on 24/24 with no ambiguity flags. The calibration found 22 items similar and 2 easier, style 3.9 on average, bands 8 easy / 12 medium / 4 hard, and changeFirst = v-synonym-02, v-collocation-02, v-collocation-05, v-synonym-03, v-synonym-01.

Result:
- **Step 1:** 6 items rewritten: the five changeFirst items plus v-synonym-05. They are set to `reviewed: False` and need a round-2 blind review.
- **Step 2:** 11 explanation fields fixed in 7 unchanged items, 1 vocab gloss changed (v-business-02), and 8 level changes. No stem, option or answer of an unchanged item was touched.
- **Flags:** 18 items set to `reviewed: True`.
- **`v`:** stays 1 on every item because nothing in this set has been published yet, which matches the grammar logs.
- **Header comment:** it said "reviewed stays False until a human reviewer signs off". It now describes the DESIGN.md appendix process instead, because the flags are now set by that process.

## What the file now covers (the brief's targets)

| target | where |
|---|---|
| Four same-part-of-speech words that all fit the slot on their own, where only sentence context decides (at least 2) | **v-synonym-01** (wage / pension / commission / allowance: "earn a ___" fits all four; *of 4 percent on every contract* decides). **v-synonym-02** (rents / lends / borrows / donates: "The IT department ___ projectors" fits all four; *to staff*, *free of charge* and *up to two weeks* each rule out one). **v-synonym-05** (hard; see the next row). The unchanged v-business-02 (receipt / estimate / refund / invoice) is a fourth, at medium. |
| At least one adverb vocabulary item | **v-synonym-05**: markedly / slightly / steadily / temporarily. All four fit "visits ___ increased". *40 percent* rules out slightly, *jumping … in the first week* rules out steadily, and *for the rest of the year* rules out temporarily. It is hard: the whole sentence has to be read, and the key is the least frequent word. |
| Synonym items decided by meaning or collocation; at most one decided by a verb pattern | The only pattern item left is v-synonym-04 (comprises; the calibrator rated it hard, style 4). v-synonym-01, -02 and -05 are decided by meaning in context, v-synonym-03 by collocation, and v-synonym-06 by meaning. The old raise/rise, tell, reply-to and notify items are gone. |
| Units 6 each | collocation 6, synonym 6, business 6, family 6 |
| Band mix about 7 / 11 / 6 | My estimate is **7 easy / 11 medium / 6 hard** (details below). `level` now matches it: 7 / 11 / 6. |
| Answer letters | A 6, B 6, C 6, D 6 |

## Step 1 — rewritten items

| id | before | after | reason |
|---|---|---|---|
| v-collocation-02 | "Because of ___ traffic on the bridge…" strong / **heavy** / hard / large | "The revised travel policy will ___ effect on July 1, so trips booked after that date must follow the new rules." come / **take** / go / make (key B) | Calibrator: easier than real items, style 3, "reads like a textbook drill". *Take effect* is a staple business collocation at the easy end of a real set. The distractors are the lure: learners know *come into effect* and *go into effect*, and only the missing *into* rules them out. I did not use the calibrator's *extensive road repairs* (spacious / wide / roomy). *Wide road repairs* can be parsed as repairs to a wide road, and the size words fail at a glance, which was the original problem. Level 1, easy. |
| v-collocation-05 | strike / punch / beat / knock (key A) | Stem unchanged; **pull / run / strike / lift** (key C) | Uses the calibrator's fix. The distractors are now verbs with business collocations of their own (*run a business*, *lift a ban*), so they no longer look out of register. *Run a balance* (carry a card balance) exists, but not with *between A and B*, and the wrong entry says so. Level 2, medium. |
| v-synonym-01 | rise / arise / **raise** / arouse (verb pattern: transitivity) | "Sales representatives earn a ___ of 4 percent on every contract they sign, in addition to their base salary." wage / pension / **commission** / allowance (key C) | The calibrator's fix (raise / rise / climb / grow) is still decided by transitivity only. The brief allows at most one pattern item, so the item is now a meaning item where all four pay nouns fit *earn a ___*. Each distractor fails for its own reason: a wage is regular pay (and the base salary is already mentioned), a pension is paid after retirement, and an allowance is a fixed sum. Level 1, easy. |
| v-synonym-02 | said / **told** / spoke / talked (verb pattern; calibrator style 2, "ESL drill") | "The IT department ___ projectors to staff who meet clients off-site, free of charge and for up to two weeks at a time." rents / **lends** / borrows / donates (key B) | The calibrator's fix (informed / announced / explained / mentioned) is still a verb-pattern item (inform + person + that), so I did not use it. The new item is a context item with a separate clue for each distractor: *free of charge* rules out rents, *to staff* rules out borrows (wrong direction), and *up to two weeks* rules out donates. Chinese 借 covers both lend and borrow, so borrows is a real trap. I used projectors, not laptops, because a listening option reads "Lend her a newer laptop". Level 2, medium. |
| v-synonym-03 | answered / contacted / **replied** / informed ("to" decides) | "Guests who ___ additional charges, such as room service or minibar purchases, must settle them at checkout." suffer / undergo / endure / **incur** (key D) | The calibrator's fix only rewrote the stem, so *reply to* would still decide the item by its preposition. The new item is a near-synonym collocation item: all four verbs translate as 承受／遭受, and only *incur* takes *charges*. *Room service or minibar purchases* are chosen by the guest, which also rules out *suffer* (bad things that happen to you). Hotel setting chosen to avoid echoing v-business-05 (reimbursed for fuel). Level 3, hard. |
| v-synonym-05 | notice / announce / declare / **notify** (object pattern) | Showroom visits, markedly / slightly / steadily / temporarily (key A) | Not in changeFirst. Changed because, after the three rewrites above, it and v-synonym-04 would have been two verb-pattern synonym items (the calibrator named notify as one). It is now the set's adverb item and its hard context item. Level 3, hard. The options are change-description adverbs rather than strict synonyms. They sit in `synonym` because DESIGN §7 defines the unit as options "靠…語境才能定", and no other unit fits. |

Every changed item has a new point, why, wrong, zh and vocab.

### Covered-key solve of the changed items

I printed the six stems and options in shuffled order, without answers or explanations (scratchpad only, not in `review/`), and substituted every option:

| id | my answer | key | alternatives considered |
|---|---|---|---|
| v-collocation-02 | B take | B | *come/go into effect* need *into*; *make effect* does not exist. The item works the same in British and American English. |
| v-collocation-05 | C strike | C | *run a balance* is a credit-card phrase and cannot take *between A and B*. |
| v-synonym-01 | C commission | C | An allowance can be a percentage of salary, but not per contract signed. |
| v-synonym-02 | B lends | B | *rents … free of charge* is a contradiction. *loans* (correct in American English) is not offered. |
| v-synonym-03 | D incur | D | *suffer higher costs* occurs in journalism, but not with voluntary purchases like room service. |
| v-synonym-05 | A markedly | A | *steadily* is the lure (the level stays steady afterwards), but *steadily increased* describes a gradual rise, and the rise here is a jump. |

All 6 agree with the key, with one defensible answer each. They still need the round-2 blind review (DESIGN appendix step 4).

## Step 2 — fixes in unchanged items

| id | field | before → after | reason |
|---|---|---|---|
| v-collocation-03 | wrong[0] | set 搭配 a goal、a date，不說 set an order → …；訂貨不說 set an order | Too broad. *Set the order* (a sequence) and *set a buy order* (trading) exist; the concrete failure is ordering goods. |
| v-collocation-04 | point | keep an eye on（密切注意）→ keep a close eye on（密切注意） | *Keep an eye on* is 留意; *close* is what makes it 密切. The point now names the tested phrase. |
| v-collocation-04 | why | …；要看到後面的 on 才確定。→ 「密切注意某事」固定說 keep a close eye on，on 後面接要注意的事，這裡是 cash flow。 | The *on* does not decide: *set eyes on* also has it, and *take a close eye* fails with any preposition. |
| v-business-01 | wrong[0], wrong[3] | inventory 是庫存清單 / warranty 是產品保固書 → + 不會列航班和飯店 / + 跟行程無關 | These only glossed the word; now each says why it fails in this sentence. |
| v-business-02 | vocab | invoice 請款單、發票 → 請款單、帳單 | In Taiwan, 發票 is what a shopper gets after paying, close to *receipt*, which is this item's main distractor. |
| v-business-04 | wrong[1] | decline 是「下降、婉拒」，不能這樣用被動 → decline 是「下降」（不及物）或「婉拒」，都不是扣錢 | The old entry was inaccurate: *decline* in the sense of 婉拒 does take the passive (*the offer was declined*). |
| v-business-05 | wrong[2], wrong[3] | recruit 是招募人才 / reserve 是預訂或保留 → + 跟油錢無關 / + 不是還錢 | Now each names why it fails here. |
| v-family-02 | wrong[0], wrong[2] | sensible 是「明智的、合理的」/ senseless 是「無意義的」→ + 不表示要保密 / + 跟要鎖起來無關 | Same as v-business-01. |
| v-family-03 | wrong[2] | respectable 是「體面的、像樣的」→ + 不表示「各自的」 | Same as above. |

### Level changes (unchanged items)

`level` is shown to learners before they answer, so it now follows the calibrated band (easy 1, medium 2, hard 3), using the DESIGN §7 definitions as tie-breakers.

| id | level | calibrator band | reason |
|---|---|---|---|
| v-collocation-06 | 3 → 2 | medium | One collocation with the clue (*majority*) right after the blank. The difficulty is the low-frequency words and the *overriding* lure. |
| v-synonym-04 | 2 → 3 | hard | All four verbs mean "make up". The solver has to see that the subject is the whole and the object is the parts, and every distractor is correct in another frame. |
| v-synonym-06 | 3 → 1 | easy | *our lease* right after the blank already rules out expand, enlarge and stretch. |
| v-business-01 | 1 → 2 | medium | The clues (*flight times*, *hotel*, *travel agent*) are away from the blank, and *agenda* is a near miss. |
| v-business-02 | 1 → 2 | medium | The deciding clue (*payable within 30 days*) is at the end of the sentence. |
| v-family-02 | 1 → 2 | medium | *Sensible* is a well-known trap, and the confidential sense comes from *locked* and *salaries*. |
| v-family-03 | 2 → 3 | hard | The three distractors are the better-known words, and the key depends on the two people and *their*. |
| v-family-05 | 3 → 2 | medium | A single meaning contrast, with the clue (*plain language*) given early. |

### Checked and left as is

- Every other point, why, wrong, zh and vocab entry is accurate for its sentence. The zh reads as natural Taiwan usage. 報銷 in v-business-05 is also used in Taiwan and was kept.
- v-business-06 wrong entries (adopt / attach / acquire) name each verb's usual objects, and that is the concrete reason; left as is.
- Names: the only personal names are Ms. Lin and Mr. Hale (v-family-03). Both are common surnames, and no business is named. The new items use no names.
- ETS resemblance: none of the new stems is modelled on an item I recognise. *Take effect* and *incur charges* are common in prep material, but these sentences are original.
- Cross-item cues: no new stem gives away an answer in the grammar or listening files. I checked for take effect, effective, commission, lend, rent, incur, markedly and renovation. The listening item's option "Lend her a newer laptop" is why v-synonym-02 uses projectors.

## Band estimate for the file

Unchanged items use the calibrator's bands; the six new items use mine.

- **Easy (7):** col-01, col-02*, col-03, syn-01*, syn-06, bus-03, fam-01
- **Medium (11):** col-04, col-05*, col-06, syn-02*, bus-01, bus-02, bus-04, bus-05, fam-02, fam-04, fam-05
- **Hard (6):** syn-03*, syn-04, syn-05*, bus-06, fam-03, fam-06

\* = rewritten in step 1. These bands are my own and should be checked in the round-2 calibration.

## For the builder

- Round 2: `python review/make_blind.py items_vocab v-collocation-02,v-collocation-05,v-synonym-01,v-synonym-02,v-synonym-03,v-synonym-05` writes `review/blind_vocab_round2.json`.
- v-synonym-05 is labelled `synonym`, but its options are not near-synonyms, so a learner in 依考點練習 → 近義辨析 may find it off-label. If the unit list ever gains a "context" or "adverb" vocab unit, move it there.
