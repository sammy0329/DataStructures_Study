"""
게임 맵 최단거리

maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
"""
from collections import deque


def solution(maps):
    num_row = len(maps)
    num_col = len(maps[0])

    visited = [[-1 for _ in range(num_col)] for _ in range(num_row)]
    visited[0][0] = 1

    que = deque([(0, 0)])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < num_row and 0 <= ny < num_col:
                if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                    if nx == num_row - 1 and ny == num_col - 1:
                        return visited[x][y] + 1

                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))

    return -1


print(solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
