import java.util.*;

class Solution {
    static int[][] distances = {{1, 1}, {3, 2}, {4, 2}, {4, 3}};
    
    public int upperSearch(int target, int[] weights, int start, int end) {
        while(start < end) {
            int mid = (start + end) / 2;
            
            if(target < weights[mid]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        return start;
    }
    
    public int lowerSearch(int target, int[] weights, int start, int end) {
        while(start < end) {
            int mid = (start + end) / 2;
            
            if(target <= weights[mid]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        return start;
    }
    
    public long solution(int[] weights) {
        long answer = 0;
        
        Arrays.sort(weights);
        
        for(int[] distance : distances) {
            for(int i = 0; i < weights.length; i++) {
                int x = weights[i];
                
                if(x * distance[0] % distance[1] != 0)
                    continue;
                
                int y = (distance[0] * x) / distance[1];
                
                int upper = upperSearch(y, weights, i + 1, weights.length);
                int lower = lowerSearch(y, weights, i + 1, upper);
                
                answer += upper - lower;
            }
        }
        
        return answer;
    }
}
