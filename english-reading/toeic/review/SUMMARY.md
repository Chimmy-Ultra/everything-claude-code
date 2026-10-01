# 題庫審核摘要

題庫：文法 92 題、字彙 47 題、聽力 29 組（53 題），共 192 題。全部原創。（第一版 102 題；第三輪加了 39 題並修了 11 題；第四輪依 Fable 的新規則再加 51 題，見下方。）

## 流程
1. 出題（三個 agent 平行）。
2. **盲審**：另一個 agent 只拿到題目（沒有答案與解析），自己作答、檢查是否有兩個以上說得通的答案、是否像真題。
3. **難度校準**（同樣看不到答案）：每題判斷跟真題同考點的題比「偏簡單／相當／偏難」、在真題裡屬於「簡單／中等／困難」、風格相似度 1–5。
4. 依校準結果修題（偏簡單的改寫，並補上真題有、題庫沒有的題型），同時校對解析。
5. **改過的題重新盲審**。聽力題改完後全部重錄，並用 Whisper 語音辨識把每個音檔轉回文字和原稿比對。
6. 改過的題的解析，最後再由另一個 agent 獨立校對一次。

## 結果
- 每一輪盲審的答案都和答案鍵一致：第一輪 96/96，改題後的各輪 5/5、4/4、6/6、26/26、3/3。
- 沒有任何一題被標為「有兩個以上可辯護的答案」，也沒有任何一題被認出是真題或近似真題。
- 聽力 71 個音檔，語音辨識比對全部吻合（數字、序數、重音符號先統一再比）。

## 最後的難度分布（每題取最新一輪的判斷）
| 組別 | 題數 | 簡單 / 中等 / 困難 | 比真題偏簡單 / 相當 / 偏難 | 風格相似度 |
|---|---|---|---|---|
| 文法 A | 24 | 9 / 12 / 3 | 1 / 23 / 0 | 4.8 |
| 文法 B | 28 | 10 / 14 / 4 | 0 / 27 / 1 | 4.7 |
| 字彙 | 24 | 7 / 13 / 4 | 0 / 24 / 0 | 4.2 |
| 聽力 | 26 | 11 / 15 / 0 | 0 / 26 / 0 | 4.5 |
| 合計 | 102 | 37 / 54 / 11 | 1 / 100 / 1 | |

## Fable 獨立盲審（第二道把關）
原本的審核者和出題者是同一類模型，所以最後再請更強、不同的模型 Fable 對整個題庫（102 題）做一次盲審，同樣看不到答案、解析和之前的審核紀錄，並要求它主動找第二個說得通的答案。

- 答案：**102/102 與答案鍵一致**，全部信心最高；沒有任何一題被判為有疑義（mustFix 為零），也沒有認出任何真題或近似真題。
- 跟真題比：相當 99、偏簡單 2（g-tense-02、v-synonym-02）、偏難 1（g-conditional-02）。
- 難度分布（Fable 的判斷）：文法 簡單 28／中等 21／困難 3；字彙 14／9／1；聽力 9／17／0。Fable 認為文法和字彙比真題**偏簡單**，真題的中等題比例更高。
- 風格相似度：84 題 5 分、18 題 4 分，沒有 3 分以下。
- 建議修改（不影響答案正確性）：g-tense-02、v-synonym-02、g-voice-02（干擾選項 have been risen 不是真實存在的錯誤形式）、g-connect-03、g-participle-01（Web site → website）、g-pos-06／v-family-01（同一個字族重複當答案）、v-synonym-04、l-qr-03 與 l-talk-01（英式拼字與用字，真題文字多為美式）、g-toing-01（用了真實城市 Leeds）。
- 題庫缺的題型：動詞＋介系詞搭配、as … as、副詞位置、正式書信片語（in accordance with、on behalf of），以及聽力的三人對話和圖表題。

完整紀錄：`fable_blind_*.json`、`fable_solved.json`。

## 第三輪：找出偏簡單的根本原因後重出
Fable 指出第一版偏簡單。原因在出題規則（詳見 DESIGN.md 附錄二）：「錯誤選項的理由要能 45 字內講完，否則換掉」把最有鑑別度的誘答篩掉；出題者為了避免兩個答案而避開所有經典陷阱；難度目標 40/40/20 且由出題者自評；題幹限 25 字；聽力證據限 1–2 句。

改了規則（每題至少一個「近乎正確」的誘答、可以用真題陷阱、唯一答案交給 Fable 判斷、難度以盲審為準、題幹可到 35 字、聽力證據可跨句、加三人對話與圖表題）之後：
- 修了 Fable 點名的 11 題，新增文法 16、字彙 10、聽力 7 組（含三人對話、表格圖表題、較難的應答題）。
- **Fable 盲審 52/52 一致**，沒有必須修正的題；修正後又盲審 8 題，8/8 一致。
- Fable 的判斷：這批「明顯比第一版難、更接近真題」，用到真題常見陷阱（who/whom 插入句、that 子句原形、Each of … is、Those who … are、近義詞的介系詞搭配、圖表題）。但分布**仍偏簡單**：新文法 22 題裡簡單 9／中等 10／困難 3，字彙 13 題 5／7／1，聽力 6／10／1。出題者自評的困難題，Fable 多半判為中等。

