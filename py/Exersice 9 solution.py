# pip install gtts 
# Use gtts
import gtts
import os

text = "Hi Nigga How are you doing Nigggggga ?"

voice = gtts.gTTS(text)
    
voice.save("nigga.mp3")

os.system(f"start nigga.mp3")