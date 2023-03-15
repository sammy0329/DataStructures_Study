"""
롤케이크 길이: 100만
토핑 종류: 1만
"""


def solution(topping: list[int]):
    lo = 0
    hi = len(topping) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        left = topping[:mid]
        right = topping[mid:]

        if len(set(left)) >= len(set(right)):
            hi = mid - 1
        else:
            lo = mid + 1

    floor = lo

    lo = 0
    hi = len(topping) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        left = topping[:mid]
        right = topping[mid:]

        if len(set(left)) > len(set(right)):
            hi = mid - 1
        else:
            lo = mid + 1

    ceil = hi

    return ceil - floor + 1


topping = [1, 2, 1, 3, 1, 4, 1, 2]  # 2
print(solution(topping))

import collections

lst = [1, 2, 3, 4]
deq = collections.deque(lst)

lst.pop()
print(lst)

