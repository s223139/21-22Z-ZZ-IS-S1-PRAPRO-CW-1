import math
a= input()
b= input()
c= input()

a= float(a)
b= float(b)
c= float(c)

s=(a+b+c)/2

area= math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)