from collections import deque

def solution(n):
    answer = ''
    
    queue = deque([])
    while n:
        
        if (n % 3) == 0:
            queue.appendleft(str(4))
            n = n // 3 -1
        else:
            queue.appendleft(str(n%3))
            n = n // 3

    answer = str("".join(list(queue)))
    
    return answer