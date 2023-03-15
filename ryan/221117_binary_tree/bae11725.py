import sys

n = int(input())

roots = [0 for _ in range(n)]
connection_info = {key: [] for key in range(1, n+1)}

for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    connection_info[node1].append(node2)
    connection_info[node2].append(node1)

roots[0] = 1
stage = [1]
count = 1

while True:
    stage_temp = []
    for node_idx in stage:
        connected: list = connection_info[node_idx]
        for node_idx_2 in connected:
            if roots[node_idx_2-1] == 0:
                roots[node_idx_2-1] = node_idx
                stage_temp.append(node_idx_2)
                count += 1

    stage = stage_temp

    if count >= n:
        break

for each in roots[1:]:
    print(each)
