# Question bank for TOEIC 練習室. Items live in the items_*.py files (schema in DESIGN.md section 5);
# this module collects them and names the units.
from items_grammar_a import ITEMS as GRAMMAR_A
from items_grammar_b import ITEMS as GRAMMAR_B
from items_vocab import ITEMS as VOCAB
from items_listen import ITEMS as LISTEN

ITEMS = GRAMMAR_A + GRAMMAR_B + VOCAB + LISTEN

# unit id -> (中文名稱, group). Grammar names follow the 多益文法考點 page.
UNITS = {
    "pos": ("詞性判斷", "grammar"),
    "tense": ("動詞時態", "grammar"),
    "voice": ("主動與被動", "grammar"),
    "participle": ("分詞：-ing 與 -ed", "grammar"),
    "connect": ("連接詞、介系詞、連接副詞", "grammar"),
    "agree": ("主詞與動詞一致", "grammar"),
    "relative": ("關係代名詞", "grammar"),
    "pronoun": ("代名詞", "grammar"),
    "prep": ("介系詞：時間、期限與常用片語", "grammar"),
    "toing": ("to 的陷阱與動詞後接的形式", "grammar"),
    "mandative": ("要求與建議：that 子句用原形", "grammar"),
    "conditional": ("假設語氣與倒裝", "grammar"),
    "compare": ("比較", "grammar"),
    "quantity": ("數量詞與可數名詞", "grammar"),
    "parallel": ("平行結構與成對連接詞", "grammar"),
    "collocation": ("搭配詞", "vocab"),
    "synonym": ("近義辨析", "vocab"),
    "business": ("商業字彙", "vocab"),
    "family": ("同字根不同義", "vocab"),
    "qr-wh": ("應答：wh 問句", "listen"),
    "qr-yesno": ("應答：Yes/No 與附加問句", "listen"),
    "qr-indirect": ("應答：間接回答", "listen"),
    "conv-topic": ("對話：主旨與場合", "listen"),
    "conv-detail": ("對話：細節", "listen"),
    "conv-intent": ("對話：意圖與推論", "listen"),
    "conv-next": ("對話：下一步", "listen"),
    "talk-topic": ("短講：主旨", "listen"),
    "talk-detail": ("短講：細節", "listen"),
    "talk-next": ("短講：下一步", "listen"),
}
