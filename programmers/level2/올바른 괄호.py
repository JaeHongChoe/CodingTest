def solution(s):
    answer = True
    pp =[]
    
    for i in s:
        if i =='(':
            pp.append(i)
        elif i ==')' and len(pp) != 0:
            pp.pop()
        else:
            return False
    
    if pp:
        return False
    else:
        return answer
