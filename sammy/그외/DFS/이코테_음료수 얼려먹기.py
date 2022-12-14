import sys

n,m=map(int,sys.stdin.readline().strip().split())
graph=[]

# graph 입력 처리
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# dfs 탐색
def dfs(x,y):
    # 범위를 벗어나면 False 반환
    if x>=n or x<=-1 or y<=-1 or y>=m:
        return False
    
    if graph[x][y]==0:
        graph[x][y]=1 # 방문한 곳은 1로 바꿈

        for i in range(4): # 상하좌우 재귀적으로 호출
            dfs(x+dx[i],y+dy[i])   
        return True
    
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)
    
   