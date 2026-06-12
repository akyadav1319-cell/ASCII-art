inventory=[None]*7
locks=["main key required","crowar is required to remove the wooden plank","you need to switch on the electric current for lifting up the door"]
attic_locks=["crowbar required to remove the wooden plank and acquire the padllock key"]
drawing_locks=["padlock key needed to open the box","mystery room key required"]
mroom_locks=["lever required to restore the electricity back"]
def game():
    print("current room-Main room\n")
    door=int(input("choose one door/stair \n1)door to drawing room\n2)door to tv room\n3)stairs to attic\n4)MAIN DOOR TO ESCAPE \n: "))
    if door==1:
        drawing_room()
    if door==2:
        tv_room()
    if door==3:
        attic()
    if door==4: 
        main_door() 
def drawing_room():
    print("drawing room")
    for _ in drawing_locks:
        print(_)
    if "padlock key" in inventory and "padlock key needed to open the box" in drawing_locks:
        print("padlock key used,box has been opened\nmain key acquired!")
        inventory[0]="main key"  
        drawing_locks.pop(0)
        drawing_room()
    if "mystery key" in inventory:
        
        print("mystery key has been used, mystery room has opened..")
        inventory.remove("mystery key") 
        drawing_locks.remove("mystery room key required")
        drawing_room()   
    if "mystery room key required" not in drawing_locks:
        y=int(input("rooms to enter\n 1)mystery room \n2)main room\n"))
        if y==1:
            mystery_room()
        if y==2:
            game() 
    else:
        r=input("return back(Y/N)")    
        if r=='Y':
            game()

def mystery_room():
    for _ in mroom_locks:
            print(_)
    if inventory[1]==None:
        print("crowbar acquired and entered to inventory")
        inventory[1]="crowbar"
    if "lever" in inventory and mroom_locks[0]=="lever required to restore the electricity back":
        print("lever plugged in,electricity restored")
        mroom_locks.pop
        inventory[2]="switched_on"
    r=input("return back(Y/N)")    
    if r=='Y':
        drawing_room()   

def tv_room():
    print("tv room")
    if inventory[5]==None:
        inventory[5]="mystery key"
        print("mystery key just found and added to inventory")
        tv_room()
    r=input("return back(Y/N)")    
    if r=='Y':
        game()    


def attic():
    print("attic")
    for _ in attic_locks:
        print(_)
    if "crowbar" in inventory and inventory[3]!="padlock key":
        print("wooden planks removed, padlock key acquired")
        inventory.insert(3,"padlock key")
        print("padlock key justadded to the inventory")
        attic_locks.pop(0)
        attic()
    if  inventory[4]==None:
        inventory[4]="lever"
        print("lever just added to the inventory")
        attic()
    r=input("return back(Y/N)")    
    if r=='Y':
        game()        
        

    
def main_door():
    print("main door")
    for _ in (locks):
        print(_)
    if "main key" in inventory:
        print("main key used")
        inventory.pop(0)
        locks.pop(0)
        main_door()
    if "crowbar" in inventory and "crowar is required to remove the wooden plank" in locks:
        print("wooden planks removed")
        locks.remove("crowar is required to remove the wooden plank")
        main_door()
    if "switched_on" in inventory:
        print("door has been uplifted")
        locks.remove("you need to switch on the electric current for lifting up the door")
        inventory.remove("switched_on")
        main_door()
    
    if len(locks)==0:
        print("Door has finally opened\nhouse escape completed succesfully\nGOOD JOB✨✨🌟🌟")
        O=input("return back(Y/N)")    
        if O=='Y':
            main() 
    r=input("return back(Y/N)")    
    if r=='Y':
        game() 



def instruct():
    print("The instructions are as follow:\n1)There are 6 main rooms - the attic, the bedroom, the dinning room, tv room, main room, mystery room\n2)you will be provided an inventory which you will fill with items as find as you progress in the game\n3)GOOD LUCK ")
    i=input("return(Y/N)?")
    if i=='Y':
        main()
def main():
    print("Welcome to the game- HOUSE ESCAPE (GRANNY CHEAP VERSION)\n")
    option=int(input("slecect the options-\n1)START\n2)INSTRUCTIONS\n3)EXIT\n: "))
    if option==1:
        game()
    if option==2:
        instruct()
    if option==3:
        print("game over,thanks for playing")    

if __name__=='__main__':
    main()    