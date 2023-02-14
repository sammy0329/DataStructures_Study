"""
name	return
"JEROEN"	56
"JAN"	23

name은 모두 대문자
len(name) [1, 20]

A to Z
65 to 90 (26)
0 to 25
"""


def serachContinuousA(name):

    return


def solution(name):
    LARGE_A = 65

    max_continue_A = 0

    # for each in name:


    answer = len(name)-1

    for idx, word in enumerate(name):
        target = ord(word) - LARGE_A

        answer += min(target, 26 - target)

    return answer


print(solution("JEROEN"))
print(solution("JAN"))
