def show_game_board():
    for i in range(3):
        for j in range(3):
            print (a[i][j],end="    ")
        print()

a=[["-","-","-"],
   ["-","-","-"],
   ["-","-","-"]]

show_game_board()
def players_number1():
        print("player 1 ")
        row=int(input("enter row: "))
        col=int(input("enter col: "))
        a[row][col]="x"

def players_number2():
        print("player2 ")
        row=int(input("enter row: "))
        col=int(input("enter col: "))
        a[row][col]="o"

while True:
    players_number1()

 

    show_game_board()

    players_number2()

    show_game_board()



    
 