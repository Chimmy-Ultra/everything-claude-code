# Listens back to every listening clip with Whisper small.en (sherpa-onnx) and compares it with the script,
# since nobody can listen to each file by hand here. Prints clips where the recognised words differ.
#   python check_audio.py /path/to/sherpa-onnx-whisper-small.en
import os, re, sys, difflib
import numpy as np, miniaudio, sherpa_onnx
from content import ITEMS

HERE = os.path.dirname(os.path.abspath(__file__))
W = sys.argv[1].rstrip("/") + "/"
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=W + "small.en-encoder.int8.onnx", decoder=W + "small.en-decoder.int8.onnx",
                                                 tokens=W + "small.en-tokens.txt", language="en", task="transcribe", num_threads=4)
import unicodedata
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
ORD = {"one": "first", "two": "second", "three": "third", "five": "fifth", "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}

def num2words(n, to="cardinal"):
    if n < 20: w = ONES[n]
    elif n < 100: w = TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    elif n < 1000: w = ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + num2words(n % 100))
    else: w = num2words(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + num2words(n % 1000))
    if to == "ordinal":
        head, _, last = w.rpartition(" ")
        last = ORD.get(last, last[:-1] + "ieth" if last.endswith("y") else last + "th")
        w = (head + " " + last).strip()
    return w

def words(t):
    # compare words, not spelling: strip accents, spell out digits (Whisper writes "45", the script says "forty-five")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().replace("’", "'")
    t = re.sub(r"(\d+)(st|nd|rd|th)\b", lambda m: num2words(int(m.group(1)), to="ordinal"), t)
    t = re.sub(r"\d+", lambda m: " " + num2words(int(m.group(0))) + " ", t)
    t = re.sub(r"[^a-z' ]+", " ", t)
    return t.split()

bad = 0
for it in ITEMS:
    if it["type"] != "listen":
        continue
    for ln in it["audio"]["lines"]:
        d = miniaudio.decode_file(os.path.join(HERE, it["audio"]["dir"], ln["file"]), output_format=miniaudio.SampleFormat.FLOAT32, nchannels=1, sample_rate=16000)
        s = rec.create_stream(); s.accept_waveform(16000, np.frombuffer(d.samples, dtype=np.float32)); rec.decode_stream(s)
        heard, want = words(s.result.text), words(ln.get("say") or ln["text"])
        ratio = difflib.SequenceMatcher(None, heard, want).ratio()
        if ratio < 0.9:
            bad += 1
            print(f"{it['id']}/{ln['file']}  match {ratio:.2f}\n  script: {' '.join(want)}\n  heard:  {' '.join(heard)}")
print("clips to check:", bad)
