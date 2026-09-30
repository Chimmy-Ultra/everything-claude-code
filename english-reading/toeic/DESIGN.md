# TOEIC 練習室 — 設計文件

給今晚要動手蓋頁面的人。每一節都直接下決定，理由一句話帶過；能抄的格式都寫成可以照抄的樣子。

**頁面名稱**：TOEIC 練習室（`<title>` 用這四個字）。
**檔案配置**（沿用本資料夾其他頁的慣例）：`english-reading/toeic/` 底下放 `content.py`（題庫）、`make_audio.py`（Kokoro 產 mp3 到 `audio/`）、`template.html`、`build_page.py`（把題庫以 JSON 塞進 `<script type="application/json" id="bank">` 並做檢查，輸出 `toeic.html`）。發佈時 `toeic.html` 是主頁，`audio/**` 用 `files` 一起發。Hub 頁加一個「Exam」區塊連過來。

**貫穿全頁的三條規矩**
1. 頁上不出現任何「官方」數字：沒有題數、沒有每題秒數、沒有分數換算。計時器的秒數是學習者自己設的，介面就叫「自訂節奏」。
2. 手寫題庫每題都經過審核才發佈；Claude 在執行期或之後寫進 db 的題目一律標「Claude 出題・未審核」，不會混進手寫題庫。
3. 解釋短、只答這題問的事。每段有字數上限，`build_page.py` 超過就警告。

---

## 1. 每一題的流程

### 作答前
- 頂列：左邊「‹ 離開」，中間進度 `7 / 20`，右邊難度小點（●、●●、●●●）。
- **綜合／依題型模式下，作答前不顯示考點名稱**——「主動與被動」四個字就等於提示答案；「依考點練習」模式本來就知道，才顯示。
- 題幹：空格顯示為 `______`，字級 18px 以上。四個選項 A–D 各是一整條可點的按鈕，高度至少 48px，選項順序每次顯示都重洗（seed = itemId + sessionId，同一場內重看順序不變）。
- 選項上方一顆小開關「我是猜的」，預設關、每題答完自動關。**一點選項就送出**，不做「先選再按確認」的兩段式：學習者要的是節奏，有用的訊號只有「我在猜」，不是「我很確定」。
- 作答秒數從題目顯示到點選項為止，靜默記錄，不顯示碼表（節奏模式除外，見第 4 節）。

### 作答瞬間
- 點下的選項立刻變綠或紅；正確選項一律變綠；其他選項變淡。不用動畫延遲。
- 答錯或「猜的」開著答對：畫面下方浮一行「已加入錯題庫」。

### 作答後：解釋卡
解釋卡直接在選項下方展開，不換頁。**立即可見**的部分要能在一個手機螢幕內看完：

```
✔ 答對了 · 12 秒                                  [☆ 收藏] [⚑ 有問題]
┌ 考點 · 動詞時態 ──────────────────────────────────┐
│ 規則  by the time + 未來時間 → will have + p.p.          │
│ 為什麼是 (B) will have reviewed                       │
│   by the time the auditors arrive next Monday 是未來    │
│   的截止點，「到那時已經做完」用 will have + p.p.        │
│ 其他選項                                             │
│   ▶ (A) has reviewed  現在完成式不能配未來的截止點      │  ← 學習者選的排第一、加底色
│     (C) reviewed      過去式，時間方向相反               │
│     (D) is reviewing  進行式只講「正在做」，沒有「做完」  │
│ By the time the auditors arrive next Monday, the      │
│ finance department will have reviewed all the invoices.│
│ 等下週一稽核人員到的時候，財務部就已經把所有發票審完了。   │
│ [詞彙 ▾]   [文法頁：動詞時態 ↗]   [問 Claude ▾]          │
└──────────────────────────────────────────────────┘
                     [ 下一題 → ]
```

- 「其他選項」三行：學習者選錯的那一項排最前並加底色；答對時照 A–D 順序。
- **藏在點一下後面**：`詞彙`（2–4 個字＋中文）、`問 Claude`（第 6 節）。
- `文法頁：動詞時態 ↗` 連到「多益文法考點」整頁（那頁沒有 hash 定位，所以規則正文一定寫在題目的 `point` 欄，連結只是「想多讀」用）。字彙題與聽力題沒有這顆按鈕。
- 字數上限（以字串長度計，英文字母與空格也算）：`point` ≤ 40、`why` ≤ 90、每條 `wrong` ≤ 45、`zh` 一句完整翻譯。理由：學習者明講喜歡「問什麼答什麼」的短解釋，超過就是離題。
- 「下一題」固定在底部；桌機按 Enter。

