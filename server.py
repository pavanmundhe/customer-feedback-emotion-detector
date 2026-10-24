"""Serve the emotion detector web application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)
INVALID_TEXT_MESSAGE = "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    """Render the emotion detector interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the supplied text and return formatted emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "").strip()
    if not text_to_analyze:
        return INVALID_TEXT_MESSAGE, 400

    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return INVALID_TEXT_MESSAGE, 400

    formatted_scores = ", ".join(
        f"'{emotion}': {result[emotion]}"
        for emotion in ("anger", "disgust", "fear", "joy", "sadness")
    )
    return (
        f"For the given statement, the system response is {formatted_scores}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
