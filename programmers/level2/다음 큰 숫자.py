##############
###1씩 추가 x##
### 변환 함수 사용 x##
### 2진수에서 발생하는 공통점을 찾기###
### 111 -> 1011으로 맨앞 1을 0으로 변환후 1을 앞으로 보내고 
### 뒤에있는 1들은 맨끝으로 정렬시키기###
### 1001100 -> 1010001
########################

def rev(n):
    p=1
    total =0
    for k in range(len(n)-1,-1,-1):
        total += n[k]*p
        p *=2
    return total
        

def solution(n):
    zeros =[]
    while True:
        temp = n%2
        n = n // 2
        zeros.append(temp)
        if n < 2:
            zeros.append(n)
            break
    
    zeros.reverse()
    ans = zeros
    ans.insert(0,0)
    if not zeros.count(0):
        zeros.insert(1,0)
        return rev(zeros)
    else:
        for k in range(len(zeros)-1,0,-1):
            if zeros[k] == 1 and zeros[k-1] == 0:
                ans[k] = 0
                ans[k-1] = 1
                nnnn = ans[k+1:]
                nnnn.sort()
                answer = ans[:k+1] + nnnn
                return rev(answer)
    
    return ''
