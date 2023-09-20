f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')                 #if(data[3]>'50'    === string
    if(int(data[3])>50):
        print(data[1:5])