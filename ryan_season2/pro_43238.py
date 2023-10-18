"""
입국 심사

입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
심사관은 1명 이상 100,000명 이하입니다.

n	times	return
6	[7, 10]	28
"""
# CHECK


def solution(n, times):
    inf = 10 ** 18

    s = 0
    e = inf

    while e - s > 1:
        passed = 0
        mid = (s + e) // 2
        for each in times:
            passed += mid // each

        if passed >= n:
            e = mid

        elif passed < n:
            s = mid

    return mid


print(solution(6, [7, 10]))
