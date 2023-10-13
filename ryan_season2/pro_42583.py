"""
다리를 지나는 트럭

bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]

bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time_now = 0

    weight_now = 0
    on_bridge = deque([])
    standby = deque(truck_weights)

    while on_bridge or standby:
        time_now += 1

        if on_bridge:
            if on_bridge[0][0] == time_now:
                dest_time, truck_weight = on_bridge.popleft()
                weight_now -= truck_weight

        if standby:
            if len(on_bridge) < bridge_length and weight_now + standby[0] <= weight:
                truck_weight = standby.popleft()
                dest_time = time_now + bridge_length

                on_bridge.append((dest_time, truck_weight))
                weight_now += truck_weight

    return time_now


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

