"""
n	    k	result
437674	3	3
110011	10	2
"""
def isprime(n):
    if n <= 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False

        i += 1

    return True


def transer(n, k) -> str:
    target = []
    while True:
        t = n % k
        target.append(t)

        if n < k:
            break

        n = n // k

    target.reverse()

    str_target = ''
    for each in target:
        str_target += str(each)

    return str_target


def solution(n, k):
    answer = 0

    n_k = transer(n, k)
    temp = n_k.split('0')

    for p in temp:
        if p == '':
            continue

        if isprime(int(p)):
            answer += 1

    return answer
