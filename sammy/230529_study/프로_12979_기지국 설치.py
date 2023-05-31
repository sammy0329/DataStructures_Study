def solution(n, stations, w):
    answer = 0
    dp=[0 for _ in range(n+1)]

    for s in stations:
        dp[s]=1
        for _ in range(w):
            if s-1>0:
                dp[s-1]=1
            if s+1<n+1:
                dp[s+1]=1

    current_idx=0

    while True:
        if current_idx > n+1: break
        if dp[current_idx]==0:
            answer+=1
            if dp[current_idx + w] == 0:

                current_idx+=2*w
            else:
                for i in range(w,-1,-1):
                    if current_idx+i<n+1 and dp[current_idx + i]==0:
                        current_idx+=i+w
                        answer+=1
                        break

    return answer

print(solution(	11, [4, 11], 1),3)
print(solution(	11, [4, 11], 1))