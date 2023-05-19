import requests
import random
from gtts import gTTS
import os
from pygame import mixer

def obtener_palabra():
    response = requests.get("https://api.datamuse.com/words?ml=ringing")
    palabras = response.json()
    return random.choice(palabras)["word"]

def main():
    palabra = obtener_palabra()
    print(f"La palabra aleatoria es: {palabra}")

    # Convertir la palabra en audio
    tts = gTTS(text=palabra, lang='en')
    tts.save("palabra.mp3")

    # Reproducir el audio
    mixer.init()
    mixer.music.load("palabra.mp3")
    mixer.music.play()

    # Esperar hasta que termine el audio
    while mixer.music.get_busy():
        continue

    # Borrar el archivo de audio
    os.remove("palabra.mp3")

if __name__ == "__main__":
    main()
