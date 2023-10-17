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