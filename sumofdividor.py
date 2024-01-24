n=28
k=n
sum=0
div=int(n/2)
while div>0:
    print(k,div)
    if k%div==0:
        sum=sum+div
    div=div-1
print(sum)