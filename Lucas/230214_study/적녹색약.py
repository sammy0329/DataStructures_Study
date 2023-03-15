#%%
from collections import deque
N = int(input())
maps = []
for i in range(N):
    maps.append(list(input()))

visited = [[0 for i in range(N)] for i in range(N)]
visited1 = [[0 for i in range(N)] for i in range(N)]


def bfs_normal(maps,visited,N):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    ans = 0
    queue = deque([])
    a=0
    b=0
    while True:
        if a > N-1 or b >N-1:
            break
        if visited[a][b] == 1:
            if a == N-1:
                b+=1
                a=0
            else:
                a+=1
            continue
        queue.append((a,b))
        while queue:

            x,y = queue.popleft()
            visited[x][y] = 1
            goal = maps[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if(nx<0 or nx>=N or ny <0 or ny>=N):
                    continue
                if(visited[nx][ny] == 1):
                    continue
                if(maps[nx][ny] == goal):
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
        ans += 1

        if a == N-1:
            b+=1
            a=0
        else:
            a+=1
    return ans

def bfs_notnormal(maps,visited,N):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    ans = 0
    queue = deque([])
    a=0
    b=0
    while True:
        if a > N-1 or b >N-1:
            break
        if visited[a][b] == 1:
            if a == N-1:
                b+=1
                a=0
            else:
                a+=1
            continue
        queue.append((a,b))
        while queue:

            x,y = queue.popleft()
            visited[x][y] = 1
            goal = maps[x][y]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if(nx<0 or nx>=N or ny <0 or ny>=N):
                    continue
                if(visited[nx][ny] == 1):
                    continue
                if goal == "R":
                    if(maps[nx][ny] == "R" or maps[nx][ny] == "G"):
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                elif goal == "G":
                    if(maps[nx][ny] == "R" or maps[nx][ny] == "G"):
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
                else:
                    if(maps[nx][ny] == goal):
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
        ans += 1

        if a == N-1:
            b+=1
            a=0
        else:
            a+=1
    return ans
print(bfs_normal(maps,visited,N),bfs_notnormal(maps,visited1,N))