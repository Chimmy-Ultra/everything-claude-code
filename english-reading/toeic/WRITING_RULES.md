# TOEIC 題庫出題規則（WRITING_RULES.md）

這份文件是所有**新題**的現行規則，取代 DESIGN.md 第 7 節「怎麼寫好的干擾選項」「審核者對每一題的檢查清單」「難度」三段，以及附錄一、附錄二裡的規則條文（那些段落保留作為歷史紀錄；DESIGN.md 第 7 節的數量計畫與字彙四類定義仍然有效）。

對象是三個角色：**出題者**（寫題）、**盲審者**（看不到答案與解析，作答、判唯一答案、判難度）、**修題者**（看得到答案，依盲審結果修）。前兩個角色由較便宜的模型擔任，所以這裡的規則寫得很具體，能照抄就照抄。

通篇所有英文例句都是**示例，不是題目**，只用來說明型態；不要把示例原句收進題庫。本文裡所有「真題怎麼樣」的描述都是我們的判斷，沒有統計根據；頁面與文件一律不寫官方題數、秒數或分數換算。

---

## 0. 三條原則（先讀這個）

1. **難度來自「誘答在局部成立」，不是來自句子長或字冷僻。** 一題難，是因為有一個選項放進空格前後幾個字裡讀起來完全對，要讀到遠處的線索、或要用一條好學生常搞錯的規則，才能排除它。句子長只是讓線索有地方可以藏。
2. **唯一答案的標準是「標準正式書面英文（英式與美式都算）」，不是「沒有人可能選別的」。** 口語才通、過度矯正、常見錯誤，都是合法的陷阱，不是歧義。出題者負責把題做難；盲審者負責判斷第二個答案是否真的站得住。
3. **難度等級由盲審者決定，不由出題者自評。** 第一版和第三輪的經驗都是：出題者自認的「困難」，盲審多半判「中等」。出題者仍要做第 3.4 節的自我測試，但只是用來把題往上推，不用來標 `level`。

為什麼要有這份文件：第一版題庫偏簡單，根本原因在規則而不在出題者——「錯誤選項的理由要 45 字內講完，否則換掉」把最有鑑別度的誘答先篩掉；出題者為了避免兩個答案而避開所有經典陷阱；難度自評；題幹短；聽力證據限 1–2 句；加上模型天生愛寫最典型、最乾淨的例句。第三輪放寬規則後題目明顯接近真題，但仍然底重：困難題少，出題者標的困難題多半被判中等。這份文件要補的就是「什麼才算困難」的具體定義。

---

## 1. Part 5 型（文法 `gap`、字彙 `gap`）：真題的難是怎麼做出來的

### 1.1 決定性線索放哪裡

同一個考點，線索的位置決定了大半的難度。以未來完成式為例：

```
鄰近（簡單）    By next June, Ms. Rowe ______ at the firm for twenty years.
                ✓ will have worked —— 句首的 By next June 直接給答案。

同子句內（中等）Ms. Rowe ______ at the firm for twenty years by the time the merger is completed next June.
                ✓ will have worked   ≈ has worked 在 ______ at the firm for twenty years 這一段完全通，
                要讀到 by the time … next June 才排除。

跨子句（困難的材料）
                Ms. Rowe, who joined the firm as a trainee and now heads its tax practice, ______ there for
                twenty years when the merger that she helped negotiate is completed next June.
                ✓ will have worked   ≈ has worked —— 前面的 now heads 主動把讀者推向現在完成式，
                只有句尾 when … next June 能排除。
```

規則：
- **中等以上的題，決定性線索不能在空格前後四個字之內**。線索放在另一個子句、逗號之後、或句尾；空格靠近句首時線索放句尾，空格在句尾時線索放句首。
- **線索不能是教科書訊號詞放在句首**（Currently, …／By the time …／Yesterday, …）。第三輪 g-tense-02 被判簡單，盲審的原話是「真題通常把時間線索埋起來」。要用訊號詞，就把它放在句子後半，或改用不那麼顯眼的（still、yet、so far、at that point、once … is completed）。
- 線索可以是**另一個動詞的時態**（are entitled 決定主詞是複數）、**一個遠處的名詞**（three bids 決定 the other）、**一個介系詞**（by 決定 abide）、**整句的邏輯方向**（rarely 排除 Because）。
- 線索一定要**在句內**；不靠常識、不靠背景知識。但「句內」可以是離空格二十個字遠的地方。

### 1.2 近乎正確誘答的定義：局部視窗測試

把題幹只露出空格前後各四個字，其他遮起來。**近乎正確誘答**是通過這個測試的選項：在這八個字裡文法對、意思順，要靠視窗外的東西才能排除。

```
視窗   … the hiring committee has invited back only the three candidates ______ it believes are …
       whom 在視窗內完全合理（candidates whom it believes），要把 it believes 拿掉、看到 are 才知道要 who。
```

每一題中等以上**至少一個**選項要通過局部視窗測試；困難題通常兩個。這個測試同時也是盲審判 band 的第一道問題（第 5 節）。

### 1.3 各考點的近乎正確誘答與遠處線索

下面每一條：先寫誘答長什麼樣、線索該放哪，再給一個示例（✓ 正解、≈ 近乎正確誘答、其他為一般誘答）。示例句都偏長，因為它們示範的是中等到困難的做法。

**時態 tense**
- 誘答：跟正解只差一個時間層的形式（現在完成 vs 未來完成；過去 vs 過去完成；簡單現在 vs 現在進行）。
- 線索：句尾的時間子句、另一個動詞的時態、since / for / by the time / once 之類的詞放在空格之後很遠的地方。
- 困難的做法：前半句放一個**把人往錯的方向推**的字（now heads、already、last year），正確線索放最後。
```
示例  The replacement switch finally arrived on Thursday, but the technicians ______ the cause of the original
      outage ever since the first alarm went off on Monday morning and have not yet found it.
      ✓ have been investigating   ≈ were investigating（配前半句的 arrived on Thursday 很順，被 ever since +
      have not yet found 排除）   investigated / will investigate
```

**主動與被動 voice**
- 誘答：主詞看起來可以當動作者的主動形式；或 rise/raise、lie/lay 這種及物／不及物對。
- 線索：空格後面有沒有受詞、by 片語在很後面、或使役結構（have + 受詞 + p.p.）的 by 片語。
- 不要用的：ergative 動詞（the meeting will begin / be begun 之類兩邊都通）；「prices have risen / have been raised」這種兩個都對的對子。
```
示例  Ahead of the trade fair, the marketing director had all two thousand copies of the new catalog ______
      by an outside firm rather than on the office printers.
      ✓ printed   ≈ print（had + 受詞 + 原形是「叫某人做」，局部看很像；被句尾 by an outside firm 排除）
      printing / to print
```

