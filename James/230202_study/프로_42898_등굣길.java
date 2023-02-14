class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n][m];
        int xDistance, yDistance;
        
        if(puddles[0].length > 0) {
            for(int[] puddle : puddles) {
                int row = puddle[1];
                int column = puddle[0];
                dp[row - 1][column - 1] = -1; 
            }
        }
        
        // 행 관련 dp
        for(int i = 1; i < n; i++) {
            if(dp[i][0] == -1 || dp[i - 1][0] == -1)
                dp[i][0] = -1;
            
            else
                dp[i][0] = 1;
        }
        
        // 열 관련 dp
        for(int i = 1; i < m; i++) {
            if(dp[0][i] == -1 || dp[0][i - 1] == -1)
                dp[0][i] = -1;
            
            else
                dp[0][i] = 1;
        }
        
        // 경로 계산
        for(int i = 1; i < n; i++) {
            for(int j = 1; j < m; j++) {
                if(dp[i][j] != -1) {
                    if(dp[i][j - 1] == -1)
                        xDistance = 0;
                    
                    else
                        xDistance = dp[i][j - 1];
                    
                    if(dp[i - 1][j] == -1)
                        yDistance = 0;
                    
                    else
                        yDistance = dp[i - 1][j];
                
                    if(xDistance + yDistance == 0)
                        dp[i][j] = 0;
                    
                    else 
                        dp[i][j] = (xDistance + yDistance) % 1000000007;
                }
                
            }
        }
        
        if(dp[n - 1][m - 1] == -1)
            return -1;
        
        else
            return dp[n - 1][m - 1];
        
    }
}
