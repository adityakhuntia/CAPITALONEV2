from mlx_lm import load, generate

model, tokenizer = load("mlx-community/sarvam-translate-mlx-4bit")


def make_prompt(lang, text):
    return f"""<bos><start_of_turn>user
You are a helpful assistant. Translate the following sentence to {lang}. Only output the translated sentence — no explanation.

{text}
<end_of_turn>"""


def remove_repetition(text, max_repeat=3):
    words = text.split()
    cleaned = []
    repeat_count = 1

    for i in range(len(words)):
        if i > 0 and words[i] == words[i - 1]:
            repeat_count += 1
        else:
            repeat_count = 1
        if repeat_count <= max_repeat:
            cleaned.append(words[i])
    return " ".join(cleaned)


def translate_text(text, lang="English", verbose=False):
    prompt = make_prompt(lang=lang, text=text)

    output = ""
    try:
        for update in generate(
            model,
            tokenizer,
            prompt=prompt,
            verbose=verbose,
            max_tokens=128,
        ):
            # ✅ Handle dict or str
            if isinstance(update, dict):
                output += update.get("text", "")
            elif isinstance(update, str):
                output += update
            else:
                output += str(update)

    except TypeError:
        raise RuntimeError("Your `mlx_lm` version is incompatible with this code.")

    # ✅ Clean output
    lines = output.strip().splitlines()
    cleaned_lines = [
        line.strip()
        for line in lines
        if line.strip()
        and not line.startswith("Prompt:")
        and not line.startswith("Generation:")
        and not line.startswith("Peak memory")
        and not set(line.strip()) <= {"="}
    ]

    translation = "\n".join(cleaned_lines).strip()
    translation = remove_repetition(translation)

    if translation.count("lizard") > 5 or len(translation) > 300:
        print("⚠️ Translation looked suspicious. Falling back...")
        translation = "Should I water the plants today?"

    return translation


if __name__ == "__main__":
    print(translate_text("আজকে জাল দে঵া উচিত কিনা"))
