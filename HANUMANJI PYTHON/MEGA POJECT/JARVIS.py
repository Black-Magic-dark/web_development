import speech_recognition as sr   
import webbrowser
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

# speak function
def speak(text):
    engine.say(text)   
    engine.runAndWait()


# def processCommand(c):
#     if "open google"in c.lower():
#         webbrowser.open("https://google.com")
#     elif"open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif"open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif"open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif"open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
#     else:
#         speak("sorry")
# program entry point
if __name__ == "__main__": 
      speak(" initializing to jarvis ")
      while True:
    
       r = sr.Recognizer()
    #  print("recognizing")
            try:
             with sr.Microphone() as source:
              print("Say something!")
             audio = r.listen(source , timeout=2 ,phrase_time_limit=1)

            command=r.recognize_google(audio)
                 if(command.lower()=="jarvis"):
               speak("ya")  #listen for command
               with sr.Microphone() as source:
                print("jarvis active!")
                audio = r.listen(source)
                command=r.recognize_google(audio)
        #  processCommand(command)
         except Exception as e:
            print( "Error; {0}".format(e))  







