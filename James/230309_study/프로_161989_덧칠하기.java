import java.util.*;

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int data = 1;
        
        for(int s : section) {
            if(data <= s) {
                answer++;
                data = s + m;
            }
        }
        
        return answer;
    }
}
