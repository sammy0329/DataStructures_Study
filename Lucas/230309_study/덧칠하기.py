#%%
def solution(n, m, section):
    
    answer = 0
    
    paint = [1 for i in range(n)]
    for i in section:
        paint[i-1] = 0
        
    now = 0 
    
    while True:

        if(now >= n):
            break
        if paint[now] == 0:
            answer += 1
            
            for i in range(0,m):
                if((now + i) >= n):
                    continue
                paint[now+i] = 1
            now += m
        else:
            now += 1

    return answer
print(solution(8,4,[2, 3, 6]))
print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))
# %%
