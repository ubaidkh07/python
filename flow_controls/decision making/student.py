sid=int(input("enter id"))
h=int(input("held"))
sh=int(input("how class attended"))
print(sid,"attendens",sh)
per=sh/h*100
print(per,"%")
if(per>75):
    print("allowed exam")
else:
    print("not allowed exam")