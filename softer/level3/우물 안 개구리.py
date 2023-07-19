import sys

n, m = map(int,input().split())

w = list(map(int,input().split()))
check = [0 for _ in range(len(w))]

for _ in range(m):
    w1, w2 = map(int, input().split())
    if w[w1-1] == w[w2-1]:
        check[w1-1] = 1
        check[w2-1] = 1
    elif w[w1-1] < w[w2-1]:
        check[w1-1] = 1
    else:
        check[w2-1] = 1

print(check.count(0))
