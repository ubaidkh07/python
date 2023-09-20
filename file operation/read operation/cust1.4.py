f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    if((data[-2]=='Doctor')&(data[3]>'50')):       #agee>50 & prof=Doctor fn,ln,age
        print(data[1:4])