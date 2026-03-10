"""
Renombra la función y las variables siguiendo snake_case y nombres con sentido
• Separa la lógica en al menos 3 funciones pequeñas y con un solo propósito
• Maneja correctamente el error cuando el usuario escribe texto en vez de número (ValueError)
• Agrega un mensaje de bienvenida + instrucciones claras

"""

import random

#variable global, para usarlo como parámetro de input_game


def print_instructions():
    print("==============================================")
    print("¡Bienvneido al juego de adivinar el número!")

def start_game():
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    while guess != number:
        guess = int(input("Ingresa tu intento: "))
        attempts += 1
    if guess < number:
        print("Muy bajo")
    elif guess > number:
        print("Muy alto")
    elif guess == number:
        print("¡Correcto!")
    else:
        print("Error")
    print("Número de intentos:", attempts)

def input_game():
    pass


def validations_game():
    pass

