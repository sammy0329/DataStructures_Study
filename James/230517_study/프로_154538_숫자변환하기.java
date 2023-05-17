/*dp 풀이*/
import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] dp = new int[y + 1];
        int max = Integer.MAX_VALUE;
        
        for(int i = x + 1; i <= y; i++) {
            int a = 0, b = 0, c = 0, d = 0;
            
            if(i / 2 > 0 && i % 2 == 0 && x <= i / 2)
                a = dp[i / 2];
            else
                a = max;
            
            if(i / 3 > 0 && i % 3 == 0 && x <= i / 3)
                b = dp[i / 3];
            
            else
                b = max;
            
            if(x <= i - n)
                c = dp[i - n];
            
            else
                c = max;
            
            d = Math.min(a, Math.min(b, c));
            
            dp[i] = d < max ? d + 1 : max;
        }
                
        return dp[y] < max ? dp[y] : -1;
    }
}

/* bfs 풀이 */
class Solution {
    public int bfs(HashSet<Integer> hs, Queue<Integer> queue, int x, int y, int n) {
        int cnt = 0;
        queue.add(x);
        
        while(!queue.isEmpty()) {
            int size = queue.size();
            
            for(int i = 0; i < size; i++) {
                int data = queue.poll();
                
                if(data == y) {
                    return cnt;
                }
                
                if(data * 2 <= y && !hs.contains(data * 2)) {
                    hs.add(data * 2);
                    queue.add(data * 2);
                } 
                
                if(data * 3 <= y && !hs.contains(data * 3)) {
                    hs.add(data * 3);
                    queue.add(data * 3);
                } 
                
                if(data + n <= y && !hs.contains(data + n)) {
                    hs.add(data + n);
                    queue.add(data + n);
                }
            }
            
            cnt++;
        }
        
        return -1;
    }
    
    public int solution(int x, int y, int n) {
        int answer;
        HashSet<Integer> hs = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        
        answer = bfs(hs, queue, x, y, n);
        
        return answer;
    }
}
