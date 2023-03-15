class Node:
    def __init__(self, idx, adjacent=[]):
        self.idx = idx
        self.adjacent = adjacent


def search_2d(maps, row, col) -> list:
    rows = len(maps)
    cols = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    adjacents = []

    for direct in range(4):
        row_ = row + dx[direct]
        col_ = col + dy[direct]

        if not(0 <= row_ < rows and 0 <= col_ < cols): continue

        if maps[row_][col_] != 'X':
            adjacents.append(row_ * cols + col_)

    return adjacents


def get_distance(node_ea, start, dest):
    is_visited = [False for _ in range(node_ea)]
    count = 0
    stage = [start]

    while stage:
        count += 1
        next_stage = []
        for each in stage:
            for adj in each.adjacent:
                if adj == dest: return count
                if not is_visited[adj.idx]:
                    is_visited[adj.idx] = True
                    next_stage.append(adj)

        stage = next_stage

    return -1


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    nodes = [Node(idx=idx) for idx in range(rows * cols)]

    for idx in range(rows * cols):
        row = idx // cols
        col = idx % cols

        node_type = maps[row][col]

        if node_type == 'X': continue
        if node_type == 'S': start = nodes[idx]
        if node_type == 'L': lever = nodes[idx]
        if node_type == 'E': enter = nodes[idx]

        adjacents = search_2d(maps, row, col)
        adjacents = [nodes[adj_idx] for adj_idx in adjacents]
        nodes[idx].adjacent = adjacents

    start2lever = get_distance(len(nodes), start, lever)
    lever2enter = get_distance(len(nodes), lever, enter)

    if start2lever == -1 or lever2enter == -1:
        return -1

    return start2lever + lever2enter


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
