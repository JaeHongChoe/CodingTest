import sys

n, k = map(int, input().split())

ph = list(input())
cnt =0


for i in range(n):
    temp = cnt
    if ph[i] == 'P':
        for nn in range(k,0,-1):
            if i-nn >=0 and ph[i-nn] == 'H':
                # ph[i]='a'
                ph[i-nn] ='b'
                cnt+=1  
                break       
        if cnt == temp:
            for nn in range(1,k+1):
                if i+nn < n and ph[i+nn] == 'H':
                    # ph[i]='a'
                    ph[i+nn]='b'
                    cnt+=1
                    break
            
            
                

print(cnt)
