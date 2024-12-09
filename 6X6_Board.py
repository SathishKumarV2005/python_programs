'''
Problem #2
You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial.
If the player A rolls the dice and if player B already has their initial in the same row,col
add a point to A and change the initial to A.
Player who gets 5 points first wins the game.'''
import random
board=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
def dice():
    row = random.randint(1,6)
    col = random.randint(1,6)
    return row,col
def turn(i1,points):
    global board
    j=0
    row,col=dice()
    print(f"you got {row,col} in dice")
    if board[row-1][col-1] !=0 and board[row-1][col-1] != i1 :
        points+=1
        j=1
    board[row-1][col-1]=i1
    for b in board:
        print(b)
    print()
    return points,j
def check_winner(points):
        if points == 5:
            return 1
        else:
            return 0
def main():
    global board
    print('''You have 6 x 6 game board where each cell is shown as a *
This is a two player dice game. The die has numbers 1 to 6.
Each player rolls the dice twice. First roll is row number, second roll is col number.
After the player rolls the dice, in the (row,col) enter the player's initial.
If the player A rolls the dice and if player B already has their initial in the same row,col
add a point to A and change the initial to A.
Player who gets 5 points first wins the game.\n''')
    players=int(input("Enter how many players:(4 maximum):"))
    players_dict={}
    flag=0
    if players<=1 or players>4:
        print("Not in Limit of players ")
    else:    
        for p in range(players):
            key=input(f"Enter Player {p+1} Intial:")
            players_dict[key]=0
        print(" 6X6 Board\n","*"*10,"\n")
        for b in board:
            print(b)
        print()
        print("Player 1 start the Game")
        while True:
            i=1
            for p,points in players_dict.items():
                permit1=int(input(f"Player {i} Enter {i} to roll the dice:"))
                while permit1!=i:
                    permit1=int(input(f"Enter {i} correctly to roll the dice:"))
                points,f=turn(p,points)
                players_dict[p]=points
                if f:
                    print(f"Player {i} your point is",players_dict[p])
                w=check_winner(players_dict[p])
                if w==1:
                    print(f"Player {i} Won the Game")
                    flag=1
                    break
                i+=1
            if flag ==1:
                break
main()
