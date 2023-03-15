#stack 개념 사용
from collections import deque
import sys

def solution(string):
    q=deque()

    
    answer=True
    for check in string:
        if check=='(':
            q.append(check)
        elif check==')':
            if q:
                q.pop()
            else:
                answer=False
                return answer

    if q:
        answer=False
        return answer
    else:
        return answer
    
print(solution(sys.stdin.readline()))