l=[]
f=open('numbers1', 'r')
for i in f:
    a=int(i)    #if(int(i)%2==0):
    if(a%2==0):
        l.append(a)
print(l)
print(sum(l))