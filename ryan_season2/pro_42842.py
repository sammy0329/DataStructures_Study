"""
카펫

8 <= b <= 5000
1 <= y <= 2000000

b y return
10	2	[4, 3]
8	1	[3, 3]
24	24	[8, 6]
"""


def solution(brown, yellow):
    num_units = brown + yellow

    for w in range(3, int(num_units ** 0.5) + 1):
        if num_units % w != 0:
            continue

        h = num_units // w
        b = (2 * (w + h)) - 4

        if b == brown:
            return [h, w]

    return


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

