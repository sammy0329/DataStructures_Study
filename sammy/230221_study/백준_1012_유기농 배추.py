import sys
from collections import deque

def bfs(x,y):
    # 상하좌우 움직임 처리
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    q= deque()
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        # 방문하지 않았다면 방문처리
        if visited[x][y]==False:
            visited[x][y]=True
            
            # 상하좌우 움직임 처리
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                # 배추가 있고, 범위 안에 있다면 q에 append
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==1:
                    q.append((nx,ny))
 
input = sys.stdin.readline
t = int(input().rstrip())

for tc in range(t):
    m,n,k=map(int,input().split())
    
    matrix = [[0]*m for _ in range(n)] # 행열 저장할 리스트
    visited=[[False]*m for _ in range(n)] # 방문처리 저장할 리스트
    
    check_q=deque() # 배추가 있는 곳 저장할 queue
    
    # 배추 있는 지역 matrix에 1로 처리 후 check_q에 저장
    for i in range(k):
        y,x=map(int,input().split())
        matrix[x][y]=1
        check_q.append((x,y))
            
    cnt=0
    # 배추 있는 지역 중 방문처리가 되지 않은 곳 bfs 진행
    while check_q:
        i,j=check_q.popleft()
        if visited[i][j]==False:  
            bfs(i,j)
            cnt+=1
    
    print(cnt)