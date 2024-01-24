m=int(input("Enter Marks of Maths:"))
e=int(input("Enter Marks of English:"))
s=int(input("Enter Marks of Science:"))

r=(m+e+s)/3
print("Result",r)
if(r>=90):
    print("Distiction")
elif(r>=80 and r<=89):
    print("First Class")
elif(r>=70 and r<=79):
    print("Second class Class")
elif(r>=60 and r<=69):
    print("Avrage")
elif(r>=50 and r<=59):
    print("Pass Class")
else:
    print("Fail")