import java.util.*;

class Solution {
    static Map<String, List<Integer>> map = new HashMap<>();
    
    public static void dfs(String[] data, String text, int cnt) {
        if(cnt == 4) {
            if(!map.containsKey(text)) {
                List<Integer> list = new ArrayList<>();
                map.put(text, list);
            }
            
            int score = Integer.parseInt(data[4]);
            map.get(text).add(score);
            return;
        }
        
        dfs(data, text + "-", cnt + 1);
        dfs(data, text + data[cnt], cnt + 1);
    }
    
    public static int binarySearch(String key, int score) {
        List<Integer> list = map.get(key);
        int start = 0;
        int end = list.size() - 1;
        
        while(start <= end) {
            int mid = (start + end) / 2;
            
            if(list.get(mid) < score) {
                start = mid + 1;
            }
            
            else {
                end = mid - 1;
            }
        }
        
        // 전체 점수 리스트의 갯수에서 score보다 작은 index(start)를 빼주면 score 이상의 점수 갯수가 됨. 
        return list.size() - start;
    }
    
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        
        for(int i = 0; i < info.length; i++) {
            String[] data = info[i].split(" ");
            dfs(data, "", 0);
        }
        
        // System.out.println(map.toString());
        
        for(String key : map.keySet()) {
            Collections.sort(map.get(key));
        }
        
        for(int i = 0; i < query.length; i++) {
            query[i] = query[i].replaceAll(" and ", "");
            String[] queryData = query[i].split(" ");
            
            if(map.containsKey(queryData[0])) {
                answer[i] = binarySearch(queryData[0], Integer.parseInt(queryData[1]));
            }
        }
    
        // System.out.println(Arrays.toString(query));
        
        return answer;
    }
}
