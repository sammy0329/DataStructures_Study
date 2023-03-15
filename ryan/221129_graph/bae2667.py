def is_isolated(i, j, size, ans_count):
    row_search = [1, -1]
    col_search = [1, -1]

    if i == 0:
        row_search.remove(-1)
    elif i == size-1:
        row_search.remove(1)

    if j == 0:
        col_search.remove(-1)
    elif j == size-1:
        col_search.remove(1)

    for rs in row_search:
        if info[i+rs][j] == 1:
            answer[i+rs][j] = ans_count

    for ls in col_search:
        if info[i][j+ls] == 1:
            answer[i][j+ls] = ans_count


size = int(input())
info = [[0 for _ in range(size)] for _ in range(size)]
answer = [[0 for _ in range(size)] for _ in range(size)]
ans_count = 0

for i in range(size):
    row = input()
    for j, each in enumerate(row):
        info[i][j] = int(each)

for i in range(size):
    for j in range(size):
        if info[i][j] != 0 and answer[i][j] == 0:
            ans_count += 1
            answer[i][j] = ans_count
            is_isolated(i, j, size, ans_count)

        elif answer[i][j] != 0:
            is_isolated(i, j, size, answer[i][j])

for each in answer:
    print(each)
