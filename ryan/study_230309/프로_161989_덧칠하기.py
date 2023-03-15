"""
1m 구역 * n: int
롤러의 길이 m: int
다시 칠할 section: list
    sorted by asc
    no dup

1 <= m <= n <= 100000
"""


def solution(n, m, section):
    now = 0
    cnt = 0
    for each in section:
        if now < each:
            now = (each + m - 1)
            cnt += 1

    return cnt


n = 4
m = 1
section = [1, 2, 3, 4]
print(solution(n, m, section))
