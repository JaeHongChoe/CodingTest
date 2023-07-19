import sys

n = int(input())
block =[]
for i in range(n):
    block.append(list(input()))

# print(block[0][1])

def check(block,x,y):
    cnt =0
    if x < 0 or y <0 or x == len(block) or y == len(block):
        return 0

    if block[x][y] =='0':
        return 0
    else: 
        block[x][y] = '0'
        cnt +=1
        cnt += check(block, x+1, y)
        cnt += check(block, x, y+1)
        cnt += check(block, x-1, y)
        cnt += check(block, x, y-1)
    return cnt

many =[]

for i in range(n):
    for k in range(n):
        cnt=0
        cnt = check(block,i,k)
        if cnt !=0:
            many.append(cnt)


print(len(many))
many = sorted(many)
for i in range(len(many)):
    print(many[i])
