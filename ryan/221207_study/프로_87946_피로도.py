"""
k	dungeons	result
80	[[80,20],[50,40],[30,10]]	3
"""


def solution(k, dungeons):
    import itertools

    answer = -1

    for order in itertools.permutations(dungeons):
        pw = k
        count = 0
        for req, consum in order:
            if pw >= req:
                pw -= consum
                count += 1
            else:
                break

        answer = max(answer, count)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]

print(solution(k, dungeons))
