import math
a_parametr=float(input("enter number for a = "))
x=float(input("enter number for x = ")) 

if x > 1:
    y= math.sqrt(a_parametr+ math.log10(x)) 
elif abs(x) < 1:
    y = math.asin(x)
else:
    y = x**a_parametr

print("Expression value y = ", y)
