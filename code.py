"""
Juego de adivinar el numero.

- Maneja entradas invalidas con try/except
- Muestra instrucciones claras y una pista por intento
- Permite salir con 'q'
"""

import random


def print_instructions():
    print("Bienvenido al juego de adivinar el numero!")
    print("Instrucciones:")
    print("1. El programa generara un numero aleatorio entre 1 y 20.")
    print("2. Tu objetivo es adivinar el numero en el menor numero de intentos posible.")
    print("3. Despues de cada intento, recibiras una pista si tu intento es muy bajo, muy alto o correcto.")
    print("4. Puedes salir escribiendo 'q'.")
    print("Buena suerte!")


def print_result(guess_number, random_number):
    if guess_number < random_number:
        print("Muy bajo")
    elif guess_number > random_number:
        print("Muy alto")
    else:
        print("Correcto!")


def get_user_guess():
    while True:
        guess_raw = input("Ingresa tu intento (o 'q' para salir): ").strip().lower()
        if guess_raw == "q":
            return None
        try:
            return int(guess_raw)
        except ValueError:
            print("Error: por favor ingresa un numero valido.")


def generate_random_number():
    return random.randint(1, 20)


def start_game():
    random_number = generate_random_number()
    attempts = 0

    print_instructions()
    while True:
        guess_number = get_user_guess()
        if guess_number is None:
            print("Saliste del juego.")
            break
        attempts += 1
        print(f"Intento #{attempts}")
        print_result(guess_number, random_number)
        if guess_number == random_number:
            break

    print("Numero de intentos:", attempts)


if __name__ == "__main__":
    start_game()
