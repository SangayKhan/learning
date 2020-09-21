a = []
x = []
for j in range(10):
    y = int(input())
    a.append(y)
    
for i in a:
   A = i%42 
   x.append(A)

s = set(x)
l = list(s)
print(len(l))
