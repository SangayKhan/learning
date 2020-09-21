a = [int(i) for i in input().split()]
b = [str(j) for j in input().split()]
c = sorted(a)
tem = []
ans = []

dis = {"A":c[0], "B":c[1], "C":c[2]}
for y in b:
    tem.append(str(dis.get(y)))    
    
print(tem)