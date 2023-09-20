f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
    loc=data[-1]
    if(loc=='india'):
        print(data[1:5])