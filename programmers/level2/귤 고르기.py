########################
## dictionary를 사용해서 배열에 있는 숫자들 저장하기
## 1번크기, 2번크기등 저장된 dict에서 가장 많이 들어가있는 
## 귤부터 검색해서 박스에 넣기
#######################

def solution(k, tangerine):
    
    many_dict = {}
    box=0
    ans =0
    cnt= -1 
    
    for l in range(len(tangerine)):
        if tangerine[l] in many_dict:
            many_dict[tangerine[l]] += 1
        else:
            many_dict[tangerine[l]] = 1
    
    sorted_many = sorted(many_dict.values())
    
    while(box < k):
        box += sorted_many[cnt]
        ans +=1
        cnt -= 1
    
    return ans
