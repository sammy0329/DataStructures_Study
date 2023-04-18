"""
1   ... M
...
N

N = [1, 1000]
M = [1, 1000]
i(n, m) = [1, 1000]

len(skill) = [1, 250000]
skiil = [[type, r1, c1, r2, c2, degree],
        ...
        ]


"""


def count_alive(boards):
    cnt = 0

    for v_dict in boards.values():
        for v in v_dict.values():
            if v >= 1:
                cnt += 1

    return cnt


def solution(boards, skill):

    boardsDict = {}
    accumulate_by_row_range = {}

    for row_idx, row in enumerate(boards):

        accumulate_by_row_range[row_idx] = {}

        boardsDict[row_idx] = {}
        now = boardsDict[row_idx]

        for col_idx, each in enumerate(row):
            now[col_idx] = each

    for turn in skill:
        type_, row_start, col_start, row_end, col_end, degree = turn

        range_key = (col_start, col_end + 1)
        sign = -1 if type_ == 1 else 1

        effect = degree * sign

        for row_idx in range(row_start, row_end + 1):
            now = accumulate_by_row_range[row_idx]

            if now.get(range_key) is None:
                now[range_key] = effect

            else:
                now[range_key] += effect

    for row_idx, accumulates in accumulate_by_row_range.items():
        now = boardsDict[row_idx]
        for attack_range, effect in accumulates.items():
            for col_idx in range(attack_range[0], attack_range[1]):
                now[col_idx] += effect

    return count_alive(boardsDict)


board_ = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill_ = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board_, skill_))

board_ = [[1,2,3],[4,5,6],[7,8,9]]
skill_ = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board_, skill_))
