# English review: reading set A (items_read_a, r-p6-01 to r-p6-04)

Scope: 4 Part 6 items, 16 questions (point and why, English and Chinese), 22 word cards. Checked against `en/STYLE.md`, the passages, options and keys, and the Chinese explanations in `items_read_a.py`. `python3 en/check.py items_read_a` prints ok. The notes file was not edited; every replacement below is a drop-in string for the named field (index 0 is the English line, index 1 the Chinese twin).

## What was checked and found sound

- Keys: all 16 explanations lead to the keyed answer; `_flags` stays empty (no key looks wrong).
- Clues: every why uses the same deciding clue as the Chinese explanation in `items_read_a.py`, and points to the right place (the sentence before, the next sentence, paragraph 3, the header date, the article date).
- Quotes: every quoted phrase (in em tags) was matched by script against the passage text (or against the keyed option for the inserted-sentence blanks, or the passage with the answer filled in, such as `submitted late`). No misquotes found.
- Grammar statements: `late` is both adjective and adverb; `Should you prefer` = `If you prefer` with `if` left out; the parenthetical `our records show` does not change the subject role of the relative pronoun; `given the opportunity to`; the tense chains in r-p6-01 q3 and r-p6-03 q1. All correct.
- STYLE.md: no lines about wrong options, no banned phrases, no exclamation marks, only em tags as markup. The remark that `rejected` sounds negative (r-p6-02 q0) is about the passage, not an option, so it is allowed.
- Chinese twins: faithful to the English, Taiwan Traditional Chinese, English terms kept in English. No simplified characters or mainland terms.
- Word cards: all 22 `w` strings occur in the documents with the same case (including `Conversion`); counts are 5, 5, 6, 6 (limit 3 to 6); every example is 6 to 11 words and uses the headword; parts of speech and glosses fit the context. Not changed: `rejected` is a participial adjective in the passage but its card teaches the verb `reject`, which is acceptable under the dictionary-form rule.

## mustFix

None.

## shouldFix

All are clarity or precision fixes. Each leaves the quotes, the clue and the keyed answer unchanged.

### 1. r-p6-01, q[1].why (shouldFix)

Problem: Two small clarity problems. 'One elevator is singular: it.' reads oddly (the elevator is not 'singular', the noun is). The Chinese 要留下來的 can be misread as 'what stays', when the point is what the lower-floor tenants leave free for others.

- EN: `Tenants on the lower floors are asked to <em>leave … free for residents of the upper floors</em>. What they leave free is the elevator in the sentence before: <em>The elevator that remains in service</em>. Paragraph 1 says only one elevator is shut down at a time, so just one is running. That is one elevator, a singular noun, so the pronoun is <em>it</em>.`
- ZH: `低樓層住戶被要求 leave … free for residents of the upper floors。他們要空出來給高樓層的，是前一句的 The elevator that remains in service。第一段說一次只停一部，所以施工期間只有一部在運轉。一部電梯是單數名詞，代名詞用 it。`

### 2. r-p6-01, q[2].why (shouldFix)

Problem: '6 to 8 a.m. is its `early in the morning`' is ambiguous: 'its' could point to the freight elevator or to the 6 to 8 a.m. window. The quote and the logic are right; only the pronoun needs fixing.

- EN: `The sentence itself does not decide; paragraph 3 does. It says the freight elevator is <em>open to tenants for these deliveries from 6 to 8 a.m. each weekday</em>. <em>these deliveries</em> are the furniture and large items in the blank's sentence, and 6 to 8 a.m. is the time that sentence calls <em>early in the morning</em>. So large items may come in through the loading dock at that time, and at any other time they are postponed: <em>unless</em>.`
- ZH: unchanged (it already says 那句的 early in the morning, which is clear).

### 3. r-p6-02, q[0].why (shouldFix)

Problem: '`far fewer` rejected claims is good news' pairs a plural subject with 'is' inside a quote, which reads as a slip. Same meaning, cleaner grammar below. The Chinese twin only needs to name the phrase the same way.

- EN: `The sentence before says the sales staff <em>reported far fewer rejected claims than they had with the paper forms</em>. <em>rejected</em> sounds negative, but <em>far fewer</em> of them means good news: the trial worked. Because of this, Tallyway will replace the paper forms for everyone. The blank's sentence is the result of the one before: <em>As a result</em>.`
- ZH: `前一句說業務部同仁 reported far fewer rejected claims than they had with the paper forms。rejected 雖然是負面字，但被退回的申請 far fewer（少很多）是好消息：試用很成功。因為這樣，全公司都改用 Tallyway。這一句是前一句的結果：As a result。`

### 4. r-p6-03, q[0].why (shouldFix)

Problem: 'The missing sentence is the point that this explains' is vague: 'this' could mean the missing sentence itself, so the direction of the explanation is unclear. The quotes are exact and the answer is right.

