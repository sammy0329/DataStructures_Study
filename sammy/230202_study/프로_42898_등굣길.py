def solution(m, n, puddles):
    # 행열 만들기
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)] 
    
    for puddle in puddles:
        dp[puddle[1]][puddle[0]]=0
    
    check=False # 1행, 1열 도중에 puddle이 있는지 확인을 위해
    # 도중에 puddle이 없는한 1로 처리
    for i in range(1,n+1):
        if dp[i][1]==0: check=True
        
        if check: dp[i][1]=0
        else: dp[i][1]=1
        
    check=False # 1행, 1열 도중에 puddle이 있는지 확인을 위해
    # 도중에 puddle이 없는한 1로 처리
    for i in range(1,m+1):
        if dp[1][i]==0: check=True
        
        if check: dp[1][i]=0
        else: dp[1][i]=1

    # 2행 2열부터 왼쪽과 위에 해당하는 값을 더하여 최신화 진행
    for i in range(2,n+1):
        for j in range(2,m+1):
            if dp[i][j]==0: continue
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

    return dp[-1][-1]%1000000007

# print(solution(4,3,[[2, 2]]))

# 프로그래머스 -님이 올리셨던 반례 참고
#https://school.programmers.co.kr/questions/15698?question=15698

# print(solution(2, 2, []), 2)
# print(solution(3, 3, []), 6)
# print(solution(3, 3, [[2, 2]]), 2)
# print(solution(3, 3, [[2, 3]]), 3)
# print(solution(3, 3, [[1, 3]]), 5)
# print(solution(3, 3, [[1, 3], [3, 1]]), 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
# print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
# print(solution(4, 4, [[3, 2], [2, 4]]), 7)
# print(solution(100, 100, []), 690285631)

