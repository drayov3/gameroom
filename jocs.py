import random

#Definimos la funcion de adivinar el numero
def adivina_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 3
    print("Adivina el número entre 1 y 10. Tienes 3 intentos.")
    
    for i in range(intentos):
        respuesta = int(input("Introduce un numero: "))
        if respuesta < numero_secreto:
            print("El número es mayor.")
        elif respuesta > numero_secreto:
            print("El número es menor.")
        else:
            print("Ganaste!")
            return
    print(f"Game Over. El numero era {numero_secreto}.")

# Función para jugar a "Piedra - Papel - Tijeras"
def piedra_papel_tijeras():
    opciones = ["Piedra", "Papel", "Tijeras"]
    puntuacion_usuario = 0
    puntuacion_cpu = 0

    while puntuacion_usuario < 3 and puntuacion_cpu < 3:
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        eleccion = input("Introduce tu eleccion en numero: ")

        if eleccion == "1":
            eleccion_usuario = "Piedra"
        elif eleccion == "2":
            eleccion_usuario = "Papel"
        elif eleccion == "3":
            eleccion_usuario = "Tijeras"
        else:
            print("Por favor elige una opcion valida")
            continue
        
        eleccion_cpu = random.choice(opciones)
        print(f"La CPU eligio: {eleccion_cpu}")

        if eleccion_usuario == eleccion_cpu:
            print("Empate.")
        elif (eleccion_usuario == "Piedra" and eleccion_cpu == "Tijeras") or \
             (eleccion_usuario == "Papel" and eleccion_cpu == "Piedra") or \
             (eleccion_usuario == "Tijeras" and eleccion_cpu == "Papel"):
            print("Ganaste la ronda")
            puntuacion_usuario += 1
        else:
            print("La CPU gano esta ronda")
            puntuacion_cpu += 1

    print(f"\nResultado final: Usuario {puntuacion_usuario} - Cpu {puntuacion_cpu}")

# Definimos la funcion para el ahorcado
#
def ahorcado():
    # Cargamos las palabras desde el archivo que creamos anteriormente
    
    with open('listadopalabras.txt', 'r') as file:
        palabras = [linea.strip() for linea in file if linea.strip()]

    # Escoge una palabra al azar
    palabra = random.choice(palabras).lower()
    intentos = len(palabra) * 2
    letras_adivinadas = []
    tablero = ["_" for _ in palabra]
    
    print(f"Ahorcado: Tienes {intentos} intentos para adivinar la palabra.")
    
    while intentos > 0 and "_" in tablero:
        print(" ".join(tablero))
        letra = input("Introduce una letra: ").lower()
        
        #Verificamos de que no se pase de más de un char
        if len(letra) != 1 or not ('a' <= letra <= 'z'):
            print("Por favor, introduce solo una letra.")
            continue
        
        if letra in letras_adivinadas:
            print("Ya has probado esa letra.")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            for index, char in enumerate(palabra):
                if char == letra:
                    tablero[index] = letra
            print("Has adivinado una letra")
        else:
            intentos -= 1
            print(f"Fallaste, te quedan {intentos} intentos.")

    if "_" not in tablero:
        print(f"Ganaste!!! Has acertado la palabra: {palabra}")
    else:
        print(f"Game Over. La palabra era: {palabra}")
# Función principal
def main():
    while True:
        print("Menu:")
        print("1. Adivina número")
        print("2. Piedra - Papel - Tijeras")
        print("3. El Ahorcado")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == "1":
            adivina_numero()
        elif opcion == "2":
            piedra_papel_tijeras()
        elif opcion == "3":
            ahorcado()
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
