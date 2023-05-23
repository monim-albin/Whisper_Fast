from faster_whisper import WhisperModel

model = WhisperModel("large-v2")

segments, info = model.transcribe("C:/Users/User/Documents/Sound recordings/content/Recording (2).m4a")
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))