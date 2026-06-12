word=["_"]*7
#sweater
n=0
print("This is a Hangman game/n you'll get 5 tries")
x=5
for _ in word:
            print(_,end=" ")
while x!=0:
    guess=input("Enter the letter").upper().strip()
    if guess=='A':
        word[3]='A'
        for _ in word:
            print(_,end=" ")
    elif guess=='S':
        word[0]='S'
        for _ in word:
            print(_,end=" ")
    elif guess=='E':
        word[2]='E'
        word[5]='E'
        for _ in word:
            print(_, end=" ")        
    elif guess=='W':
        word[1]='W'
        for _ in word:
            print(_,end=" ")
    elif guess=='T':
        word[4]='T'
        for _ in word:
            print(_,end=" ") 
    elif guess=='R':
        word[6]='R'
        for _ in word:
            print(_,end=" ")  
    else:
        x-=1  
        print("lives remaining: ",x)                            
    if '_' not in word:
        break   
if x==0:
    print("oops you lost the game")
else:
    print("you guessed the word correctly")    
