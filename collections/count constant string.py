string='luminartechnolab'
v='aeiou'
c=[]
for i in string:
    if i not in v:
      c.append(i)
print(len(c))
