tablerito = [" "] * 9
turno = "☻"
combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

for _ in range(9):
    posicion = int(input(f"Turno de {turno}. Elige posición (1-9): ")) - 1
    if 0 <= posicion < 9 and tablerito[posicion] == " ":
        tablerito[posicion] = turno
    else:
        print("Posición inválida.")
        continue

    print(f" {tablerito[0]} | {tablerito[1]} | {tablerito[2]} ")
    print("---+---+---")
    print(f" {tablerito[3]} | {tablerito[4]} | {tablerito[5]} ")
    print("---+---+---")
    print(f" {tablerito[6]} | {tablerito[7]} | {tablerito[8]} ")

    for a, b, c in combinaciones:
        if tablerito[a] == tablerito[b] == tablerito[c] and tablerito[a] != " ":
            print(f"¡{tablerito[a]} ha ganado!")
            exit()

    turno = "☺" if turno == "☻" else "☻"

print("¡Empate!")
