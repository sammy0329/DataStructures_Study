"""
소수 찾기

"17"	3
"011"	2
"""

# Posting
# https://maramarathon.tistory.com/39
# https://velog.io/@mmy789/Algorithm-%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98-%EC%B2%B4
# 에라토스테네스의 체(고정) vs 일반(유동)
# 에라토스테네스: n까지 일괄, n 이하 수들 모두 판별, 메모리 많이 사용, 판별 대상이 많은 경우
# 일반: 단일 숫자에 대해서만, 판별 많이 하지 않는 경우 (이번 케이스)
# 판별 대상의 수에 따라 다르다!

# from itertools import permutations
#
#
# def solution(numbers):
#     lim = 10**(len(numbers))
#     prime_numbers = [True for _ in range(lim)]
#
#     for idx, each in enumerate(prime_numbers):
#         if idx <= 1:
#             prime_numbers[idx] = False
#             continue
#
#         mul = 2
#         while prime_numbers[idx] and idx * mul < lim:
#             prime_numbers[idx*mul] = False
#             mul += 1
#
#     sample = []
#     for num_pick in range(1, len(numbers)+1):
#         for each in permutations(numbers, num_pick):
#             str_idx = ''
#             for e in each:
#                 str_idx += e
#             sample.append(int(str_idx))
#
#     answer = 0
#     for idx in set(sample):
#         if prime_numbers[idx]:
#             answer += 1
#
#     return answer


from itertools import permutations


def isPrime(x):
    if x < 2:
        return False

    else:
        for each in range(2, int((x ** 0.5)) + 1):
            if x % each == 0:
                return False

        else:
            return True


def solution(numbers):
    sample = []

    for num_pick in range(1, len(numbers)+1):
        for each in permutations(numbers, num_pick):
            str_idx = ''.join(each)
            sample.append(int(str_idx))

    answer = 0
    for idx in set(sample):
        if isPrime(idx):
            answer += 1

    return answer


print(solution('17'))
print(solution('011'))
