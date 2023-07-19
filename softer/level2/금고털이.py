import sys

w, num = map(int, input().split())
t_m=[]

for _ in range(num):
    m  = [tuple(map(int, input().split()))]
    t_m.extend(m)

t_m.sort(key=lambda x :  -x[1])

price=0

for k in t_m:
    m, p = k[0], k[1]
    if w - m <0:
        price += w * p
        break
    else:
        w -= m
        price += m * p
        

print(price)
