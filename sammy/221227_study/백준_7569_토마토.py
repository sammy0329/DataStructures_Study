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
        
        
        for idx,num in enumerate(data):
            if num==1:
                tomato.append((j,idx,i)) # 1인 값 큐에 삽입
                
        graph[i].append(data) # 3차원 배열 만들기
        


while tomato:
    x,y,z=tomato.popleft() # 큐에서 꺼내기
    
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        
        
        # 위치 벗어나면 continue
        if nx<0 or nx>=N or ny<0 or ny>=M or nz<0 or nz>=H:
            continue

        if graph[nz][nx][ny]==-1: # 토마토가 없으면 continue
            continue
        
        if graph[nz][nx][ny]==0: # 0이면 1씩 증가시켜 나가기
            graph[nz][nx][ny]=graph[z][x][y]+1
            tomato.append((nx,ny,nz))
            

check=False
          
for i in range(H):
    for j in range(N):
         
        for k in range(M):
            if graph[i][j][k]==0: # 0이 남아있는지 check
                check=True
                break
        cnt=max(cnt,max(graph[i][j])) # cnt에 최댓값 갱신
            
if check:
    print(-1)
else:
    print(cnt-1)           