### 確信度（「我是猜的」）拿來做什麼
- 猜對 = 不算會。這一題進錯題庫，`reason: "guess"`。
- 統計頁每個考點多一欄「猜對」，猜對多的考點就是知識不穩的考點，比正確率更誠實。
- 場次總結把「猜對的題」獨立列一段。
- 這是後設認知（知道自己會不會）的應用，只用來分流，不算分。

---

## 2. 錯題庫

### 進入
| 情況 | 進入？ | `reason` |
|---|---|---|
| 答錯 | 是 | `wrong` |
| 猜的開著且答對 | 是 | `guess` |
| 節奏模式超時但答對 | 否（只記 `timedOut`） | — |
| 確定且答對 | 否 | — |

已在庫中的題再答錯：`wrongCount` +1，`level` 歸 0。

### 複習排程（Leitner 階梯，間隔是我們自己設的，不是研究數字）
`level` 0→1→2→3，對應下次複習間隔 1、3、7、14 天。複習時答對且不是猜的 → 升一級並照新間隔排 `due`；答錯或猜對 → 歸 0、明天再來。**level 3 再答對一次即「畢業」**：`graduatedAt` 寫入，預設不再出現，但保留紀錄可查。

理由：間隔重複（spacing）與提取練習（retrieval practice）的效果是學習研究裡最穩的兩條，見 Cepeda et al. (2006, *Psychological Bulletin*) 與 Roediger & Karpicke (2006, *Psychological Science*)。具體天數選常見的倍增序列，不宣稱最佳。

### 已知風險與對策
同一題看第三次，記的是「這題答 B」不是規則。對策：(1) 選項每次重洗；(2) 複習畫面把答錯次數與考點放在題幹上方提醒「這題考的是規則」；(3) 之後由 Claude 依錯題庫產「同考點變體題」（第 5、6 節）。

### 學習者怎麼看、怎麼管
- 首頁一張卡：「今日待複習 N 題」，點了直接開複習場。
- 錯題庫頁：預設**依考點分組**（每組顯示題數、最近答錯日期），可切到**依日期**（最近進庫的在上）。篩選 chip：`待複習｜全部｜猜對的｜已畢業`。搜尋框比對題幹、筆記、考點名稱。
- 每列：題幹（空格處顯示正確答案、粗體）、考點、`錯 2 次`、`下次 9/30`、筆記圖示。點列展開解釋卡（同第 1 節的卡），底部有「筆記」文字框（存到 `toeic_marks`，輸入停 1 秒才寫）與「移出錯題庫」。
- 移出 = 寫 `removedAt`，不刪文件；「已畢業」與「已移出」都在 `全部` 篩選裡可以找回。

---

## 3. 聽力

### 做得到的題型（純 TTS、無圖）
| 題型 | 內容 | 做法 |
|---|---|---|
| Part 2 型 應答問題 `qr` | 一句問句/敘述＋三個口說回應，選項不印出來 | 問句一個聲音、三個回應另一個聲音；畫面只有 A/B/C 三顆鈕 |
| Part 3 型 簡短對話 `conv` | 2 人（之後可 3 人）6–9 句，配 3 題四選一（實作時依校準結果從 2 題改為 3 題，跟真題一致） | 每句一個 mp3，頁面串播 |
| Part 4 型 簡短獨白 `talk` | 1 人 90–120 字，配 3 題（同上，實作時改） | 同 `conv` 的渲染，說話者只有一位 |

Part 1 看圖題與圖表題（表格版本可以之後用 HTML 表格做，見第 6 節）今晚不做。

**腔調要說清楚**：Kokoro 只有美式與英式，沒有澳洲與加拿大腔。設定頁寫一行「本頁音檔為美式與英式合成語音」，不要假裝涵蓋全部。

### 聲音配置（固定六個，其他頁已驗證過的優先）
`af_sarah`（美女）、`am_michael`（美男）、`bf_emma`（英女）、`bm_george`（英男）、`af_bella`（美女 2）、`bm_lewis`（英男 2）。每題在 `audio.lines[].voice` 明寫；對話固定一男一女，同一題內腔調可混（現實裡也會）。題目層級記 `accent: "us" | "uk" | "mixed"` 供之後篩選。

