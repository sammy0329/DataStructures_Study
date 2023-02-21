import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int index = 0;
        int max;
        int numberLength = number.length() - k;
        
        for(int i = 0; i < numberLength; i++) {
            max = 0;
            for(int j = index; j < k + i + 1; j++) {
                if(max < number.charAt(j) - '0') {
                    max = number.charAt(j) - '0';
                    index = j + 1;
                }
            }
            sb.append(max);
            // System.out.println(sb.toString());
        }
        
        answer = sb.toString();
        
        return answer;
    }
}
