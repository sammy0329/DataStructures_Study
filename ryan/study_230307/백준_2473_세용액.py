def solutioin(n, info):
    now = 3000000000
    for _ in range(n-2):
        fixed = info.pop()

        lo = 0
        hi = len(info) - 1

        while lo < hi:
            now_temp = [info[lo], info[hi], fixed]
            sum_temp = sum(now_temp)

            if abs(sum_temp) < abs(now):
                best = now_temp
                now = sum_temp

            if sum_temp > 0: hi -= 1
            elif sum_temp < 0: lo += 1
            else:
                best = now_temp
                best.sort()

                return best

    best.sort()

    return best


n = int(input())
info_original = list(map(int, input().split()))
info_original.sort()

answer = solutioin(n, info_original)
for each in answer:
    print(each, end=' ')
