"""
전력망을 둘로 나누기

n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

n	wires	result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	1
"""
from collections import defaultdict


def bfs(n, info, start):
    cnt = 0
    visited = [False for _ in range(n)]

    to_visit = [start]

    while to_visit:
        next_stage = []

        for idx in to_visit:
            visited[idx] = True
            cnt += 1

            for next_idx in info[idx]:
                if not visited[next_idx] and next_idx not in next_stage:
                    next_stage.append(next_idx)

        to_visit = next_stage

    return cnt


def solution(n, wires):
    answer = n
    info = defaultdict(list)

    for n1, n2 in wires:
        n1 -= 1
        n2 -= 1

        info[n1].append(n2)
        info[n2].append(n1)

    for n1, n2 in wires:
        n1 -= 1
        n2 -= 1

        info[n1].remove(n2)
        info[n2].remove(n1)

        child_nodes = bfs(n, info, n1)
        answer = min(answer, abs(child_nodes - (n - child_nodes)))

        info[n1].append(n2)
        info[n2].append(n1)

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
