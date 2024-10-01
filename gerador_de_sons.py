from gtts import gTTS

idioma = 'pt'
texto = "Não é o ferroseed vou continuar procurando"

audio = gTTS(text=texto, lang=idioma, slow=False)

audio.save("procurando.mp3")
