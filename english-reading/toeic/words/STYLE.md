# Word cards: style and format

The Workbook's word chapter holds one card per high-frequency TOEIC word. The word selection comes from the TOEIC Service List 1.2 (Browne & Culligan, CC BY-SA 4.0; files in `words/tsl/`), limited to words that appear in our questions. The learner memorises words mainly **through example sentences**, and wants each word tied to related words (family, synonyms, antonyms, collocations) so the words form a network.

The learner is a Taiwanese adult working toward TOEIC 700–850. English first; every English line has a Traditional Chinese (Taiwan) twin.

## One card

```json
{
  "w": "invoice",
  "pos": "n., v.",
  "zh": "發票、請款單；開發票",
  "def": ["A document that lists goods or services and asks for payment.", "列出商品或服務並要求付款的文件。"],
  "ex": [
    ["Please send the <em>invoice</em> to our accounts department.", "請把發票寄到我們的會計部。"],
    ["The supplier <em>invoiced</em> us for the extra parts.", "供應商就額外的零件向我們開了發票。"]
  ],
  "coll": [["issue an invoice", "開立發票"], ["pay an invoice", "支付發票款項"]],
  "family": [{"w": "invoicing", "pos": "n.", "zh": "開立發票（作業）"}],
  "syn": [{"w": "bill", "note": ["Everyday word; invoice is more formal and used between businesses.", "日常用語；invoice 較正式，多用於公司之間。"]}],
  "ant": [],
  "confuse": [{"w": "receipt", "note": ["A receipt shows you have paid; an invoice asks you to pay.", "收據證明已付款；invoice 是要求付款。"]}]
}
```

- `w`: the TSL headword exactly as given to you (lower case).
- `pos`: the parts of speech the card covers, from `n.` `v.` `adj.` `adv.` `prep.` `conj.` `pron.`, comma-separated.
- `zh`: short Chinese meanings for the senses that matter in business English.
- `def`: one plain English definition, max 20 words.
- `ex`: **4 to 6** example sentences. This is the most important part.
  - Original, natural business or everyday-work English (offices, travel, shops, hotels, deliveries, meetings, HR, finance), 6–20 words each.
  - Each uses the word (any inflection), wrapped in `<em>…</em>`.
  - Together they cover the main senses and patterns (e.g. noun and verb uses, a typical preposition, a typical collocation).
  - Vary the scenes. No two examples with the same structure.
- `coll`: 3–6 common collocations or patterns (`comply with`, `be eligible for`), each a real, frequent usage.
- `family`: 0–5 related forms that really exist and are useful (`verify` → `verification`, `verifiable`). Don't list inflections (verified, verifies).
- `syn`: 0–4 near-synonyms, each with a one-line note on how it differs (register, pattern, meaning). Only real near-synonyms.
- `ant`: 0–3 antonyms with `zh`, only where a clear opposite exists. `[]` is fine.
- `confuse`: 0–2 words learners often confuse with this one (look-alikes, false friends), with a one-line note.

## Hard rules
- Correctness first: every usage, collocation, family member and synonym must be real and current. If unsure, leave it out.
- No invented facts about the TOEIC (frequency, "appears often in the test", ranks).
- No praise, emoji, exclamation marks, or meta phrases.
- Only `<em>` tags, only inside `ex`.
- Do not write IPA; the build adds it from the CMU Pronouncing Dictionary.

Write a JSON array of cards. Check with `python3 words/check.py words/cards/<file>.json` until it prints `ok`.
