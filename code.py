"""
Renombra la función y las variables siguiendo snake_case y nombres con sentido
• Separa la lógica en al menos 3 funciones pequeñas y con un solo propósito
• Maneja correctamente el error cuando el usuario escribe texto en vez de número (ValueError)
• Agrega un mensaje de bienvenida + instrucciones claras

"""

import random

#variable global, para usarlo como parámetro de input_game


def print_instructions():
    print()
    print("==============================================")
    print("¡Bienvenido al juego de adivinar el número!\n")
    print("==============================================\n\n")
    print("Instrucciones:\n")
    print("1. El usuario debe de adivinar el número al azar que está entre\n" 
            "el uno y el 20")
    print("2. A partir del número ingresado el programa le va a indicar si\n" 
    "dicho número fue muy bajo, mul alto o si adivinó\n\n")


def input_game():
    try:
        guess = int(input("Ingresa tu intento: "))
        if(guess > 20 or guess <= 0):
            print("valor inválido; debe de estar entre 1 y 20")
        return guess
    except ValueError:
        print("valor inválido; debe de ser un número y estar en rango 1 y 20")
    


def validations_game():
    number = random.randint(1, 20)
    guess = input_game()
    attempts = 0
    while guess != number:
        attempts += 1
        if guess < number:
            print("Muy bajo\n")
            guess = input_game()
        elif guess > number:
            print("Muy alto\n")
            guess = input_game()
        elif guess == number:
            print("¡Correcto!\n")
            return
        else:
            print("Error\n")
    print("Número de intentos:", attempts)

def main():
    print_instructions()
    print("Adivina el número entre 1 y 20")
    validations_game()

main()

