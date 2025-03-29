from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    data = request.get_json()
    text_to_analyze = data.get("text", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided to check"}), 400

    result = emotion_detector(text_to_analyze)
    formatted = (
        f"For this statement response is 'anger': {result['anger']},"
        f"'disgust': {result['disgust']}, 'fear': {result['fear']},"
        f"'joy': {result['joy']}, 'sadness': {result['sadness']}."
        f"Dominant emotion is: {result['dominant_emotion']}."
    )
    return jsonify(result=result, formatted=formatted)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)