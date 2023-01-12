#%%
from collections import deque

def solution(places):
    
    answer = []
    
    
    def bfs(places):
        visited = [[0,0,0,0,0] for i in range(5)]
        dx =[1,-1,0,0]
        dy = [0,0,1,-1]
        
        queue = deque([])
        
        x = 0
        y = 0
        for i in range(25):

            if(places[x][y] == "P"):
                queue.appendleft((x,y,-1,-1,0))
                #visited[x][y] = 1
            if(x == 4):
                x = 0
                y += 1
            else:
                x+=1
            
        while queue:

            num = 0
            x,y,x1,y1,check = queue.pop()
            
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if(nx < 0 or ny < 0 or ny>4 or nx > 4):
                    continue
                    
                elif(places[nx][ny] == "X"):
                    continue
                    
                elif(places[nx][ny] == "P"and visited[nx][ny] == 0):
                    if(x1 == nx and y1 == ny):
                        continue
                    return 0
                
                elif(places[nx][ny] == "O" and check == 0 and visited[nx][ny] == 0):
                    
                    visited[nx][ny] = 1
                    queue.append((nx,ny,x,y,1))
                    
                else:
                    continue

        return 1

    answer = [bfs(places[0]),bfs(places[1]),bfs(places[2]),bfs(places[3]),bfs(places[4])]
    
    return answer
# %%
"2"+"1"
# %%
