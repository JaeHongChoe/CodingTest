def cal(s):
    cnt=0
    temp=[]
    for k in s:
        temp.append(k)
        if len(temp) >=2 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()
            
    return temp
            

def solution(s):
    
    s = list(s)
    t = cal(s)
    
    if len(t) ==0:
        return 1
    else:
        return 0
