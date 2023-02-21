import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        if(n > s) {
            return new int[] {-1};
        }
        
        int[] answer = new int[n];
        int quota = s / n;
        int remain = s % n;
        
        for(int i = 0; i < n; i++) {
            answer[i] = quota;
        }
        
        for(int i = 0; i < remain; i++) {
            answer[i]++;
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}