### 播放規則
- 一定要有播放鈕：行動瀏覽器只允許使用者點過之後才播。**整頁只用一個 `<audio>` 元素**，第一次由學習者點「開始」解鎖，之後換 `src` 串播（`ended` 事件接下一段，段與段間隔 `gapMs`，Part 2 回應之間預設 900 ms）。每題仍保留「▶ 重播」當備援。
- **練習模式（預設）**：無限次重播；速度 0.85× / 1× / 1.15×，用 `audio.playbackRate`（不預錄多個速度，省檔案）；可逐句點播（作答後）。
- **嚴格模式**（設定頁開關）：整段只播一次、不能暫停、作答後才解鎖重播。
- `conv`/`talk` 的題目與選項**在播放時就顯示**——正式考試題本上印著題目，邊聽邊看題是要練的技能；`qr` 的 A/B/C 鈕在第一次播完才啟用。
- 聽力題不計作答秒數，節奏模式的計時器不套用。

### 逐字稿與解釋
- 作答前逐字稿隱藏（兩種模式都一樣）。
- 作答後展開逐字稿：每句一列，說話者標籤（W / M），**證據句加底色**（`explain.evidence` 指到的行），點任一句重播該句；「顯示中文 ▾」展開每句中文。
- 解釋卡結構同第 1 節，但「考點」換成聽力技巧標籤，`why` 必須寫出**改述對應**（音檔說的 → 選項寫的），`wrong` 標明陷阱類型：`同字陷阱`（選項重複聽到的字但意思不對）、`答錯問句類型`（wh 問句回 Yes/No）、`張冠李戴`（是另一位說話者做的事）。

聽力技巧標籤（`unit` 欄）：`qr-wh` wh 問句、`qr-yesno` Yes/No 與附加問句、`qr-indirect` 間接回答、`conv-topic` 主旨/場合、`conv-detail` 細節、`conv-intent` 意圖/推論、`conv-next` 下一步、`talk-topic`、`talk-detail`、`talk-next`。

---

## 4. 模式與導覽

單頁應用，畫面用 view 堆疊切換，**每個畫面左上都有「‹ 返回」**，不依賴瀏覽器上一頁（在 Claude app 內不可靠）。畫面：`home` / `session` / `summary` / `bank` / `stats` / `settings`。

### 首頁（由上到下）
1. 「今日待複習 N 題 → 開始複習」（N = 0 時顯示「錯題庫沒有到期的題」）。
2. 快速開始四顆：`文法 10 題`、`字彙 10 題`、`聽力 5 題`、`綜合 20 題`。長按或旁邊的 ⚙ 可改題數（10 / 20 / 自訂）。
3. 「依考點練習」：15 個文法單元＋4 種字彙類型＋聽力技巧，每列顯示 `做過 12 · 正確 75% · 猜對 2`，點了就開該考點的一場（題數 = min(10, 該考點可用題數)）。
4. 「Claude 給你的加練」：只有 `toeic_added` 有未做過的題時才出現。
5. 底列：`錯題庫 (N)`、`統計`、`設定`。右上角小字：`已同步`（db 可用）或 `本機儲存`。

### 出題規則（一場的組成）
- 綜合 20 題 = 10 文法 + 6 字彙 + 4 聽力；文法與字彙隨機交錯（交錯練習有助分辨考點），**聽力集中放在最後**並顯示「戴上耳機」分隔，因為實際上要換情境。
- 選題優先序：沒做過的 → 做過最久的；正確率低於 70% 的考點權重加倍（70% 是我們的設定，可在程式頂端改）。錯題庫裡的題不在一般場次出現，它們走複習場。
- 場次進行中每答一題把狀態存到 localStorage；重開頁面看到「繼續上次的場次？」。

### 節奏模式（設定頁開關，預設關）
學習者自己設每題秒數（預設選項 20 / 30 / 45 秒，介面寫「自訂節奏，非官方時間」）。題目上方一條倒數進度條；到時**不會自動跳題**，只把這題標 `timedOut: true`，總結會顯示「超時 N 題」。理由：練的是「在時限內做決定」，強制跳題只會增加挫折。

