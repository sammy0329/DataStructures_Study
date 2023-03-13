import java.util.*;

class Solution {
    public String solution(int n) {
        String answer = "";
        String[] rules = {"4", "1", "2"};
        int num = n;
        
        while(num > 0) {
            int remain = num % 3;
            num /= 3;
            
            if(remain == 0) {
                num--;
            }
            
            answer = rules[remain] + answer;
        }
        
        return answer;
    }
}
