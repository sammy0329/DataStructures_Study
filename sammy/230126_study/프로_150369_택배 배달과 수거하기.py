def solution(cap, n, deliveries, pickups):
    # 멀리 있는 곳들의 작업을 먼저 끝내야 이동횟수 최소화 가능하므로 배열을 역으로 뒤집는다.
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    deli_cnt = 0
    pick_cnt = 0
    for i in range(n):
        deli_cnt += deliveries[i]
        pick_cnt += pickups[i]
        
        # deli와 pick 값이 음수이면 오고 가는 길에 배달 혹은 픽업이 가능
        while deli_cnt > 0 or pick_cnt > 0:
            deli_cnt -= cap
            pick_cnt -= cap
            
            # 한번 가면 다시 물류창고로 돌아와야하기 때문에 (n-i)*2 처리
            answer += (n - i) * 2
        
    return answer