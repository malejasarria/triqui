def jugar():
    while True:  # Bucle principal para jugar de nuevo
        tablero = [" "] * 9
        turno = "X"
        combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        while True:
            # Mostrar tablero
            print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
            print("---+---+---")
            print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
            print("---+---+---")
            print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

            # Turno de jugador
            try:
                posicion = int(input(f"Turno de {turno}. Elige posición (1-9): ")) - 1
                if 0 <= posicion < 9 and tablero[posicion] == " ":
                    tablero[posicion] = turno
                else:
                    print("Posición inválida.")
                    continue
            except ValueError:
                print("Por favor ingresa un número válido entre 1 y 9.")
                continue

            # Verificar ganador
            for a, b, c in combinaciones:
                if tablero[a] == tablero[b] == tablero[c] and tablero[a] != " ":
                    print(f"¡{tablero[a]} ha ganado!")
                    break
            else:
                turno = "O" if turno == "X" else "X"

                # Comprobar si hay empate
                if " " not in tablero:
                    print("¡Empate!")
                    break
                continue

            # Si hay ganador, salimos del bucle
            break

        # Preguntar si el usuario quiere jugar de nuevo
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (sí/no): ").strip().lower()
        if jugar_de_nuevo != "sí":
            print("¡Gracias por jugar!")
            break  # Salir del bucle principal si no quiere jugar de nuevo

# Ejecutar juego
jugar()
