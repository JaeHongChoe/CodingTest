####################
##뭔가 이상하게 푼듯?..##
#####################
def cal(k):
    rem1 = 0
    rem2 = 0
    total =1
    for i in range(2,k):
        rem2 = total
        total += rem1
        rem1 = rem2
    return total,rem1

def solution(n):
    a,b = cal(n)
    return (a+b)%1234567
