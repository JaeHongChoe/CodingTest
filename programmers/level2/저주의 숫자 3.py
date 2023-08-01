
def solution(n):
    total=0
    for i in range(n):
        total+=1
        while True:
            l = (total //10) //10
            r = (total //10) % 10
            if total % 3 ==0 or total % 10 == 3 or l ==3 or r == 3:
                total+=1
            else: break
    return total
