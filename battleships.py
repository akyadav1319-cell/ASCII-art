grid=[[' ']*10]*10
player1=[]
player2=[]
def pgrid():


    for x in grid:
        print()
        print("-"*21)
        print("|",end="")
        for y in x:
            print(y,end="|")
        
    print()
    print("-"*21)        
print("Enter the coordniates of the ship- \nCarrier (5)\n Battleship (4)\n Cruiser (3)\n Destroyer (2) ")
for _ in 14:
    x,y=int(input("x coordinate")),int(input("y input"))
    player1=[[x,y]]