**分詞 participle**
- 誘答：完整的被動式（were hired）放在名詞後面——前半句是一個完整句子，要讀到後面的主要動詞才發現撞了兩個動詞；或 -ing 與 -ed 的主被動（the firm conducting the audit vs the audit conducted by the firm）。
- 線索：遠處的主要動詞；或名詞是做動作的人還是被動的對象。
```
示例  Staff ______ for last year's pilot program, most of whom are now based in the Pelham office, will be
      asked to mentor the new hires who start on the third.
      ✓ selected   ≈ were selected（Staff were selected for last year's pilot program 是完整句子，被遠處的
      will be asked 排除）   selecting / select
      （不要用 enroll、register 這種人會自己做的動詞：Staff enrolling in the program 主動也通。）
```

**連接詞、介系詞、連接副詞 connect**
- 誘答兩種：(a) 同類別、邏輯方向相反（Because / Although；unless / provided that；so that / even if）；(b) 類別不同但在空格後的幾個字裡看起來對（Although 後面接名詞片語，要讀到逗號前都沒有動詞才知道該用 Despite）。
- 線索：主要子句裡的一個副詞（rarely、still、nevertheless）、整句的因果方向、或逗號前「沒有動詞」這件事本身。
- 不要用的：既是介系詞又是連接詞的字當誘答（before、after、since、until、as）；whereas 當讓步的誘答（正式英文接受 whereas 表對比，容易變第二答案）。
```
示例  ______ the heavy rain that the regional forecast had predicted for the whole of Thursday, the
      groundbreaking ceremony went ahead as planned, with only the speeches moved indoors.
      ✓ Despite   ≈ Although（Although the heavy rain that the regional forecast had predicted 一路都像子句，
      要到逗號才發現沒有主要動詞）   Even if / Nevertheless
```

**關係代名詞 relative**
- 誘答：whom 當主詞的過度矯正（中間插 it believes / we think / she said）；that 與 what 的混用（What impressed … was）；which 指人；where 與 which 的差別靠後面有沒有介系詞。
- 線索：插入語後面的動詞、句子後半缺不缺主詞、空格後面有沒有名詞（whose 要接名詞）。
- 不要用的：介系詞放句尾的 who/whom（the consultant who the report was sent to；正式英文對 who 的容忍度不一致）；限定子句的 that/which（英式接受 which）。
```
示例  ______ impressed the selection panel most was not the design itself but the team's unusually detailed
      analysis of the maintenance costs over the first ten years.
      ✓ What   ≈ That（That impressed the selection panel most 單看是一個完整句子，但後面的 was 就沒有主詞了）
      Which / Whom
```

**主詞與動詞一致 agree**
- 誘答：被空格前最近的複數名詞吸過去的複數動詞（each of the offices, including the three that … ___）；the number of 配複數；as well as 當 and。
- 線索：真正的主詞在句首，中間隔一長串修飾語或插入語。
- 不要用的：集合名詞（the committee has / have，英式接受複數）；one of the few X that is / are（兩邊都有人堅持）。
```
示例  The number of complaints about late deliveries, which rose sharply during the spring promotions and
      prompted two internal reviews, ______ fallen steadily since the new courier was hired.
      ✓ has   ≈ have（被 complaints、deliveries、promotions、reviews 四個複數帶走，主詞是句首的 The number）
      having / are
```

**代名詞 pronoun**
- 誘答：Anyone / Whoever 配遠處的複數動詞；another / the other 靠遠處的數字決定；反身代名詞與受格；its / their 靠主詞決定。
- 線索：遠處的動詞數、句首的數量（Of the two bids）。
- 不要用的：單數 they（anyone … their，現代正式英文已廣泛接受）；he or she 的題。
```
示例  Of the two bids the city received for the bridge repairs, one was withdrawn before the deadline, and
      ______ was rejected last week for exceeding the approved budget by nearly a third.
      ✓ the other   ≈ another（and another was rejected 局部完全通，被句首的 two bids 排除）
      others / each other
```

**介系詞與動詞＋介系詞 prep**
- 誘答：空格前後幾個字裡搭得起來的介系詞（shipments from delays），但真正決定介系詞的動詞在很前面（attribute … to）；credit A to B 與 credit B with A 這種方向相反的對子；within 與 in；多字介系詞之間（in accordance with / in response to / in addition to）。
- 線索：空格前很遠的那個動詞；受詞拉長到十個字以上，動詞與介系詞就分開了。
- 困難的做法：動詞有兩種介系詞用法，受詞類型決定用哪一種。
```
示例  In its year-end letter, the board credited the turnaround in sales during the second half of the year
      largely ______ the three new regional distributors appointed in March.
      ✓ to   ≈ with（credit … with 也是真的用法，但那是 credit 人 with 功勞；受詞是 the turnaround，
      所以是 credit A to B）   for / by
```

**比較 compare**
- 誘答：more 配 as（twice more powerful，要讀到後面的 as 才排除）；比較級與最高級靠句首的 Of all the … 決定；than 與 to（superior to、prefer … to）。
- 線索：句首的範圍（Of all the venues）、句尾的第二個 as 或 than。
- 不要用的：兩者比較用最高級（the tallest of the two；美式口語接受，爭議大）。
```
示例  Of all the venues the committee visited during the spring, the Harborview Hall was ______ to the
      railway station, though it was also the most expensive by a wide margin.
      ✓ the closest   ≈ closer（was closer to the railway station 局部通，被句首 Of all the venues 排除）
      as close / closely
      （不要放原級 close 當誘答：was close to the station 文法上也通，會變第二答案；也不要放不帶 the 的
      closest，述語位置的最高級可以省 the。）
```

**數量詞 quantity**
- 誘答：few 配不可數（few of the backlog）；less 配可數（真題常考，但盲審認為考生都會，判簡單）；much / many 靠遠處的名詞；a number of / the number of。
- 線索：被修飾的中心名詞離空格很遠（______ of the backlog that built up…），或中心名詞前面先出現一個像不可數的修飾語（less shipping and billing errors）。
```
示例  Despite the temporary staff brought in after the holidays, ______ of the backlog that had built up in
      the claims department had been cleared by the time the auditors arrived.
      ✓ little   ≈ few（few of the … 的形狀很常見，要看到 backlog 是不可數才排除）   a few / fewer
```

