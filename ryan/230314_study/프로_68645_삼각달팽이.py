from typing import List

def solution(n: int) -> List[int]:
    movement = [(1, 0), (0, 1), (-1, -1)]

    result = [[0 for _ in range(n)] for _ in range(n)]

    value = 1
    count = 0
    coords = [-1, 0]

    while count < n:
        x, y = coords
        dx, dy = movement[count % 3]

        for _ in range(n-count):
            x += dx
            y += dy

            result[x][y] = value
            value += 1

        count += 1
        coords = [x, y]

    answer = []

    for idx, each in enumerate(result):
        answer += each[:idx+1]

    return answer


print(solution(6))
