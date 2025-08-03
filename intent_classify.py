from sentence_transformers import SentenceTransformer, util
import torch

# Load model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Semantic examples per intent
INTENT_EXAMPLES = {
    "weather_query": [
        "What's the weather like today?",
        "Will it rain tomorrow?",
        "Weather forecast for my village",
    ],
    "crop_advice": [
        "Which crop should I grow now?",
        "What is the best crop for this season?",
        "Suggest crops based on soil",
    ],
    "market_price": [
        "What's the price of wheat in Delhi?",
        "Market rate for tomatoes today",
        "How much are onions selling for?",
    ],
    "disease_diagnosis": [
        "My plant has yellow spots",
        "Leaves are falling off suddenly",
        "Is this a pest or disease?",
    ],
    "soil_health": [
        "How fertile is my soil?",
        "Check soil pH levels",
        "Soil testing report advice",
    ],
    "irrigation_schedule": [
        "Should I water the plants tomorrow?",
        "When to irrigate my farm?",
        "Watering schedule for rice",
    ],
    "govt_scheme": [
        "Tell me about PM Kisan scheme",
        "Am I eligible for subsidies?",
        "Apply for government farming loan",
    ],
    "equipment_help": [
        "How to use a tractor?",
        "Sprayer machine not working",
        "Where can I rent equipment?",
    ],
    "fertilizer_advice": [
        "Which fertilizer to use?",
        "Urea or DAP for this crop?",
        "How much fertilizer is safe?",
    ],
    "general_chat": [
        "Hi there!",
        "How are you?",
        "What's up?",
    ],
}

# Pre-encode all examples
intent_embeddings = []
intent_labels = []

for intent, examples in INTENT_EXAMPLES.items():
    embs = model.encode(examples, convert_to_tensor=True)
    intent_embeddings.append(embs)
    intent_labels.extend([intent] * len(examples))

# Concatenate all embeddings into one tensor
intent_embeddings = torch.cat(intent_embeddings)

def classify_intent(user_input: str, threshold: float = 0.5):
    input_emb = model.encode(user_input, convert_to_tensor=True)
    scores = util.cos_sim(input_emb, intent_embeddings)[0]
    best_idx = torch.argmax(scores).item()
    best_score = scores[best_idx].item()

    if best_score < threshold:
        return "unknown"
    
    return intent_labels[best_idx]
