n1 = int(input("first number"))
n2 = int(input("second number"))
n3 = int(input("third number"))
# nestedif
if (n1 > n2) & (n1 > n3):
    if (n2 > n3):
        print(n2, "second largest")
    else:
        print(n3, "second largest")
elif (n2 > n1) & (n2 > n3):
    if (n1 > n3):
        print(n1, "second largest")
    else:
        print(n3, "second largest")
elif (n3 > n1) & (n3 > n2):
    if (n2 > n1):
        print(n2, "second largest")
    else:
        print(n1, "second largest")
else:
    print("number is equal")
# or
'''num1=int(input("enter"))
num2=int(input("enter"))
num3=int(input("enter"))
if(num1<num2) and (num1<num3) and (num3>num2):
	print(num2)
elif(num1<num2) and (num1<num3) and (num3<num2):
	print(num3)
elif(num2<num1) and (num2<num3) and (num1>num3):
     print(num3)
elif(num2<num1) and (num2<num3) and (num1<num3):
	print(num1)
elif(num3<num1) and (num3<num2) and (num1<num2):
	print(num1)
elif(num3<num1) and (num3<num2) and (num1>num2):
	print(num2)
else:
	print("error")'''
