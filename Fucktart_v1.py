import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random

speech = sr.Recognizer()
# ======================[ Word Dictionaries ]============================================
greeting_dict = {"hello": "hello", "hi": "hi"}
open_dict = {"open": "open", "launch": "launch"}
social_dic = {"Twitter": "http://www.twitter.com", "Facebook": "http://www.facebook.com",
              "Instagram": "http://www.instagram.com"}
google_searches_dict = {"what": "what", "why": "why", "who": "who", "which": "which", "when": "when", "where": "where"}
meme_word_dict = {"lol": "lol", "LMAO": "LMAO", "XD": "XD"}

# ======================[ MP3 Lists ]=============================================
google_searches = ["MP3's/google_search_1.mp3", "MP3's/google_search_2.mp3", "MP3's/google_search_3.mp3",
                   "MP3's/google_search_4.mp3", "MP3's/google_search_5.mp3"]
after_greeting = ["C:\Users\\tomas\PycharmProjects\Aiidk\MP3's\\after_greeting.mp3",
                  "C:\Users\\tomas\PycharmProjects\Aiidk\MP3's\\after_greeting_2.mp3"]
open_list = ["MP3's/open_1.mp3", "MP3's/open_2.mp3", "MP3's/open_3.mp3"]
bye_mp3s = ["MP3's/bye_1.mp3", "MP3's/bye_2.mp3", "MP3's/bye_3.mp3"]
# ================================================================================


def is_valid_google_search(phrase):
    if google_searches_dict.get(phrase.split(" ")[0]) == phrase.split(" ")[0]:  # Checks if the phrases are the same
        return True  # Returns True for the elif statements


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)  # Just a thing which makes it below look a bit neater
    playsound(mp3)


def read_voice_cmd():
    voice_text = ""  # Makes sure there are no errors in the beginning
    print("Listening.....") # So we know when it is starting to listen
    with sr.Microphone() as source:
        audio = sr.Recognizer.listen(sr.Recognizer(), source=source)  # Starts to listen
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:  # If it doesn't know what you said
        pass
    except sr.RequestError:  # Can't get what you are saying from the mic
        print("Network Error")
    except sr.WaitTimeoutError:  # If you take to long to respond
        pass
    return voice_text  # So you can get it from other methods


def is_valid_greeting(greet_dic, voice_notes): # This is to check if what they said is "hello" or "hi"
    for key, value in greet_dic.iteritems(): # Checks every value in the greeting dictionary
        # and compares it to the first word in the voice note
        if value == voice_notes.split(" ")[0]:  # It is the fist one because the greeting will always be first
            return True  # Returns True/False for the If statements
    return False


def is_valid_open(open_dic, voice_notes):  # Valid open basically checks if you said "open" or "launch"
    try:
        for keys, value in open_dic.iteritems():
            if value == voice_notes.split(" ")[0]:  # checks if the first word is "open" or "launch"
                return True  # for the if statements
            elif value == voice_note.split(" ")[1]:  # Checks for the facebook and instagram things
                return True
        return False
    except IndexError:  # Except if there is not command there is no array to look at so it is out of bounds,
        # that's the reason for this
        return False


if __name__ == '__main__':  # This is basically what it runs first, before anything else

    playsound("C:\Users\\tomas\PycharmProjects\Aiidk\MP3's\Hi.mp3")  # Plays the start sound

    while True:  # Keeps looping to make sure it is always on

        voice_note = read_voice_cmd()  # Initializes the read voice cmd to the variable voice_note
        print("cmd : {}".format(voice_note))  # So i can see what the program thinks I said

        if is_valid_greeting(greeting_dict, voice_note):  # Checks for valid greeting then does the next things:
            print("In greeting")
            play_sound(after_greeting)  # Initializes the play_sound() thing so it picks a random mp3 from that list
            continue  # Makes sure it is always checking for everything

        elif is_valid_open(open_dict, voice_note):  # Checks for either the social media things or the file
            print("Opening.....")
            play_sound(open_list)  # Picks a random MP3 from the list
            if is_valid_open(social_dic, voice_note):  # Makes sure the command wasn't a social media one
                key = voice_note.split(" ")[1]  # Sets the key to the second word if it was a social media one
                webbrowser.open(social_dic.get(key))  # And finally opens the website
            else:  # If it isn't a social media one
                # This executes a command through the command prompt opening the explorer
                os.system('explorer C:\\"{}"'.format(
                voice_note.replace("open ", "").replace("launch ", "").capitalize()))
            continue  # ALWAYS checking

        elif is_valid_google_search(voice_note):  # Checks if the first word was one of the five W's
            print("searching on google.....")  # So we know what is happening
            # Opens the browser with a google search query
            webbrowser.open("https://www.google.co.uk/search?q={}".format(voice_note))
            play_sound(google_searches)  # Plays one of the five google search MP3's

        elif "by" in voice_note:  # It is "by" because that is what the software thinks you say when you say "bye"
            play_sound(bye_mp3s)  # Plays one of the bye MP3's
            exit()

        # To easily check a word either use a function
        '''def (name) (a_dictionary_of_words, the voice_note variable):
                for key,value in a_dictionary_of_words.iteritems():
                    if value == voice_note.split(" "):
                        return True
                    else:
                        return False'''

        # The you can do an if statement
        '''if nameOfFunction(dict, voice_note):#
                what you want to do if true
                play_sound(list of mp3) or playsound(one mp3)'''


