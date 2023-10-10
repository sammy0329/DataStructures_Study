"""
완주하지 못한 선수

participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
"""

from collections import defaultdict


def solution(par, com):
    answer = ""
    logs = defaultdict(int)

    for name in par:
        logs[name] += 1

    for name in com:
        logs[name] -= 1

    for name, cnt in logs.items():
        if cnt != 0:
            answer = name

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
