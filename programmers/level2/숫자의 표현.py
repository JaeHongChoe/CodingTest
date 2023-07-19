def solution(n):
    finn = 0
    cnt = 1
    raw = 1
    total =0
    
    while True:
        if (n//2)+1 <= raw:
            break
        total +=  cnt
        cnt +=1
        if total == n:
            finn+=1
            total=0
            raw +=1
            cnt = raw
        elif total > n:
            total=0
            raw +=1
            cnt = raw
    
        
    return finn +1
