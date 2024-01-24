a=[12,13,14,15,16]
c=int(input("enter element to find :"))
for i in a:
    if(i==c):
        print(a.index(i))
        break
print(a)