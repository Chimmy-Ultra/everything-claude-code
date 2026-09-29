# Generates every MP3 for the page with Kokoro v1.0 (kokoro-onnx).
# Setup: pip install kokoro-onnx lameenc numpy; apt-get install espeak-ng;
# pass the folder holding kokoro-v1.0.onnx and voices-v1.0.bin (from the
# github.com/thewh1teagle/kokoro-onnx releases, tag model-files-v1.0).
#   python make_audio.py /path/to/model-folder
import os, re, sys
import numpy as np, lameenc
from kokoro_onnx import Kokoro, EspeakConfig
from content import GROUPS, SCENES, VOICES

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = sys.argv[1] if len(sys.argv) > 1 else "."
k = Kokoro(os.path.join(MODEL, "kokoro-v1.0.onnx"), os.path.join(MODEL, "voices-v1.0.bin"),
           espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                      data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))

def plain(markup):
    s = re.sub(r"\[[a-d]\d:([^\]]+)\]", r"\1", markup)
    s = re.sub(r"\{([^|}]+)\|[^|}]+\|[^}]+\}", r"\1", s)
    return s.replace("“", '"').replace("”", '"')

def spoken(text):
    # The model reads "Wei" as "why"; "Way" gives the right /weɪ/.
    return re.sub(r"\bWei\b", "Way", text)

def save(text, voice, lang, rel):
    path = os.path.join(HERE, "audio", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    s, sr = k.create(spoken(text), voice=voice, speed=1.0, lang=lang)
    x = np.concatenate([np.zeros(int(sr * .12), np.float32), s.astype(np.float32), np.zeros(int(sr * .2), np.float32)])
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
    with open(path, "wb") as f:
        f.write(enc.encode((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()) + enc.flush())
    print(rel, round(len(x) / sr, 2), "s")

n = 0
for _, _, _, items in GROUPS:
    for wid, word, _, ex, _, _, _ in items:
        voice, lang = VOICES["E" if n % 2 == 0 else "G"]
        save(word, voice, lang, f"w/{wid}.mp3")
        if ex:
            save(ex, voice, lang, f"w/{wid}e.mp3")
        n += 1

for sid, _, _, _, lines in SCENES:
    for i, (who, markup, _) in enumerate(lines, 1):
        voice, lang = VOICES[who]
        save(plain(markup), voice, lang, f"{sid}/{i:02d}.mp3")
