import java.util.*;

class Solution {
    static int answer = 0;
    static boolean[] visited;
    
    public static void dfs(String begin, String target, String[] words, int idx) {
        if(begin.equals(target)) {
            answer = idx;
            return;
        }
        
        for(int i = 0; i < words.length; i++) {
            if(visited[i])
                continue;
            
            if(isPossible(begin, words[i])) {
                visited[i] = true;
                dfs(words[i], target, words, idx + 1);
                visited[i] = false;
            }
        }
        
    }
    
    public static boolean isPossible(String begin, String word) {
        int wordDifferenceCnt = 0;
            
        for(int i = 0; i < begin.length(); i++) {
            if(begin.charAt(i) != word.charAt(i))
                wordDifferenceCnt++;
        }
        
        if(wordDifferenceCnt == 1)
            return true;
        
        else
            return false;
    }
     
    public int solution(String begin, String target, String[] words) {
        int cnt = 0;
        visited = new boolean[words.length];
        dfs(begin, target, words, 0);
        
        return answer;
    }
}
