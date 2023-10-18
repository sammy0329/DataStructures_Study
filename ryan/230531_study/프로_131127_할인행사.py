"""
할인행사

1 ≤ want의 길이 = number의 길이 ≤ 10
1 ≤ number의 원소 ≤ 10
number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.
10 ≤ discount의 길이 ≤ 100,000
want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12

want	number	discount	result
["banana", "apple", "rice", "pork", "pot"]	[3, 2, 2, 2, 1]	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	3
["apple"]	[10]	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]    0
"""
from collections import deque, defaultdict


def isPossible(target, que):
    info = defaultdict(int)

    for each in que:
        info[each] += 1

    for k, v in target.items():
        if v != info[k]:
            return False

    else:
        return True


def solution(want, number, discount):
    answer = 0

    target = {k:v for k, v in zip(want, number)}
    que = deque()

    for each in discount:
        que.append(each)

        if len(que) > 10:
            que.popleft()

        if isPossible(target, que):
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