**要求與建議的 that 子句 mandative**
- 誘答：Ving（recommend checking 本身是對的，所以眼熟）、過去式、進行式、to V。
- **不要用 -s 形式當誘答**（recommended that the team checks）：英式正式書面英文接受 that 子句用直說法，所以依第 4 節的標準它是第二個可辯護答案。第三輪 g-mandative-03 已經因此把 checks 換成 checking。同理，主要動詞是過去式時不要用過去式當誘答（insisted that she went，英式可接受）；主要動詞用現在式或現在完成式就沒這個問題。
- 不要用 suggest 或 insist 當主要動詞（suggest 另有「暗示」義、insist 另有「堅稱」義，後面接直說法都是對的）；用 recommend、request、require、propose、demand、ask，或 It is essential / imperative / vital that。
- 線索：主要動詞與 that 之間插一段（in their final report that …），讓讀者忘了這是 that 子句。
```
示例  Citing two near misses on the loading dock, the safety consultant has recommended in every progress
      report since March that each forklift operator ______ a refresher course before the end of the quarter.
      ✓ complete   ≈ completing（recommend completing 本身是對的，所以眼熟；但 that + 主詞之後子句要有動詞）
      completed / is completing
      （不要用 insist 當主要動詞：insist that + 直說法另有「堅稱某事屬實」的意思，completed 就會變成可辯護。）
```

**假設語氣與倒裝 conditional / inversion**
- 誘答：If 放在倒裝句首（If the courier … been informed）、Would 放在 Should 的位置（讀起來像問句）、Unless 的邏輯顛倒。
- 線索：倒裝的關鍵字（been、have）要離空格遠——把主詞拉長。
- 不要用的：Under no circumstances should / are 這類兩個助動詞都通的句型。
```
示例  ______ the courier that the firm has used for the past six years been told about the change of
      address, the signed contracts would have reached the client before the hearing.
      ✓ Had   ≈ If（If the courier that the firm has used for the past six years 一路都通，直到 been）
      Should / Unless
```

**平行結構與成對連接詞 parallel**
- 誘答：and also 放在 not only 的後半；to V 放在一串 Ving 的最後；nor 與 or。
- 線索：成對連接詞的前半在很前面；列舉的前兩項形式。
- 不要用的：單獨的 but 當 not only 的誘答（not only … but 沒有 also 也是對的）。
```
示例  The revised travel policy applies not only to full-time staff at head office ______ to contractors who
      have worked on site for more than ninety consecutive days.
      ✓ but also   ≈ and also（and also to contractors 局部通，被二十個字前的 not only 排除）
      as well / or else
```

**詞性 pos**
- 誘答：形容詞放在副詞的位置但局部讀得通（made it dramatic / find the center easy）；名詞放主要動詞的位置，整句就沒有動詞；-ly 結尾的形容詞（timely、costly、orderly）當副詞的陷阱。
- 線索：空格修飾的是比較級、是動詞片語、還是整句缺動詞；主要動詞不在局部視窗內。
- 困難的做法：空格與它修飾的東西之間隔東西（made it ______ easier for staff to…）；或 -ing 名詞與一般名詞（advertising / advertisement）。
```
示例  Although the proposal arrived only two days before the board met, its ______ delivery allowed the
      finance committee to add the figures to the agenda.
      ✓ timely   ≈ time（time delivery 像複合名詞）   timing / timeliness
      （不要放 timed：a timed delivery「定時配送」是真的說法。）
```

**搭配詞 collocation**
- 誘答：跟題幹裡另一個名詞搭得起來的動詞（run short of + cash，但這裡是 target）；一般意義上是同義詞但不搭這個名詞的動詞（do a decision）；跟正解同一語意場的字（house / host / board 與 lodge）。
- 線索：被搭配的名詞離空格遠（fell ______ of the target that…），或名詞前面先出現干擾的修飾語。
- 不要用的：兩個都正確的搭配（reach a deal / strike a deal）。
```
示例  Any additional costs ______ as a direct result of the port closure, including storage charges at the
      terminal, will be borne by the supplier under clause 12 of the agreement.
      ✓ incurred   ≈ occurred（costs occurred 看起來像「發生的費用」，但 occur 不及物、不能這樣當分詞修飾）
      arisen / resulted
```

**近義辨析 synonym**
- 四個字在一般意義上都對，差別只在：介系詞（abide by / comply with / adhere to / conform to）、受詞的類型（waive 費用 / exempt 人）、方向（lend / borrow；comprise / constitute）、是否可逆（suspend … resume / terminate）、或後面接的結構（assure 人 that / ensure that）。
- 線索：介系詞或受詞離空格遠；或在第二個子句（resume）。
- 這一類是字彙題裡最容易做到困難的，因為誘答在意思上完全對。
```
示例  The clinic ______ patients in its confirmation letter that any change to an appointment time will be
      sent by text message at least twenty-four hours in advance.
      ✓ assures   ≈ ensures（意思對，但 ensure 不接「人 + that 子句」）   insures / secures
```

**同字根不同義 family**
- 誘答：同詞性、同字根、意思不同的字（considerable / considerate；economic / economical；respective / respectable）。純詞性的題歸 pos。
- 線索：只有整句的意思能排除，所以題幹要給夠語境，但**不能替那個字下定義**（stem defines the word → 簡單）。
- 不要用的：confident / confidential 這種太有名的對子當唯一考點（盲審判簡單）。
```
示例  Given how ______ the negotiations have become since the second bidder withdrew, the board has asked
      that no figures be shared outside the room until the agreement is signed.
      ✓ sensitive   ≈ sensible（同詞性，局部通；只有「不能外洩」這個語境能排除）   senseless / sensory
```

**商業字彙 business**
- 誘答：同領域、同詞性、常一起出現的字（deposit / rebate / dividend / premium）。
- 線索：句子要靠「這筆錢怎麼流動」這類結構訊息決定，不是靠一句解釋。「with the balance due upon delivery」這種等於定義的尾巴會讓題變簡單；要留，就把它改成需要推一步的說法。
- 正解可以是中頻商業字（reconcile、waive、lodge、incur），但**誘答也要同頻率**，不能一個難字配三個常用字。

### 1.4 題幹的長度與形狀