### 場次結束：總結頁
- 大字 `15 / 20`、總時間、文法／字彙平均秒數。
- 「錯的題」清單（題幹＋考點，點開看解釋）、「猜對的題」清單。
- 本場依考點的小表（每考點 對/總）。
- 「已加入錯題庫 N 題」。
- 按鈕：`再練這場錯的`（只抽這場錯的＋猜對的，立刻再做一輪）、`再來一組`、`回首頁`。

---

## 5. 資料模型

### 題目 schema（`content.py` 裡的 dict，`build_page.py` 轉成 JSON）

共同欄位：

| 欄位 | 型別 | 說明 |
|---|---|---|
| `id` | string | `g-<unit>-<nn>`（文法）、`v-<unit>-<nn>`（字彙）、`l-<format>-<nn>`（聽力）、`c-<unit>-<yyyymmdd>-<nn>`（Claude 之後加的）。全域唯一 |
| `type` | `"grammar" \| "vocab" \| "listen"` | |
| `format` | `"gap" \| "qr" \| "conv" \| "talk"` | 文法與字彙都是 `gap` |
| `unit` | string | 文法：15 個單元 id；字彙：`collocation \| synonym \| business \| family`；聽力：第 3 節的技巧標籤 |
| `level` | 1 \| 2 \| 3 | 見第 7 節 |
| `source` | `"hand" \| "claude" \| "claude-runtime"` | 手寫題一律 `hand` |
| `reviewed` | boolean | 手寫題發佈時必為 `true` |
| `v` | integer | 題目內容版本，改題就 +1（錯題庫紀錄會帶 `v`，之後可以知道是改前還是改後答的） |

#### 文法題範例
```json
{
  "id": "g-tense-04", "type": "grammar", "format": "gap", "unit": "tense", "level": 2,
  "source": "hand", "reviewed": true, "v": 1,
  "stem": "By the time the auditors arrive next Monday, the finance department ______ all the invoices.",
  "options": ["has reviewed", "will have reviewed", "reviewed", "is reviewing"],
  "answer": 1,
  "explain": {
    "point": "by the time + 未來時間 → will have + p.p.",
    "why": "by the time the auditors arrive next Monday 是未來的截止點，「到那時已經做完」用 will have reviewed。",
    "wrong": ["現在完成式不能配未來的截止點", null, "過去式，時間方向相反", "進行式只講「正在做」，沒有「做完」"],
    "zh": "等下週一稽核人員到的時候，財務部就已經把所有發票審完了。",
    "vocab": [["auditor", "稽核人員"], ["invoice", "發票、請款單"]]
  }
}
```
`answer` 是原始 `options` 的索引；`wrong` 與 `options` 同序，正解位置放 `null`。頁面重洗選項時只動顯示層，紀錄一律存原始索引。

#### 字彙題範例
```json
{
  "id": "v-collocation-03", "type": "vocab", "format": "gap", "unit": "collocation", "level": 1,
  "source": "hand", "reviewed": true, "v": 1,
  "stem": "The committee is expected to ______ a decision on the merger by Friday.",
  "options": ["reach", "arrive", "come", "do"],
  "answer": 0,
  "explain": {
    "point": "搭配詞：reach / make a decision",
    "why": "decision 的動詞搭配是 reach 或 make；空格後直接接受詞，所以是 reach a decision。",
    "wrong": [null, "要說 arrive at a decision，缺了 at", "要說 come to a decision，缺了 to", "do 不和 decision 搭配"],
    "zh": "委員會預計在星期五前對這樁併購案做出決定。",
    "vocab": [["merger", "併購"], ["committee", "委員會"]]
  }
}
```

