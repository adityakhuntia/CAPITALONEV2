from sarvamai import SarvamAI

client = SarvamAI(
    api_subscription_key="sk_0w5etw1v_MYYLiMqU4Z1XG02MS74LiYA9",
)

def translate_text_cloud(text: str, target_lang: str, source_lang: str = "auto") -> str:

    response = client.text.translate(
        input=text,
        source_language_code=source_lang,
        target_language_code=target_lang,
        mode="formal",
        model="sarvam-translate:v1",
        numerals_format="native",
        speaker_gender="Male",
        enable_preprocessing=False,
    )

    # some clients return dict with .output / .text
    if isinstance(response, dict):
        return response.get("output", response)
    return response


print(translate_text_cloud("আজকে জাল দে঵া উচিত কিনা", "en-IN", "bn-IN"))
