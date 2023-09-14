def check(l,r):
    if l[-1] in [']','}',')','0']:
        return l.append(r)
    if l[-1] == '[' and r == ']':
        l.pop()
        return l
    elif l[-1] == '(' and r == ')':
        l.pop()
        return l
    elif l[-1] == '{' and r == '}':
        l.pop()
        return l
    else:
        return l.append(r)
    
    return ''
        
    
    

def solution(s):
    answer = 0
    for i in range(len(s)):
        temp=['0']
        for k in s[i:len(s)]:
            check(temp, k)
        for k in s[0:i]:
            check(temp, k)
        if len(temp) ==1:
            answer+=1
            
    return answer
