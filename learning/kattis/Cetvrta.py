x = set()
y = set()

no = 0

while (no<3):
    p = [int(j) for j in input().split()]
    if p[0] in x:
        x.remove(p[0])
    else:
        x.add(p[0])
        
    if p[1] in y:
        y.remove(p[1])
    else:
        y.add(p[1])
    
    no += 1
 
print(x.pop(), y.pop())