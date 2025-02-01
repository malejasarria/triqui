# solo implente un movimiento
tablero = [" "] * 9
posicion = int(input("Elige una posición (1-9): ")) - 1
tablero[posicion] = "☻"


print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
print("---+---+---")
print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
print("---+---+---")
print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
