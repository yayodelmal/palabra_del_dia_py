import requests
import random
from gtts import gTTS
import os
from pygame import mixer
from translate import Translator

def traducir(texto):
    try:
        translator = Translator(from_lang='english', to_lang='spanish')
        resultado = translator.translate(texto)
        return resultado
    except Exception as e:
        return "Traducción no disponible"


def obtener_palabra():
    response = requests.get("https://api.datamuse.com/words?ml=ringing")
    palabras = response.json()
    return random.choice(palabras)["word"]

def reproducir_palabra(palabra):
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

def borrar_archivo():
    if os.path.exists("palabra.mp3"):
        os.remove("palabra.mp3")

def imprimir_instrucciones():

    print(f"-----------------------INSTRUCCIONES----------------------------")
    print(f"-- Pulsa \"1\" y luego Enter para volver a escuchar la palabra. --")
    print(f"-- Pulsa \"2\" y luego Enter para una nueva palabra aleatoria.  --")
    print(f"")
    
def main():
    palabra = [obtener_palabra()]
    print(f"-----------------------PALABRAS---------------------------------")
    print(f"La palabra aleatoria es: {palabra[0]}")
    print(f"En español: {traducir(palabra[0])}")
    print(f"")
    
    imprimir_instrucciones()
    reproducir_palabra(palabra[0])

    while True:
        decision = input()
        if decision == '1':
            reproducir_palabra(palabra[0])
        elif decision == '2':
            borrar_archivo()
            palabra[0] = obtener_palabra()
            print(f"La nueva palabra aleatoria es: {palabra[0]}")
            print(f"En español: {traducir(palabra[0])}")
            imprimir_instrucciones()
            reproducir_palabra(palabra[0])

if __name__ == "__main__":
    main()
