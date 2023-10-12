"""
피로도

k는 1 이상 5,000 이하인 자연수입니다.
dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.
dungeons의 가로(열) 길이는 2 입니다.
dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.
"최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.
"최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.
서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.

k dungeons return
80	[[80,20],[50,40],[30,10]]	3
"""
from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons):
        temp_k = k
        cnt = 0

        for demand, consume in order:
            if temp_k >= demand:
                temp_k -= consume
                cnt += 1

            else:
                break

        answer = max(answer, cnt)

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))
