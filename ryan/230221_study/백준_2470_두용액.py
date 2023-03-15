def solution(info):
    info.sort()

    ph_min = 2000000000

    idx_front = 0
    idx_end = len(info)-1
    best = [idx_front, idx_end]

    while idx_front < idx_end:
        ph_now = info[idx_front] + info[idx_end]

        if abs(ph_now) < ph_min:
            ph_min = abs(ph_now)
            best = [info[idx_front], info[idx_end]]

        if ph_now == 0:
            best = [info[idx_front], info[idx_end]]
            break

        elif ph_now > 0: idx_end -= 1
        else: idx_front += 1

    return best


N = int(input())
info = list(map(int, input().split()))

result = solution(info)
print(f'{result[0]} {result[1]}')