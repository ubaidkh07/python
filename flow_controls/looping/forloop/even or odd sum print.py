n1=int(input("lower number"))
n2=int(input("upper number"))
esum=0
osum=0
for i in range(n1,n2+1):
    if(i%2==0):
        esum+=i
    else:
        osum+=i
print(esum)
print(osum)