from itertools import combinations_with_replacement
no = 10
a = [2,3,5,6]
q=[]
for i in list(range(len(a))):
    # Finds every combination (with replacement) for each object in the list
    q.append(list(combinations_with_replacement(a, i+1)))


count = 0
if no % min(a)==0:
    count = count+1
for j in q:
    for k in j:
        if sum(k) == no:
            print k
            count = count+1
print count
