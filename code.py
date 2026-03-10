"""
• Renombra la función y las variables siguiendo snake_case y nombres con sentido
• Separa la lógica en al menos 3 funciones pequeñas y con un solo propósito
• Maneja correctamente el error cuando el usuario escribe texto en vez de número (ValueError)
• Agrega un mensaje de bienvenida + instrucciones claras

"""

import random

def print_instructions():
    print("¡Bienvenido al juego de adivinar el número!")
    print("Instrucciones:")
    print("1. El programa generará un número aleatorio entre 1 y 20.")
    print("2. Tu objetivo es adivinar el número en el menor número de intentos posible.")
    print("3. Después de cada intento, recibirás una pista si tu intento es muy bajo, muy alto o correcto.")
    print("¡Buena suerte!")

def print_result(guess_number, random_number):
    if guess_number < random_number:
        print("Muy bajo")
    elif guess_number > random_number:
        print("Muy alto")
    elif guess_number == random_number:
        print("¡Correcto!")
    else:
        print("Error")

def get_user_guess():
    while True:
        try:
            guess = int(input("Ingresa tu intento: "))
            return guess
        except ValueError:
            print("Error: por favor ingresa un número válido.")


def start_game():
    random_number = random.randint(1, 20)
    attempts = 0

    print_instructions()
    while True:
        guess_number = get_user_guess()
        attempts += 1
        print_result(guess_number, random_number)
        if guess_number == random_number:
            break

    print("Número de intentos:", attempts)

if __name__ == "__main__":
    start_game()