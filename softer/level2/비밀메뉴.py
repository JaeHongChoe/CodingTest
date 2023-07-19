import sys

num1, total, many = map(int,input().split())

code = list(map(int,input().split()))
init = list(map(int,input().split()))
cnt =0

for i in range(total - num1+1):
    if init[i] == code[0]:
        for k in range(num1):
            if init[i+k] == code[k]:
                cnt +=1
    if cnt == num1:
        print("secret")
        break
    else:
        cnt=0

if cnt != num1:
    print("normal")
