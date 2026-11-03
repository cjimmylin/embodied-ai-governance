"""Narrate a script and assemble the video. Usage: python3 make_talk.py <script.md> <frames_dir> <work_dir> <voice> <title> <out.mp4> [rate]
Each '## N. Title' section is one slide; frames are the sorted PNGs in frames_dir (one per section)."""
import asyncio, re, subprocess, sys, os, glob, json
script, FR_DIR, WORK, VOICE, TITLE, OUT = sys.argv[1:7]; RATE = sys.argv[7] if len(sys.argv) > 7 else "-3%"
AUD = os.path.join(WORK, "audio"); SEG = os.path.join(WORK, "segments"); os.makedirs(AUD, exist_ok=True); os.makedirs(SEG, exist_ok=True)
text = open(script, encoding="utf8").read()
parts = re.split(r"^## (\d+)\. (.*)$", text, flags=re.M)
slides = [(int(parts[i]), parts[i+1].strip(), parts[i+2].strip()) for i in range(1, len(parts), 3)]
FR = sorted(glob.glob(os.path.join(FR_DIR, "*.png")))
assert len(FR) == len(slides), (len(FR), len(slides))
json.dump([{"n": n, "title": t, "words": len(b.split())} for n, t, b in slides], open(os.path.join(WORK, "script_stats.json"), "w"), indent=1)
print("sections", len(slides), "words", sum(len(b.split()) for _, _, b in slides), flush=True)

async def edge(n, body):
    import edge_tts
    out = os.path.join(AUD, f"{n:02d}.mp3")
    if os.path.exists(out) and os.path.getsize(out) > 1000: return True
    for attempt in range(5):
        try:
            c = edge_tts.Communicate(body, VOICE, rate=RATE); await c.save(out)
            if os.path.getsize(out) > 1000: return True
        except Exception as e:
            print("edge retry", n, attempt, repr(e)[:120], flush=True); await asyncio.sleep(3 + 3*attempt)
    return False
def piper(n, body):
    wav = os.path.join(AUD, f"{n:02d}.wav"); model = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tts", "en_GB-alan-medium.onnx")
    subprocess.run(["piper", "--model", model, "--output_file", wav], input=body.encode(), check=True, capture_output=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, os.path.join(AUD, f"{n:02d}.mp3")], check=True)
async def narrate():
    fb = []
    for n, _, body in slides:
        ok = await edge(n, body)
        if not ok: piper(n, body); fb.append(n)
        print("audio", n, "edge" if ok else "piper", flush=True)
    print("narration done; piper fallback:", fb, flush=True)
asyncio.run(narrate())

PAD = 1.0
def dur(f): return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout.strip())
segs, t, chapters, srt = [], 0.0, [], []
def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")
for i, ((n, title, body), fr) in enumerate(zip(slides, FR), 1):
    au = os.path.join(AUD, f"{n:02d}.mp3"); out = os.path.join(SEG, f"{i:02d}.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", "24", "-i", fr, "-i", au, "-af", f"apad=pad_dur={PAD}",
                    "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-shortest", out], check=True)
    d = dur(out); chapters.append((t, t + d, title))
    # subtitle: split narration into ~12-word cues spread over the segment
    words = body.split(); cues = [" ".join(words[k:k+12]) for k in range(0, len(words), 12)]; per = (d - PAD) / max(len(cues), 1)
    for k, cue in enumerate(cues): srt.append(f"{len(srt)+1}\n{ts(t + k*per)} --> {ts(t + (k+1)*per - 0.05)}\n{cue}\n\n")
    t += d; segs.append(out); print("segment", i, round(d, 1), "s", flush=True)
open(os.path.join(SEG, "list.txt"), "w").write("".join(f"file '{s}'\n" for s in segs))
meta = f";FFMETADATA1\ntitle={TITLE}\n" + "".join(f"\n[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(a*1000)}\nEND={int(b*1000)}\ntitle={ti}\n" for a, b, ti in chapters)
open(os.path.join(WORK, "chapters.txt"), "w").write(meta)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(SEG, "list.txt"), "-i", os.path.join(WORK, "chapters.txt"), "-map_metadata", "1", "-c", "copy", "-movflags", "+faststart", OUT], check=True)
open(OUT[:-4] + ".srt", "w", encoding="utf8").write("".join(srt))
print("FINAL", OUT, round(t/60, 1), "minutes", os.path.getsize(OUT)//1_000_000, "MB", flush=True)
