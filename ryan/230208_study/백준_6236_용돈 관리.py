import sys


def isPos(draw, history, unit):
    count = 1
    balance = unit
    for each in history:
        if balance >= each: balance -= each
        else:
            balance = unit - each
            count += 1

        if count > draw:
            return False

    return True


def solution(draw, history):
    ceil = sum(history)  # isPos > True
    floor = max(history)-1  # isPos > False
    while True:
        mid = (ceil + floor) // 2
        if isPos(draw=draw, history=history, unit=mid): ceil = mid
        else: floor = mid

        if floor + 1 == ceil: break

    return ceil


numDay, draw = map(int, input().split())
history = []

for _ in range(numDay):
    each = sys.stdin.readline().strip()
    history.append(int(each))

print(solution(draw=draw, history=history))