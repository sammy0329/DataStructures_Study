import sys


def solution(info, target):
    lo = 1
    hi = 2**31 - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        cut_result = sum([each//mid for each in info])
        print(lo, hi, mid, cut_result)

        if cut_result < target: hi = mid - 1
        elif cut_result >= target: lo = mid + 1

    return hi


N, target = map(int, input().split())
info = [int(sys.stdin.readline().strip()) for _ in range(N)]

print(solution(info, target))
