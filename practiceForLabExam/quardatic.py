# equation = -b sqrt(+- b*b - 4ac)/2a
import math

a = float(input())
b = float(input())
c = float(input())

d = b*b-4*a*c

if d>0:

    r1 = (-b + (math.sqrt(d))) / (2*a)
    r2 = (-b - (math.sqrt(d))) / (2*a)
    print("Roots are ", r1, r2)

elif d==0:
    r = -b/(2*a)
    print("Two equal roots are ",r)

else:
    print("Roots are imiginary")






