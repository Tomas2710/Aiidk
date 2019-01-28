import speech_recognition as sr
import pyttsx3
import webbrowser
import os

speech = sr.Recognizer
try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested  Driver Is Not found")
except RuntimeError:
    print("Driver failed to initialize")
voices = pyttsx3.init().getProperty("voices")



engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
rate = engine.getProperty("rate")
engine.setProperty("rate", rate)


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()



def read_voice_cmd():
    voice_text = ""
    print("Listening.....")
    with sr.Microphone() as source:
        audio = sr.Recognizer.listen(sr.Recognizer(), source)

    try:
        voice_text = speech.recognize_google(sr.Recognizer(), audio)

    except sr.UnknownValueError:
        pass

    except sr.RequestError as e:
        print("Network Error")

    return voice_text


if __name__ == '__main__':

    speak_text_cmd("Hello there this is Thomas' AI")

    while True:

        voice_note = read_voice_cmd()
        print("cmd : {}".format(voice_note))

        if "hello" in voice_note:
            speak_text_cmd("Hello there, How are you?")
            continue

        elif "open" in voice_note:
            os.system("explorer C:\\ {}".format(voice_note.replace("Open ", "")))
            continue

        elif "bye" in voice_note:
            speak_text_cmd("Bye, if you need any help just start me up!")
            exit()

        elif "Thomas is best" in voice_note:
            speak_text_cmd("Well of course he is")


 