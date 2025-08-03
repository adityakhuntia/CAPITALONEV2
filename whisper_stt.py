import subprocess
import os

def transcribe_with_whisper(audio_path, whisper_dir="whisper.cpp", model_name="ggml-large-v3-turbo.bin", lang="hi"):
    abs_audio_path = os.path.abspath(audio_path)
    model_path = os.path.join(whisper_dir, "models", model_name)
    cli_path = os.path.join(whisper_dir, "build", "bin", "whisper-cli")

    if not os.path.isfile(cli_path):
        raise FileNotFoundError(f"whisper-cli not found at: {cli_path}")
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model not found at: {model_path}")

    subprocess.run(
        [cli_path, "-m", model_path, "-f", abs_audio_path, "-l", lang, "-otxt"],
        check=True
    )

    transcript_path = abs_audio_path + ".txt"
    if not os.path.exists(transcript_path):
        raise FileNotFoundError(f"Expected output file not found: {transcript_path}")

    with open(transcript_path, "r", encoding="utf-8") as f:
        transcription = f.read().strip()

    os.remove(transcript_path)
    return transcription



#text = transcribe_with_whisper("audio.mp3")
#print("TRANSCRIPTION:", text)
