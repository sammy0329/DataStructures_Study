"""
주식 가격

prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

prices  return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
"""


def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stack = []

    for sec, price in enumerate(prices):
        while stack:
            if stack[-1][1] > price:
                added_sec, _ = stack.pop()
                answer[added_sec] = sec - added_sec

            else:
                break

        stack.append((sec, price))

    return answer


print(solution([1, 2, 3, 2, 3]))


