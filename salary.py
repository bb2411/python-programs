s=int(input("enter salary per hour:"))
h=int(input("enter your hours :"))
regular=s*h
if(h>40):
    exthour=h-40
    ratesalary=s*1.5
    extsalary=ratesalary*exthour
    regular=extsalary+regular
    print("extra salary is :",extsalary)
    print("total salary :",regular)
else:
    print("total salary :",regular)