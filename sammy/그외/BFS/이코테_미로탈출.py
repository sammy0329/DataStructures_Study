import sys
from collections import deque 

n,m=map(int,sys.stdin.readline().rstrip().split())
graph=[]

for i in range(n): # 미로 graph 저장
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

# 상하좌우 이동할 방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    
    while q:
        x,y=q.popleft()
        
        for i in range(4): # 상하좌우 이동 가능한지 파악
            nx=x+dx[i]
            ny=y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m: # 공간 벗어날시 continue
                continue
            
            if graph[nx][ny]==0: continue # 0일시 지나가지 못하므로 continue
            
            if graph[nx][ny]==1: # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
                
    return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단거리 반환

print(bfs(0,0))
