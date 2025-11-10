cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
possibilities=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], 
               [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
def display_table():
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
    
    display_table()

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

    

    for possibility in possibilities:
        if cells[possibility[0]]==cells[possibility[1]]==cells[possibility[2]]:
            print(f"Player {cells[possibility[0]]} wins!")
            running = False
            break




