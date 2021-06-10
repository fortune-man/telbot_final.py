from gtts import gTTS #pip install gTTS
def tts(x,bot, chat_id):
    tts = gTTS(x, lang='ko')
    tts.save("x.ogg")
    audio = open("x.ogg",'rb')
    bot.send_audio(chat_id, audio=audio)