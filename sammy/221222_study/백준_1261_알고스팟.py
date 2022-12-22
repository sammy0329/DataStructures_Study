import sys
from collections import deque


input=sys.stdin.readline
M,N=map(int,input().split())

# 상하좌우 움직임 처리
dx=[1,-1,0,0]
dy=[0,0,1,-1]

maps=[]

for i in range(N):
    maps.append(list(map(int,input().rstrip())))
    
visited=[[-1]*M for _ in range(N)]

q=deque()
q.append((0,0)) # 첫 시작은 0,0에서 시작
visited[0][0]=0 # (0,0) 방문처리

while q:
    x,y=q.popleft()
       
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        # 위치 벗어나면 안됨
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        
        if visited[nx][ny] == -1:
            if maps[nx][ny] == 0:
                q.appendleft((nx,ny))
                visited[nx][ny]=visited[x][y]
            
            else:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
                
print(visited[N-1][M-1])
            
        
