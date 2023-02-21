def solution(n, s):
    avg = s//n
    remain = s % n

    if avg == 0: return [-1]

    result = [avg for _ in range(n)]

    for idx in range(1, remain+1):
        result[idx*(-1)] += 1

    return result
