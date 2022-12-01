import speech_recognition as SpeechRecognition

def record_volume():
    r = SpeechRecognition.Recognizer()
    r.pause_threshold = 0.5
    with SpeechRecognition.Microphone(device_index = 33) as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language = 'ru-RU')
    except:
        return 'Error'