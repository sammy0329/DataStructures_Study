import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        HashSet<String> cache = new HashSet<>(cacheSize);
        Map<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < cities.length; i++) {
            String city = cities[i].toLowerCase();
            
            if(!cache.contains(city) && cache.size() < cacheSize) {
                cache.add(city);
                
                answer += 5;
                map.put(city, i);
            }
            
            else {
                if(!cache.contains(city) && cache.size() >= 1) {
                    String lastKey = "";
                    int value = Integer.MAX_VALUE;
                    Iterator<String> it = cache.iterator();
                    
                    while(it.hasNext()) {
                        String key = it.next();
                        
                        if(map.get(key) < value) {
                            lastKey = key;
                            value = map.get(key);
                        }
                    }
                    
                    cache.remove(lastKey);
                    map.remove(lastKey);
                    cache.add(city);
                    answer += 5;
                }
                
                else if(cache.contains(city)) {
                    answer += 1;
                }
                
                else {
                    answer += 5;
                }
                
                map.put(city, i);
            }
        }
        
        return answer;
    }
}
