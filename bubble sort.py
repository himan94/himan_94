def bubble(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp    
    return a

x = [1,6,3,9,8,2,7]
for l in range(len(x)-1):
    bubble(x)

print x    

   
