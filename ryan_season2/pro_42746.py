"""
가장 큰 수

[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
6 2 20 > 6 2 20
6 2 21 > 6 2 21
6 2 23 > 6 23 2
"""
# CHECK


def solution(numbers):
    numbers = [str(each) for each in numbers]

    numbers.sort(key=lambda x: x*3, reverse=True)

    answer = ''
    for each in numbers:
        answer += each

    if answer[0] == '0':
        return '0'

    return answer


print(solution([6, 10, 2, 0]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
