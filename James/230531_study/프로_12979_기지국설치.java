import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int leftStart = 1;
        
        for(int station : stations) {
            if(leftStart < station - w) {
                int leftEnd = station - w;
                int length = leftEnd - leftStart;
                int cnt = length / (w * 2 + 1);
                
                if(length % (w * 2 + 1) != 0) {
                    cnt++;
                }
                
                answer += cnt;
            }
            
            leftStart = station + w + 1;
        }
        
        if(stations[stations.length - 1] + w + 1 <= n) {
            leftStart = stations[stations.length - 1] + w + 1;
            
            int leftEnd = n + 1;
            int length = leftEnd - leftStart;
            int cnt = length / (w * 2 + 1);
            
            if(length % (w * 2 + 1) != 0) {
                cnt++;
            }
            
            answer += cnt;
        }

        return answer;
    }
}
