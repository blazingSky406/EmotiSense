"""
Flask-based web application for emotion detection.

This application provides an API to detect emotions from text input.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Constants for configuration
PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def render_index_page():
    """
    Renders the index page with an input form for emotion detection.

    Returns:
        HTML page rendered from the 'index.html' template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emot_detector():
    """
    Detects emotions in a given text input.

    Expects a query parameter 'textToAnalyze' with the text to analyze.

    Returns:
        JSON response with the predicted emotions or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return '<strong>Invalid text! Please try again!</strong>'
    dom_emotion = f"<strong>{response['dominant_emotion']}</strong>"
    output = (
        f"For the given statement, the system response is {response}. "
        f"The dominant emotion is {dom_emotion}."
    )
    return output
if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
