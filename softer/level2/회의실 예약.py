#############################
######어거지;;; #########3
######################3

import sys

num1, num2 = map(int, input().split())

rooms, res =[], []

for _ in range(num1):
    rooms.append(input())

rooms = sorted(rooms)

for _ in range(num2):
    res.extend([tuple(input().split())])

for i in range(num1):
    print(f"Room {rooms[i]}:")
    avai=[]
    now =[]
    for k in range(len(res)):
        if rooms[i] == res[k][0]:
            avai.append((int(res[k][1]),int(res[k][2])))
    avai = sorted(avai)
    check =0
    if len(avai) == 0:
        now.append("09-18")
        check +=1
    elif avai[0][0] != 9:
        now.append(f"09-{avai[0][0]}")
        check +=1

    for n in range(len(avai)):
        if n == len(avai)-1 and avai[n][-1] !=18:
            now.append(f"{avai[n][1]}-18")
            check +=1
        elif n != len(avai)-1 and avai[n][1] != avai[n+1][0]:
            now.append(f"{avai[n][1]}-{avai[n+1][0]}")
            check +=1
    if check == 0:
        print("Not available")
    else:
        print(f"{check} available:")
        for nn in range(check):
            print(now[nn])
    
    if i+1 !=  num1:
        print("-----")
