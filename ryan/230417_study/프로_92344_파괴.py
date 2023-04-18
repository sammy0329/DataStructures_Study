"""
1   ... M
...
N

N = [1, 1000]
M = [1, 1000]
i(n, m) = [1, 1000]

skiil = [[type, r1, c1, r2, c2, degree],
        ...
        ]


"""
from typing import List


def count_alive(boards: List) -> int:
    cnt: int = 0

    for row in boards:
        for each in row:
            if each >= 1: cnt += 1

    return cnt


def solution(boards: List, skill: List) -> int:
    for turn in skill:
        type_, row_start, col_start, row_end, col_end, degree = turn

        sign = -1 if type_ == 1 else 1

        for row in range(row_start, row_end+1):
            for col in range(col_start, col_end+1):

                boards[row][col] += (degree * sign)

    return count_alive(boards)


board_ = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill_ = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board_, skill_))

board_ = [[1,2,3],[4,5,6],[7,8,9]]
skill_ = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board_, skill_))
