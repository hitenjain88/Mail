from gtts import gTTS
import os
from playsound import playsound

mytext='hello everyone this is the text to speech converter for the emails.'

language='en'

myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save('welcome.mp3')
playsound('welcome.mp3')
