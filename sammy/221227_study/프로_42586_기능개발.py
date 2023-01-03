import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    last=deque() # 남은 기간 표시
    
    for idx,value in enumerate(progresses):
        # 올림을 적용하여 last 배열에 남은 기간 표시
        last.append(math.ceil((100-value)/speeds[idx])) 
    
    while last:
        data=last.popleft() # 왼쪽부터 pop
        cnt=1
        
        if last:
            while data>=last[0]: # pop한 data 크기보다 작은 값들은 pop 해주고, cnt+1
                last.popleft()
                cnt+=1
                if len(last)==0: break # last 배열이 비워지면 break
        
        answer.append(cnt)
             
    return answer

# print(solution([93, 30, 55],[1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))