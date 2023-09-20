d={}
f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')       #each prof count
    prof=data[4]
    if prof not in d:
        d[prof]=1
    else:
        d[prof]+=1
#print(d)
for k,v in d.items():
    print(k,",",v)