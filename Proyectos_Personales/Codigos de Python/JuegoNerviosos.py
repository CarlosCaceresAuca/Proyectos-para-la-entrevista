import random

def asignar_numeros_a_jugadores(num_jugadores):
    
    numero_inicial = random.randint(1, 10)
    
    jugadores = [f"Jugador {i}" for i in range(1, num_jugadores + 1)]
    
    numeros_jugadores = {}
    numero_actual = numero_inicial
    for jugador in jugadores:
        numeros_jugadores[jugador] = numero_actual
        numero_actual += 1
    
    return numeros_jugadores

def asignar_cartas_a_jugadores(num_jugadores):
    
    valores_cartas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    random.shuffle(valores_cartas)
    
    jugadores = [f"Jugador {i}" for i in range(1, num_jugadores + 1)]
    
    cartas_jugadores = {}
    for jugador in jugadores:
        carta_asignada = valores_cartas.pop()
        cartas_jugadores[jugador] = carta_asignada
    
    return cartas_jugadores

def jugar_juego(num_jugadores):
    
    while True:
        numeros_jugadores = asignar_numeros_a_jugadores(num_jugadores)
        cartas_jugadores = asignar_cartas_a_jugadores(num_jugadores)
        
        print("\nNúmeros asignados a los jugadores:")
        for jugador, numero in numeros_jugadores.items():
            print(f"{jugador} tiene el número {numero}")
        
        print("\nCartas asignadas a los jugadores:")
        for jugador, carta in cartas_jugadores.items():
            print(f"{jugador} tiene la carta {carta}")
        
        ganador = None
        for jugador, carta in cartas_jugadores.items():
            if carta == str(numeros_jugadores[jugador]) or (carta == "J" and numeros_jugadores[jugador] == 11) or (carta == "Q" and numeros_jugadores[jugador] == 12) or (carta == "K" and numeros_jugadores[jugador] == 13):
                print(f"¡El jugador {jugador} tiene una coincidencia! ¡{jugador} ha ganado!")
                ganador = jugador
                break
        
        if ganador:
            break
        else:
            print("\nNingún jugador ha ganado.")
            opcion = input("Seleccione una opción:\n1. Siguiente turno\n2. Terminar juego\n")
            if opcion == "2":
                print("¡Juego terminado!")
                return

def presentacion():
    print("Bienvenidos al juego de Nervioso")
    print("1. Iniciar")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        num_jugadores = int(input("Ingrese el número de jugadores (2-4): "))
        if num_jugadores < 2 or num_jugadores > 4:
            print("Número de jugadores no válido. El juego requiere entre 2 y 4 jugadores.")
            presentacion()
        else:
            jugar_juego(num_jugadores)
    elif opcion == "2":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        presentacion()

presentacion()

