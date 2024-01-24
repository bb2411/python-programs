n=[]
for i in range(2,10000):
    k=i
    j=i//2
    sum=1
    while j>=1:
        if k%j==0:
            sum=sum+j
        j=j-1
    if sum==k:
        n.append(i)
        print(i)
print(n)