- 新題題幹 **18–38 字**；困難題通常 24 字以上，但長不等於難（見第 0 節）。
- 兩個子句是常態：主句＋副詞子句、主句＋非限定關係子句、分詞片語開頭、或句中插入語。長度要用在三件事上：(1) 把線索推遠；(2) 放一個把人往錯方向推的字；(3) 給字彙題足夠語境。純粹加形容詞不算。
- 商業場景：合約、物流、人資、財務、差旅、活動、客服、設施。不用真實公司、真人、真地名、真商品名。拼字與用字用美式（catalog、center、elevator、college），題目本身不考拼字。
- 同一批題裡，一題的正解不能是另一題的誘答（第三輪 g-prep-05 / g-prep-07 的 on behalf of）；同一單元不要連續同一種誘答型態（不能三題都考副詞、每題正解都是 -ed）。

### 1.5 字彙負荷

- 題幹可以含 1–2 個中高階商業字（reimburse、discrepancy、subcontractor、consecutive），放在**不是**決定性線索的位置。
- 決定性線索本身要用常用字：線索在 are、by、two、rarely、since 這種字上，才是「讀得仔細就會」；線索在冷僻字的意思上，是「背過才會」，真題很少這樣。
- 正解與近乎正確誘答都應該是**常用字的不常用行為**（contribute to 的 to 是介系詞；credit 的兩種方向；lodge 的「提出」義），不是冷僻字。

### 1.6 盲審判「簡單」的具體樣子（新題不要這樣）

從第三輪盲審的判詞整理：
- 訊號詞在句首（Currently, …）。
- 題幹替正解下定義（a ______ of 15 percent … with the balance due upon delivery；keep every detail strictly ______）。
- 固定公式（I am writing on behalf of … to invite you）。
- 國中程度的動詞型（decided to）。
- 三個誘答跟正解意思差很遠，看一眼就淘汰。
- 四個選項不同類別（一個動詞、一個名詞、一個形容詞、一個副詞），而且不是 pos 單元。
- 題幹短、沒有商業語境。

---

## 2. 聽力 Part 2 / 3 / 4 型

### 2.1 合成語音的限制（先知道做不到什麼）

音檔是 Kokoro 的美式與英式聲音。因此：
- **不用相似音陷阱**（copy / coffee）；合成語音的發音與真人不一定一樣。**同字陷阱**可以用（選項或回應重複音檔裡的字，但意思不對）。
- **不用靠語調的題**：反諷、附加問句的升降調、重音位置改變意思（I didn't say HE took it）。意圖題要靠字面與上下文就能推出來。
- 數字、時間、金額、縮寫、頭銜、人名一律寫 `say`；避免同形異音字（read、lead、live、record、present）出現在證據句，用了就要親耳聽過。
- 三人對話：兩位同性別的說話者用不同聲音（一美一英），而且**名字要在對話裡被叫到**（Victor, Hannah, thanks for joining me），題目用名字問（What will Hannah do next?）。
- 每句不超過 25 字左右，合成語音長句會塌。

### 2.2 Part 2 型 `qr`：回應從哪裡變難

**三種回應**，由易到難：
1. 直接回答（When → By Friday）。
2. 間接回答：給理由、反問、說還沒決定、把問題丟回去、答另一個相關的事。
3. 用理由暗示「不用／不行」（Could you show the new designer…? → She used the same one at her last job）。

**誘答的兩種做法**：
- **形式對、情境錯**：這個回應符合問句的類型（who 問句回一個人名、Yes/No 問句回 Yes），但跟問句裡的某個細節矛盾或無關。這是真題 Part 2 最有鑑別度的誘答。第三輪 l-qr-09：Who's going to lead the training now that Ms. Harlan has retired? → ≈ Ms. Harlan will be leading it.（形式全對，被 retired 排除）。
- **同字陷阱**：重複問句裡的字但答的是別的事（booking system → the booking fee is included）。

**問句本身**要有一個**附帶條件**才藏得住誘答：now that Ms. Harlan has retired、since the budget was cut、before the client arrives。沒有附帶條件的問句，形式對的回應就等於正解。

**敘述句當題幹**（The quarterly figures still don't add up.）：正解是接話（追問原因、提議對策、表示會處理）；誘答是語氣自然但方向相反的接話（Good, then we can send them to the board）——聽懂 still don't 才能排除。

```
示例（三個回應的聲音都是另一人）
Q  Has the revised price list gone out to the distributors yet, now that Marta has signed off on it?
✓  The courier only collects on Fridays.             （間接：所以還沒）
≈  Yes, they're listed in alphabetical order.         （Yes 形式對；答的是清單怎麼排）
   No, it was about four percent.                     （No 形式對；答的是漲幅）
```

難度判斷（跟第 5 節一致）：
- 簡單：直接回答，兩個誘答類型明顯不同（wh 問句回 Yes、答另一個 wh）。
- 中等：間接回答，或敘述句題幹；一個誘答形式對。
- 困難：間接回答＋**兩個**誘答都形式對或同字；問句帶附帶條件；或正解要用問句裡的細節推一步（retired → 不可能是她）。

### 2.3 Part 3 / 4 型 `conv` `talk`：證據整合與改述距離

**改述距離**（正解與音檔之間），由近到遠：
0. 同字——只准出現在誘答。
1. 換字：buy → purchase；manager → supervisor。
2. 換結構：we're out of toner → a supply has run out；the painters have the whole floor booked → part of the facility will be closed。
3. 推論：parking downtown is expensive → she will take the train；my manager asked me to go to the one right after it → his supervisor wants him at a different session。

中等題至少距離 2；困難題距離 3，而且誘答用距離 0。

**證據整合**：真題的中等以上題，證據常常不在一句裡：
- **跨句**：代名詞或指示詞要回頭找（that day → Friday；them → the supplier；it → the badge）。
- **跨說話者**：A 提議、B 否決、C 定案，問的是最後結果。
- **跨時間詞**：音檔給兩個期限（月底完成訓練、星期五前報名），題目問其中一個，誘答是另一個。
- `evidence` 可以指 1–4 句；`why` 要寫出怎麼串起來。

```
示例（節錄三句）
W  Can we move the client call to Thursday? The samples won't be here before then.
M  Thursday's the board meeting. What about the day after?
W  Fine, I'll let them know.
Q  When will the call most likely take place?    ✓ On Friday   ≈ On Thursday（提到的日期）   On Wednesday
```