#### 聽力題範例（Part 2 型）
```json
{
  "id": "l-qr-04", "type": "listen", "format": "qr", "unit": "qr-wh", "level": 1,
  "source": "hand", "reviewed": true, "v": 1, "accent": "mixed",
  "audio": {
    "dir": "audio/l-qr-04", "gapMs": 900,
    "lines": [
      {"file": "q.mp3", "who": "W", "voice": "bf_emma",   "text": "When is the quarterly report due?"},
      {"file": "a.mp3", "who": "M", "voice": "am_michael", "text": "By the end of next week."},
      {"file": "b.mp3", "who": "M", "voice": "am_michael", "text": "Yes, it's on the second floor."},
      {"file": "c.mp3", "who": "M", "voice": "am_michael", "text": "The report was very detailed."}
    ]
  },
  "transcriptZh": ["季報什麼時候要交？", "下週末前。", "是的，在二樓。", "那份報告寫得很詳細。"],
  "questions": [{
    "q": null, "options": null, "answer": 0,
    "explain": {
      "point": "When 問時間，要找講「時間點」的回應",
      "why": "By the end of next week 直接回答了 when。",
      "evidence": [1],
      "wrong": [null, "答錯問句類型：wh 問句不能用 Yes 回，而且 floor 答的是地點", "同字陷阱：重複 report，但講的是內容不是時間"],
      "vocab": [["quarterly", "每季的"], ["due", "到期、該交"]]
    }
  }]
}
```
`qr` 的 `options` 為 `null`，頁面固定畫 A/B/C；`evidence` 指 `audio.lines` 的索引。

#### 聽力題範例（Part 3 型，節錄）
```json
{
  "id": "l-conv-02", "type": "listen", "format": "conv", "unit": "conv-detail", "level": 2,
  "source": "hand", "reviewed": true, "v": 1, "accent": "us",
  "audio": {
    "dir": "audio/l-conv-02", "gapMs": 500,
    "lines": [
      {"file": "01.mp3", "who": "W", "voice": "af_sarah",   "text": "Hi Mark, the client wants to move the product demo from Thursday to Wednesday. Can your team be ready a day early?"},
      {"file": "02.mp3", "who": "M", "voice": "am_michael", "text": "Wednesday is tight. We're still testing the new checkout feature. Could we do Wednesday afternoon instead of the morning?"},
      {"file": "03.mp3", "who": "W", "voice": "af_sarah",   "text": "Let me check with them. If they agree, I'll book the large conference room."},
      {"file": "04.mp3", "who": "M", "voice": "am_michael", "text": "Great. I'll let the developers know by 3 p.m.", "say": "Great. I'll let the developers know by three P M."}
    ]
  },
  "transcriptZh": ["嗨 Mark，客戶想把產品展示從星期四提前到星期三。你們團隊能提早一天準備好嗎？", "星期三很趕。我們還在測試新的結帳功能。可以改成星期三下午而不是早上嗎？", "我問問他們。如果他們同意，我就訂大會議室。", "太好了。我會在下午三點前通知開發人員。"],
  "questions": [{
    "q": "What does the man ask for?",
    "options": ["A later time on Wednesday", "A larger conference room", "A different client", "A new checkout feature"],
    "answer": 0,
    "explain": {
      "point": "細節題：找「男方提出的要求」，注意改述",
      "why": "男方說 Wednesday afternoon instead of the morning，選項改述成 a later time on Wednesday。",
      "evidence": [1],
      "wrong": [null, "張冠李戴：會議室是女方要訂的", "沒有人提到換客戶", "同字陷阱：checkout feature 是在測試的東西，不是要求"],
      "vocab": [["demo", "展示"], ["tight", "（時間）很緊"]]
    }
  }]
}
```
`say` 是選填的 TTS 覆蓋文字（`text` 顯示、`say` 送給 Kokoro）：數字、縮寫、金額、人名要念對時用（例：`"Q3"` → `"the third quarter"`、`"Wei"` → `"Way"`）。`make_audio.py` 逐 `lines` 產檔到 `audio/<id>/<file>`，64 kbps 單聲道，沿用 game-night 的作法；`build_page.py` 檢查每個 `file` 都存在。

### 使用者狀態（db；登出或站外時同結構存 localStorage，key = `toeic:` + 邏輯路徑）
邏輯路徑以 `data/users/<uid>/` 開頭；實際的 collection／document 分層以 `artifact-capabilities` skill 為準，這裡的名稱照搬即可。

