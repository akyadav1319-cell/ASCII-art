import random
print("This is a dice game of user v/s computer")
x=int(input("enter 1 to roll the dice\n"))
if x==1:
    user=random.randint(1,6)
    print("user:",user)
comp=random.randint(1,6) 
print("computer:",comp)
if user>comp:
    print(user,">",comp,"user wins")   
elif user<comp:    
    print(user,"<",comp,"computer wins") 
else:
    print(user,"=",comp,"its a draw")