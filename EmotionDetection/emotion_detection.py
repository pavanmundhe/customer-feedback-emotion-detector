"""Analyze text with the Skills Network Watson emotion model."""

import requests

EMOTION_DETECTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_HEADER = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def _empty_result():
    """Return the complete result shape with no predictions."""
    return {emotion: None for emotion in (*EMOTIONS, "dominant_emotion")}


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the dominant emotion for the text."""
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    response = requests.post(
        EMOTION_DETECTION_URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers=MODEL_HEADER,
        timeout=30,
    )
    if response.status_code == 400:
        return _empty_result()
    response.raise_for_status()

    emotion_scores = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: emotion_scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(EMOTIONS, key=result.get)
    return result
