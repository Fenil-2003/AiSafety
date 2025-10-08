import collections
from transformers import pipeline
import config

def load_all_models():
    print("-> Loading Abuse Detector...")
    loaded_models = {}
    loaded_models['abuse'] = pipeline("text-classification", model=config.MODEL_NAMES["abuse"], top_k=None)
    print("-> Loading Crisis Intervenor...")
    loaded_models['crisis'] = pipeline("text-classification", model=config.MODEL_NAMES["crisis"], top_k=None)
    print("-> Loading Content Filter...")
    loaded_models['filter'] = pipeline("zero-shot-classification", model=config.MODEL_NAMES["filter"])
    print("-> Loading Sentiment Analyzer...")
    loaded_models['sentiment'] = pipeline("sentiment-analysis", model=config.MODEL_NAMES["sentiment"])
    return loaded_models

# --- All analysis functions now accept a 'models_dict' argument ---

def analyze_abuse(text, models_dict):
    predictions = models_dict['abuse'](text)[0]
    toxic_score = next((p['score'] for p in predictions if p['label'] == 'toxic'), 0.0)
    return {"is_abusive": toxic_score > config.ABUSE_THRESHOLD, "Abuse Score": round(toxic_score, 2)}

def analyze_crisis(text, models_dict):
    predictions = models_dict['crisis'](text)[0]
    for pred in predictions:
        if pred['label'] in config.CRISIS_EMOTIONS and pred['score'] > config.CRISIS_THRESHOLD:
            return {"is_crisis": True, "emotion": pred['label'], "Crisis Score": round(pred['score'], 2)}
    return {"is_crisis": False}

def filter_content(text, age_profile, models_dict):
    text_lower = text.lower()
    for keyword in config.KEYWORD_FILTERS.get(age_profile, set()):
        if keyword in text_lower:
            return {"is_blocked": True, "reason": f"Keyword '{keyword}'"}

    candidate_topics = config.TOPIC_FILTERS.get(age_profile, [])
    if candidate_topics:
        topic_results = models_dict['filter'](text, candidate_labels=candidate_topics)
        if topic_results['scores'][0] > config.FILTER_TOPIC_THRESHOLD:
            return {"is_blocked": True, "reason": f"Topic '{topic_results['labels'][0]}'"}
    return {"is_blocked": False}

def analyze_escalation(text, models_dict,conversation_history):
    CONVERSATION_HISTORY=conversation_history
    sentiment = models_dict['sentiment'](text)[0]
    score = -sentiment['score'] if sentiment['label'] == 'NEGATIVE' else sentiment['score']
    CONVERSATION_HISTORY.append(score)
    print(f"Updated Conversation History: {list(CONVERSATION_HISTORY)}")

    if len(CONVERSATION_HISTORY) < 3:
        return {"status": "Stable", "reason": "Not enough history."}
    if all(s < 0 for s in list(CONVERSATION_HISTORY)[-3:]):
        return {"status": "High", "reason": "Last 3 messages were negative."}
    if sum(CONVERSATION_HISTORY) / len(CONVERSATION_HISTORY) < -0.5:
        return {"status": "Medium", "reason": "Overall sentiment is negative."}
    return {"status": "Stable", "reason": "Conversation appears stable."}

def analyze_message_fully(text, user_profile, models_dict,conversation_history):
    abuse_result = analyze_abuse(text, models_dict)
    crisis_result = analyze_crisis(text, models_dict)
    
    # --- THIS IS THE FIX ---
    # OLD LINE:
    # filter_result = filter_content(text, user_profile, models_dict)
    
    # NEW LINE:
    # Extract the age_profile string from the user_profile dictionary before passing it.
    age_profile_string = user_profile.get("age_profile", "adult")
    filter_result = filter_content(text, age_profile_string, models_dict)
    # -----------------------

    escalation_result = analyze_escalation(text, models_dict,conversation_history)

    final_action = "Allow"
    if abuse_result["is_abusive"] or filter_result["is_blocked"]:
        final_action = "Block"
    elif crisis_result["is_crisis"]:
        final_action = "Flag for Human Review"
        
    return {
        "Final Action": final_action,
        "Abuse Detection": abuse_result,
        "Crisis Intervention": crisis_result,
        "Content Filter": filter_result,
        "Escalation Status": escalation_result,
    }