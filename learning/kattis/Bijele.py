a = [1,1,2,2,2,8]
b = [int(j) for j in input().split()]
g = []

for i in range(6):    
     d = a[i]-b[i]
     g.append(d)
        
print(g)
     