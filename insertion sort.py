s = [54,26,93,17,77,31,44,55,20]

for i in range(1,len(s)+1):
    b = s[0:i]
    a = b
    count = 0
    #print a
    while count<len(a):                  # while loop to perform the for loop len(a) number of times-like in bubble sort
        for j in range(len(a)-1):        # for loop compares every j'th element with next element
            if a[j] >= a[j+1-len(a)]:
                temp = a[j]
                a[j] = a[j+1-len(a)]
                a[j+1-len(a)] = temp
                
        count = count+1
        
print a    
        
    
        
        


           

