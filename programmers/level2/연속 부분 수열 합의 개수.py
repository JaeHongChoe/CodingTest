def solution(elements):
    answer = []
    
    for i in range(1,len(elements)):
        for k in range(len(elements)):
            temp =[]
            temp.extend(elements[k:k+i])
            if k+i > len(elements):
                temp.extend(elements[0:k+i - len(elements)])
            answer.append(sum(temp))
    answer.append(sum(elements))
    
    
    return len(set(answer))
