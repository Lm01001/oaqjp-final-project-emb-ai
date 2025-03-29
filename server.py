from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    data = request.get_json()
    
    print(f"Received data: {data}")

    text_to_analyze = data.get("text", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided to check"}), 400

    print(f"Text to analyze: {text_to_analyze}")
    result = emotion_detector(text_to_analyze)
    print(f"Emotion detection result: {result}")

    formatted = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']}, and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify(result=result, formatted=formatted)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
