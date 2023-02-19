import java.util.*;

public class Main {
    static int m, n;
    static boolean[][] visited;
    static int[][] graph;
    static int cnt;

    public static void dfs(int x, int y) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        visited[x][y] = true;

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || ny < 0 || nx >= m || ny >= n) {
                continue;
            }

            if(graph[nx][ny] == 1 && !visited[nx][ny]) {
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i = 0; i < t; i++) {
            m = sc.nextInt();
            n = sc.nextInt();
            int k = sc.nextInt();
            graph = new int[m][n];
            visited = new boolean[m][n];
            cnt = 0;

            for(int j = 0; j < k; j++) {
                int x = sc.nextInt();
                int y = sc.nextInt();  
                graph[x][y] = 1;
            }

//            System.out.println(Arrays.deepToString(graph));
            for(int a = 0; a < m; a++) {
                for(int b = 0; b < n; b++) {
                    if(!visited[a][b] && graph[a][b] == 1) {
                        dfs(a, b);
                        cnt++;
                    }
                }
            }

            System.out.println(cnt);
        }
    }
}
