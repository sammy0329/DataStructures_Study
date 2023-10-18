"""
섬 연결하기

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.

n	costs	return
4	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	4
"""


# Check: Call by Value issue, 확인


from collections import defaultdict


def updateParent(n, graph):
    parent = [i for i in range(n)]
    visited = [False for _ in range(n)]
    stack = []

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        stack += graph[i]

        while stack:
            now = stack.pop()
            if not visited[now]:
                parent[now] = i
                visited[now] = True

                stack += graph[now]

    return parent


def solution(n, costs):
    answer = 0
    buf = -1

    info = defaultdict(list)
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])

    for debug_idx in range(n-1):
        while True:
            buf += 1
            n1, n2, cost = costs[buf]

            if parent[n1] != parent[n2]:
                break

        info[n2].append(n1)
        info[n1].append(n2)

        parent = updateParent(n, info)
        answer += cost

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