**誘答的四種做法**（每題至少用兩種）：
- **提到但不是問的**：對話裡真的有、也屬實，但不是題目問的那件事（沒拿識別證是真的，但問的是「為什麼不去那場」）。
- **張冠李戴**：另一位說話者要做的事。
- **時間／期限錯置**：另一個日期或另一個期限。
- **方向相反**：音檔說講者很棒，選項說講者不好。

**圖表題 `graphic`**（表格，由頁面以 HTML 顯示）：
- 音檔**不能說出答案那一格**。音檔給表格的一個座標（the one right after the contracts workshop／the cheapest plan／the session that starts at ten），題目問另一欄（Which room? / Which plan? / Who is the speaker?）。
- 表格 4 行左右，欄名簡單（Time / Workshop / Room）。同字陷阱是「音檔提到的那一行」（contracts → Room 115），正解是從它推出來的另一行。
- 題目開頭固定 Look at the graphic.

**引句題**（What does the speaker mean when she says, "…"?）：
- 引的句子要在上下文裡有一個**非字面**的功能（That's not a typo → 真的要那麼久；Let's just say it wasn't my idea → 她不贊成）。
- 誘答一定要有一個**字面解讀**（A printing error will be fixed）；其他誘答用音檔裡別處提到的事。
- 引句前後各一句就是證據；`evidence` 指這兩三句。

**意圖／推論題**：Why does the man mention the board meeting? → To explain why a date is unavailable。正解是功能，不是內容；誘答是內容（To announce a meeting）。

**問題順序**：三題依音檔順序；第一題常是主旨／場合／身分，第三題常是下一步或推論。三題裡**至多一題**簡單。

**對話與獨白長度**：`conv` 7–10 句，`talk` 90–130 字；困難的題組可以用上限。獨白要有一個轉折或一個例外（Sessions are on the 12th, 14th and 19th — but the 14th is already full），不然三題找不到地方藏誘答。

### 2.4 盲審判「簡單」的聽力樣子（新題不要這樣）

- 正解與證據句共用一個內容字，而且證據只有一句。
- 因果用 so 明講，題目問 why。
- 只有一個誘答沾得上邊，另外兩個跟對話無關。
- Part 2 的問句沒有附帶條件，兩個誘答都是答錯類型。

---

## 3. 出題者程序

### 3.1 你的工作

把每一題做到**跟真題的困難題一樣難**，同時在標準正式書面英文（英式與美式）裡**只有一個答案**。這兩件事不衝突：陷阱的意思就是「看起來對、其實不對」，不是「兩個都對」。

你**不負責**判斷「會不會有人選錯」——那正是題目要的。你也**不負責**最後的唯一答案判定，那是盲審者的事；你只要做到 3.3 的檢查。

### 3.2 寫一題的順序（照這個順序，不要先寫句子）

1. **選考點**，然後**先選近乎正確誘答**，再選正解。例：考 contribute to + Ving，誘答是 to reduce。
2. **先寫一個「誘答是對的」句子**。例：The new machines were installed to reduce the time… 這一步是對付模型愛寫典型句的方法：你先讓誘答自然，再去破壞它。
3. **改寫句子，讓正解成為唯一答案，但只在局部視窗之外改**。把決定因素（這裡是 contributed … to）放到離空格四個字以上，中間塞一個副詞或一段受詞。
4. **加第二個子句或插入語**，功能是：(a) 再推遠線索；(b) 放一個把人推向誘答的字；(c) 給語境。長度到 18–38 字。
5. **補齊四個選項**：同一類別（都是動詞形式／都是介系詞／都是同詞性同義詞）。第二個誘答最好也能通過局部視窗測試；第三個可以是一般誘答。
6. **四個選項逐一代入整句**，用第 4 節的標準問：「英國或美國的正式商業文件編輯會不會讓這句原樣通過？」只要有兩個「會」，改句子（通常是把線索寫得更明確），**不是把那個誘答換成軟的**。
7. **做 3.4 的難度自測**。自測結果是「簡單」就回到第 3、4 步，不是交出去。
8. 寫解說（第 6 節）。
9. 在這一輪的 `review/round<N>_<組>.json` 的 `notes` 裡，每題一行寫：近乎正確誘答是哪個、它為什麼局部通、決定性線索在哪、自測的 band。這份筆記盲審者看不到，修題者和下一輪校準會用。

聽力的順序一樣：先決定正解的改述與誘答的同字，再寫對話，最後確認音檔沒有把答案講白。

### 3.3 必須做的檢查

- 每個誘答在**整句**裡都有一個可以說清楚的錯——錯的理由可以很長，寫進 `wrongMore`；**理由長不是換掉誘答的理由**。
- 決定性線索在句內，不靠常識。
- 正解在英式與美式正式書面英文裡都對；正解不能是只有一邊接受的用法（write me、different than、on the weekend、the tallest of the two）。
- 第 1.3 節各考點「不要用的」清單——那些是會變成第二答案的東西，是真的不能用，不是保守。
- 同一批題：正解不當另一題的誘答；同一單元誘答型態要變化；場景（front desk、parking garage）不要重複三次以上。
- 沒有真實公司、真人、真地名、真商品；不是記憶中真題改幾個字。

### 3.4 難度自測（跟盲審者判 band 用同一套問題）

對每一題回答四個問題：

| 代號 | 問題 | 怎麼判 |
|---|---|---|
| **L 局部** | 至少一個誘答通過局部視窗測試（空格前後各四個字內讀起來對）？ | 遮住其他字自己讀 |
| **D 距離** | 排除它的線索在視窗外（另一個子句、逗號後、句首或句尾）？ | 找到線索那個字，數距離 |
| **B 誤信** | 那個誘答是好學生會**主動相信是對的**形式？過度矯正（whom 當主詞）、口語標準（less + 可數）、把一個句型套到另一個（to reduce 當目的）、動詞的另一種真實用法（credit … with）、同義詞的錯用（ensure 人 that） | 問自己：中高級學習者會不會理直氣壯選它 |
| **S 兩步** | 解題要兩個動作？先拿掉插入語再判主詞、先認出 to 是介系詞再選 Ving、先找真正的主詞再選單複數 | 數動作 |

判定：
- **簡單**：L 否。不管句子多長、字多難。
- **中等**：L 是，而且 D 或 B 其中之一是。
- **困難**：L 是，D 是，而且 B 或 S 至少一個是。

這跟第三輪盲審的實際判法對得上：g-tense-06（線索在句尾，但「未來完成式配 when 子句」是大家都會的規則：L、D 是，B、S 否）判中等；g-relative-04（who/whom 插入語：L、D、B、S 全是）判困難；g-toing-04（to reducing：L、D、B 是）判困難；g-quantity-04（less/fewer：L 是但 B 否，大家都知道）判簡單。**出題者過去的錯是把 L＋D 當成困難；困難還要 B 或 S。**

