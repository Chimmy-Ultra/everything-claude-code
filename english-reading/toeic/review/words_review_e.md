# Word card review: e.json

32 cards reviewed; 21 cards changed; 55 changes. The other 11 cards were read in full and left as is: audit, copyright, defective, machinery, overpay, passport, pet, takeover, trademark, traveler, urgent.

Change counts by type: ant 6, coll 8, def 1, ex 29, family 3, syn 6, zh 2

`python3 words/check.py words/cards/e.json` -> ok (32 cards).

## Changes (one line each)

- accordingly: zh: "相應地、照著情況" -> "據此、配合情況" (Taiwan usage)
- accordingly: ex[0] rewritten: zh "相應" -> "據此"
- accordingly: ex[1] rewritten: three "so ... accordingly" frames in one card; now a passive billing sentence
- accordingly: ex[4] rewritten: repeated "so they can act accordingly" frame; now mid-sentence use
- accordingly: coll[2] changed: zh "相應調整" -> "據此調整"
- copier: family: removed "copying" (-ing form, not a useful separate member); added copy (n.)
- copier: syn photocopier note: softened US/UK claim (photocopier is also used in the US)
- patent: def: "only person" -> "only person or company"
- patent: ex[4] rewritten: "patent pending" is a fixed phrase and needs quotation marks
- evacuate: ex[2] rewritten: "were told/ordered to evacuate" repeated in ex 0 and 2
- evacuate: ex[3] rewritten: "must evacuate the floor" duplicated ex 0 structure
- evacuate: ex[4] rewritten: "The airline had to evacuate the terminal" is odd (airport authority evacuates) and repeated "to evacuate the X"
- hazard: ex[1] rewritten: zh "隱患" -> Taiwan wording
- hazard: ex[3] rewritten: "are a trip hazard" / "are a serious safety hazard" were the same frame
- hazard: coll[0] changed: zh "安全隱患" -> Taiwan wording
- hazard: coll[1] changed: zh "火災隱患" -> Taiwan wording
- inquire: ex[4] rewritten: "to inquire" infinitive frame duplicated ex 0
- inquire: syn query note: "put a question to an authority" was vague; rewritten
- interfere: ex[1] rewritten: "interferes in how" is unnatural; "in the way"
- interfere: ex[3] rewritten: three "X interfered with Y" frames (ex 0, 2, 3)
- interfere: coll[4] changed: "without interfering" is not a collocation
- interrupt: ex[1] rewritten: "power cut" is British; US "power outage"
- interrupt: ex[3] rewritten: three "[event] interrupted [thing]" frames (ex 1, 3, 4)
- mislead: ex[2] rewritten: "misled X by hiding/cutting off" repeated the same frame as ex 0
- misplace: ex[1] rewritten: three "[Subj] misplaced [obj]" frames (ex 0, 1, 2); now passive
- misplace: ant: removed "find" (not a true opposite of misplace; it is the result of searching)
- misplace: syn mislay note: dropped "old-fashioned" claim, kept "less common/more formal"
- occupancy: coll[4] changed: zh "使用許可證" -> Taiwan term 使用執照
- occupancy: syn: removed "tenancy" (a related legal term, not a near-synonym; note only contrasted them)
- occupancy: ant vacancy: zh now states the sense (hotel/rental occupancy vs vacancy)
- occupant: ex[0] rewritten: four "occupant of the X" frames
- occupant: ex[1] rewritten: same
- occupant: ex[3] rewritten: same
- occupation: ex[1] rewritten: "change occupation" (singular) unnatural
- occupation: ex[3] rewritten: "favorite weekend occupation" (pastime) is dated and off-sense for a business card
- occupation: coll[2] changed: plural is the natural form
- occupation: coll[4] changed: "occupation and income" is not a collocation
- overcharge: ex[1] rewritten: three "[Subj] overcharged X for Y" frames
- overcharge: ex[4] rewritten: zh clarified "多收"
- poorly: ex[2] rewritten: three "poorly + past participle" frames (ex 1, 2, 4)
- poorly: ex[5] rewritten: "did poorly" duplicated "sold/performed poorly"
- precede: ex[2] rewritten: two "that preceded/precedes" relative clauses (ex 2, 3)
- precede: family: removed "unprecedented" (derives from precedent, not from precede); kept precedent/precedence, which are the noun forms of the same Latin verb
- prospective: zh: "有望的" is ambiguous -> "潛在的、預期的、未來的"
- prospective: ex[3] rewritten: three "[verb] prospective [plural noun]" frames
- prospective: family: removed "prospectus" (same Latin root, not a derivative of prospective)
- recruitment: ant: removed dismissal, layoff (related HR events, not clear opposites of recruitment)
- turnover: ex[1] rewritten: "annual turnover" in dollars sounds American but is mainly British; pounds signals the British usage
- turnover: ex[4] rewritten: "scheme" is British; US "program"
- turnover: coll[2] changed: zh marks British usage
- turnover: ant retention: zh states the sense (staff turnover only)
- vacate: syn move out note: "Informal" was inaccurate (it is neutral)
- vacate: ant: zh now states the sense (spaces only)
- valid: syn: removed "legal" (not a synonym of valid; note only contrasted)
- valid: ant expired: zh states the sense (tickets, IDs); invalid kept

## Decisions on flagged items

- precede family: kept precedent and precedence (noun forms of the same Latin verb, transparent to learners); dropped unprecedented (derives from precedent).
- inquire/query: kept; query note rewritten. inquire is the US spelling (enquire is British).
- misplace/mislay: kept; mislay note no longer says old-fashioned. misplace/find antonym removed.
- turnover: kept `annual turnover` (sales sense) but marked as British usage in coll and example; revenue note already says US usage is revenue.
- occupancy/vacancy, vacate/occupy/move in, valid/expired, turnover/retention: kept, with the sense stated in the zh field. valid/invalid kept as plain opposites.
- recruitment dismissal/layoff, misplace find: removed (not clear opposites).
- Checked and left unchanged: no TOEIC frequency claims were found; all spelling is American (color, center, organized, program, outage).
- Not changed, low risk: audit (inspection/review synonyms are loose but the notes state the difference); occupant (tenant is a subtype, kept with its note); flawless as antonym of defective (acceptable, superlative).
