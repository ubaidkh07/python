l=int(input("lower number"))
u=int(input("upper number"))
esum=0
osum=0
while(l<=u):
    if(l%2==0):
        esum+=l
    else:
     osum+=l
    l+=1
print(esum)
print(osum)

