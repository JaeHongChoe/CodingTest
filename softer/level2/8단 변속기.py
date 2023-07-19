import sys

n =  input()
current =[]
for i in range(0,13,2):
    # print(i)
    current.append(int(n[i+2])-int(n[i]))

cc = list(set(current))

if cc == [1]:
    print("ascending")
elif cc ==[-1]:
    print("descending")
else:
    print("mixed")
