from collections import deque

def solution(bridge_length, weight, truck_weights):
    q=deque(truck_weights)
    running=deque([0]*bridge_length)
    time=0
    bridge_weight=0

# 시간복잡도 때문에 sum 사용하지 않고 변수로 처리하자!
    while running:
        time+=1
        data=running.popleft()
        bridge_weight-=data
        
        if q:
            if bridge_weight+q[0]<=weight:
                x=q.popleft()
                running.append(x)                      
                bridge_weight+=x
            else:
                running.append(0)

    return time


print(solution(	100, 100, [10]))
print(solution(	100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(	2, 10, [7, 4, 5, 6]))