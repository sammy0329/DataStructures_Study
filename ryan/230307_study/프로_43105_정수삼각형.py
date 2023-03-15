def solution(triangle: list) -> int:
    dynamic_copy = [[0 for _ in range(i)] for i in range(1, len(triangle)+1)]

    for row, _ in enumerate(triangle):
        if row == 0:
            dynamic_copy[0][0] = triangle[0][0]
            continue

        for col in range(row+1):
            if col == 0:
                dynamic_copy[row][col] = triangle[row][col] + dynamic_copy[row-1][col]

            elif col == row:
                dynamic_copy[row][col] = triangle[row][col] + dynamic_copy[row-1][col-1]

            else:
                dynamic_copy[row][col] = triangle[row][col] + max(dynamic_copy[row-1][col], dynamic_copy[row-1][col-1])

    max_value = max(dynamic_copy[-1])

    return max_value


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