- EN: `The sentence before says orders <em>have nearly doubled</em> and the ovens <em>now run around the clock</em>, so Mill Road is working at its limit. The sentence after says <em>The bakery sits on a narrow lot between a school and a row of houses</em>: there is no room to build more there. So the blank states the conclusion that the narrow lot supports: <em>Expanding the original bakery was never an option.</em> That is why the company is opening a second site.`
- ZH: unchanged.

### 5. r-p6-03, q[1].point (shouldFix)

Problem: 'dateline' is newspaper jargon; a TOEIC 700 reader may not know it. The why already says 'the date June 12', so the point should use the same plain words.

- EN: `Tense: the article's date shows that March is past.`
- ZH: unchanged (the Chinese point already says 報導日期).

### 6. r-p6-04, q[0].point (shouldFix)

Problem: 'the first paragraph' is ambiguous in a letter: on the page, 'Dear Subscriber,' is a separate line above the first body paragraph, and a reader may count it. Anchor the clue by position instead.

- EN: `Same or different? Check the start of the letter.`
- ZH: `相同還是不同？看信的開頭。`

### 7. r-p6-04, q[0].why (shouldFix)

Problem: Same problem as the point: 'The first paragraph' can be read as the salutation. The quotes are exact and the answer is right.

- EN: `The first paragraph after <em>Dear Subscriber</em> says the printed copy <em>often arrives a week or more after the first of the month</em>. The blank's sentence says <em>the digital edition will reach you on the first of every month</em>. The two editions differ, so the answer is <em>Unlike</em>.`
- ZH: `稱呼 Dear Subscriber 後面的第一段說紙本 often arrives a week or more after the first of the month。空格這一句說 the digital edition will reach you on the first of every month。兩種版本不同，所以用 Unlike（和……不同）。`
- Note: The item's own Chinese explanation also says 第一段; that file is left as is, since it is the same clue.

### 8. r-p6-04, q[2].why (shouldFix)

Problem: Misleading as written: 'The blank comes right before the verb have already paid' is false for the printed sentence, where `our records show` sits between the blank and the verb. It is only true after the phrase is taken out. A reader who checks the passage will see the mismatch. Also, 'a subject that refers to people' is loose; say the blank stands for the people just named.

- EN: `<em>our records show</em> is an extra phrase placed inside the clause. Without it, the sentence reads <em>Subscribers … have already paid for next year</em>, and the blank sits right before the verb <em>have already paid</em>. So the blank is the subject of that verb and stands for the people just named: <em>who</em>.`
- ZH: `our records show 是插在關係子句中間的插入語。拿掉它，句子是 Subscribers … have already paid for next year，空格就緊接在動詞 have already paid 前面。所以空格是這個動詞的主詞，代表前面提到的人：who。`

### 9. r-p6-04, q[3].why (shouldFix)

Problem: The reason 'after the comma comes an instruction, so the first half must be a condition' is asserted, not shown, and a learner can fairly ask why an instruction needs a condition. The real reason is in the meaning: the box applies only to readers who want the magazine by mail. Quotes are exact and the grammar statement about `should` is correct.

- EN: `After the comma comes what the reader should do: <em>please check the box on the enclosed form</em>. It applies only to readers who want the magazine by mail, so the first half sets that condition: <em>you prefer to keep receiving the magazine by mail</em>. <em>Should you prefer</em> is a formal way to say <em>If you prefer</em>: <em>if</em> is left out and <em>should</em> comes before the subject.`
- ZH: `逗號後面是要讀者做的事：please check the box on the enclosed form。這件事只適用於想繼續收紙本的讀者，所以前半句是這個動作的條件：you prefer to keep receiving the magazine by mail。Should you prefer 是 If you prefer 的正式說法：省略 if，把 should 放到主詞前面。`

## Verdict

The English notes for r-p6-01 to r-p6-04 are accurate and ready to use. All 16 explanations lead to the keyed answer through the same clue as the Chinese explanations, every quoted phrase matches the passage or the keyed option, the grammar statements are correct, and the Chinese twins say the same thing in natural Taiwan Traditional Chinese. The 22 word cards are correctly formed, fit their context and respect the length limits. There are no mustFix items. The nine shouldFix entries (eight places; r-p6-04 q0 has a point and a why) are small: two ambiguous pronoun references (r-p6-01 q1 and q2), one plural-subject slip inside a quote (r-p6-02 q0), one vague 'this' (r-p6-03 q0), one piece of newspaper jargon (r-p6-03 q1 'dateline'), one ambiguous 'first paragraph' in a letter with a salutation (r-p6-04 q0, point and why), one sentence that is only true after the parenthetical is removed (r-p6-04 q2), and one reason that is asserted rather than shown (r-p6-04 q3). The last two are the ones most worth applying, because a learner who checks the passage against the note could be confused by them. All replacement strings were run through `en/check.py` on a patched copy and pass.
