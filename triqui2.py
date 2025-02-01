# triqui4.py - Alternar entre X y O
tablero = [" "] * 9
turno = "☻"

for _ in range(9):
    posicion = int(input(f"Turno de {turno}. Elige posición (1-9): ")) - 1
    if 0 <= posicion < 9 and tablero[posicion] == " ":
        tablero[posicion] = turno
    else:
        print("Posición inválida, intenta otra vez.")
        continue

    # Mostrar tablero
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

    turno = "☺" if turno == "☻" else "☻"
