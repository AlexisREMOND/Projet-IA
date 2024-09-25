import pyttsx3
from PyPDF2 import PdfReader

#inspiré de cette vidéo : https://www.youtube.com/watch?v=yudd6JXyoQM&t=422s

droid = pyttsx3.init()

#initialisation de la voix
voices = droid.getProperty('voices')
droid.setProperty('voice', voices[0].id)

# Talk
droid.say("Bonjour Alexis !")
droid.say("Je vais te parler de l'intelligence émotionnelle")

#Lecture de pdf
livre = open("Intelligence émotionnelle.pdf", "rb")
lecture = PdfReader(livre)
pages = len(lecture.pages)
print(pages)

debut_lecture = lecture.pages[0]
texte = debut_lecture.extract_text()
droid.say(texte)

droid.runAndWait()
