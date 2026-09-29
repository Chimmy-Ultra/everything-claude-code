# Generates every MP3 for the page with Kokoro v1.0 (kokoro-onnx).
# Setup: pip install kokoro-onnx lameenc numpy; apt-get install espeak-ng;
# pass the folder holding kokoro-v1.0.onnx and voices-v1.0.bin (from the
# github.com/thewh1teagle/kokoro-onnx releases, tag model-files-v1.0).
#   python make_audio.py /path/to/model-folder   (existing files are kept; FORCE=1 redoes all)
import os, sys
import numpy as np, lameenc
from kokoro_onnx import Kokoro, EspeakConfig
from content import GROUPS, TRAPS

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = sys.argv[1] if len(sys.argv) > 1 else "."
k = Kokoro(os.path.join(MODEL, "kokoro-v1.0.onnx"), os.path.join(MODEL, "voices-v1.0.bin"),
           espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                      data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))
EMMA, GEORGE = "bf_emma", "bm_george"

def plain(text):
    return text.replace("**", "").replace("“", '"').replace("”", '"').replace("…", "...")

def save(text, voice, rel):
    path = os.path.join(HERE, "audio", rel)
    if os.path.exists(path) and not os.environ.get("FORCE"):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s, sr = k.create(plain(text), voice=voice, speed=1.0, lang="en-gb")
    x = np.concatenate([np.zeros(int(sr * .12), np.float32), s.astype(np.float32), np.zeros(int(sr * .2), np.float32)])
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
    with open(path, "wb") as f:
        f.write(enc.encode((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()) + enc.flush())
    print(rel, round(len(x) / sr, 2), "s")

for _, _, _, items in GROUPS:
    for wid, word, _, _, _, _, _, examples in items:
        save(word.replace("…, ", "").replace(" / ", ", "), EMMA, f"w/{wid}.mp3")
        for n, (ex, _) in enumerate(examples, 1):
            save(ex, EMMA if n % 2 else GEORGE, f"ex/{wid}-{n}.mp3")

for i, (_, rights, _) in enumerate(TRAPS, 1):
    for j, right in enumerate(rights, 1):
        save(right, GEORGE, f"trap/{i}-{j}.mp3")
