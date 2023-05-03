import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int lastEnd = 0;
        
        Arrays.sort(targets, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];        
            }
        });
                
        for(int i = 0; i < targets.length; i++) {
            int start = targets[i][0];
            int end = targets[i][1];
            
            if(start >= lastEnd) {
                answer++;
                lastEnd = end; 
            }          
        }
        
        return answer;
    }
}
