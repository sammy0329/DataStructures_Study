import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input()) for _ in range(n)]
visited=[[False]*n for _ in range(n)]

# 상하좌우 움직임 처리
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,color):
    q= deque()
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        
        if visited[x][y]==False:
            # 특정 색깔 영역만 True 처리
            visited[x][y]=True
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<n and 0<=ny<n:
                    # 특정 색깔일 경우 q에 추가
                    if matrix[nx][ny]==color:
                        q.append((nx,ny))

#색약이 아닐경우 처리        
cnt=0
# 방문처리가 되지 않은 곳의 color로 bfs 진행
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            color=matrix[i][j]
            bfs(i,j,color)
            cnt+=1

# 색약일 경우 처리
visited = [[False] * n for _ in range(n)]
colorWeakness_cnt=0

# 빨강과 초록의 구분이 없기 때문에 R을 G로 바꿔주기
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'  

# 방문처리가 되지 않은 곳의 color로 bfs 진행
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            color=matrix[i][j]
            bfs(i,j,color)
            colorWeakness_cnt+=1   

print(cnt,colorWeakness_cnt)