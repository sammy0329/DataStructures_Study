import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        String answer = "";
        Stack<Integer> history = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int tableSize = n;
        
        for(int i = 0; i < cmd.length; i++) {
            char c = cmd[i].charAt(0);
            
            if(c == 'U') {
                k -= Integer.parseInt(cmd[i].substring(2));
            } else if(c == 'D') {
                k += Integer.parseInt(cmd[i].substring(2));
            } else if(c == 'C') {
                history.add(k);
                tableSize--;
                
                if(tableSize == k)
                    k--;
                
            } else if(c == 'Z') {
                if(history.pop() <= k)
                    k++;
                
                tableSize++;
            }
        }
        
        for(int i = 0; i < tableSize; i++) {
            sb.append('O');
        }
                
        while(!history.isEmpty())
            sb.insert(history.pop().intValue(), 'X');
        
        answer = sb.toString();
        return answer;
    }
}
