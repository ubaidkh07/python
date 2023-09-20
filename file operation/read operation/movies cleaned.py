#year>2005 name,year,rtng,dur
'''f=open('/home/ubaid/Downloads/movies_cleaned_pandas.csv','r')
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    if(year>'2005'):
        print(data[1:])'''
#rtng>4 name,year,rtng
'''f=open('/home/ubaid/Downloads/movies_cleaned_pandas.csv','r')
for i in f:
    data=i.rstrip('\n').split(',')
    rtng=data[3]
    if(rtng>'4'):
        print(data[1:4])'''

#year>2000 & rtng>=4.5 name,year,rtng
'''f=open('/home/ubaid/Downloads/movies_cleaned_pandas.csv','r')
for i in f:
    data=i.rstrip('\n').split(',')
    year=int(data[2])
    rtng=float(data[3])
    if((year>2000)and(rtng>=4.5)):
        print(data[1:4])'''

#each year movie count
d={}
f=open('/home/ubaid/Downloads/movies_cleaned_pandas.csv','r')
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[2]
    rtng=data[3]
    if(rtng=='4.5'):
        if year not in d:
            d[year]=1
        else:
            d[year]+=1
print(d)
for k,v in d.items():
    print(k,",",v)

    #'''if year not in d:
     #   d[year]=1
    #else:
     #   d[year]+=1
#print(d)'''
