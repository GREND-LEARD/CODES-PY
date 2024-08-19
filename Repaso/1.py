import random

numero_aleatorio = random.randint(1, 100)
intentos = 0
maximosintento = 10
print("Adivina un número entre 1 y 100. Tu objetivo es adivinarlo con el menor número de intentos posibles.")

while True:
    suposicion = int(input("Ingresa tu suposición: "))
    intentos += 1
    if suposicion < numero_aleatorio:
        print("Tu suposición es demasiado baja.")
    elif suposicion > numero_aleatorio:
        print("Tu suposición es demasiado alta.")
    else:
        print("¡Felicidades! Has adivinado el número.")
        break
    print(f"Has hecho {intentos} intentos.")
    if intentos == maximosintento:
        print("Has agotado todos los intentos. El número era:", numero_aleatorio)
        break

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").strip().lower()
    if jugar_de_nuevo != "si":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
