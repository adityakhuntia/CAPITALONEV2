import threading
import time
from sarvam_translate import translate_text
from whisper_stt import transcribe_with_whisper
from intent_classify import classify_intent

# 🧠 Shared results
results = {
    "transcription": None,
    "translation": None,
    "intent": None
}

# ✅ Event for translation readiness
translation_ready = threading.Event()

# ⏱️ Timer decorator
def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"⏱️ Time taken by '{func.__name__}': {duration:.2f} seconds")
        return result
    return wrapper

# 🌐 Translator (Sarvam)
@timed
def run_translation():
    if results["transcription"]:
        results["translation"] = translate_text(results["transcription"], lang="English")
    translation_ready.set()  # ✅ Signal completion

# 🧠 Intent Classifier
@timed
def run_classification():
    translation_ready.wait()  # ✅ Wait until translation is ready
    if results["translation"]:
        results["intent"] = classify_intent(results["translation"])

# 🚀 Main pipeline
def run_pipeline(audio_path):
    wall_start = time.perf_counter()

    # Step 1: Transcription
    print("Transcribing...")
    results["transcription"] = transcribe_with_whisper(audio_path, lang="bn")

    # Step 2 & 3: Parallel translation + classification
    print("Translating and classifying...")
    t1 = threading.Thread(target=run_translation)
    t2 = threading.Thread(target=run_classification)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    wall_total = time.perf_counter() - wall_start

    # ✅ Final output
    print("\nFinal Output:")
    print("Original:", results["transcription"])
    print("Translated (EN):", results["translation"])
    print("Predicted Intent:", results["intent"])
    print(f"\n🕒 Total wall-clock time: {wall_total:.2f} seconds")

# 🧪 Example run
if __name__ == "__main__":
    run_pipeline("audio.mp3")
