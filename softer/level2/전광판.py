import sys

ans = {'0' : '1110111',
    '1' : '0010001',
    '2' : '0111110',
    '3' : '0111011',
    '4' : '1011001',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110001',
    '8' : '1111111',
    '9' : '1111011',
    'n' :'0000000'}

num = int(input())


for _ in range(num):
    cnt =0
    case1, case2 =  input().split()
    if len(case1) != 5:
        case1 = "n"*(5- len(case1)) +case1
    if len(case2) !=5:
        case2 = "n"*(5- len(case2)) +case2
    
    for i in range(5):
        if case1[i] != case2[i]:
            for k in range(7):
                if ans[case1[i]][k] != ans[case2[i]][k]:
                    cnt+=1
    print(cnt)
