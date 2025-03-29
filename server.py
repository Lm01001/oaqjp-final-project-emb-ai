"""
This module is responsible for running the Flask web application that 
handles emotion detection requests. The application receives data 
through the '/emotionDetector' endpoint, and after all operations
returns the result along with a formatted response.
It provides a home page created from the index.html template.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page.
    
    Responsible for the route to the home page and renders the 
    index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Analyzes the emotion in the provided text.
    
    This function handles the '/emotionDetector' POST request. It expects 
    a JSON object with a 'text' field. After all operations results are 
    returned in a JSON response. In case when input is invalid, 
    it returns an error message.
    """
    data = request.get_json()

    print(f"Received data: {data}")

    text_to_analyze = data.get("text", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided to check"}), 400
    if not text_to_analyze.strip():
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    print(f"Text to analyze: {text_to_analyze}")
    result = emotion_detector(text_to_analyze)
    print(f"Emotion detection result: {result}")

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    formatted = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']}, and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify(result=result, formatted=formatted)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='localhost', port=5000)
