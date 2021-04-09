import pyttsx3
import speech_recognition

while True:
  engine = pyttsx3.init()
  r = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as mic:
      print("Say something!")
      audio = r.listen(mic)
  try:
      youSaid = r.recognize_google(audio)
      print("youSaid: " + youSaid)
  except: youSaid = ""

  if youSaid == "":
    botSay= "I can't hear you, try again"
  elif "hello" in youSaid:
    botSay= "Hello can i help you something"
  elif "bye" in youSaid:
    engine.say("goodbye see you again")
    engine.runAndWait()
    break
  else: botSay = "oh i just learn listen hello, try it out"

  engine.say(botSay)
  engine.runAndWait()