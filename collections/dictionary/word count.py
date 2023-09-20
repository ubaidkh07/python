d={}
line='hadoop sqoop pig hadoop spark sqoop'
data=line.split(' ')
for i in data:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)



