#%%
from collections import deque
def solution(m, n, puddles):
    
    answer = 0
    maps = []
    
    for i in range(n):
        maps.append([0 for i in range(m)])
    for i in puddles:
        maps[i[1]-1][i[0]-1] = -1
    
    def bfs(maps,start):
        queue = deque([start])
        dx = [1,0]
        dy = [0,1]
        count = 1
        while queue:
            
            x,y = queue.popleft()
            k = 0
            for i in range(2):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if(nx >= m or ny >= n):
                    k = 1
                    continue
                if(maps[ny][nx] == -1):
                    k = 1
                    continue
                    
                queue.append((nx,ny))
            if(k == 1):
                count += 0
            else:
                count += 1
        return count
                
    cnt = bfs(maps,(0,0))
    answer = cnt%1000000007
    return answer
#%%
print(solution(2, 2, []), 2)
#%%
print(solution(3, 3, []), 6)
#%%
print(solution(3, 3, [[2, 2]]), 2)
#%%
print(solution(3, 3, [[2, 3]]), 3)
#%%
print(solution(3, 3, [[1, 3]]), 5)
#%%
print(solution(3, 3, [[1, 3], [3, 1]]), 4)
#%%
print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
#%%
print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
#%%
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
#%%
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
#%%
print(solution(100, 100, []), 690285631)
# %%
