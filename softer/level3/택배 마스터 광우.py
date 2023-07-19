######################################
##permutations(순열)만 알면 쉽다.#########
######################################
import sys
from itertools import permutations

n, m, k = map(int,input().split())

rail = list(map(int, input().split()))

rail = list(permutations(rail, n))
maxx =[]

for i in rail:
    total =0 
    cnt =0
    ind =0
    task=0
    while(cnt != k):
        if ind == n:
            ind = 0

        if total + i[ind] <= m:
            total += i[ind]
            ind+=1
        else:
            cnt+=1
            task+=total
            total=0
    maxx.append(task)

print(min(maxx))
