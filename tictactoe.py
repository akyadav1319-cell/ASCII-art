tic=[["1 ","2 ","3 "],[" 4","5 ","6 "],["7 ","8 ","9 "]]

def board():
    print(tic[0][0],"|",tic[0][1],"|",tic[0][2])
    print("-------------")
    print(tic[1][0],"|",tic[1][1],"|",tic[1][2])
    print("-------------")
    print(tic[2][0],"|",tic[2][1],"|",tic[2][2])
def row1(a,player):
    if player=="player1":
        if a==1:
            tic[0][0]='O'
        if a==2:
            tic[0][1]='O' 
        if a==3:
            tic[0][2]='O'       
    elif player=="player2":
        if a==1:
            tic[0][0]='X'
        if a==2:
            tic[0][1]='X' 
        if a==3:
            tic[0][2]='X'
    
def row2(a,player):
    if player=="player1":
        if a==4:
            tic[1][0]='O'
        if a==5:
            tic[1][1]='O' 
        if a==6:
            tic[1][2]='O'       
    elif player=="player2":
        if a==4:
            tic[1][0]='X'
        if a==5:
            tic[1][1]='X' 
        if a==6:
            tic[1][2]='X'   
    
def row3(a,player):
    if player=="player1":
        if a==7:
            tic[2][0]='O'
        if a==8:
            tic[2][1]='O' 
        if a==9:
            tic[2][2]='O'       
    elif player=="player2":
        if a==7:
            tic[2][0]='X'
        if a==8:
            tic[2][1]='X' 
        if a==9:
            tic[2][2]='X' 
        
board()

def player1():
    a=int(input("please select your position"))
    if a==1 or a==2 or a==3:
        row1(a,"player1")
    elif a==4 or a==5 or a==6:
        row2(a,"player1")
    elif a==7 or a==8 or a==9:
        row3(a, "player1")  


def player2():
    a=int(input("please select your position"))
    if a==1 or a==2 or a==3:
        row1(a,"player2")
    elif a==4 or a==5 or a==6:
        row2(a,"player2")
    elif a==7 or a==8 or a==9:
        row3(a,"player2")
def win_():
    if tic[0][0] in ['O','X']:
        if tic[0][1] in ['O','X'] and tic[0][2] in['O','X']:
            if tic[0][0]==tic[0][1]==tic[0][2]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][0]==tic[0][1]==tic[0][2]=='O':
                print("player 1 is winner")
                return 9
        if tic[1][0] in ['O','X'] and tic[2][0] in ['O','X']:
            if tic[0][0]==tic[1][0]==tic[2][0]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][0]==tic[1][0]==tic[2][0]=='O':
                print("player 1 is winner")
                return 9 
        if tic[1][1] in ['O','X'] and tic[2][2] in ['O','X']:
            if tic[0][0]==tic[1][1]==tic[2][2]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][0]==tic[1][1]==tic[2][2]=='O':
                print("player 1 is winner") 
                return 9    
    if tic[0][1] in ['O','X']:
        if tic[1][1] in ['O','X'] and tic[2][1] in ['O','X']:
            if tic[0][1]==tic[1][1]==tic[2][1]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][1]==tic[1][1]==tic[2][1]=='O':
                print("player 1 is winner")
                return 9
    if tic[0][2] in ['O','X']:
        if tic[1][2] in ['O','X'] and tic[2][2] in ['O','X']:
            if tic[0][2]==tic[1][2]==tic[2][2]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][2]==tic[1][2]==tic[2][2]=='O':
                print("player 1 is winner")
                return 9
        if tic[1][1] in ['O','X'] and tic[2][0] in ['O','X']:
            if tic[0][2]==tic[1][1]==tic[2][0]=='X':
                print("player 2 is winner")
                return 9
            elif tic[0][2]==tic[1][1]==tic[2][0]=='O':
                print("player 1 is winner")
                return 9
    if tic[1][0] in ['O','X']:
        if tic[1][1] in ['O','X'] and tic[1][2] in ['O','X']:
            if tic[1][0]==tic[1][1]==tic[1][2]=='X':
                print("player 2 is winner")
                return 9
            elif tic[1][0]==tic[1][1]==tic[1][2]=='O':
                print("player 1 is winner")
                return 9
    if tic[2][0] in ['O','X']:
        if tic[2][1] in ['O','X'] and tic[2][2] in ['O','X']:
            if tic[2][0]==tic[2][1]==tic[2][2]=='X':
                print("player 2 is winner")
                return 9
            elif tic[2][0]==tic[2][1]==tic[2][2]=='O':
                print("player 1 is winner")  
                return 9   
    return 1                        

win=0
while win<9:
    player1()
    board()
    win+=win_()
    player2()
    win+=win_()
    board()
x=win_()
if x==0:
    print("its a draw")

