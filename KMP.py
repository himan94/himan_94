a = 'acacagt'
b = 'acatxacgacacagtqacacye'
prefix = []
suffix = []
table = [0]

k=0 #k,a,n,i,l,m
while k<len(a):
    n = a[0:k+1]
    for i in range(1,len(n)):
        prefix.append(n[0:i])
        suffix.append(n[i:len(n)])
    
    for l in prefix:
        for m in suffix:
            if l==m:
                table.pop(k)
                table.insert(k+1,len(l))
                break
    
    table.insert(k+1,0)
    del prefix[:]
    del suffix[:]
    k = k+1

table.pop(len(table)-1)
print table

c = 0 #count
c1 = 0
c2 = 0
while c2<12:
    for i1,j in zip(range(len(a)),range(c,len(b))):
        if a[i1] == b[j]:
            c1 = c1+1
            if c1 == len(a):
                print 'match'
                c = c+len(a)
        elif j>=len(b):
            print 'end of computation'
            break       
        elif a[i1]!=b[j]:
            c1 = 0
            q = table[i1]
            if q == 0:
                r = 1
            else:
                r = i1+1-q
            print i1,j,r,q
            c = c + r
            break
    print c
    c2 = c2+1

