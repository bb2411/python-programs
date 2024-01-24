a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]
for i in a:
    if(i%2==0):
        print(i)
        b.append(i)
        c.append(i-1)
print(c)
print(b)