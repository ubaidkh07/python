lst=[1,2,3,4,5,6,7,8,9,10]
lst1=list(filter(lambda n1:n1%2==1,lst))
print(lst1)
lst2=list(map(lambda n1:n1**2,lst1))
print(lst2)