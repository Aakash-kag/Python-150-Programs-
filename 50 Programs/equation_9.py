#Write a Python program to solve quadratic equation.
#The standard form of a quadratic equation is:  ax^ + bx + c = 0
#where
#a,b and c are real numbers and a != 0 The Solutions of this Quadratic equation is given by: (-b+-(b^2 + 4ac)1/2)/(2a)

import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


discriminant = b**2 - 4*a*c

if discriminant > 0 :
    root1 = (-b + math.sqrt(discriminant)) / (2*a) 
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif discriminant == 0 :
    # one real root(repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    #Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)

    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")