d={}
f=open('news', 'r')
for i in f:
    data=i.rstrip('\n').split(' ')
for j in data:
    if j not in d:
        d[j]=1
    else:
        d[j]+=1
print(d)
for k,v in d.items():
    print(k,",",v)