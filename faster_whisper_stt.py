import time
from faster_whisper import WhisperModel

# Load the model (do this only once; it's slow the first time)
model = WhisperModel("large-v3", compute_type="int8")

# Start timing
start_time = time.time()

# Run transcription
segments, _ = model.transcribe("audio.mp3")

# End timing
end_time = time.time()

# Output transcription
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# Show time taken
print(f"\n⏱️ Transcription took {end_time - start_time:.2f} seconds")
