"""
아이템 줍기

rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
전체 배점의 50%는 직사각형이 1개인 경우입니다.
전체 배점의 25%는 직사각형이 2개인 경우입니다.
전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.

rectangle	characterX	characterY	itemX	itemY	result
[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
[[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
[[1,1,5,7]]	1	1	4	7	9
[[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
[[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10
"""


# WIP, 231009
def visit(path, maps, visited, answer=None):
    x, y = path[-1]

    if sum([sum(each) for each in visited]) == sum([sum(each) for each in maps]):
        answer = path
        return answer

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
            if not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True

                answer = visit(path+[(nx, ny)], maps, visited)

                visited[nx][ny] = False

    return answer


def rectangle_presentation(maps, rectengle_coord, erase=False):
    x1, y1, x2, y2 = rectengle_coord
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if erase:
                maps[x][y] = 0

            else:
                maps[x][y] = 1

    return maps


def solution(rectangle, characterX, characterY, itemX, itemY):
    rectangle_inner = []
    for (x1, y1, x2, y2) in rectangle:
        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1

        if x1 <= x2 and y1 <= y2:
            rectangle_inner.append([x1, y1, x2, y2])

    maps = [[0 for _ in range(51)] for _ in range(51)]

    for each in rectangle:
        maps = rectangle_presentation(maps, each)

    for each in rectangle_inner:
        maps = rectangle_presentation(maps, each, erase=True)

    visited = [[False for _ in range(51)] for _ in range(51)]
    visited[characterX][characterY] = True
    answer = visit([(characterX, characterY)], maps, visited)

    aside = answer.index((itemX,itemY))
    bside = len(answer)-answer.index((itemX,itemY))

    answer = aside if aside < bside else bside

    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
