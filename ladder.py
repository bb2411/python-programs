import math


h=int(input("enter hight :"))
a=int(input("enter angle :"))
rad=math.radians(a)
l=h/math.sin(rad)
print("LADDER LENTH :",l)