def calculate(x, y, more=0):
    z = int(100*(y+more)/(x+more))
    return z

def solution(x, y):
    z = calculate(x, y)

    if z >= 99: return -1

    lo, hi = 0, x
    while True:
        mid = (lo + hi)//2
        stat = calculate(x, y, more=mid)
        if stat > z + 1: hi = mid
        elif stat == z: lo = mid
        else:
            hi = mid
            break
        if lo + 1 == hi:
            return hi

    while True:
        mid = (lo + hi)//2
        if lo + 1 == hi:
            return hi

        if calculate(x, y, mid) == z: lo = mid
        else: hi = mid


x, y = map(int, input().split())
print(solution(x, y))