字彙題的對照：L = 誘答意思對；D = 排除它的介系詞／受詞／第二子句離空格遠；B = 差別在介系詞、受詞類型、方向、可逆性這種「意思對但用法不對」的層面（純意思差別算否）；S 通常否。題幹替正解下定義 → 直接簡單。

聽力的對照：L = 至少一個誘答形式對或同字；D = 證據跨兩句以上或要用問句裡的附帶條件；B = 正解是間接回答／距離 3 的改述／引句的非字面義；S = 要整合兩位說話者或表格。

### 3.5 不准做的事

- 不准因為「這個誘答的理由寫不進 45 字」而換掉它。
- 不准因為「這個陷阱太經典、怕有人說兩個都對」而避開 who/whom、each of、those who、-ing 名詞、to + Ving、fewer/less。這些是真題的主菜；唯一答案的判定交給盲審。
- 不准把線索放在句首的訊號詞上。
- 不准讓題幹替正解下定義。
- 不准用四個不同類別的選項（pos 除外）。
- 不准自己把 `level` 標成 3 來「平衡分布」；`level` 由盲審 band 換算。
- 不准為了保險把兩個誘答都換成「明顯錯」的——那是把題改簡單，不是改安全。
- 聽力：不准讓音檔把正解的字講出來；不准讓圖表題的音檔說出答案那一格；不准用相似音與語調。

---

## 4. 盲審者的歧義標準

### 4.1 標準

第二個選項**可辯護**（`ambiguous: true`，必修），當且僅當同時滿足：

1. **文法**：把它放進整句，句子在**標準正式書面英文**裡是對的。英式與美式都算標準；兩邊只要有一邊的正式書面英文接受，就算。
2. **意思**：整句的意思連貫，而且跟句子描述的商業情境不矛盾，**不需要句子沒給的假設**。

兩個條件缺一個就不算可辯護，只能是誘答。

### 4.2 不算可辯護的（這些是合法陷阱，不要擋）

- **只在口語或非正式文字接受**：less + 可數名詞；flat adverb（drive slow、find it easy 當副詞用）；like 當連接詞；me and the manager 當主詞；it don't。
- **過度矯正**：whom 當插入語後的主詞；between you and I；myself 當主詞。
- **描述性詞典記錄為「常見但正式寫作會被改掉」**的用法（MWDEU 式的註記）。判斷的基準是「編輯會不會改」，不是「有沒有人這樣寫」。
- **文法對但意思荒謬**（the chemicals are stored in addition to the guidelines）。
- **要加句子沒有的假設才通**（rents：假設 IT 部門對內部收費）。這類標 `shouldFix`（換掉那個誘答），不標 `ambiguous`。

### 4.3 算可辯護的（出題者應避開；盲審者遇到要標 `ambiguous`）

- 英式正式書面接受的形式：mandative that 子句用直說法（recommended that the team checks）、過去式回推（insisted that she went）、集合名詞配複數（the committee have）、限定子句用 which、take a decision、at the weekend、in hospital。
- 美式正式書面接受的形式：different than、write me、on the weekend、the tallest of the two（這個有爭議，當可辯護處理）。
- 兩邊都接受的現代用法：單數 they、data is / are、due to 當介系詞、hopefully 當句副詞、since / while 表原因與對比、one of the few X that is / are 的任一邊、受格 who（the consultant who we hired；正式文件編輯意見不一，當可辯護處理）。
- 兩個真實搭配（reach / strike a deal；rise / be raised）。
- 既是介系詞又是連接詞的字放在兩種結構都通的位置。

### 4.4 盲審程序（每一題）

1. **先作答**，記 `confidence`。
2. **對每個其他選項**，刻意替它找一個讀法：代入整句，用 4.1 的兩個條件問。問的是「英國或美國正式商業文件的編輯會不會原樣放行」，不是「有沒有學生會選」。
3. 有一個通過 → `ambiguous: true`，寫進 `alsoPossible`，`reason` 要寫出那個讀法與它在哪一種英文裡成立。這是 `mustFix`。
4. 差一點通過（需要外加假設、或只有描述性詞典記錄）→ `ambiguous: false`，但在 `editorNote` 寫明，列入 `shouldFix`，建議換掉那個誘答。
5. 完全不通過但是個好陷阱 → 什麼都不標；這題的 `why` 可以提它是好誘答。
6. 英式與美式判斷不同、而正解是美式用法時：正解必須在英式也對才算合格。正解只在一邊對 → `mustFix`（換正解或改句）。
7. 聽力：一個回應／選項可辯護，是指**一個合作的說話者在那個情境下可以自然這樣回，而且不與問句或對話的任何細節矛盾、不需要額外假設**。「形式對但被某個細節排除」是合法陷阱；「要假設問句沒說的事才矛盾」不是排除，要標 `shouldFix`。

### 4.5 盲審者同時交的其他欄位

沿用現有格式：`answer`、`confidence`、`ambiguous`、`alsoPossible`、`reason`、`vsToeic`（easier / similar / harder）、`band`（easy / medium / hard，依第 5 節）、`style`（1–5）、`why`（為什麼是這個 band，一句）、`fix`（具體建議，可空）、`tooClose`、`editorNote`。整組另有 `overall`、`mustFix`、`shouldFix`。

`band` 的 `why` 要指名是哪個問題（L / D / B / S）沒過，修題者才知道往哪裡推。

---

## 5. 難度目標與 band 的決定

### 5.1 band 怎麼定

- band 由**盲審者**用第 3.4 節的四個問題判。出題者的自測只寫在 round notes，不進題目。
- `level` 從 band 換算：easy 1、medium 2、hard 3；`conv` / `talk` 取三題裡最高的 band。
- 盲審與出題者自測不一致時，以盲審為準；修題者在 log 裡記下差異（哪個問題判法不同），累積三輪後再看是否調整 3.4 的文字。
- 這些都是審核模型的判斷，不是統計；不跟任何分數或百分位對應。

### 5.2 新批次的目標分布（以盲審 band 計）

現有題庫偏底重（第三輪後文法、字彙、聽力的困難題都只佔一到兩成）。整體題庫的長期目標仍是附錄二的 **簡單 25 / 中等 50 / 困難 25**（我們的判斷）；為了把整體拉回去，**新批次**要超配困難題：

