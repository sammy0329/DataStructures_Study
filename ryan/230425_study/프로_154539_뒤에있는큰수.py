"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""


def solution(numbers):
    NUMBERS_SIZE = len(numbers)

    answer = [-1 for _ in range(NUMBERS_SIZE)]

    stack = []

    for i in range(NUMBERS_SIZE):
        while stack:
            if numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]

            else:
                break

        stack.append(i)

    return answer


numbers = [2, 3, 3, 5]  # [3, 5, 5, -1]
print(solution(numbers))

numbers = [9, 1, 5, 3, 6, 2]  # [-1, 5, 6, 6, -1, -1]
print(solution(numbers))
