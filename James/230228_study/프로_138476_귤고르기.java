import java.util.*;

class Solution {
    static Map<Integer, Integer> map = new TreeMap<>();
    
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        for(int key : tangerine) {
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        
        ArrayList<Integer> al = new ArrayList<>(map.keySet());
        Collections.sort(al, new userComparator());
        
        // System.out.println(al.toString());
        
        for(int key : al) {
            if(k <= 0)
                break;
            
            answer++;
            k -= map.get(key);
        }
        
        return answer;
    }
    
    public class userComparator implements Comparator<Integer> {
        @Override
        public int compare(Integer o1, Integer o2) {
            return map.get(o2).compareTo(map.get(o1)); // 귤의 크기의 개수로 정렬
        }
    } 
}
