import java.util.*;

class Solution {
    static List<Integer> answer = new ArrayList<>();
    static int n, m;
    static boolean[][] visited;
    
    static class Node {
        int x, y;
        
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public static int bfs(String[] maps, int a, int b) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(a, b));
        visited[a][b] = true;
        int cnt = maps[a].charAt(b) - '0';
        
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int x = node.x;
            int y = node.y;
            
            for(int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx < 0 || ny < 0 || nx >= n || ny >= m)
                    continue;
                
                if(maps[nx].charAt(ny) == 'X' || visited[nx][ny])
                    continue;
                
                if(maps[nx].charAt(ny) != 'X' && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    cnt += maps[nx].charAt(ny) - '0';
                    queue.add(new Node(nx, ny));
                }
            }
        }
        
        return cnt;
    }
    
    public int[] solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        
        visited = new boolean[n][m];
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                visited[i][j] = false;
            }
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(!visited[i][j] && maps[i].charAt(j) >= '0' && maps[i].charAt(j) <= '9') {
                    int result = bfs(maps, i, j);
                    answer.add(result);
                }    
            }
        }
        
        if(answer.isEmpty()) {
            return new int[] {-1};
        }
        
        return answer.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}
