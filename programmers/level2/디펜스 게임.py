import heapq

def solution(n, k, enemy):
    
    if k >= len(enemy):
        return len(enemy)
    
    cnt =0
    kn=k
    cont =[]
    
    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(cont,(enemy[i]*-1))
        
        if n  < 0 and kn ==0:
            return cnt
        elif n < 0 and kn!=0:
            n += (heapq.heappop(cont)*-1)
            kn-=1
        cnt+=1
    
    return cnt
