import java.util.*;

class Solution {
    
    static Map<String, Integer> map;
    
    public static void combination(String order, StringBuilder sb, int start, int cnt, int courseCnt) {
        if(cnt == courseCnt) {
            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
            return;
        }
        
        for(int i = start; i < order.length(); i++) {
            sb.append(order.charAt(i));
            combination(order, sb, i + 1, cnt + 1, courseCnt);
            sb.delete(cnt, cnt + 1);
        }
    }
    
    public String[] solution(String[] orders, int[] course) {
        ArrayList<String> answer = new ArrayList<>();
        
        for(int i = 0; i < orders.length; i++) {
            char[] charArr = orders[i].toCharArray();
            
            Arrays.sort(charArr);
            orders[i] = String.valueOf(charArr);
        }
        
        // System.out.println(Arrays.toString(orders));
        
        for(int i = 0; i < course.length; i++) {
            map = new HashMap<>();
            int max = Integer.MIN_VALUE;
            
            for(int j = 0; j < orders.length; j++) {
                StringBuilder sb = new StringBuilder();
                
                if(course[i] <= orders[j].length()) {
                    combination(orders[j], sb, 0, 0, course[i]);
                }
            }
            
            for(Map.Entry<String, Integer> entry : map.entrySet()) {
                max = Math.max(max, entry.getValue());
            }
            
            for(Map.Entry<String, Integer> entry : map.entrySet()) {
                if(max >= 2 && entry.getValue() == max) {
                    answer.add(entry.getKey());
                }
            }
        }
        
        Collections.sort(answer);
        
        return answer.stream().toArray(String[]::new);
    }
}
