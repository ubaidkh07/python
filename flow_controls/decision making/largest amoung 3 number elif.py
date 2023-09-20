n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
if(n1>n2):             #or if(n1>n2)&(n1>n3):
    print(n1,"largest")
elif(n2>n3):           #or if(n2>n1)&(n2>n3):
    print(n2,"largest")
elif(n3>n1):           # else
    print(n3,"largest")