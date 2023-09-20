d={}
f=open('/home/ubaid/Downloads/temper','r')
for i in f:
    data=i.rstrip('\n').split(',')
    dstrct=data[0]
    temp=data[1]
    if dstrct not in d:
        d[dstrct]=temp
    else:
        oldvar=d[dstrct]
        if temp>oldvar:
            d[dstrct]=temp
print(d)
