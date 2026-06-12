#pyramid
n=8
for i in range(n):
    print()

    for _ in range(n-i):
            print(" ",end="")
    for _ in range(i):        
        print("* ",end="")
#diamond        
for i in range(n):
    print()

    for _ in range(n-i):
            print(" ",end="")
    for _ in range(i):        
        print("* ",end="")
for i in range(n):
    print()

    for _ in range(i):
            print(" ",end="")
    for _ in range(n-i):        
        print("* ",end="") 
print()        
#hollow square
print("$ "*n)
for _ in range(n-2):
    print("$",end="")
    for _ in range(n-2):
        print("  ",end="")
    print(" $")     
print("$ "*n)    
print()
#right angeled triangle
for i in range(n):
    print()

    for _ in range(n-i):
            print(" ",end="")
    for _ in range(i):        
        print("*",end="")

#hourglass
for i in range(n):
    print()

    for _ in range(i):
            print(" ",end="")
    for _ in range(n-i):        
        print("* ",end="")       
for i in range(2,n+1):
    print()

    for _ in range(n-i):
            print(" ",end="")
    for _ in range(i):        
        print("* ",end="")           
#hollow pyramid
for i in range(n-1):
    print()
    
    for _ in range(n-i):
            print(" ",end="")
    print("* ",end="")        
    for _ in range(i-1):
            print("  ",end="")
    if i!=0:
        print("* ",end="")    
print("\n","* "*n)       

#butterfly pattern
for i in range(n):
    print()
    print("*"*i, end="")
    for _ in range((n-i)*2):
        print(" ", end="")
    print("*"*i, end="") 
for i in range(n):
    print()
    print("*"*(n-i), end="")
    for _ in range(i*2):
        print(" ", end="")
    print("*"*(n-i), end="")    
print()

#x shape
for i in range(n-1):
    print()
    print(" "*i,end="")
    print("*",end="")
    print(" "*(n-i-1)*2,end="")
    print("*",end="")
for i in range(n):
    print()
    print(" "*(n-1-i),end="")
    print("* ",end="")
    print(" "*(i-1)*2,end="")
    if i!=0:
        print("*",end="")    
