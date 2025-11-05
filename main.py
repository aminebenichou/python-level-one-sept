cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
print("___|___|___")
print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
print("___|___|___")
print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
print("   |   |   ")
running = True
player = "X"
# turn = 0
while running:
    # if turn%2==0:  # % -> reste du division sur 2
    #     player="X"
    # else:
    #     player="O"
    player_input = int(input("Enter a position to place X (1-9): "))

    i=0
    while i<9:
        if cells[i]==player_input:
            cells[i] = player
            break  
        i = i + 1

    if player=="X":
        player="O"
    else:
        player="X"

    

    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("___|___|___")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("___|___|___")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("   |   |   ")

    turn += 1
    k=0
    while k <7:
        if cells[k]==cells[k+1]==cells[k+2]:
            print("You win")
            running = False
        k += 3
    k=0
    while k <3:
        if cells[k]==cells[k+3]==cells[k+6]:
            print("You win")
            running = False
        k += 1
    if cells[0]==cells[4]==cells[8]:
            print("You win")
            running = False
    if cells[2]==cells[4]==cells[6]:
            print("You win")
            running = False


