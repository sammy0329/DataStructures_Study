import copy
import itertools

answer = True

table = []

num_input = int(input())

for _ in range(num_input):
    row = input().split()
    table.append(row)

idx = 0
empty_index_list = []
teacher_index_list = []

for row in table:
    for each in row:
        if each == 'X':
            empty_index_list.append(idx)
        elif each == 'T':
            teacher_index_list.append(idx)

        idx += 1

for i in itertools.combinations(empty_index_list, 3):
    print(i)

for i in itertools.combinations(empty_index_list, 3):
    exp = copy.deepcopy(table)
    answer = True

    for each in i:
        num_row = each // num_input
        num_col = each % num_input

        exp[num_row][num_col] = 'O'

    for each in teacher_index_list:
        num_row = each // num_input
        num_col = each % num_input

        left, right = num_row, num_row
        up, down = num_col, num_col

        while left > 0:
            left -= 1
            if exp[left][num_col] == 'O':
                break
            elif exp[left][num_col] == 'S':
                answer = False
                break

        while right < num_input-1 and answer:
            right += 1
            if exp[right][num_col] == 'O':
                break
            elif exp[right][num_col] == 'S':
                answer = False
                break

        while up > 0 and answer:
            up -= 1
            if exp[num_row][up] == 'O':
                break
            elif exp[num_row][up] == 'S':
                answer = False
                break

        while down < num_input-1 and answer:
            down += 1
            if exp[num_row][down] == 'O':
                break
            elif exp[num_row][down] == 'S':
                answer = False
                break

        if not answer:
            break

    if answer:
        break

outputs = 'YES' if answer else 'NO'
print(outputs)
