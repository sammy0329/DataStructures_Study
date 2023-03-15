"""
maps	answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
"""


def solution(maps):
    from collections import deque

    deq = deque()
    deq.append((0,0))
    num_row = len(maps)
    num_col = len(maps[0])
    visited = [[False for _ in range(num_col)] for _ in range(num_row)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while deq:
        x, y = deq.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= num_row or ny < 0 or ny >= num_col:
                continue

            if maps[nx][ny] == 0 or visited[nx][ny]:
                continue

            maps[nx][ny] += maps[x][y]
            deq.append((nx,ny))

    answer = maps[num_row-1][num_col-1] if maps[num_row-1][num_col-1] != 1 else -1

    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))
