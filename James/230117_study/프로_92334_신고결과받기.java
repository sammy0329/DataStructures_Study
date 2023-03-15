import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> userMap = new HashMap<>();
        Map<String, Integer> countMap = new HashMap<>();
        
        for(int i = 0; i < id_list.length; i++) {
            countMap.put(id_list[i], 0);
        }
        
        for(int i = 0; i < report.length; i++) {
            String key = report[i].split(" ")[0];
            String value = report[i].split(" ")[1];
            
            if(userMap.get(key) == null) {
                userMap.put(key, new HashSet<>());
                userMap.get(key).add(value);
                countMap.put(value, countMap.get(value) + 1);
            }
            
            else {
                if(userMap.get(key).contains(value)) {
                    userMap.get(key).add(value);
                    countMap.put(value, countMap.get(value));
                }
                
                else {
                    userMap.get(key).add(value);
                    countMap.put(value, countMap.get(value) + 1);   
                }
            }
        }
        
        // System.out.println(userMap.toString());
        // System.out.println(countMap.toString());
        
        for(String key : countMap.keySet()) {
            int count = countMap.get(key);
            
            if(count >= k) {
                for(int i = 0; i < id_list.length; i++) {
                    if(userMap.containsKey(id_list[i]) && userMap.get(id_list[i]).contains(key))
                        answer[i]++;
                }
            }
        }
        
        return answer;
    }
}
