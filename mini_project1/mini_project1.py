import math

a1 = float(input("X coordinates of point a:"))
a2 = float(input("Y coordinates of point a:"))
b1 = float(input("X coordinates of point b:"))
b2 = float(input("Y coordinates of point b:"))

metro_a = math.sqrt(a1 ** 2 + a2 ** 2)
metro_b = math.sqrt(b1 ** 2 + b2 ** 2)
esoteriko_ginomeno = a1 * b1 + a2 * b2
costh = esoteriko_ginomeno / (metro_a * metro_b)
print("The meassures are: a=",metro_a,"b=",metro_b,"\nThe scalar product is:",esoteriko_ginomeno,"\nCos of angle th is:",costh)

gonia_a = math.degrees(math.atan2(a1, a2))
gonia_b = math.degrees(math.atan2(b1, b2))
goniath = math.fabs(gonia_a - gonia_b)
print("The angle is",goniath,"degrees")
