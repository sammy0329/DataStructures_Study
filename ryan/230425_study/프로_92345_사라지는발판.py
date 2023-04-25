"""
https://school.programmers.co.kr/learn/courses/30/lessons/92345

1. 승자와 패자를 결정 - role 부여
2. role에 따라 최선의 플레이: 도주 vs 추격
"""
from typing import List


def FourDirectSerach(board: List, nloc: List, visit=False) -> List:

    BOARD_SIZE = len(board)

    possibleCoords = []

    nx, ny = nloc

    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    for idx in range(4):
        nx_ = nx + dx[idx]
        ny_ = ny + dy[idx]

        x_status:bool = (0 <= nx_ < BOARD_SIZE)
        y_status:bool = (0 <= ny_ < BOARD_SIZE)

        if x_status and y_status and board[nx_][ny_] == 1:
            possibleCoords.append([nx_, ny_])

            if visit: board[nx_][ny_] = 0

    return possibleCoords


def ShortestPathSearch(board: List, aloc: List, bloc: List):

    board_ = board.copy()
    que_now = [aloc]
    que_next = []
    distance = 0

    while que_now:

        distance += 1

        for now_x, now_y in que_now:
            if [now_x, now_y] == bloc:
                return distance

            board_[now_x][now_y] = 0
            que_temp = FourDirectSerach(board=board_, nloc=[now_x, now_y], visit=True)

            que_next += que_temp

        que_now = que_next

    return 0


board, aloc, bloc = [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]  # 5
print(ShortestPathSearch(board, aloc, bloc))

board, aloc, bloc = [[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]  # 4
print(ShortestPathSearch(board, aloc, bloc))

board, aloc, bloc = [[1, 1, 1, 1, 1]], [0, 0], [0, 4]  # 4
print(ShortestPathSearch(board, aloc, bloc))

board, aloc, bloc = [[1]], [0, 0], [0, 0]  # 0

