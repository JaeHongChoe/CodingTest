#######################################
####시간복잡도를 줄이는데 많이 힘들었다.#############
#### 처음에 pop을 사용했는데 O(N)으로 반복문과 사용하면
#### O(N^2)로 효율성을 통과하지 못한다.
#### 그래서 people를 정렬하고 최대, 최소 인덱스를 활용하였다.
####################################################
def solution(people, limit):
    people.sort()
    r = len(people)-1
    l = 0
    cnt =0
    while l <=r:
        if people[l] + people[r] <= limit:
            l+=1
            r-=1
            cnt+=1
        else:
            r-=1
            cnt+=1
    
    return cnt
