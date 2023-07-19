import sys

n, k = map(int, input().split())

score = list(map(int,input().split()))

for _ in range(k):
    temp=0
    cnt =0
    s, e = map(int,input().split())
    for i in range(s-1,e):
        temp+=score[i]
        cnt+=1
    print("{:.2f}".format(temp/cnt))
