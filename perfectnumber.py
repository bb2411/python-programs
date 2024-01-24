n = []
for i in range(2, 10000):
    k=i
    sum=0
    div=int(k/2)
    while div>0:
        if k%div==0:
            sum=sum+div
        div=div-1
    if sum == i:
        n.append(i)
        print(i)
print("Perfect numbers less than 10,000:", n)
