# English explanations: style and format

The Workbook's explanations are written in English. The learner is a Taiwanese adult working toward TOEIC 700–850. They read English comfortably, but explanations must be plain. Chinese is kept as a hidden backup: each English line has a Chinese twin, shown only when the learner asks.

These rules come from the learner's own feedback on a demo. Follow them exactly.

## What the learner sees after answering

**Grammar (`gap`, type grammar)**
1. `point`: the rule only, as short as possible. No qualifiers, no "however long…", no "remember", no "note that".
   - Good: `make + object + adjective.` / `The blank is the subject: use a noun.` / `forbid someone to do something.`
   - Bad: `make + object + adjective, however long the object is.`
2. `why`: how to see it **in this sentence**. Quote the sentence's own words in `<em>…</em>`. Name the answer at the end. No word limit: say as much as it takes.
   - Good: `The object of <em>makes</em> is the whole phrase <em>the items that customers order most often</em>. The blank says what those items become, so it needs an adjective: <em>accessible</em>.`
3. **No lines about the wrong options.** Not one.

**Vocabulary (`gap`, type vocab)**
1. `point` and `why` as above.
2. `usage`: for **each wrong option**, one line on how that word is really used: its pattern or meaning, then one short original example sentence in `<em>…</em>`. Put `null` at the answer's index. No word limit. Don't say "this is wrong because"; just show how the word is used.
   - Good: `<em>prohibit</em> someone <em>from</em> doing something. <em>The rules prohibit staff from eating at their desks.</em>`
   - Good: `<em>prevent</em> someone <em>from</em> doing something; it means stopping it from happening, not a rule. <em>The fence prevents visitors from entering the site.</em>`

**Listening (`qr`, `conv`, `talk`)**: for each question, `point` and `why` only.
- `point`: the skill in a few words (e.g. `An indirect answer: someone else will handle it.` / `Look for the reason given after "because".`).
- `why`: quote the deciding words from the transcript in `<em>…</em>` and connect them to the answer. For graphic questions, say which row or cell and why. No word limit.
- No lines about the wrong options.

## Word cards (`gloss`)

After answering, the learner can tap words in the sentence (or transcript) to see a card. Pick the words a TOEIC 700 learner may not know: business terms, less common verbs, and phrases. Skip basic words (company, meeting, report…).
- Gap items: 2–4 entries. Listening sets: 3–5 entries.
- `w`: the text **exactly as it appears** in the stem or a transcript line (same case, same inflection, whole word or phrase). The page underlines this text, so it must match.
- `hw`: the dictionary form (`pickers` → `picker`).
- `pos`: one of `n.` `v.` `adj.` `adv.` `prep.` `phr.` (`phr.` for multi-word phrases that aren't simple nouns).
- `zh`: Traditional Chinese (Taiwan) meaning **in this context**, short.
- `ex`: one original example sentence, at most 12 words, natural business English, using `hw` (any inflection).
- Do **not** write IPA. A script adds it from a pronunciation dictionary.

## Chinese twins

Every `point`, `why` and `usage` line is a pair `[English, Chinese]`. The Chinese is a short, natural Traditional Chinese (Taiwan) rendering of the English line. You may reuse the item's existing Chinese explanation if it says the same thing. English terms in the Chinese stay in English (`make + 受詞 + 形容詞`).

## Hard rules
- Never change a stem, option, transcript, answer or anything in the `items_*.py` files. Only write the JSON file you are given.
- The explanation must agree with the answer key. If you think a key is wrong, still explain the key, and list the id under `"_flags"` with a one-line reason.
- No invented facts about the TOEIC (no scores, percentages or "this appears in X% of tests").
- No praise, no exclamation marks, no emoji, no meta phrases ("Let's", "Remember", "Note that", "Tip:").
- Use `<em>` only for quoted words and example sentences. No other HTML.
- Straight ASCII apostrophes and quotes are fine. Use `…` for an omitted part of a quote.

## File format (`en/<items file name>.json`)

```json
{
  "g-pos-09": {
    "point": ["<em>make</em> + object + adjective.", "make + 受詞 + 形容詞。"],
    "why": ["The object of <em>makes</em> is …", "makes 的受詞是 …"],
    "gloss": [{"w": "layout", "hw": "layout", "pos": "n.", "zh": "配置、布局", "ex": "We changed the layout of the lobby."}]
  },
  "v-synonym-10": {
    "point": ["…", "…"], "why": ["…", "…"],
    "usage": [["<em>prohibit</em> someone <em>from</em> …", "prohibit 人 from Ving。"], ["…", "…"], ["…", "…"], null],
    "gloss": […]
  },
  "l-conv-07": {
    "q": [{"point": ["…", "…"], "why": ["…", "…"]}, {…}, {…}],
    "gloss": […]
  },
  "l-qr-13": {"q": [{"point": ["…", "…"], "why": ["…", "…"]}], "gloss": […]},
  "_flags": []
}
```

Check your file with `python3 en/check.py <items file name>` before you finish; it must print `ok`.
