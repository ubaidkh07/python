num1=10
num2=20
print("before swapping")
print("num1 is",num1)
print("num2 is",num2)
print("after swapping")

print("num1 is",num1+num1)
print("num2 is",num2-num1)
#or
num1=num1+num2 #num1=10+20=30
num2=num1-num2 #num2=30-20=10
num1=num1-num2 #num1=30-10=20



#single line swapping
#........................
#[a,b,c=10,20,30]
num1,num2=10,20
num1,num2=num2,num1
print(num1)
print(num2)