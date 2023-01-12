import java.util.*;

class Solution {
    public boolean primeNumber(long number) {
        if(number == 2)
            return true;
        
        for(int i = 2; i <= Math.sqrt(number); i++) {
            if(number % i == 0)
                return false;
        }
        
        return true;
    }
    
    public int solution(int n, int k) {
        int answer = -1;
        Integer.toBinaryString(n);
        String changedNum = Integer.toString(n, k);
        String[] changedNumArray = changedNum.split("0");
        //System.out.println(Arrays.toString(changedNumArray));
        int cnt = 0;
        
        for(String s : changedNumArray) {
            if(s.equals("") || s.equals("1"))
                continue;
            
            long number = Long.parseLong(s);
            
            if(primeNumber(number))
                cnt++;
        }
        
        //System.out.println(cnt);
        
        answer = cnt;
        return answer;
    }
}
