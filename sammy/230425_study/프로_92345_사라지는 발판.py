n,m=0,0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visit=[[0]*5 for _ in range(5)]

def outArea(x,y):
    return x < 0 or x >= n or y < 0 or y >= m

def dfs(board,cur_x,cur_y,op_x,op_y):
    if visit[cur_x][cur_y]: return 0
    canWin = 0

    for i in range(4):
        nx,ny=cur_x+dx[i],cur_y+dy[i]
        if outArea(nx,ny) or visit[nx][ny] or board[nx][ny] == 0: continue
        visit[cur_x][cur_y]=1 # 방문처리
        op_result = dfs(board,op_x,op_y,nx,ny) + 1
        visit[cur_x][cur_y]=0 # 방문 끝남 처리

        # 현재 저장된 값 패배인데 상대가 졌다고 하면 이기는 경우로 저장
        if canWin % 2 == 0 and op_result % 2 == 1 : canWin = op_result
        # 현재 저장된 값 패배인데 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
        elif canWin % 2 == 0 and op_result % 2 == 0 : canWin = max(canWin,op_result)
        # 현재 저장된 값 승리인데 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
        elif canWin % 2 == 1 and op_result % 2 == 1 : canWin = min(canWin,op_result)
        
    return canWin

def solution(board, aloc, bloc):
    global n,m
    n,m=len(board),len(board[0])
    return dfs(board,aloc[0],aloc[1],bloc[0],bloc[1])
    


print(solution(	[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]),5)
print(solution(	[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]),4)
print(solution(	[[1, 1, 1, 1, 1]], [0, 0], [0, 4]),4)
print(solution(	[[1]], [0, 0], [0, 0]),0)

# 항상 이기는 플레이어 B, 먼저 시작하는 플레이어 A