def solution(bridge_length, weight, truck_weights):
    time_count = 0
    idx = 0
    bridge_weight = 0
    bridge_time_count = [0 for _ in range(len(truck_weights))]

    while True:
        if bridge_weight + truck_weights[idx] <= weight:
            idx += 1

    return time_count


if __name__ == '__main__':
    # solution(2, 10, [7, 4, 5, 6])
    print(solution(2, 10, [7, 4, 5, 6]))
