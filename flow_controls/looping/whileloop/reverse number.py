n1=int(input("enter number"))
res=0
while(n1!=0):
     m=n1%10
     res=res*10+m
     n1=n1//10
print(res)