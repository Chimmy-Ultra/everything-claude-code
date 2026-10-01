# Word stories: style and format

The word chapter is a set of short scene stories, not a word list. The learner hates the feel of a vocabulary book; they learn words by meeting them in sentences. Each story is a short piece of workplace life that naturally uses 8–11 of the high-frequency words (TOEIC Service List words that have a card in `words/cards/*.json`). Tapping a word opens its card.

## Plan (`words/stories/plan.json`)
```json
[{"id": "s01", "scene": "Airport, delayed flight", "words": ["passport", "luggage", "valid", "…"]}]
```
Every card word appears in exactly one story's `words`. Group words that would really meet in one scene.

## One story (`words/stories/<id>.json`)
```json
{
  "id": "s01",
  "title": ["The 7:40 to Denver", "七點四十分飛丹佛的班機"],
  "paras": [
    ["Mia reached the counter with her {{passport|passport}} in one hand and …", "米亞一手拿著護照……"],
    ["…", "…"]
  ]
}
```
- `title`: a short, concrete title (a moment, not a topic label), with a Chinese twin.
- `paras`: 3–5 paragraphs, 130–220 English words in total. Each paragraph is `[English, Chinese]`; the Chinese is a natural Traditional Chinese (Taiwan) translation of that paragraph.
- Mark each target word once, where it first carries meaning: `{{headword|text as written}}`, e.g. `{{inquire|inquired}}`, `{{valid|valid}}`. The headword must be one of this story's planned words. Every planned word is marked exactly once.
- Write a real little story: people with names, a small problem, a turn, an ending. Plain, natural American English at TOEIC 700–850 level; varied sentences; dialogue is fine. Each target word used in its common business sense, in a sentence that makes its meaning guessable.
- No lists, no definitions inside the story, no "Today we will learn". No claims about the TOEIC.
- Don't reuse sentences from the questions (`items_*.py`) or from the cards' examples.

Check with `python3 words/check_stories.py` until it prints ok.
