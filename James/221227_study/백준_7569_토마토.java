package Day04;

import java.util.*;

public class ex03 {
    static Queue<Node> queue = new LinkedList<>();
    static int h, n, m;
    static int[][][] graph;
  
    static class Node {
        int x, y, z;

        Node(int z, int y, int x) {
            this.x = x; // 가로
            this.y = y; // 세로
            this.z = z; // 높이
        }
    }

    public static int bfs() {
        int result = Integer.MIN_VALUE;
        int[] dx = {1, -1, 0, 0, 0, 0}; // 상하좌우높이(위)높이(아래)
        int[] dy = {0, 0, 1, -1, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};

        while(!queue.isEmpty()) {
            Node data = queue.poll();
            int x = data.x;
            int y = data.y;
            int z = data.z;

            for(int i = 0; i < 6; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];

                if(nx < 0 || ny < 0 || nz < 0 || nx >= m || ny >= n || nz >= h)
                    continue;

                if(graph[nz][ny][nx] == 0) {
                    graph[nz][ny][nx] = graph[z][y][x] + 1;
                    queue.add(new Node(nz, ny, nx));
                }
            }
        }
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < n; j++) {
                for(int k = 0; k < m; k++) {
                    if(graph[i][j][k] == 0) {
                        return -1;
                    }

                    result = Math.max(result, graph[i][j][k]);
                }
            }
        }

        return result - 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        m = sc.nextInt(); // 가로
        n = sc.nextInt(); // 세로
        h = sc.nextInt(); // 높이
        graph = new int[h][n][m];
        int answer = 0;

        for(int i = 0; i < h; i++) {
            for(int j = 0; j < n; j++) {
                for(int k = 0; k < m; k++) {
                    int num = sc.nextInt();
                    graph[i][j][k] = num;

                    if(graph[i][j][k] == 1) {
                        queue.add(new Node(i, j, k)); // 높이 좌표, 세로 좌표, 가로 좌표 add
                    }
                }
            }
        }

        answer = bfs();
        System.out.println(answer);
        //System.out.println(Arrays.deepToString(graph));
    }
}
