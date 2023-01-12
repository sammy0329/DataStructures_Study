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
        
        if visited[nx][ny] == -1: # 방문을 아직 안했을 경우
            if maps[nx][ny] == 0: # 지나갈 수 있으면
                q.appendleft((nx,ny)) # 먼저 처리할 수 있도록 leftappend
                visited[nx][ny]=visited[x][y] # 벽을 부수지 않았으므로 visited[x][y]에 해당하는 값 저장
            
            else:
                visited[nx][ny]=visited[x][y]+1 # 벽을 부쉈으므로 visited[x][y] + 1에 해당하는 값 저장
                q.append((nx,ny)) # 벽을 부수지 않고 가는 경우가 먼저 큐에 들어와 방문 처리 되기 때문에 벽을 부수고 도착한 경우를 무시 가능
                
print(visited[N-1][M-1])
            
        
