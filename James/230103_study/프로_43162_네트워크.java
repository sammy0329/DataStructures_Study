import java.util.*;

class Solution {
    public static void bfs(int i, int[][] computers, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        
        queue.add(i);
        visited[i] = true;
        
        while(!queue.isEmpty()) {
            int popIndex = queue.poll();
            for(int j = 0; j < computers.length; j++) {
                if(popIndex != j && visited[j] == false && computers[popIndex][j] == 1) {
                    visited[j] = true;
                    queue.add(j);
                }
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for(int i = 0; i < computers.length; i++) {
            if(visited[i] == false) {
                bfs(i, computers, visited);
                answer++;   
            }
        }
        
        return answer;
    }
}
