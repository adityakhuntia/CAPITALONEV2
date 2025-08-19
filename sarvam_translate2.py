from mlx_lm import load, generate

# Load model and tokenizer
model, tokenizer = load("mlx-community/sarvam-translate-mlx-4bit")


#def make_prompt(lang, text):
#    return f"""<bos><start_of_turn>user
#Translate the text below to {lang}.
#
#{text}<end_of_turn>
#"""


def make_prompt(lang, text):
    return f"Translate to {lang}:\n{text}"



def translate_text(text, lang="English", verbose=False):
    prompt = make_prompt(lang=lang, text=text)
    raw_output = generate(model, tokenizer, prompt, verbose=False)
    
    # Clean the output
    lines = raw_output.strip().splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip() and not line.startswith("Prompt:") and not line.startswith("Generation:") and not line.startswith("Peak memory")]
    
    # Filter out separators like "=========="
    translation = "\n".join(line for line in cleaned_lines if not set(line) <= {"="})
    return translation.strip()


#result = translate_text("मेरा नाम आदित्य है, क्या मैं कल पॉधों में पानी डालूं?")
#print(result)

print(translate_text("আজকে জাল দে঵া উচিত কিনা"))