import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        ArrayList<Integer> answer = new ArrayList<>();
        int primaryMinute = fees[0]; // 기본 시간(분)
        int primaryFee = fees[1]; // 기본 요금(원)
        int unitMinute = fees[2]; // 단위 시간(분)
        int unitFee = fees[3]; // 단위 요금(원)
        Map<String, Integer> tmpTimeMap = new HashMap<>();
        Map<String, Integer> totalTimeMap = new TreeMap<>();
        int lastTime = 23 * 60 + 59;
        
        for(int i = 0; i < records.length; i++) {
            String[] newRecords = records[i].split(" ");
            String[] time = newRecords[0].split(":");
            int resultTime = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
            String key = newRecords[1];
            int value = resultTime;
            
            if(tmpTimeMap.containsKey(key)) {
                if(totalTimeMap.containsKey(key)) {
                    totalTimeMap.put(key, value
                                     - tmpTimeMap.get(key) + totalTimeMap.get(key));
                }
                
                else {
                    totalTimeMap.put(key, value - tmpTimeMap.get(key));
                }
                tmpTimeMap.remove(key);
            }
            
            else {
                tmpTimeMap.put(key, value);
            }
        }
        
        for(String key : tmpTimeMap.keySet()) {
            if(!totalTimeMap.containsKey(key))
                totalTimeMap.put(key, 0);
                
            totalTimeMap.put(key, totalTimeMap.get(key) + lastTime - tmpTimeMap.get(key));
        }
        
        System.out.println(totalTimeMap.toString());
        
        for(Integer minute : totalTimeMap.values()) {
            if(minute <= primaryMinute) {
                answer.add(primaryFee);
            }
            
            else {
                int result = primaryFee + 
                    (int)Math.ceil((double)(minute - primaryMinute) / unitMinute) * unitFee;
                answer.add(result);
            }       
        }
        
        //System.out.println(answer.toString());
        return answer.stream().mapToInt(Integer::intValue).toArray(); 
    }
}