結論：改規則有效，但「模型寫不出夠難的題」的傾向還在。若要更多困難題，下一步可以讓 Fable 直接出困難題，再由另一個模型盲審。

## 第四輪：照 Fable 寫的規則（WRITING_RULES.md）出新題
這一輪 Fable 只當顧問寫規則，不審題；出題與盲審都用一般模型。不改舊題，只出新題。

- 新增文法 24、字彙 13、聽力 8 組（14 題，含一組三人對話、一組運費表圖表題）。
- **盲審 51/51 與答案鍵一致**；沒有任何一題被判為有兩個可辯護的答案（mustFix 為零）。
- 建議修改（shouldFix）只採用一題：l-qr-14 的選項 A 原本「跟問句無關」而不是「跟問句矛盾」，改成跟 before you leave 衝突的 when I get back，重錄音檔，再單獨盲審一次：答案一致、判為困難、無疑義。其他建議（g-mandative-04 的 will be invoiced、v-collocation-11 的 occupied、v-collocation-12 的 at short warning）審核者判為誘答而非可辯護，保留不改。
- 難度（盲審的 band，不是出題者自評）：

| 區塊 | 題數 | 簡單 / 中等 / 困難 | 規則 5.2 的目標 | 達標？ |
|---|---|---|---|---|
| 文法 | 24 | 0 / 15 / 9 | 簡單 ≤20%、困難 ≥30% | 是（困難 38%） |
| 字彙 | 13 | 2 / 8 / 3 | 簡單 ≤20%、困難 ≥30% | 困難只有 23%，未達 |
| 聽力 qr | 5 | 1 / 2 / 2 | 簡單 ≤25%、困難 ≥25% | 是 |
| 聽力 conv/talk | 9 題 | 3 / 4 / 2 | 簡單 ≤25%、困難 ≥25% | 未達（每組各一題簡單） |

- 跟前幾輪比：第三輪文法 22 題只有 3 題困難（Fable 判），這一輪 24 題有 9 題（一般模型判，審核者不同，不能直接比）。
- **要注意的一點**：審核者把文法 9 題、字彙 3 題、聽力 4 題判為「比真題偏簡單」（vsToeic: easier），文法約 38%。規則 5.2 寫「任何一批 easier 超過一成，整批退回重做」。這一輪沒有整批重做：使用者指示不要改舊題、直接出新題；而且這些題答案正確、沒有歧義，band 都在中等或簡單。但規則沒有定義 easier 是跟「同考點的真題」還是「同難度的真題」比，審核者似乎把「中等裡偏低的題」也標成 easier。這個定義留給 Fable 下次修規則時處理。
- 同批重複：文法有約 10 題用分公司／新辦公室／倉庫場景，g-tense-07 和 g-tense-08 設計相同；字彙有 4 題題幹用 Because 開頭。下一輪出題時避開。

紀錄：`round4_blind_*.json`、`solved_*_round4.json`、`round4_reblind_l-qr-14.json`、`solved_listen_b_round4b.json`。

## 要知道的限制
- 這些都是**審核 agent 的判斷，不是統計**，沒有跟真人考生的作答資料比對過。前幾輪審核者和出題者是同一類模型；最後一輪改由 Fable 獨立盲審，結論一致。
- 整體仍偏「簡單到中等」，困難題比真題少。
- 聽力已有一組表格圖表題和一組三人對話，但沒有看圖題（需要圖片）；只有美式和英式口音。
- 真題的題型比例、題數、每題秒數等官方數字，頁面上一律不提。

各輪的原始紀錄都在這個資料夾：`blind_*.json`（給盲審者的題目）、`solved_*.json` / `calib_*.json`（盲審與校準結果）、`log_*.md` / `revised_*.json`（修改紀錄）。

## The Workbook: English notes (2026-10-01)
The page was renamed The Workbook and redesigned as a printed workbook at the learner's request. All 192 questions got English notes (`en/*.json`, style in `en/STYLE.md`): grammar and listening show only the rule and how to see it; vocabulary also shows how each other option word is used. The reviewed Chinese stays as a hidden twin.
- Seven writer agents drafted the notes from the reviewed Chinese explanations; five other agents reviewed every entry against the items and fixed 33 entries (logs: `en_review_*.md`). No answer key was questioned.
- Word-card phonetics come from the CMU Pronouncing Dictionary (`en/ipa.py`); two phrases it lacks (barcode scanning, minibar) show no phonetics rather than a guess.
