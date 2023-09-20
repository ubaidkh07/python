ls=[]
f=open('numbers', 'r')
for i in f:
    ls.append(int(i.rstrip('\n')))
print(ls)
print(sum(ls))

