# 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주.
from collections import deque

def solution(queue1, queue2):
    answer = 0
    n=len(queue1)
    
    # popleft를 위해 deque 사용
    queue1=deque(queue1)
    queue2=deque(queue2)

    # 두 개의 queue 합 구하기
    sum_q1=sum(queue1)
    sum_q2=sum(queue2)
    
    while sum_q1!=sum_q2: # 두 개의 queue 합이 같지 않다면 반복

        if answer > n*2+1: # 큐가 원상복귀 된다는 것은 같게 만들지 못한다는 것
            return -1
        
        if sum_q1>sum_q2: # q1의 합이 크면 q1 값 popleft 후 q2에 넣어주기
            if queue1: 
                data=queue1.popleft()
                sum_q1-=data
                sum_q2+=data      
                queue2.append(data)
                answer+=1
            
        else:
            if queue2: # q2의 합이 크면 q2 값 popleft 후 q1에 넣어주기
                data=queue2.popleft()
                sum_q1+=data  
                sum_q2-=data    
                queue1.append(data)
                answer+=1
        # print(queue1,queue2)
    
    return answer

# print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
# print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
# print(solution([1, 1],[1, 5]))