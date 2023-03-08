import java.util.*;

class Solution {
    static Set<HashSet<String>> answer;
    
    public static void dfs(HashSet<String> hs, String[] user_id, String[] banned_id) {
        if(hs.size() == banned_id.length) {
            if(check(hs, banned_id)) {
                answer.add(new HashSet<>(hs));
            }   
            return;
        }
        
        for(int i = 0; i < user_id.length; i++) {
            if(hs.add(user_id[i])) {
                dfs(hs, user_id, banned_id);
                hs.remove(user_id[i]);
            }
        }
    }
    
    public static boolean check(HashSet<String> hs, String[] banned_id) {
        int index = 0;
        
        for(String userId : hs) {
            String banId = banned_id[index++];
            
            if(userId.length() != banId.length())
                return false;
            
            for(int i = 0; i < banId.length(); i++) {
                if(banId.charAt(i) == '*')
                    continue;
                
                if(userId.charAt(i) != banId.charAt(i))
                    return false;
            }
        }
        
        return true;
    }
    
    public int solution(String[] user_id, String[] banned_id) {
        answer = new HashSet<>();
        
        dfs(new LinkedHashSet<>(), user_id, banned_id);
        
        // System.out.println(answer.toString());
        return answer.size();
    }
}
