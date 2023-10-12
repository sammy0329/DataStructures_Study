"""
모의고사

[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
"""


def solution(answers):
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    scores = [0, 0, 0]

    for idx, answer in enumerate(answers):
        for s in range(3):
            if answer == patterns[s][idx % len(patterns[s])]:
                scores[s] += 1

    answer = []
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
