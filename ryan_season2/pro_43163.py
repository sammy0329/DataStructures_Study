"""
단어 변환

각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.

begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
"""


def word_comparison(a, b):
    num_diff = 0
    for x, y in zip(a, b):
        if x != y:
            num_diff += 1

    is_valid = True if num_diff == 1 else False

    return is_valid


def visit(path, target, words, answer):
    now = path[-1]

    if now == target:
        min_count = len(path)-1
        answer = min_count if min_count < answer else answer

        return answer

    is_valid = [word_comparison(now, word) for word in words]

    for idx, (word, val) in enumerate(zip(words, is_valid)):
        if val:
            new_path = path + [word]
            new_words = words[:idx] + words[idx + 1:]
            answer = visit(path=new_path, target=target, words=new_words, answer=answer)

    return answer


def solution(begin, target, words):
    answer = visit(path=[begin], target=target, words=words, answer=len(words)+1)
    answer = 0 if answer == len(words)+1 else answer

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
