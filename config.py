
MODEL_NAMES = {
    "abuse": "martin-ha/toxic-comment-model",
    "crisis": "j-hartmann/emotion-english-distilroberta-base",
    "filter": "typeform/distilbert-base-uncased-mnli",
    "sentiment": "distilbert-base-uncased-finetuned-sst-2-english"
}

ABUSE_THRESHOLD = 0.6
CRISIS_THRESHOLD = 0.7
CRISIS_EMOTIONS = {"sadness", "fear"}
FILTER_TOPIC_THRESHOLD = 0.5
ESCALATION_HISTORY_SIZE = 6

KEYWORD_FILTERS = {
    "child": {"violence", "weapon", "death", "gun"},
    "teen": {"politics", "finance", "gambling"}
}

TOPIC_FILTERS = {
    "child": ["War", "Politics", "Religion", "Finance"],
    "teen": ["Stock Market", "Gambling"]
}