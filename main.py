import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import sys
import os

translator = Translator()
record = sr.Recognizer()

x = True
while(x):
    try:
        spok_lang = int(input("Turkish = 1 \nEnglish = 2 \nGerman = 3 \nFrench = 4 \nSpanish = 5 \nExit = 6" + "\nPlease specify the number of the language you will speak:"))

        if spok_lang == 1:
            spok_lang = "tr-TR"
            x = False
        elif spok_lang == 2:
            spok_lang = "en-US"
            x = False
        elif spok_lang == 3:
            spok_lang = "de-DE"
            x = False
        elif spok_lang == 4:
            spok_lang = "fr-FR"
            x = False
        elif spok_lang == 5:
            spok_lang = "es-ES"
            x = False
        elif spok_lang == 6:
            sys.exit(2)
        else:
            print("Please enter one of the indicated numbers")
    except SystemExit:
        sys.exit(2)
    except:
        print("Please enter one of the indicated numbers")

x = True
while(x):
    try:
        lang_trans = int(input("Turkish = 1 \nEnglish = 2 \nGerman = 3 \nFrench = 4 \nSpanish = 5 \nExit = 6" + "\nPlease select the number of the language to be translated:"))

        if lang_trans == 1:
            lang_trans = "tr"
            x = False
        elif lang_trans == 2:
            lang_trans = "en"
            x = False
        elif lang_trans == 3:
            lang_trans = "de"
            x = False
        elif lang_trans == 4:
            lang_trans = "fr"
            x = False
        elif lang_trans == 5:
            lang_trans = "es"
            x = False
        elif lang_trans == 6:
            sys.exit(2)
        else:
            print("Please enter one of the indicated numbers")
    except SystemExit:
        sys.exit(2)
    except:
        print("Please enter one of the indicated numbers")


while True:
    try:
        y = int(input("Press 1 to start talking \nPress 2 to exit:"))

        if y == 1:
            print("Please speak...")
            def language_translator(spoken_language, language_to_translate):
                with sr.Microphone() as source:

                    audio = record.listen(source)
                    voice = record.recognize_google(audio, language=spoken_language)

                    print("Perceived Speech: " + voice)

                    trn = translator.translate(text=voice, dest=language_to_translate).text
                    print("Translation: " + trn)

                    tts = gTTS(trn, lang=language_to_translate)
                    file = "audio-" + ".mp3"
                    tts.save(file)
                    playsound(file)
                    os.remove(file)
        elif y == 2:
            break
        else:
            raise Exception

        language_translator(spok_lang, lang_trans)

    except ValueError:
        print("Please enter one of the indicated numbers")
    except:
        print("Please enter one of the indicated numbers")











