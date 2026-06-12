
x=99
while(x!=0):
    if x==1:
        print(x," bottle of beer on the wall,",x,"bottle of beer")
    else:
        print(x," bottles of beer on the wall,",x,"bottles of beer")
    x-=1
    if x==1 :
        print("Take one down and pass it around,",x,"bottle of beer on the wall.")
    else:
        print("Take one down and pass it around,",x,"bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")