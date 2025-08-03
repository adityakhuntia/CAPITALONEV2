import time
from intent_classify import classify_intent
from sarvam_translate import translate_text
from whisper_stt import transcribe_with_whisper


def timed(func):
    """Decorator to time functions and print their duration."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ Time taken by '{func.__name__}': {end - start:.2f} seconds\n")
        return result
    return wrapper


@timed
def step1_transcribe(audio_path: str, lang: str = "hi") -> str:
    print("Step 1: Transcribing Audio...")
    return transcribe_with_whisper(audio_path, lang=lang)


@timed
def step2_translate(text: str, target_lang: str = "English") -> str:
    print("Step 2: Translating Text...")
    return translate_text(text, lang=target_lang, verbose=False)


@timed
def step3_classify_intent(text: str) -> str:
    print("Step 3: Classifying Intent...")
    return classify_intent(text)


def pipeline(audio_path: str):
    # Step 1: Transcription
    transcription = step1_transcribe(audio_path)

    # Step 2: Translation
    translated_text = step2_translate(transcription)

    # Step 3: Intent Classification
    intent = step3_classify_intent(translated_text)

    print("Final Output:")
    print(f"Original (HI): {transcription}")
    print(f"Translated (EN): {translated_text}")
    print(f"Predicted Intent: {intent}")


if __name__ == "__main__":
    pipeline("audio.mp3")
