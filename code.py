import random


def mostrar_instrucciones():
    """Imprime el mensaje de bienvenida y las reglas del juego."""
    print("==============================================")
    print("  ¡Bienvenido al juego de adivinar el número! ")
    print("==============================================\n")
    print("Instrucciones:")
    print("1. El sistema elegirá un número al azar entre 1 y 20.")
    print("2. Debes intentar adivinarlo.")
    print("3. Te indicaremos si tu número es muy alto o muy bajo.\n")


def obtener_entero_valido(minimo, maximo):
    """
    Solicita un número al usuario y valida que sea un entero 
    dentro del rango especificado. Reintenta hasta que sea válido.
    """
    while True:
        try:
            valor = int(input(f"Ingresa tu intento ({minimo}-{maximo}): "))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El valor debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, escribe un número entero.")


def ejecutar_partida():
    """Contiene la lógica principal del ciclo del juego."""
    numero_secreto = random.randint(1, 20)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = obtener_entero_valido(1, 20)
        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo. ¡Intenta de nuevo!\n")
        elif intento > numero_secreto:
            print("Muy alto. ¡Intenta de nuevo!\n")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            adivinado = True


def main():
    """Punto de entrada principal del programa."""
    mostrar_instrucciones()
    ejecutar_partida()


if __name__ == "__main__":
    main()