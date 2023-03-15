from collections import deque
def solution(maps):#레버까지 최단거리 찾고 그다음에 출구까지 최단거리를 찾자
    answer = 0
    start = 0
    lever = 0
    end = 0
    for i in range(len(maps)):
        maps[i] = list(maps[i])  
        
        if('S' in maps[i]):

            start = (i,maps[i].index('S'))
            
        if('L' in maps[i]):

            lever = (i,maps[i].index('L'))
            
        if('E' in maps[i]):

            end = (i,maps[i].index("E"))

    def bfs(start,end):
        
        visited = [[200 for j in range(len(maps[i]))] for i in range(len(maps))]
        visited[start[0]][start[1]] = 0
        queue = deque([])
        queue.append(start)
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        while queue:
            print(visited)
            x,y = queue.popleft()
            print(x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print(nx,ny)
                if(nx<0 or nx>=len(maps) or ny<0 or ny>=len(maps[0])):
                    continue
                    
                if(maps[nx][ny] == 'X'):
                    continue
                    
                if(visited[nx][ny]>visited[x][y]+1):
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                
        return visited[end[0]][end[1]]
    print(bfs(start,lever))
    print(bfs(lever,end))
    answer = bfs(start,lever)+ bfs(lever,end)
    if(answer >= 200):
        answer = -1
        
    return answer

solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
# %%
