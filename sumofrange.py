i=1
sum=0
while i!=100 and (i+2)<=99:
    print(f"{i}/{i+2}")
    div=i/(i+2) 
    sum=sum+div
    i=i+2
print(sum)