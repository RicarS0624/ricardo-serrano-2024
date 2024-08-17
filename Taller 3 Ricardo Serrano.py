import random
numero_secreto = random.randint(1, 100)
print("¡Bienvenido al juego de adivinanza de números!")
print("He elegido un número entre 1 y 100. Intenta adivinarlo.")
print("Escribe 'salir' para terminar el juego en cualquier momento.")

while True:
    intento = input("Introduce tu adivinanza: ")
    if intento.lower() == 'salir':
        print("Gracias por jugar. ¡Hasta luego!")
        break
    try:
        adivinanza = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido o 'salir' para salir.")
        continue

    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif adivinanza > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número correcto:", numero_secreto)
        break
    