| 區塊 | 簡單 | 中等 | 困難 |
|---|---|---|---|
| 文法 `gap` | ≤ 20% | 45–55% | ≥ 30% |
| 字彙 `gap` | ≤ 20% | 45–55% | ≥ 30% |
| 聽力 `qr` | ≤ 25% | ~50% | ≥ 25% |
| 聽力 `conv` / `talk`（以題計） | ≤ 25% | ~50% | ≥ 25%；每組三題至多一題簡單 |

- 分布是**整批**的目標，不是每一題。簡單題仍然要有：題庫需要讓初學者有入口。
- 盲審後若困難題不到目標：**補寫**困難題（針對缺的單元），不要把已通過的簡單題硬改成困難。改題只用於 mustFix / shouldFix。
- 出題者每批交題時，自測的困難題要**超過**目標（例如交 40% 自測困難），因為經驗上會有一部分被判成中等。
- 任何一批 `vsToeic: easier` 超過一成，整批退回重做，不逐題修。

---

## 6. 解說規則（不限制題目難度）

解說沒有字數上限：長度由要講清楚的內容決定，寫完整比寫短重要。`wrong` 是一眼看到的那一句，`wrongMore` 是點開才看到的補充；兩者的分工照下表，但不用字數來切。

| 欄位 | 長度 | 寫什麼 |
|---|---|---|
| `point` | 一句 | 考的規則，一句；不含答案以外的多餘資訊。字彙題寫「搭配詞：fall short of」這種形式；聽力寫技巧（跨說話者：that day 要回頭找 Friday）。 |
| `why` | 講清楚為止 | **一定要指出決定性線索在哪**（句尾 when … next month；拿掉插入的 it believes）。聽力一定要寫改述對應（音檔的字 → 選項的字）。 |
| `wrong[i]` | 講清楚為止 | 先一句話點出錯在哪。近乎正確誘答的格式：「<為什麼看起來對>；<哪個字排除>」（例：shipments from 看似通順，但 attribute 要配 to）。聽力要標陷阱類型。 |
| `wrongMore[i]` | 講清楚為止 | **近乎正確誘答必填**：先承認它在哪裡是對的（recommend checking 本身是對的說法），再說這一句為什麼不行。一般誘答可為 `null`。形狀同 `wrong`，正解位置 `null`。 |
| `zh` | 一句 | 填入正解後整句的翻譯，中文要自然。 |
| `vocab` | 2–4 組 | 題幹裡的中高階字＋中文；不放正解。 |
| `evidence`（聽力） | 1–4 個索引 | 跨句就全列；`why` 要寫怎麼串。 |

聽力 `wrong` 的陷阱類型標籤：`同字陷阱`、`答錯問句類型`、`張冠李戴`、`形式對情境錯`、`提到但不是問的`、`時間錯置`／`期限錯置`、`方向相反`、`字面陷阱`（引句題）、`語境矛盾`。

其他：
- `point` 與 `why` 用的是同一條規則；`wrong` 不能跟 `why` 矛盾。
- 文法術語跟「多益文法考點」頁一致（Ving、to V、p.p.、原形、連接副詞）。
- 解說只答這一題；延伸規則寫在 `wrongMore`，不寫在 `why`。
- 不因為解說的長短而改題。

---

## 7. 檢查清單

### 7.1 出題者（交題前逐條打勾）

1. 近乎正確誘答先選好，而且通過局部視窗測試（L）。
2. 決定性線索在視窗外（D），在句內，不靠常識；不是句首訊號詞。
3. 自測 band 寫進 round notes；自測「簡單」的題已回頭改過，或明確標為這批要的簡單題配額。
4. 四個選項同一類別（pos 除外）；第二個誘答也盡量局部通。
5. 四個選項逐一代入整句，用「英美正式文件編輯會不會放行」檢查；正解在英式與美式都對。
6. 沒用第 1.3 節「不要用的」清單裡的東西（-s 形式當 mandative 誘答、集合名詞一致、兩個真實搭配……）。
7. 題幹 18–38 字、兩個子句或一個插入語、美式拼字、商業場景、無真名；題幹沒有替正解下定義。
8. 同一批：正解不是另一題的誘答；同單元誘答型態有變化；場景不重複。
9. 解說：`why` 指出線索位置；近乎正確誘答有 `wrongMore`；解說沒有字數上限，寫完整。
10. 聽力：改述距離 ≥ 2（困難 3）、同字只在誘答、證據索引完整、圖表題音檔不說答案格、附帶條件在問句裡、`say` 補齊、沒有相似音與語調陷阱、三人對話名字有叫到。

### 7.2 盲審者（每題）

1. 先作答，記信心。
2. 每個其他選項代入整句，用 4.1 的兩個條件找讀法；分清 `ambiguous`（正式書面英美任一邊放行 → mustFix）、`shouldFix`（要外加假設才通）、合法陷阱（什麼都不標）。
3. 正解在英式與美式是否都對；只有一邊對 → mustFix。
4. 用 L / D / B / S 判 band，`why` 寫明哪一項沒過；`vsToeic` 另外判。
5. `tooClose`：認得是真題或近似真題才標，不確定不標。
6. `style` 1–5，低於 4 要在 `fix` 說為什麼不像真題（句首訊號詞、定義式題幹、公式、選項類別不同、場景不像）。
7. 看整批：同一題的正解是否出現在另一題的誘答；同單元是否重複同一型態；分布是否達到第 5.2 節的目標；`overall` 寫整批跟真題比的差距在哪。
8. 聽力：確認音檔沒有說出正解的字；圖表題音檔沒有說出答案格；引句題的誘答裡有字面解讀；每個誘答的陷阱類型標對。

---

## 8. 閱讀 Part 6 / Part 7 型（第七輪起）

這一節是閱讀題的規則；第 0、3、4 節的原則（唯一答案的標準、出題順序、盲審程序）照樣適用，「整句」換成「整份文件」。本節對真題的描述都是我們的判斷，不是統計。

### 8.1 Part 6 型 `p6`：短文填空

- 一份文件（e-mail、memo、notice、letter、article、advertisement、web page），120–200 字，2–4 段。
- 四個空格，在段落文字裡寫成 `{1}` `{2}` `{3}` `{4}`，依出現順序。四題分別是：
  - 兩到三題「字詞」空格：文法（時態、詞性、代名詞、連接詞與連接副詞、關係詞、假設語氣）或字彙。
  - **剛好一題「句子插入」**：四個選項都是完整句子，選最適合放進這個空格的一句。
