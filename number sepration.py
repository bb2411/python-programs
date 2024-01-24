num=int(input("enter number :"))
a,sum=0,0
while num!=0:
    a=num%10
    num//=10
    sum=sum+a
    print(a)
print(sum)