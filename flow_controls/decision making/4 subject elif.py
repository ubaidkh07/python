s1=int(input("subject 1"))
s2=int(input("subject 2"))
s3=int(input("subject 3"))
s4=int(input("subject 4"))
sum=s1+s2+s3+s4
print(sum)
if(sum>=180):
    print("A+")
elif(sum==160<=179): #or  elif(sum>=160)&(sum>=179):
   print("A")
elif(sum==140<=159):
    print("B+")
elif(sum==120<=139):
    print("B")
elif(sum==100<=119):
    print("C+")
elif(sum==80<=99):
    print("C")
else:
    print("fail")
