from gtts import gTTS


def text_to_speech(text, output_path):
    tts = gTTS(text=text, lang='en-in')
    tts.save(output_path)
    return output_path
