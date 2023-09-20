f=open('/home/ubaid/Downloads/customer1.txt','r')
for i in f:
    data=i.rstrip('\n').split(',')
                                         #prof=data[4]
    if(data[4]=='Doctor'):               #if prof=='Doctor'
      print(data[1::2])