| 路徑 | 一份文件 = | 內容 | 什麼時候寫 |
|---|---|---|---|
| `toeic_profile/main` | 唯一 | `settings {pace, listenSpeed, strictListen, theme}`、`totals {n, ok, guess}`、`units {<unit>: {n, ok, guess, msSum}}`、`streak {days, lastDay}` | 設定改變時；**場次結束時一次寫入**（場中只在記憶體與 localStorage） |
| `toeic_bank/<itemId>` | 每題一份 | `reason, level, due, wrongCount, enteredAt, lastAt, v, graduatedAt?, removedAt?, history[]`（`history` 只留最近 10 筆 `{at, ok, chosen, guess}`） | 進庫、複習答完、畢業、移出 |
| `toeic_attempts/<sessionId>` | 每場一份 | `startedAt, endedAt, mode, unitFilter?, items[{id, ok, chosen, guess, ms, timedOut, v}], summary {n, ok}` | 每答 5 題 merge 一次；場次結束寫最終版 |
| `toeic_marks/<itemId>` | 每題一份 | `starred, note, flagged, flagNote, at` | 星號/旗標點下時；筆記停 1 秒後 |
| `toeic_added/<itemId>` | 每題一份 | 完整題目 schema ＋ `source, reviewed:false, createdAt, basedOn[], forUnit, retired?` | 由 Claude Code 場次寫入；頁面只讀，另外在 `toeic_marks` 記旗標 |

寫入原則：沒有「每答一題就寫 profile」這種事；歷史陣列有上限；移除用時間戳不刪文件。db 第一次可用時若 localStorage 有資料而 db 是空的，問一次「把本機紀錄匯入帳號？」，其他情況以 db 為準。

### Claude 之後怎麼用這些資料（Claude Code 場次）
1. **弱點報告**：讀 `toeic_bank/*` 與 `toeic_profile/main.units`，列出猜對率高、正確率低的考點。
2. **針對性加練**：依 `basedOn` 指定的錯題寫同考點變體題，用 `ArtifactData` 批次寫入 `toeic_added/<c-...>`，`source:"claude"`、`reviewed:false`。頁面載入時把 `toeic_added` 合併進題庫，在題目頂列與解釋卡都掛「Claude 出題・未審核」徽章，並列在首頁「Claude 給你的加練」與對應考點裡；統計時 `source` 一併記錄。
3. **轉正**：審核者看過後，題目搬進 `content.py`（改成 `g-/v-/l-` id）重新發佈，原 `toeic_added` 文件設 `retired: true`，頁面就不再顯示，避免重複。
4. **處理旗標**：讀 `toeic_marks` 裡 `flagged: true` 的題，修題或回覆。

頁面因此需要：載入時合併 `toeic_added`（排除 `retired`）、徽章、旗標按鈕，以及 `history` 與 `attempts` 裡永遠帶 `v`。

---

## 6. 其他功能（優先序）

### 今晚 MVP（一個人一個晚上做得完，全部要做）
1. 第 1 節的作答迴圈（文法＋字彙）、猜的開關、秒數紀錄。
2. 第 2 節的錯題庫：進庫規則、Leitner 排程、依考點／日期列表、篩選、搜尋、筆記、移出。
3. 聽力 `qr` 與 `conv`（`talk` 的渲染與 `conv` 相同，順手支援）：練習模式、嚴格模式、速度、逐字稿與證據句、逐句重播。
4. 首頁、依考點練習、綜合場、總結頁、場次續做。
5. 儲存層：db 優先、localStorage 備援，同一組 `get/set/list` 介面。
6. 收藏星號、「⚑ 這題有問題」（寫 `toeic_marks.flagged`，附一行原因）。學習者在意正確性，這顆按鈕就是他們的回報管道。
7. 深色模式：跟系統，設定頁可強制。
8. 桌機快捷鍵：`1–4` 或 `A–D` 作答、`Enter` 下一題、`G` 切換猜的、`R` 重播音檔、`S` 收藏。
9. 連續天數：連續有完成場次的天數，首頁一行小字；不做徽章。
10. 統計頁（陽春版）：依考點表格 `做過 / 正確率 / 猜對 / 平均秒數`，資料來自 `profile.units`。

### 今晚有餘力才做
11. **「問 Claude」**（`sample`，quick tier）：解釋卡底部一個輸入框「還想問什麼？」。prompt 內含題幹、選項、正解、整份解釋、學習者選的答案與問題，指示「用繁體中文、三句以內、只回答這個問題、不要推翻既定答案」。回覆上方固定標「Claude 即時回答・未審核」。第一次用會問授權，不自動呼叫。

