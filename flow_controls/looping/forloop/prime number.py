#check given number is prime or not
#prime numbers:2,3,5,7,11,13,17,19,23,.....

#not prime:8,20,      (8=2,4),(20=2,4,5,10)

n1=int(input("enter number"))
flag=0
for i in range(2,n1):
    if(n1%i==0):
        flag=1
if(flag>0):
    print("not prime")
else:
    print("prime number")
