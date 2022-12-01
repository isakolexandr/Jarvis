import pyttsx3

def play(text):
    tts = pyttsx3.init()

    tts.setProperty('rate', tts.getProperty('rate') - 50)

    volume = tts.getProperty('volume')
    tts.setProperty('volume', volume + 0.9)

    for voice in tts.getProperty('voices'):
        if voice.name == 'Microsoft Irina Desktop - Russian':
            tts.setProperty('voice', voice.id)

    tts.say(text)
    tts.runAndWait()