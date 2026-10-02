# Generates every MP3 for the page with Kokoro v1.0 (kokoro-onnx), US voices.
# Setup: pip install kokoro-onnx lameenc numpy; apt-get install espeak-ng;
# pass the folder holding kokoro-v1.0.onnx and voices-v1.0.bin (from the
# github.com/thewh1teagle/kokoro-onnx releases, tag model-files-v1.0).
#   python make_audio.py /path/to/model-folder   (existing files are kept; FORCE=1 redoes all)
import os, re, sys
import numpy as np, lameenc
from kokoro_onnx import Kokoro, EspeakConfig
from content import SOCIAL, GAMES, VOICES

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = sys.argv[1] if len(sys.argv) > 1 else "."
k = Kokoro(os.path.join(MODEL, "kokoro-v1.0.onnx"), os.path.join(MODEL, "voices-v1.0.bin"),
           espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                      data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))

# Slots are read with a sample word so the sentence still sounds natural.
FILL = {"name": "Alex", "country": "Canada"}

def spoken(text):
    text = re.sub(r"\[([^\]]+)\]", lambda m: FILL.get(m.group(1), ""), text)
    return text.replace("…", "").replace("“", '"').replace("”", '"').strip()

def save(text, who, rel):
    path = os.path.join(HERE, "audio", rel)
    if os.path.exists(path) and not os.environ.get("FORCE"):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    voice, lang = VOICES[who]
    s, sr = k.create(spoken(text), voice=voice, speed=1.0, lang=lang)
    x = np.concatenate([np.zeros(int(sr * .1), np.float32), s.astype(np.float32), np.zeros(int(sr * .2), np.float32)])
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
    with open(path, "wb") as f:
        f.write(enc.encode((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()) + enc.flush())
    print(rel, round(len(x) / sr, 2), "s")

n = 0
def alt():
    global n
    n += 1
    return "A" if n % 2 else "B"

for _, _, _, _, items in SOCIAL:
    for pid, en, _, _ in items:
        save(en, alt(), f"p/{pid}.mp3")

for g in GAMES:
    for tid, term, _ in g.get("terms", []):
        save(g.get("say", {}).get(tid, term), alt(), f"t/{g['id']}-{tid}.mp3")
    for pid, en, _, _ in g.get("phrases", []):
        save(en, alt(), f"p/{pid}.mp3")
    if g.get("script"):
        for i, (en, _) in enumerate(g["script"]["lines"], 1):
            save(en, "B", f"s/{g['id']}-{i:02d}.mp3")