### 之後（依價值排）
12. **變體題生成**（`sample` default tier）：錯題庫裡任一題按「出一題類似的」→ 第一次呼叫產題（JSON）→ 第二次獨立呼叫只給題幹與選項要求作答 → 兩次答案一致才收進 `toeic_added`（`source:"claude-runtime"`、`reviewed:false`），否則丟棄並顯示「這次沒產出可靠的題」。這是便宜的自我一致性檢查，能擋一部分錯，不宣稱可靠。
13. 表格型聽力題（`conv`/`talk` 附一個 HTML 表格：時程、價目），不需要圖片。
14. 三人對話。
15. 統計頁趨勢（每週正確率、平均秒數）。
16. 匯出錯題庫成純文字／CSV。
17. Part 6、Part 7 型閱讀題（另一個頁面比較合理）。

---

## 7. MVP 題庫內容計畫

### 數量
| 類別 | 目標 | 最低 |
|---|---|---|
| 文法 `gap` | 52 | 30（每單元 2） |
| 字彙 `gap` | 24（4 類 × 6） | 16 |
| 聽力 `qr` | 8 | 6 |
| 聽力 `conv`（每題 3 問） | 4 | 3 |
| 聽力 `talk`（每題 3 問） | 2 | 0 |

### 文法 52 題在 15 單元的分配
依常見備考書的共識與文法頁的順序，這是我們的判斷，不是統計：`pos` 6、`tense` 5、`connect` 5、`prep` 4、`participle` 4、`voice` 3、`agree` 3、`relative` 3、`pronoun` 3、`toing` 3、`compare` 3、`quantity` 3、`parallel` 3、`mandative` 2、`conditional` 2。

### 字彙四類的定義
- `collocation` 搭配詞：四個選項同詞性、意思相近，只有一個和空格旁的名詞／動詞搭得起來（reach a decision、meet a deadline、place an order）。
- `synonym` 近義辨析：四個近義動詞或形容詞，靠句中的受詞、介系詞或語境才能定（raise / rise / arise；affect / effect）。
- `business` 商業字彙：辦公、人資、物流、財務、差旅、活動場景的常用字（invoice、quarterly、comply with、itinerary、reimburse）。
- `family` 同字根不同義：considerable / considerate、economic / economical、respective / respectable。這類考意思不考詞性；純詞性判斷歸文法 `pos`。

### 難度
- 1：單一規則，判斷線索緊鄰空格。
- 2：線索離空格較遠，或兩條規則交互作用。
- 3：要讀完整句，干擾選項在別的語境下都成立。
分佈約 40% / 40% / 20%。

### 怎麼寫好的干擾選項
1. 四個選項是同一「種類」（都是動詞變化，或都是同詞性的字），不能靠外形淘汰；`pos` 單元例外，本來就是四種詞性。
2. 每個干擾選項都要能用 ≤ 45 字說出「為什麼錯」；寫不出來就換掉它——這句話就是 `wrong` 欄。
3. 決定性線索必須在句內（時間副詞、主詞、介系詞、後面的受詞），不靠常識或背景知識。
4. 逐一把四個選項代入，想英式與美式、正式與口語，任何一個「勉強可以」就重寫（例：`take a decision` 在英式是通的，所以不能拿它當干擾選項）。
5. 同一單元不要每題都用同一種干擾模式（例：`participle` 不能每題正解都是 -ed）。
6. 題幹 12–25 字，商業場景；不用真實公司、真人、真商品名；不能是記憶中的真題改幾個字。
7. 聽力：正解與音檔之間**一定有改述**；同字陷阱只能出現在干擾選項；不用「相似音」陷阱（合成語音的發音跟真人不一定一樣）；每個問題的證據落在 1–2 句內；Part 2 至少兩題用間接回答（"I haven't seen the schedule yet."）。

### 審核者對每一題的檢查清單
1. 唯一答案：四個選項各代入一次，只有一個成立；有想過英美差異與口語用法。
2. 線索在句內，不需外部知識。
3. `unit` 標對，而且一題只考一個主要考點。
4. `point` 講的規則就是 `why` 用到的規則；`wrong` 三條與 `options` 順序對應、正解位置是 `null`。
5. `zh` 與填入答案後的英文句意思一致、中文自然。
6. 字數：`point` ≤ 40、`why` ≤ 90、每條 `wrong` ≤ 45。
7. 沒有真實公司／人名／商品，沒有真題痕跡。
8. `level` 合理。
9. 聽力：`text` 與音檔一致、**每個 mp3 都親耳聽過**、需要的 `say` 都補了、`evidence` 索引正確、改述寫進 `why`。
10. 結構：`options` 長度 4（`qr` 為 `null`）、`answer` 在範圍內、`id` 唯一、音檔存在——這一條由 `build_page.py` 自動檢查，失敗就不輸出。

