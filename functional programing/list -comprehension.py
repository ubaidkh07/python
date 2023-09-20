#method1
#.........................................
#lst=[i for i in range(1,31)]
#print(lst)

#lst=[i for i in range(1,51)]
#print(lst)

#lst=[(i,i**2) for i in range(1,21)]
#print(lst)

#lst=[(i,i**3) for i in range(1,31)]
#print(lst)

#method2
#...............................................
#lst=[i for i in range(1,31) if i%2==0]
#print(lst)

#lst=[i for i in range(1,51) if i%2==1]
#print(lst)

#lst=[i for i in range(1,51) if i%5==0]
#print(lst)

#lst=[(i,i**2) for i in range(1,31) if i%2==0]
#print(lst)

#string='luminartechnolab'
#v='aeiou'
#lst=[i for i in string if i in v]
#print(len(lst))

#method3
#............................................................

#lst=[(i,i**2) if i%2==0 else (i,i**3) for i in range(1,31)]
#print(lst)