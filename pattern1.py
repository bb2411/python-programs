n=int(input("enter hight:"))
s=n
for i in range(n+1):
    for k in range(s):
        print(end=" ")
    for j in range (i):
        print('*',end=" ")  
    s=s-1
    print()