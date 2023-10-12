"""
모음사전

word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
"""
from itertools import product


def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']

    dictionary = []

    for word_len in range(1, 6):
        for each in product(w, repeat=word_len):
            dictionary.append(''.join(each))

    dictionary.sort()
    answer = dictionary.index(word)

    return answer + 1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
