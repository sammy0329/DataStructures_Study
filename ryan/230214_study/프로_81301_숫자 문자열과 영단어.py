"""
DONE

s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123

RESTRAINTS

1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
"""


def solution(s):
    answer = ''
    cursor = 0

    # {'key': (value, string length)}
    info = {'on': ('1', 3),
            'tw': ('2', 3),
            'th': ('3', 5),
            'fo': ('4', 4),
            'fi': ('5', 4),
            'si': ('6', 3),
            'se': ('7', 5),
            'ei': ('8', 5),
            'ni': ('9', 4),
            'ze': ('0', 4)}

    while cursor < len(s):
        if s[cursor].isnumeric():
            answer += s[cursor]
            cursor += 1

        else:
            k = s[cursor:cursor+2]
            v, strLength = info[k]

            answer += v
            cursor += strLength

    return int(answer)


print(solution('2three45sixseven'))
