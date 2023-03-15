"""
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
[20, 40, 50, 50]    100
"""


def solution(people, limit):
    from collections import deque
    answer = 0

    people.sort()
    deq = deque(people)

    while len(deq) > 0:
        answer += 1
        permit = limit - deq.pop()

        if len(deq) > 0:
            temp = deq.popleft()
            if temp > permit:
                deq.appendleft(temp)

    return answer


# people = [70, 50, 80, 50]
# people = [30, 30, 70, 70]
people = [70, 80, 50]
limit = 100

print(solution(people, limit))
