import sys
sys.setrecursionlimit(10**7)

def searchNeighbor(row, col, N):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    have_to = []

    for idx in range(4):
        row_ = row + dx[idx]
        col_ = col + dy[idx]

        if 0 <= row_ < N and 0 <= col_ < N:
            if mark[row_][col_] == 0 and info[row][col] == info[row_][col_]:
                have_to.append((row_, col_))

    return have_to


def marking(row, col, mark, now):
    mark[row][col] = now

    extends = searchNeighbor(row, col, len(mark))
    for row_, col_ in extends:
        marking(row_, col_, mark, now)


N = int(input())

info_ = [input() for _ in range(N)]
info_rg = [info_[row].replace('R', 'G') for row in range(N)]

for each in [info_, info_rg]:
    info = each

    mark = [[0 for _ in range(N)] for _ in range(N)]
    now = 0
    for row in range(N):
        for col in range(N):
            if mark[row][col] == 0:
                now += 1
                marking(row, col, mark, now)

    print(now, end=' ')