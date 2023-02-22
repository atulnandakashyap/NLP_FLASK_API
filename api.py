import paralleldots

paralleldots.set_api_key("sEO8CCxoGu0TpuWd7o6jaWXUzWUcVa3XklY5JJ7f2AU")

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentiment_analysis(text):
    sentiment = paralleldots.sentiment(text)
    return sentiment

def abuse_detection(text):
    response = paralleldots.abuse(text)
    return response

def emotion_detection(text):
    response = paralleldots.emotion(text)
    return response
