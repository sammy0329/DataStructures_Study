"""
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
"""


def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
