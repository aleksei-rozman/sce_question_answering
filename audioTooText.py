import speech_recognition as speech_recog

import subprocess


def startDecod():#преобразование звука в текст
    subprocess.call(['ffmpeg', '-i', 'new_file.ogg', '-c:a', 'pcm_s16le', 'new_file.wav','-y'])
    sample_audio = speech_recog.AudioFile('new_file.wav')

    recog = speech_recog.Recognizer()
    with sample_audio as audio_file:
        audio_content = recog.record(audio_file)
    a = recog.recognize_google(audio_content, language="en-Us")
    return str(a)

