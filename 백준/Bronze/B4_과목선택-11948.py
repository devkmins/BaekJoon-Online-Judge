L = []

for _ in range(6):  
    L.append(int(input())) 
    
L1 = sorted(L[:4]) 
L2 = L[4:] 

print(sum(L1[1:]) + max(L2))