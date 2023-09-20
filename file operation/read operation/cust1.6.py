#each loc count
d={}
f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[-1]
    if loc not in d:
        d[loc]=1
    else:
        d[loc]+=1
for k,v in d.items():
   print(k,",",v)