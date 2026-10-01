# American IPA for word cards, taken from the CMU Pronouncing Dictionary (pip install cmudict).
# Nothing is guessed: a word the dictionary doesn't have gets no IPA.
import re
import cmudict

_D = cmudict.dict()
V = {"AA": "ɑː", "AE": "æ", "AH": "ʌ", "AO": "ɔː", "AW": "aʊ", "AY": "aɪ", "EH": "e", "ER": "ɜr", "EY": "eɪ",
     "IH": "ɪ", "IY": "iː", "OW": "oʊ", "OY": "ɔɪ", "UH": "ʊ", "UW": "uː"}
C = {"B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "F": "f", "G": "ɡ", "HH": "h", "JH": "dʒ", "K": "k", "L": "l", "M": "m",
     "N": "n", "NG": "ŋ", "P": "p", "R": "r", "S": "s", "SH": "ʃ", "T": "t", "TH": "θ", "V": "v", "W": "w", "Y": "j",
     "Z": "z", "ZH": "ʒ"}
ONSETS = {tuple(o.split()) for o in """P R|P L|B R|B L|T R|D R|K R|K L|G R|G L|F R|F L|TH R|SH R|S P|S T|S K|S M|S N|S L|S W|
S P L|S P R|S T R|S K R|S K W|T W|D W|K W|G W|TH W|P Y|B Y|K Y|M Y|F Y|V Y|HH Y|S K Y|S P Y""".replace("\n", "").split("|")}


def _word(phones):
    syl, cons = [], []          # syllables as (stress, onset, nucleus) with codas glued to the previous one
    for p in phones:
        m = re.match(r"([A-Z]+)(\d)?$", p)
        base, st = m.group(1), m.group(2)
        if st is None: cons.append(base); continue
        # split the consonants between the previous vowel and this one: longest legal onset goes here
        k = len(cons)
        for n in range(len(cons), 0, -1):
            tail = tuple(cons[-n:])
            if n == 1 and tail[0] != "NG" or tail in ONSETS: k = len(cons) - n; break
        else:
            k = len(cons)
        if syl: syl[-1][2] += cons[:k]
        onset = cons[k:] if syl else cons
        vowel = V[base]
        if base == "AH" and st == "0": vowel = "ə"
        if base == "ER" and st == "0": vowel = "ər"
        if st == "0" and vowel.endswith("ː"): vowel = vowel[:-1]
        syl.append([st, onset, [vowel]]); cons = []
    if syl: syl[-1][2] += cons
    out = ""
    for st, onset, rest in syl:
        mark = "ˈ" if st == "1" and len(syl) > 1 else "ˌ" if st == "2" else ""
        out += mark + "".join(C[c] for c in onset) + rest[0] + "".join(C[c] for c in rest[1:])
    return out


def ipa(text):
    """'billing department' -> '/ˈbɪlɪŋ dɪˈpɑːrtmənt/', or None if any word is missing."""
    parts = []
    for w in re.findall(r"[A-Za-z']+", text.lower()):
        prons = _D.get(w)
        if not prons: return None
        parts.append(_word(prons[0]))
    return "/" + " ".join(parts) + "/" if parts else None


if __name__ == "__main__":
    import sys
    for w in sys.argv[1:]: print(w, ipa(w))
