print("This is a calculator to perform the perations kindly enter the number assigned to them:")
x=int(input("1)addition\n2)subtarction\n3)multiplication\n4)division\n5)modulus\n"))
a,b=int(input("enter a:")),int(input("enter b:"))
if x==1:
        print(a+b)
elif x==2:
        print(a-b) 
elif x==3:
        print(a*b)
elif x==4:
        if b==0:
            print("error: division by 0")
        else:    
            print(a/b)
elif x==5:
        print(a%b)               

