def solution(s):
    cnt = 0
    zeros=0
    answer =[]
    
    while (int(s)>2):
        temp = []
        zero = s.count("0")
        zeros += zero
        many = len(s) - zero
        ##내장함수 없이##
        while True:
            rem = many % 2
            many = many //2
            temp.insert(0,rem)
            
            if many <2:
                temp.insert(0,many)
                break
                
        s =''.join(map(str,temp))
        cnt +=1
        
    return [cnt, zeros]
