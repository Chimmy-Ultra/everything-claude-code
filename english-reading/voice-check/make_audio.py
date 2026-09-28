# Regenerates the MP3s in audio/ with Kokoro v1.0 (kokoro-onnx).
# Setup: pip install kokoro-onnx lameenc numpy; apt-get install espeak-ng;
# put kokoro-v1.0.onnx and voices-v1.0.bin (github.com/thewh1teagle/kokoro-onnx
# releases, tag model-files-v1.0) next to this script, then run it here.
# "Wei" is spelled "Way" in the script so the model says /weɪ/.
import os, json, numpy as np, lameenc
from kokoro_onnx import Kokoro, EspeakConfig
k = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin",
           espeak_config=EspeakConfig(lib_path="/usr/lib/x86_64-linux-gnu/libespeak-ng.so.1",
                                      data_path="/usr/lib/x86_64-linux-gnu/espeak-ng-data"))
OUT = "audio"; os.makedirs(f"{OUT}/voices", exist_ok=True); os.makedirs(f"{OUT}/dlg", exist_ok=True)

def mp3(samples, sr, path):
    pad0 = np.zeros(int(sr*0.12), dtype=np.float32); pad1 = np.zeros(int(sr*0.2), dtype=np.float32)
    x = np.concatenate([pad0, samples.astype(np.float32), pad1])
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()
    enc = lameenc.Encoder(); enc.set_bit_rate(64); enc.set_in_sample_rate(sr); enc.set_channels(1); enc.set_quality(2)
    data = enc.encode(pcm) + enc.flush()
    open(path, "wb").write(data)
    return round(len(x)/sr, 2), float(np.sqrt(np.mean(samples**2)))

meta = {}
line = "Hi, I just moved in next door. It's really nice to meet you."
for v in ["af_heart", "af_bella", "am_michael", "am_fenrir", "bf_emma", "bm_george"]:
    s, sr = k.create(line, voice=v, speed=1.0, lang="en-gb" if v[0] == "b" else "en-us")
    meta[f"voices/{v}"] = mp3(s, sr, f"{OUT}/voices/{v}.mp3")

K, N = "af_heart", "am_michael"
dlg = [
 (K, "Hi there! You must be the new neighbor. I'm Karen, from 4B."),
 (N, "Hi, Karen. I'm Way. I just moved in last week."),
 (K, "Oh, welcome! How are you settling in?"),
 (N, "Pretty well, thanks. I'm still unpacking, though. There are boxes everywhere."),
 (K, "Ha, I remember that feeling. If you need anything, just let me know."),
 (N, "That's really kind of you. Actually, do you know when they pick up the garbage?"),
 (K, "Tuesday mornings. Just put it out the night before."),
 (N, "Got it. Thanks, that's really helpful."),
 (K, "No problem. Anyway, I'll let you get back to your boxes. See you around!"),
 (N, "See you!"),
]
for i, (v, t) in enumerate(dlg, 1):
    s, sr = k.create(t, voice=v, speed=1.0, lang="en-us")
    meta[f"dlg/{i:02d}"] = mp3(s, sr, f"{OUT}/dlg/{i:02d}.mp3")
print(json.dumps(meta, indent=0))
