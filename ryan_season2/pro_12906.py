"""
같은 숫자는 싫어

arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]
"""


def solution(arr):
    answer = []

    for each in arr:
        if not answer:
            answer.append(each)

        else:
            if answer[-1] != each:
                answer.append(each)

    return answer


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))

