# Generates every MP3 for the Scene Lab demos with Kokoro v1.0 (kokoro-onnx).
# Setup as in game-night/make_audio.py.   python make_audio.py /path/to/model-folder
# Files: w/<id>.mp3 and w/<id>e.mp3 (picture words), p/<id>-<n>.mp3 (phrase with slot option n),
# b/<id>.mp3 (barista), r/<id>.mp3 (a reply to that barista line).
import os, re, sys
import numpy as np, lameenc
from kokoro_onnx import Kokoro, EspeakConfig
from content import OBJECTS, INTENTS, BARISTA, VOICES

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = sys.argv[1] if len(sys.argv) > 1 else "."
k = Kokoro(os.path.join(MODEL, "kokoro-v1.0.onnx"), os.path.join(MODEL, "voices-v1.0.bin"),
           espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                      data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))

def spoken(text):
    return re.sub(r"\bWei\b", "Way", text)   # the model reads "Wei" as "why"

def save(text, voice, lang, rel):
    path = os.path.join(HERE, "audio", rel)
    if os.path.exists(path) and not os.environ.get("FORCE"):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s, sr = k.create(spoken(text), voice=voice, speed=1.0, lang=lang)
    x = np.concatenate([np.zeros(int(sr * .12), np.float32), s.astype(np.float32), np.zeros(int(sr * .2), np.float32)])
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
    with open(path, "wb") as f:
        f.write(enc.encode((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()) + enc.flush())
    print(rel, round(len(x) / sr, 2), "s")

def fill(chunk, n):
    return re.sub(r"\{([^}]+)\}", lambda m: m.group(1).split("|")[n], chunk)

def options(chunk):
    m = re.search(r"\{([^}]+)\}", chunk)
    return len(m.group(1).split("|")) if m else 1

B, C = VOICES["B"], VOICES["C"]
for n, (oid, word, _, ex, _, _) in enumerate(OBJECTS):
    v = B if n % 2 == 0 else C
    save(word, *v, f"w/{oid}.mp3")
    save(ex, *v, f"w/{oid}e.mp3")
for _, _, _, items in INTENTS:
    for pid, chunk, _, _ in items:
        for n in range(options(chunk)):
            save(fill(chunk, n), *C, f"p/{pid}-{n}.mp3")
for bid, line, _, reply in BARISTA:
    save(line, *B, f"b/{bid}.mp3")
    save(reply, *C, f"r/{bid}.mp3")
