from collections import deque

def solution(maps):
    answer = 0
    n=len(maps) # 행 길이
    m=len(maps[0]) # 열 길이
    
    # 상하좌우 움직임 처리
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    q=deque()
    q.append((0,0)) # 첫 시작은 0,0에서 시작
    
    while q:
        x,y=q.popleft()
           
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            # 위치 벗어나면 안됨
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            
            # 벽이면 진행 X
            if maps[nx][ny]==0:
                continue
            
            if maps[nx][ny]==1:
                if nx==0 and ny==0: continue # 정확한 파악을 위해 (0,0)는 더해주지 않는다.
                
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
        
        # 코드가 어떻게 동작하는지 파악하는 test code
        # print('current queue: ',q)
        # for tc in maps:
        #     print(tc)
        # print('===================================================')
    answer=maps[n-1][m-1]
    
    if answer==1: answer=-1 # 상대 팀 진영에 도달하는 방법이 없는경우 -1 처리   

    return answer



#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))