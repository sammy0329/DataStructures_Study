import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> quantity = new HashMap<>();
        
        for(int i = 0; i < number.length; i++) {
            quantity.put(want[i], number[i]);
        }
        
        for(int i = 0; i < discount.length - 9; i++) {
            Map<String, Integer> countMap = new HashMap<>();
            
            for(int j = 0; j < 10; j++) {
                countMap.put(discount[i + j], countMap.getOrDefault(discount[i + j], 0) + 1);   
            }
            
            boolean flag = true;
            
            for(String key : quantity.keySet()) {
                if(quantity.get(key) != countMap.get(key)) {
                    flag = false;
                    break;
                } 
            }
            
            answer += flag ? 1 : 0; 
        }
        
        return answer;
    }
}
