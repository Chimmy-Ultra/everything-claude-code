# Question bank for The Workbook (TOEIC Parts 2–5). Items live in the items_*.py files (schema in DESIGN.md section 5);
# this module collects them and names the units.
from items_grammar_a import ITEMS as GRAMMAR_A
from items_grammar_b import ITEMS as GRAMMAR_B
from items_vocab import ITEMS as VOCAB
from items_listen import ITEMS as LISTEN

ITEMS = GRAMMAR_A + GRAMMAR_B + VOCAB + LISTEN

# Rounds 4–6 (written under WRITING_RULES.md) live in their own files; they join the bank once they exist.
import importlib
for _name in ("items_grammar_c", "items_vocab_b", "items_listen_b", "items_grammar_d", "items_vocab_c", "items_listen_c",
              "items_listen_d", "items_listen_e", "items_listen_f", "items_grammar_e", "items_grammar_f", "items_grammar_g", "items_grammar_h"):
    try:
        ITEMS = ITEMS + importlib.import_module(_name).ITEMS
    except ModuleNotFoundError as _e:
        if _e.name != _name: raise

# unit id -> (中文名稱, group, English name). Grammar names follow the 多益文法考點 page; the page shows the English name.
UNITS = {
    "pos": ("詞性判斷", "grammar", "Parts of Speech"),
    "tense": ("動詞時態", "grammar", "Verb Tenses"),
    "voice": ("主動與被動", "grammar", "Active and Passive"),
    "participle": ("分詞：-ing 與 -ed", "grammar", "Participles: -ing and -ed"),
    "connect": ("連接詞、介系詞、連接副詞", "grammar", "Conjunctions, Prepositions and Linking Adverbs"),
    "agree": ("主詞與動詞一致", "grammar", "Subject–Verb Agreement"),
    "relative": ("關係代名詞", "grammar", "Relative Pronouns"),
    "pronoun": ("代名詞", "grammar", "Pronouns"),
    "prep": ("介系詞：時間、期限與常用片語", "grammar", "Prepositions of Time and Set Phrases"),
    "toing": ("to 的陷阱與動詞後接的形式", "grammar", "-ing or to + Verb"),
    "mandative": ("要求與建議：that 子句用原形", "grammar", "That-Clauses with the Base Form"),
    "conditional": ("假設語氣與倒裝", "grammar", "Conditionals and Inversion"),
    "compare": ("比較", "grammar", "Comparisons"),
    "quantity": ("數量詞與可數名詞", "grammar", "Quantifiers and Countable Nouns"),
    "parallel": ("平行結構與成對連接詞", "grammar", "Parallel Structure and Paired Conjunctions"),
    "collocation": ("搭配詞", "vocab", "Collocations"),
    "synonym": ("近義辨析", "vocab", "Near Synonyms"),
    "business": ("商業字彙", "vocab", "Business Vocabulary"),
    "family": ("同字根不同義", "vocab", "Word Families"),
    "qr-wh": ("應答：wh 問句", "listen", "Responses: Wh- Questions"),
    "qr-yesno": ("應答：Yes/No 與附加問句", "listen", "Responses: Yes/No and Tag Questions"),
    "qr-indirect": ("應答：間接回答", "listen", "Responses: Indirect Answers"),
    "conv-topic": ("對話：主旨與場合", "listen", "Conversations: Topic and Setting"),
    "conv-detail": ("對話：細節", "listen", "Conversations: Details"),
    "conv-intent": ("對話：意圖與推論", "listen", "Conversations: Intent and Inference"),
    "conv-next": ("對話：下一步", "listen", "Conversations: What Happens Next"),
    "talk-topic": ("短講：主旨", "listen", "Talks: Topic"),
    "talk-detail": ("短講：細節", "listen", "Talks: Details"),
    "talk-next": ("短講：下一步", "listen", "Talks: What Happens Next"),
}
