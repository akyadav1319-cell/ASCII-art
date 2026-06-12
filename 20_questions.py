print("we are playing 20 questions- kindly answer the questions with yes and no")
x=input("are you thinking of an animal? (Y/N)")
if x=='Y':
    y=input("is it a domestic anima?(Y/N)")
    if y=='Y':
        z=input("does this animal has 4 legs?(Y/N)")
        if z=='Y':
            a=input("does this animal meow?(Y/N)?")
            if a=='Y':
                print("its a cat😺")
            else:
                b=input("does this animal bark?(Y/N)?")
                if b=='Y':
                    print("its a Dog🐶")
                else: 
                    c=input("does this give milk?(Y/N)?")
                    if c=='Y':
                        e=input("does it moo?(Y/N)?")
                        if e=='Y':
                            print("its a cow🐄") 
                        else:
                            d=input("does it dound like maa?(Y/N)?")
                            if d=='Y':
                                print("its a G.O.A.T🐐")
                    if c=='N':
                        f=input("Is it used for riding?(Y/N)")
                        if f=='Y':
                            print("its a horse🐴")  
        if z=='N':
            u=input("does this animal or creature live in water?(Y/N)")
            if u=='Y':
                j=input("does this animal has a dumb pokemon based on it?(Y/N)")
                if j=="Y":
                    print("its a duck and the pokemon is psyduck 🦆🦆")
                else:
                    print("u have reached to the end")    
            if u=='N':
                o=input("is it a bird that acts as an alarm clock")
                if o=='Y':
                    print("its a hen 🐓 or roster")
                else:
                    print("you have reached to the end of the program")
    if y=='N':
        p=input("does this animal has 4 legs?(Y/N)")
        if p=='Y':
            q=input("is this the fastest animal on planet?(Y/N)?")
            if q=='Y':
                print("its a cheetah 🐯")
            if q=='N':
                k=input("is it based in based on a disney charcter that and is mascot of famous figure skater yuzuru hanyu?(Y/N)")
                if k=='Y':
                    print("its a bear🐻")
                if k=='N':
                    print("u have reached the end of the program")
        if p=='N':
            l=input("does this animal propse with a stone and prefers colder environment?(Y/N)")
            if l=='Y':
                print("its a penguin🐧")           
            if l=='N':
                w=("is this animal buffed up and a good fighter?(Y/N)")
                if w=='Y':
                    print("ita a kangroo 🦘")  
                if w=="N":
                    print("you have reached to the end of tHE program")                            
if x=='N':
    print("you have reached to the end of the program")