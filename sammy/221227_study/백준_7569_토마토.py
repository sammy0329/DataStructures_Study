# M은 상자의 가로 칸 수, N은 상자의 세로 칸 수, H는 상자 수
import sys
from collections import deque
input=sys.stdin.readline
M,N,H=map(int,input().split())

graph=[[] for _ in range(H)]
tomato=deque()
cnt=0

# 상하좌우 움직임 처리
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

for i in range(H):
    
    for j in range(N):
        data=list(map(int,input().split()))
        cnt+=1
        
        for idx,num in enumerate(data):
            if num==1:
                tomato.append((j,idx,i))
                
        graph[i].append(data)
        
cnt=0

while tomato:
    x,y,z=tomato.popleft()
    
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        
        
        # 위치 벗어나면 안됨
        if nx<0 or nx>=N or ny<0 or ny>=M or nz<0 or nz>=H:
            continue
        
     
        
        if graph[nz][nx][ny]==-1:
            continue
        
        if graph[nz][nx][ny]==0:
            graph[nz][nx][ny]=graph[z][x][y]+1
            tomato.append((nx,ny,nz))
            

check=False
          
for i in range(H):
    for j in range(N):
         
        for k in range(M):
            if graph[i][j][k]==0:
                check=True
                break
        cnt=max(cnt,max(graph[i][j]))
            
if check:
    print(-1)
else:
    print(cnt)           

print(graph)