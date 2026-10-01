# Chapter lessons: style and format

Each chapter of The Workbook opens with a short lesson. The learner reads it, then practises that chapter's questions (they can skip it). The learner is a Taiwanese adult working toward TOEIC 700–850. They read English comfortably but want it plain, and they dislike clutter, filler and system talk.

## Voice
- English first. Every English line has a Chinese twin (Traditional Chinese, Taiwan), shown only when asked. Keep English grammar terms in the Chinese where natural (`make + 受詞 + 形容詞`).
- Plain, short sentences. Terms like *adjective*, *passive*, *base form* are fine, but the explanation must not lean on jargon: show it with the sentence.
- Say what to look at in the sentence and what it tells you. Practical, not academic.
- No praise, no exclamation marks, no emoji, no meta phrases ("Let's", "Remember", "Note that", "Tip:", "In this chapter we will").
- **No invented facts about the test**: no counts, percentages, "appears in every test", "the most common question type", score claims, or official rules. If you don't know it for certain, don't say it.
- All examples are original business English (offices, shops, hotels, deliveries, meetings). Company and person names are invented. Each example must be correct, natural English that really shows the rule.
- `<em>…</em>` marks the words that matter in an example, or a quoted word. No other HTML.

## Shape (one JSON file per chapter: `lessons/<unit>.json`)

```json
{
  "unit": "pos",
  "lead": ["What the chapter tests and how to recognise it, 1–2 sentences, max 40 words.", "中文"],
  "steps": [["Look at the four options: …", "中文"], ["…", "…"]],
  "rules": [
    {
      "head": ["Short rule name or pattern, max 10 words", "中文"],
      "body": ["What to check and why, max 45 words.", "中文"],
      "ex": [["Example with the key words in <em>…</em>.", "中文翻譯"], ["…", "…"]]
    }
  ],
  "pairs": [
    {"right": "A correct sentence.", "wrong": "The same sentence with the typical mistake.", "why": ["One sentence on the difference.", "中文"]}
  ],
  "lists": [
    {"head": ["Group name", "中文"], "items": [["make a decision", "做決定"], ["…", "…"]]}
  ],
  "traps": [["A common trap and how to avoid it, max 40 words.", "中文"]]
}
```

- `steps`: 2–4 short steps for working a question of this type (max 25 words each). Optional for vocabulary.
- `rules`: 3–7. Each rule has 1–3 examples, max 22 words per example.
- `pairs`: 2–4 right/wrong pairs (for listening: `right` = a question and a good response, `wrong` = the same question and a typical trap response, written like `Q: … / A: …`).
- `lists`: optional. Use for vocabulary (collocation groups, word families, near-synonym patterns) and for listening (typical question wordings). 0–4 lists, 4–12 items each. Every item must be a real, common usage.
- `traps`: 2–4.
- Keep the whole lesson readable in about five minutes.

## What each part covers
- **Grammar chapters**: build on the learner's existing handout `lessons/source_grammar_page.html` (Chinese, with English examples). Keep its substance (rules, traps), rewrite in this voice, and write fresh examples where needed. Drop its frequency claims (the bubbles and "考 7 到 9 題" style notes) completely.
- **Vocabulary chapters**: what kind of choice the question asks for (collocation, near synonyms, business terms, word families), how to decide (the word next to the blank, the preposition after it, the meaning in context), and lists of high-value business collocations and patterns.
- **Listening chapters**: what the question type sounds like, what to listen for, how the typical wrong answers work (word repetition, similar sound, right topic but wrong question), and the typical wording of questions. Examples are short original exchanges.

Check your files with `python3 lessons/check.py <unit> [<unit> …]` until each prints `ok`.
