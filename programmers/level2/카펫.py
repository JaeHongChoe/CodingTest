########################
####1. 약수를 구하기#######
####2. 테두리가 잘 채워졌는지 확인##
########################


def solution(brown, yellow):
    total = brown + yellow
    
    for l in range(2, total+1):
        if total % l ==0:
            le = l
            r = total/l
            if brown == (le*2 + (r-2)*2):
                break
    
    return [r,le]
