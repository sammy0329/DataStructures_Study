import sys
sys.setrecursionlimit(10**7)


class Distinct2D:
    def __init__(self, info):
        self.ROW = len(info)
        self.COL = len(info[0])
        self.info = info
        self.info_group = [[0 for _ in range(self.COL)] for _ in range(self.ROW)]

    def is_in(self, row, col):
        if 0 <= row < self.ROW and 0 <= col < self.COL:
            return True

        return False

    def visit(self, row, col, group):
        self.info_group[row][col] = group

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for direct in range(4):
            row_next = row + dx[direct]
            col_next = col + dy[direct]

            if self.is_in(row_next, col_next):
                if self.info_group[row_next][col_next] == 0 and self.info[row_next][col_next] == 1:
                    self.visit(row_next, col_next, group)

        return


    def result(self):
        group = 0
        for row in range(self.ROW):
            for col in range(self.COL):
                if self.info_group[row][col] == 0 and self.info[row][col] == 1:
                    group += 1
                    self.visit(row, col, group)

        return group


N = int(input())

for _ in range(N):
    row_size, col_size, lines = map(int, input().split())

    info = [[0 for _ in range(col_size)] for _ in range(row_size)]

    for _ in range(lines):
        row, col = map(int, sys.stdin.readline().strip().split())
        info[row][col] = 1


    distinct_instance = Distinct2D(info)

    answer = distinct_instance.result()
    print(answer)