---

## 8. 風險與要避免的事
- **捏造**：不寫任何官方題數、秒數、分數換算；Claude 產的內容永遠掛「未審核」，永遠不進手寫題庫。
- **兩個都對的題**：最常見的漏洞是英美差異與口語用法（第 7 節第 4 條）。
- **背答案而非學規則**：選項重洗、複習時先看考點與規則、之後用變體題。
- **音檔播不出來**：單一 `<audio>` 元素＋每題保留播放鈕；介面不承諾「自動播放」。
- **TTS 念錯或腔調缺口**：`say` 覆蓋欄、每個檔都聽過；設定頁明講只有美式與英式。
- **`sample` 花學習者額度**：只在按下「問 Claude」才呼叫；回覆標示來源；不自動生成。
- **今晚做太多**：第 6 節 MVP 清單以外的全部不做；`talk` 有題就顯示、沒有就不出現。

---

## 附錄：審核流程（實作時加上的）
學習者要求題目的**難度與風格都要跟多益真題對齊**，而且要盲審。每一組題目走四步：

1. **盲審作答**：審核者只拿到 `review/blind_<組>.json`（`make_blind.py` 產生，沒有答案與解析），自己作答、標出有兩個以上可辯護答案的題（`ambiguous`），並標出認得是真題或近似真題的題（`tooClose`，不確定就不標）。
2. **難度與風格校準**（同樣看不到答案）：每題判斷跟真題同考點的題比是 `easier / similar / harder`，放在真題 Part 5（或聽力對應的 Part）裡屬於 `easy / medium / hard`，風格相似度 1–5，並給一句具體修改建議。這些都是審核者的判斷，不是統計；頁面與文件都不寫「相當於幾分」這類數字。目標是**整組的難易分布像真題**，不是每題都變難。
3. **修題與校對**（看得到答案）：盲審答案與答案鍵不一致、被標 `ambiguous`、或校準判定偏離的題，由修題者改寫或刪除；同時依第 7 節清單檢查解析、翻譯、字數。
4. **改過的題重新盲審**，一致才標 `reviewed: True`。`build_page.py` 只發佈 `reviewed: True` 的手寫題。

`review/compare.py` 比對盲審與答案鍵；`review/` 底下保留每一輪的盲審、校準與修改紀錄。


---

## 附錄二：為什麼第一版偏簡單，以及改過的出題規則（第二版）
Fable 盲審認為第一版文法與字彙比真題偏簡單（困難題很少）。原因出在規則，不在出題者：
1. 第 7 節「每個干擾選項都要能用 ≤ 45 字說出為什麼錯，寫不出來就換掉」——等於把最有鑑別度、要想一下才知道錯在哪的選項先刪掉了。
2. 「任何一個選項勉強可以就重寫」加上出題者自己的保險：刻意避開 -s 形式、their、each of + 複數、who/whom、that/which、less/fewer 等真題最常考的陷阱。
3. 難度目標 40/40/20、等級由出題者自評、等級 1 定義為「線索緊鄰空格」；題幹 12–25 字；聽力證據限 1–2 句。
4. 語言模型寫例句時偏向最典型、最乾淨的例子。

**第二版規則（取代第 7 節對應條文）**
- 干擾選項：每題至少一個「近乎正確」的誘答——在空格附近的幾個字裡是通的，只有靠遠處的線索或整句意思才能排除。`wrong` 顯示仍以 45 字為目標，但不再用它來篩掉選項；需要更長說明時寫在新欄位 `wrongMore`（同 `wrong` 形狀，點開才顯示）。
- 唯一答案的把關交給盲審：出題時可以用真題常見的陷阱；只有在標準書面英文（含英美差異）裡真的說得通第二個答案才算有問題，由 Fable 盲審判定。
- 難度以盲審校準的 `band` 為準，不用出題者自評；新題的目標分布：簡單 25%、中等 50%、困難 25%。
- 題幹 12–35 字，允許兩個子句與較少見的商業字彙。
- 聽力：證據可以跨 2–3 句（前後資訊要整合）；干擾選項可以是對話裡提到、但不是題目問的那件事；可以有三人對話與表格圖表題（`graphic` 欄位，頁面以 HTML 表格顯示）。