- **Part 6 的難度來自「本句裡四個都通」。** 中等以上的字詞空格，在自己那一句裡至少兩個選項文法對、意思順，要讀**前後句或另一段**才能決定：
  - 時態：句子本身沒有時間詞，要靠信件日期、前一段的 last month／next week 判斷。
  - 代名詞與限定詞：they／it／this／these 指誰，要回前一句找。
  - 連接副詞（However、As a result、In addition、Otherwise、Instead）：要看前後兩句的關係，本句單獨看任何一個都通。
  - 字彙：四個字放進本句都說得通，前文的細節排除其中三個（前面說是「暫時」關閉，就不能選 permanently 的意思）。
- **句子插入題**：正解要同時接得上前一句與後一句。用指涉（These changes／The same discount／this request）或邏輯（先問題後解法）把它綁住。誘答是**同主題**的句子，但：指向還沒出現的東西、跟文中某個細節矛盾（日期、人、方向）、或放在這裡打斷前後兩句的連接。不要用跟主題無關的句子當誘答（那是簡單題）。
- 四題中**至多一題**簡單；困難題至少兩題。

### 8.2 Part 7 型 `p7t`：三篇閱讀

- 三份相關文件，合計 380–560 字。常見組合：廣告／公告＋e-mail＋表單；行程表＋e-mail＋評論；文章＋信件＋發票。三份之中可以有一份是表格（時刻表、價目表、訂單）。
- 五題，依下列配置（順序可調，但跨文件題放後半）：
  1. 一題**單篇**的主旨或目的（Why was the e-mail sent?），誘答用文中真的提到、但不是目的的事。
  2. 一題**字義題**：In the e-mail, the word "X" in paragraph 2 is closest in meaning to。X 是常用多義字，正解是它在這裡的意思，**最強的誘答是它最常見的意思**（例：the figures were *settled* → decided，誘答 moved into a home）。
  3. 一題 **NOT／true** 或推論題（What is indicated about…／What is NOT mentioned as…／What is suggested about…）。推論題的正解必須由文字推得出來，不能只是「有可能」。
  4. **至少兩題跨文件題**：答案要把兩份文件的資訊合起來才拿得到（表單的訂購日期＋公告的折扣截止日 → 有沒有拿到折扣；e-mail 說選了最便宜的方案＋價目表 → 哪個方案的特點）。困難的跨文件題要三份都用到，或要先排除一個被後文更正的資訊。
- **改述距離**（同第 2.3 節）：正解與文件之間至少距離 2；同字只准出現在誘答。
- **誘答的做法**：
  - **被更正的資訊**：第一份文件的原計畫，第三份改了；誘答是原計畫。
  - **另一欄／另一行**：表格裡相鄰那一行，或另一個人、另一個日期。
  - **提到但不是問的**：文中屬實，但不是題目問的那件事。
  - **字面／最常見義**：字義題與推論題。
- 文件要像真的：e-mail 有 To／From／Date／Subject，表單有欄位，評論有星等或日期。人名、公司名、地名、產品名都要虛構；同一組裡名字不要太像。

### 8.3 閱讀的難度自測（L / D / B / S 的閱讀版）

| 代號 | Part 6 | Part 7 |
|---|---|---|
| **L 局部** | 至少一個誘答在空格自己那一句裡文法對、意思順 | 至少一個誘答用了文件裡的字，或在某一份文件裡屬實 |
| **D 距離** | 決定性線索在另一句或另一段 | 證據在兩處以上，或在題目指的那份文件以外 |
| **B 誤信** | 誘答是學生會主動相信的（本句最自然的連接副詞、最常見字義、最近的名詞當代名詞先行詞） | 誘答是被更正的舊資訊、最常見字義、或字面讀法 |
| **S 兩步** | 要先確認前文的時間或指涉，再判本句 | 要合併兩份文件、或計算日期／金額、或在 NOT 題逐一排除 |

band 的判法同第 3.4 節：L 否 → 簡單；L 是＋D 或 B → 中等；L、D 是＋B 或 S → 困難。題組的 `level` 取題組裡最高的 band（同聽力）。

**第七輪的目標（學習者要求偏難）**：以題計，簡單 ≤ 10%、困難 ≥ 50%。

### 8.4 唯一答案（閱讀）

- 正解要**被文件支持**；每個誘答要**被文件否定、或文件完全沒提**。「文件沒提，但也可能是真的」的選項放在 NOT 題以外的題型時，盲審要判它是否可辯護。
- 推論題：如果一個誘答也能由文件合理推出，就是 `ambiguous`。
- Part 6 句子插入：盲審者把四個句子逐一放進空格讀整段；有兩句都接得順 → `ambiguous`。
- Part 6 字詞空格：用第 4.1 節的標準，但「整句」換成「整段（含前後句）」。

### 8.5 格式

```python
{
 "id": "r-p6-01", "type": "read", "format": "p6", "unit": "p6", "level": 3, "source": "hand", "reviewed": False, "v": 1,
 "docs": [
  {"kind": "E-mail",
   "head": [["To", "..."], ["From", "..."], ["Date", "May 4"], ["Subject", "..."]],   # 沒有就 []
   "title": None,                                                                      # 文章、公告的標題；沒有就 None
   "paras": ["First paragraph with a {1} blank.", "Second paragraph. {2}"],          # 句子插入的空格自己就是一個 {n}
   "zh": ["第一段的翻譯（空格填入正解）", "第二段的翻譯"]}                              # 與 paras 一樣長
 ],
 "questions": [
  {"options": ["...", "...", "...", "..."], "answer": 2,                              # p6 的第 i 題對應 {i+1}；p6 沒有 "q"
   "ldbs": {"L": True, "D": True, "B": True, "S": False, "band": "hard"},
   "explain": {"point": "...", "why": "...", "evidence": [[0, 1]],                    # [文件, 段落]；表格文件的段落 = 行號
               "wrong": [...], "wrongMore": [...], "vocab": [["word", "中文"]]}}
 ]
}
```

- Part 7 `p7t`：`format` 寫 `p7t`、`unit` 寫 `p7-triple`，`docs` 三份，每題有 `"q"`。表格文件用 `"table": {"head": [...], "rows": [[...]]}` 代替 `paras`，`zh` 寫 `[]`。
- `explain` 的欄位與規則同第 6 節；`why` 要寫明證據在哪一份文件的哪一段，跨文件題要寫怎麼合起來。
