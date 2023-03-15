import sys
from stack import Stack

num_command, num_prat = map(int, input().split())

prat_stacks = [Stack() for _ in range(num_prat)]
num_count = 0

for _ in range(num_command):
    line, prat = map(int, sys.stdin.readline().strip().split())
    line = line - 1

    stack = prat_stacks[line]

    if stack.get_size() == 0:
        stack.push(prat)
        num_count += 1

    elif stack.top() < prat:
        stack.push(prat)
        num_count += 1

    elif stack.top() == prat:
        pass

    elif stack.top() > prat:
        for _ in range(stack.get_size()):
            stack.pop()
            num_count += 1

            if stack.top() > prat:
                continue

            elif stack.top() == prat:
                break

            elif stack.top() < prat:
                stack.push(prat)
                num_count += 1
                break

        else:
            stack.push(prat)
            num_count += 1

print(num_count)
