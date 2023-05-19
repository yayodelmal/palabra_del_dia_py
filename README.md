# Palabra Del Día

_"Palabra Del Día"_ es un programa en Python que selecciona una palabra aleatoria en inglés, la traduce al español, y luego reproduce el audio de la pronunciación de la palabra en inglés 📖.

## Características 🤔

- Selecciona una palabra aleatoria en inglés a partir de una lista obtenida a través de la API de datamuse.
- Traduce la palabra al español utilizando la librería 'translate'.
- Convierte la pronunciación de la palabra en inglés a audio utilizando Google Text-to-Speech (gTTS).
- Reproduce el audio de la pronunciación con pygame.

## Uso ✍🏼

Cuando se ejecuta, el programa selecciona una palabra aleatoria y muestra su traducción. Luego, reproduce el audio de la pronunciación. El usuario tiene dos opciones que puede introducir en la terminal:

1. Pulsa "1" y luego Enter para volver a escuchar la pronunciación de la palabra.
2. Pulsa "2" y luego Enter para obtener una nueva palabra aleatoria.

## Instalación 🚀

Para ejecutar este programa, necesitarás Python 3.6 o superior. También necesitarás instalar las siguientes librerías Python:

- requests
- gTTS
- pygame
- translate

Puedes instalar estas librerías con pip utilizando el siguiente comando:

```bash
pip install requests gTTS pygame translate
