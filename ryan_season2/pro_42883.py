"""
큰 수 만들기

number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.

number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"
"44441" 1   "4444"
"""


def solution(number, k):
    cursor = 0
    for _ in range(k):
        for i in range(max(0, cursor), len(number) - 1):
            if number[i] < number[i+1]:
                number = number[:i] + number[i+1:]
                break

            cursor = i - 1

        else:
            number = number[:len(number)-k]
            break

    return number


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("44441", 1))
