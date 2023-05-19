import requests
import json

def obtener_palabra(api_key):
    response = requests.get(f"http://api.wordnik.com/v4/words.json/randomWord?api_key={api_key}")
    if response.status_code == 200:
        data = json.loads(response.text)
        return data["word"]
    else:
        return "Error al obtener la palabra"

def main():
    api_key = "your_api_key"  # Reemplaza esto con tu clave API
    palabra = obtener_palabra(api_key)
    print(f"La palabra aleatoria es: {palabra}")

if __name__ == "__main__":
    main()
