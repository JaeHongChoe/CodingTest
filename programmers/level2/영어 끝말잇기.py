def solution(n, words):
    
    temp =[]
    player = 0
    time = 1
    for word in words:
        temp.append(word)
        player+=1
        if player >n:
            player = 1
            time +=1
            
        if len(temp) >1:
            if temp[-2][-1] != temp[-1][0] or temp.count(word) == 2:
                return [player, time]
            
            

    return [0,0]
                
