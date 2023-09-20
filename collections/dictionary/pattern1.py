pat='abcdgfabcd'
d={}
for i in pat:
    if i not in d:
        d[i]=1
    else:
        print(i)