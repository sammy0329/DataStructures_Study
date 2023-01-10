import java.util.*;

class Solution {
    public static int[] solution(String[][] places) {
        int[] answer = new int[5];

        for (int i = 0; i < places.length; i++) {
            String[] graph = places[i];
            boolean flag = true;
            
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < 5; k++) {
                    if (graph[j].charAt(k) == 'P') {
                        if (!bfs(graph, j, k))
                            flag = false;
                    }
                }
            }
            
            if(flag)
                answer[i] = 1;
            
            else
                answer[i] = 0;
        }

        return answer;
    }

    private static boolean bfs(String[] graph, int a, int b) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(a, b));

        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int x = node.x;
            int y = node.y;
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int distance = Math.abs(nx - a) + Math.abs(ny - b);
                
                if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5 || (nx == a && ny == b))
                    continue;
                
                if(graph[nx].charAt(ny) == 'X')
                    continue;
                
                if (graph[nx].charAt(ny) == 'P' && distance <= 2)
                    return false;
                
                if (graph[nx].charAt(ny) == 'O' && distance < 2)
                    queue.add(new Node(nx, ny));
            }
        }

        return true;
    }
    
    static class Node {
        int x, y;
        
        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
