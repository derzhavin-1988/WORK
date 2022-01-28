import math
x, y = map(float, input().split(" "))
r = float(input(""))

z, a = map(float, input().split(" "))

hyp = (x-z)**2 + (y-a)**2
rad = r*r

if hyp == rad:
    print("0")
elif hyp>rad:
    print("2")
else:
    print("1")

