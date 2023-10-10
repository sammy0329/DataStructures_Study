"""
가장 큰 수

[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
"""


def get_value(x, digits):
    temp = str(x)
    temp = temp[0] + '.' + temp[1:]
    temp = float(temp)
    temp *= (10 ** digits)

    return temp


def solution(numbers):
    digits = 0
    for each in numbers:
        digits += len(str(each))

    answer = ''

    numbers.sort(key=lambda x: (-get_value(x, digits), len(str(x))))
    numbers.sort(key=lambda x: (-get_value(x, digits), len(str(x))))

    for each in numbers:
        answer += str(each)

    return answer


print(solution([6, 10, 2]))
print(solution([3, 32, 34, 5, 9]))
