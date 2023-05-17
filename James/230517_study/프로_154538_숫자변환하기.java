import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] dp = new int[y + 1];
        int max = Integer.MAX_VALUE;
        
        for(int i = x + 1; i <= y; i++) {
            int a = 0, b = 0, c = 0, d = 0;
            
            if(i / 2 > 0 && i % 2 == 0 && x <= i / 2)
                a = dp[i / 2];
            else
                a = max;
            
            if(i / 3 > 0 && i % 3 == 0 && x <= i / 3)
                b = dp[i / 3];
            
            else
                b = max;
            
            if(x <= i - n)
                c = dp[i - n];
            
            else
                c = max;
            
            d = Math.min(a, Math.min(b, c));
            
            dp[i] = d < max ? d + 1 : max;
        }
                
        return dp[y] < max ? dp[y] : -1;
    }
}
