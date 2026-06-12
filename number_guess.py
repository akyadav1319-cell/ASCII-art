import random
print("enter the range where the number should lie")
a=int(input("enter lower limit"))
b=int(input("enter upper limit"))
x=random.randint(a,b)
guess=int(input("Guess the number"))
while(guess!=x):
    if guess>x:
        print("I'm leass than",guess)
        guess=int(input("Guess the number"))
    if guess<x:    
        print("I'm greater than",guess)
        guess=int(input("Guess the number"))
print("yess the number is",x)        