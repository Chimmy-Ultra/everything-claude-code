# Records every listening line with Kokoro v1.0 (kokoro-onnx) into audio/<item id>/<file>.
# Setup as in game-night/make_audio.py.   python make_audio.py /path/to/kokoro-model-folder
# A voice written "melo:<n>" uses MeloTTS English through sherpa-onnx instead (n: 0 US, 1 UK, 2 Indian, 3 Australian);
# pass its folder with MELO=/path/to/vits-melo-tts-en.   Existing files are kept; FORCE=1 redoes all.
import os, re, sys
import numpy as np, lameenc
from content import ITEMS

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = sys.argv[1] if len(sys.argv) > 1 else "."
_kokoro = _melo = None

def kokoro():
    global _kokoro
    if _kokoro is None:
        from kokoro_onnx import Kokoro, EspeakConfig
        _kokoro = Kokoro(os.path.join(MODEL, "kokoro-v1.0.onnx"), os.path.join(MODEL, "voices-v1.0.bin"),
                         espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                                    data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))
    return _kokoro

def melo():
    global _melo
    if _melo is None:
        import sherpa_onnx
        m = os.environ["MELO"].rstrip("/") + "/"
        _melo = sherpa_onnx.OfflineTts(sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=m + "model.onnx", lexicon=m + "lexicon.txt", tokens=m + "tokens.txt"), num_threads=4)))
    return _melo

def spoken(text):
    return re.sub(r"\bWei\b", "Way", text)   # the model reads "Wei" as "why"

def synth(text, voice):
    if voice.startswith("melo:"):
        a = melo().generate(text, sid=int(voice[5:]), speed=1.0)
        return np.array(a.samples, np.float32), a.sample_rate
    lang = "en-gb" if voice[0] == "b" else "en-us"
    return kokoro().create(spoken(text), voice=voice, speed=1.0, lang=lang)

n = 0
for it in ITEMS:
    if it["type"] != "listen":
        continue
    for ln in it["audio"]["lines"]:
        path = os.path.join(HERE, it["audio"]["dir"], ln["file"])
        if os.path.exists(path) and not os.environ.get("FORCE"):
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        s, sr = synth(ln.get("say") or ln["text"], ln["voice"])
        x = np.concatenate([np.zeros(int(sr * .12), np.float32), np.asarray(s, np.float32), np.zeros(int(sr * .2), np.float32)])
        enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
        with open(path, "wb") as f:
            f.write(enc.encode((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()) + enc.flush())
        n += 1
        print(it["id"], ln["file"], round(len(x) / sr, 2), "s")
print("recorded", n)
