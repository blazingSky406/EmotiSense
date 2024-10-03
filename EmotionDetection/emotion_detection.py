import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url = url, headers = headers, json = input_json)

    json_response = json.loads(response.text)

    output = {}
    
    if response.status_code == 200:
        pred_emotions = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(pred_emotions, key = pred_emotions.get)
        output = pred_emotions.copy()
        output['dominant_emotion'] = dominant_emotion

    elif response.status_code == 400:
        output = {'anger': None, 'sadness': None, 'joy': None, 'disgust': None, 'fear': None, 'dominant_emotion' : None}

    return output

