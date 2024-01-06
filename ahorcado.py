import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "ahorcado", "juego", "informatica", "desarrollo"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del ahorcado!")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    while intentos > 0:
        intento = input("Introduce una letra: ").lower()

        if intento in letras_adivinadas:
            print("Ya has intentado con esa letra. ¡Prueba otra vez!")

        elif intento in palabra_secreta:
            letras_adivinadas.append(intento)
            print("¡Correcto!")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")

        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

        if "_" not in mostrar_tablero(palabra_secreta, letras_adivinadas):
            print("¡Felicidades! ¡Has ganado!")
            break

    if "_" in mostrar_tablero(palabra_secreta, letras_adivinadas):
        print(f"¡Perdiste! La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_ahorcado()


