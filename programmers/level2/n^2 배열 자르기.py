def solution(n, left, right):
    ans = []
    
    for i in range(left,right+1):
        l = i % n
        r = i // n
        ans.append(max(l,r)+1)
    
    return ans
