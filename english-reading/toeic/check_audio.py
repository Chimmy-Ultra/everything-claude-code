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
NUM = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

def words(t):
    t = t.lower().replace("’", "'")
    t = re.sub(r"[^a-z0-9' ]+", " ", t)
    return [NUM.get(w, w) for w in t.split()]

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
