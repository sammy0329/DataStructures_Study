def solution(m: int, n: int, board: list) -> int:
    total_broken = 0

    board = [list(row) for row in board]

    while True:
        is_possible = [[False for _ in range(n)] for _ in range(m)]

        # check is possible to broken
        for row in range(m-1):
            for col in range(n-1):

                target_block = board[row][col]
                if target_block == '-': continue

                for dx, dy in [(0, 1), (1, 0), (1, 1)]:
                    if board[row + dx][col + dy] != target_block:
                        break

                else:
                    for dx, dy in [(0,0), (0, 1), (1, 0), (1, 1)]:
                        is_possible[row + dx][col + dy] = True

        # broken
        broken_count = 0

        for row in range(m):
            for col in range(n):
                if is_possible[row][col]:
                    broken_count += 1
                    board[row][col] = '-'

        if broken_count == 0:
            return total_broken

        total_broken += broken_count

        # gravity working
        for col in range(n):
            each_col = ''

            for row in range(m-1, -1, -1):
                each_col += board[row][col]

            each_col = each_col.replace('-', '')
            each_col = each_col.ljust(m, '-')

            for row in range(m):
                board[row][col] = each_col[m-row-1]


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
