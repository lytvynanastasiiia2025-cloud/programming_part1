import math

x = float(input("enter number for x = "))
y = float(input("enter number for y = "))

if x <= 0 or y <= 0:
    print("x and y must be positive numbers")
else:
    p = math.log(x, 5) + math.log(y, 7)
    q = (5 * x) ** y
    main_x = math.tan(p ** 3 + 12 * q)
    print("Expression value main_x =", main_x)
