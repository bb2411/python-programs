p=int(input("principle intrest :"))
r=int(input("rate of interest :"))
t=int(input("time :"))
n=int(input("number of compound :"))
intrest=(p*r*t)/100
print("intrest :",intrest)
comp=p*(1+(r/(100*n)))**(n*t)
print("compound intrest :",comp)