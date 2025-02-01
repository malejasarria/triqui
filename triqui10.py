import time

def jugar():
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    rondas = 0  # Contador de rondas jugadas

    while True:
        # Inicialización del tablero y turnos
        tablero = [" "] * 9
        turno = "X"
        combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        # Pidiendo nombres de los jugadores
        jugador1 = input("Introduce el nombre del jugador 1: ")
        jugador2 = input("Introduce el nombre del jugador 2: ")

        for _ in range(9):
            # Mostrar tablero
            print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
            print("---+---+---")
            print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
            print("---+---+---")
            print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

            # Mostrar quién tiene el turno
            print(f"\nEs el turno de {jugador1} (X) si está jugando o {jugador2} (O) si está jugando.")
            print(f"Tienes 10 segundos para elegir una posición.")

            inicio = time.time()

            try:
                posicion = int(input()) - 1  # Tomar la posición y restar 1 para que coincida con el índice
                fin = time.time()

                if fin - inicio > 10:  # Verificar si pasó más de 10 segundos
                    print("¡Tiempo agotado! El turno se pasa automáticamente.")
                    turno = "O" if turno == "X" else "X"
                    continue

                if 0 <= posicion < 9 and tablero[posicion] == " ":
                    tablero[posicion] = turno
                else:
                    print("Posición inválida. Intenta de nuevo.")
                    continue

            except ValueError:
                print("Entrada inválida. Intenta de nuevo.")
                continue

            # Verificar ganador
            for a, b, c in combinaciones:
                if tablero[a] == tablero[b] == tablero[c] and tablero[a] != " ":
                    if tablero[a] == "X":
                        puntos_jugador1 += 1
                        print(f"¡{jugador1} ha ganado esta ronda!")
                    else:
                        puntos_jugador2 += 1
                        print(f"¡{jugador2} ha ganado esta ronda!")
                    break
            else:
                turno = "O" if turno == "X" else "X"
                continue
            break  # Salir si hay un ganador

        rondas += 1  # Aumentar el contador de rondas
        print(f"Puntos acumulados: {jugador1}: {puntos_jugador1}, {jugador2}: {puntos_jugador2}")
        print(f"Rondas jugadas: {rondas}")  # Mostrar el número de rondas jugadas

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if jugar_de_nuevo != "sí":
            print(f"Gracias por jugar! Resultado final: {jugador1}: {puntos_jugador1} puntos, {jugador2}: {puntos_jugador2} puntos.")
            print(f"Rondas jugadas: {rondas}")
            break  

jugar()
