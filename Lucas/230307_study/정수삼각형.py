def solution(triangle):
    
    dp = [[0 for j in range(i+1)]for i in range(len(triangle))]
    dp[0] = triangle[0]
    
    for i in range(0,len(triangle)-1):
        
        for j in range(len(triangle[i])):

            if dp[i+1][j] < dp[i][j] + triangle[i+1][j]:
                
                dp[i+1][j] = dp[i][j] + triangle[i+1][j]
                
            if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]:
                
                dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
        
    return max(dp[len(triangle)-1])