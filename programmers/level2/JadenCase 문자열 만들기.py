def solution(s):
    answer =''
    s = s.lower()
    s = list(map(str, s.split(' ')))
    
    for i in s:
        # print(i)
        answer += i.capitalize()+" "
        
    return answer[:-1]
