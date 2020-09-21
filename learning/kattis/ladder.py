import math
p = [int(j) for j in input().split(" ")]
h = int(p[0])
v = int(p[1])

sine = math.sin(math.radians(v))
x = h / sine

print (int(math.ceil(x)))