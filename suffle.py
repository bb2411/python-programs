import random
a=list(range(1,200))
b=list(range(1,200))
print(a)
i=0
while True:
    random.shuffle(b)
    if ((b[0] is a[0]) and (b[1] is a[1]) and (b[2] is a[2]) and (b[3] is a[3])):
        print(b,a,i)
        break
    i=i+1