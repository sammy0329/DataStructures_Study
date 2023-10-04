"""
네트워크

컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.

n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""


def makeNetwork(com_idx, computers):
    networks = []
    next_step = [com_idx]

    while next_step:
        now = next_step.pop()

        for idx, isConnected in enumerate(computers[now]):
            if isConnected == 1 and idx not in networks:
                networks.append(idx)
                next_step.append(idx)

    return networks


def solution(n, computers):
    answer = 0

    network = [-1 for _ in range(n)]

    for com_idx in range(n):
        if network[com_idx] != -1:
            continue

        networkMembers = makeNetwork(com_idx, computers)

        for member_idx in networkMembers:
            network[member_idx] = answer

        answer += 1

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
