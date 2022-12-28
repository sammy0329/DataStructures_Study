import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    last=deque()
    for idx,value in enumerate(progresses):
        last.append(math.ceil((100-value)/speeds[idx]))
    
    while last:
        data=last.popleft()
        cnt=1
        
        if last:
            while data>=last[0]:
                last.popleft()
                cnt+=1
                if len(last)==0: break
        
        answer.append(cnt)
        
        
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))