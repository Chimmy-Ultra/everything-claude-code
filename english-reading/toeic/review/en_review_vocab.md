# English review: items_vocab.json

Items checked: 34 (v-collocation-01..09, v-synonym-01..09, v-business-01..08, v-family-01..08), all fields (point, why, usage, gloss, Chinese twins).
Items changed: 7 (v-collocation-02, v-collocation-08, v-synonym-05, v-business-04, v-business-06, v-family-03, v-family-05).
`python3 en/check.py items_vocab` prints `ok`.

## Changes
- v-collocation-02 | usage[3] (make) | example "The training made a real difference." did not show the collocations listed (decision, effort, profit) | new example: "We made a decision before lunch." (zh twin updated)
- v-collocation-08 | usage[1] (host) | "host … a guest" is unnatural; line was thin | "<em>host</em> an event or a party: to organize it for guests. <em>The hotel will host the awards dinner.</em>" (zh twin updated)
- v-synonym-05 | why | quoted "jumped 40 percent" is not in the stem (stem has "jumping 40 percent") | "Visits went up by 40 percent (<em>jumping 40 percent</em>) in the first week, a large rise, and stayed <em>at that level</em> for the rest of the year. So the adverb is <em>markedly</em>."
- v-business-04 | gloss[1] | w "first month's salary" was glossed as hw/pos "salary n." with a zh for the whole phrase (mismatch; salary is also basic) | w "salary", zh "薪水"
- v-business-06 | why | quoted "the shipping company's own error" is not in the stem | "The delay was <em>its own error</em>, so the shipping company takes the <em>extra cost</em> on itself instead of charging the customer. That is <em>absorb</em>."
- v-family-03 | point zh | Chinese twin added "respectful 有禮貌的", which the English point does not say | "respective 各自的。"
- v-family-05 | point zh | Chinese twin added "comprehensive 全面的", which the English point does not say | "comprehensible to 某人：易懂的。"

## Key concerns
None. All 34 answer keys agree with the sentence meaning and the reviewed Chinese explanations.
