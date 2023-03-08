from collections import deque

def bfs(matrix,start,end):
    # 상하좌우 움직임
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    # 이동 경로 체크
    visited=[[-1]*len(matrix[0]) for _ in range(len(matrix))]
    
    q=deque()
    q.append(start)

    # start지점 0으로 초기화
    visited[start[0]][start[1]]=0

    while q:
        x,y=q.popleft()

        if (x,y) == end: # end 지점일 경우 return
            return visited[x][y]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            
            if nx<0 or nx>len(matrix)-1 or ny<0 or ny>len(matrix[0])-1:
                continue
            
            # 상하좌우 움직임 처리
            if visited[nx][ny]==-1 and matrix[nx][ny] != 'X':
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))

    return -1

def solution(maps):
    matrix=[]
    # 시작, 레버, 끝 포인트 잡기
    startPoint=tuple()
    leverPoint=tuple()
    endPoint=tuple()
    
    for idx,row in enumerate(maps):
        matrix.append(list(row))
        if 'S' in row:
            startPoint=(idx,row.index('S'))
        if 'L' in row:
            leverPoint=(idx,row.index('L'))
        if 'E' in row:
            endPoint=(idx,row.index('E'))
    
    # 시작 지점에서 레버 지점까지 가는 경로 bfs 진행 
    leverLength=bfs(matrix,startPoint,leverPoint)

    if leverLength==-1: return -1

    # 레버 지점에서 끝 지점까지 가는 경로 bfs 진행
    endLength=bfs(matrix,leverPoint,endPoint)
    if endLength==-1: return -1

    return leverLength+endLength

print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]),16)
print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]),-1)
