####################
## 대진표는 항상 짝수로 나오고 
## 반씩 계속 쪼갠다는 생각으로 몫이 같을때 
## 둘이 붙는 상황임.
#####################

def solution(n,a,b):
    a = a-1
    b = b-1
    cnt =0
    while a//2 != b//2:
        a = a//2
        b = b//2
        cnt +=1
    cnt+=1
    return cnt
