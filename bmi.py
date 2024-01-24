h=int(input("enter hight :"))
l=int(input("enter wight :"))
m=h/100
bmi=l/(m**2)
print(bmi)
if(bmi>=19 and bmi<=25):
    print("healthy")
elif(bmi<19):
    print("underwight")
else:
    print("overwight")