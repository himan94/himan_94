h = raw_input("enter the movie's name:")
w = []
s = len(h)
w.append(["O"] * s)
count = 0
count1 = 0
for l,m in enumerate(h):
    if m.isspace():
        w[0][l] = "/"
        

while (count < 7):
    print w
    if count1 == s :
        print"you win"
        break

    d = raw_input("enter a letter:")
    t = d
    for i,j in enumerate(h):
        if d == j:
            print"hit in position %d"%(i+1)
            print i
            w[0][i] = t         
            count = count - 1
            count1 = count1 + 1
        

        
    count = count + 1
            



            
            
