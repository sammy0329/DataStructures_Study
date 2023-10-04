"""
타겟 넘버

numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2

주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""


def solution(numbers, target):
    graph = [0]

    for i in numbers:
        result = []

        for each in graph:
            result.append(each+i)
            result.append(each-i)

        graph = result

    answer = graph.count(target)

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
