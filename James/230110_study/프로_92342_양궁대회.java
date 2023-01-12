import java.util.*;

class Solution {
    static int[] lionInfo;
    static int maxValue = Integer.MIN_VALUE;
    static int[] finalLionInfo = {-1};
    
    public void dfs(int[] info, int arrowCnt, int n) {
        if(arrowCnt == n) {
            int apeachScore = 0;
            int lionScore = 0;
            
            for(int i = 0; i <= 10; i++) {
                if(info[i] != 0 || lionInfo[i] != 0) {
                    if(info[i] < lionInfo[i])
                        lionScore += 10 - i;
                    
                    else
                        apeachScore += 10 - i;   
                }
            }
            
            if(lionScore > apeachScore) {
                if(lionScore - apeachScore >= maxValue) {
                    finalLionInfo = lionInfo.clone();
                    maxValue = lionScore - apeachScore;
                }
            }
            
            return;
        }
        
        for(int i = 0; i <= 10; i++) {
            if(lionInfo[i] <= info[i]) {
                lionInfo[i]++;
                dfs(info, arrowCnt + 1, n);
                lionInfo[i]--;
            }
            
            else
                break;
        }
    }
    
    public int[] solution(int n, int[] info) {
        lionInfo = new int[11];
        
        dfs(info, 0, n);
        //System.out.println(Arrays.toString(finalLionInfo));
        
        return finalLionInfo;
    }
}
