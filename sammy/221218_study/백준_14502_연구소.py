import sys,copy
from itertools import combinations
from collections import deque

# dfs로 탐색
def dfs(x,y):
    maps_[x][y] = 2
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]    

        if nx <= -1 or nx >=N or ny<=-1 or ny >=M:
            continue
        if maps_[nx][ny] != 0 :
            continue
        else:
            dfs(nx,ny)
                       
# 입력 값 maps에 리스트로 저장
N,M=map(int,sys.stdin.readline().rstrip().split())
maps=list()

for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().rstrip().split())))

# 상하좌우 움직임 처리
dx=[1,-1,0,0]
dy=[0,0,1,-1]

result=0
virus=deque()
zeros = deque()
answer=[]

for i in range(N):
    for j in range(M):
        if maps[i][j]==2: # virus, zero 부분 인덱스 큐에 저장
            virus.append([i,j])
            
        elif maps[i][j]==0:
            zeros.append([i,j])

            
# 3개의 벽이 세워질 수 있는 경우의 수 모두 구하기
zeros_combi = combinations(zeros, 3)

# 3개의 벽이 세워질 수 있는 경우의 수마다 안전 지역 저장
for combi in zeros_combi:
    result = 0
    maps_ = copy.deepcopy(maps)
    
    # 3개의 벽 세우기
    maps_[combi[0][0]][combi[0][1]] = 1
    maps_[combi[1][0]][combi[1][1]] = 1
    maps_[combi[2][0]][combi[2][1]] = 1
    
    for vi in virus :
        dfs(vi[0],vi[1])
        
    for row in range(N):
        for col in range(M):
            if maps_[row][col] == 0:
                result += 1

    answer.append(result)
    
print(max(answer))
    
