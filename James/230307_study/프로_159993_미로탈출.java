import java.util.*;

class Solution {
    
    static int xLen, yLen; 
    static int[] sArray = new int[2];
    static int[] lArray = new int[2];
    static int[] eArray = new int[2];
    static char[][] graph;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    static class Node{
        int x, y, cnt; 
        public Node(int x, int y, int cnt) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
    
    public static int bfs1(int x, int y) {
        Queue<Node> queue = new LinkedList<>(); 
        queue.offer(new Node(x, y, 0)); 
        visited[x][y] = true;

        while(!queue.isEmpty()) { 
            Node node = queue.poll(); 
            int a = node.x;
            int b = node.y;
            int cnt = node.cnt;
            
            for(int i = 0; i < 4; i++) {
                int nx = a + dx[i];
                int ny = b + dy[i];

                if(nx < 0 || ny < 0 || nx >= xLen || ny >= yLen) {
                    continue;
                }

                if(graph[nx][ny] == 'X' || visited[nx][ny] == true) {
                    continue;
                }

                if(graph[nx][ny] == 'L') {
                    return cnt + 1;
                }

                queue.offer(new Node(nx, ny, cnt + 1));
                visited[nx][ny] = true; 
            }

        }
        return -1; 
    }

    public static int bfs2(int x, int y) {
        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(x, y, 0));
        visited[x][y] = true;

        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int a = node.x;
            int b = node.y;
            int cnt = node.cnt;
            
            for(int i = 0; i < 4; i++) {
                int nx = a + dx[i];
                int ny = b + dy[i];

                if(nx < 0 || ny < 0 || nx >= xLen || ny >= yLen) {
                    continue;
                }

                if(graph[nx][ny] == 'X' || visited[nx][ny] == true) {
                    continue;
                }

                if(graph[nx][ny] == 'E') {
                    return cnt + 1;
                }

                queue.offer(new Node(nx, ny, cnt + 1));
                visited[nx][ny] = true; 
            }

        }
        return -1; 
    }
    
    public int solution(String[] maps) {
        int answer = 0;
        int toLev = 0;
        int toEnd = 0;
           
        graph = new char[maps.length][];
        
        xLen = maps.length;
        yLen = maps[0].length();
        
        for(int i = 0; i < xLen; i++) {
        	for(int j = 0; j < yLen; j++){
        		graph[i]= maps[i].toCharArray();
        		
        		if(graph[i][j] == 'S') { 
        			sArray[0] = i; sArray[1] = j;
        		} else if(graph[i][j] == 'L') { 
        			lArray[0] = i; lArray[1] = j;
        		} else if(graph[i][j] == 'E') { 
        			eArray[0] = i; eArray[1] = j;
        		}  
        	}
        }
        
        visited = new boolean[xLen][yLen];
        toLev = bfs1(sArray[0], sArray[1]);
        
        visited = new boolean[xLen][yLen]; 
        toEnd = bfs2(lArray[0], lArray[1]);
        
        if(toLev == -1 || toEnd == -1) {
        	return -1;
        }
        
        return toLev + toEnd;
    }
}
