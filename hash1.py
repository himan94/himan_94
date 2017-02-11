a = []
for i in range(11):
    a.insert(i,None)

b = [13,24,35,46,57,68,79,90,101,112,123]
c = len(a)

for j in b:
    r = j%c
    if a[r]==None:
        a[r] = j
    else:
        for k in range(11):
           if a[r-len(a)+k]==None:
               a[r-len(a)+k]=j
               break
           
        
print a    
