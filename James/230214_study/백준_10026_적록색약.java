import java.util.*;

public class Main {
    static int n;
    static int normalCnt = 0;
    static int notNormalCnt = 0;
    static String[][] graph;
    static boolean[][] visited;
    
    public static boolean dfs(int x, int y) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        visited[x][y] = true;
        String color = graph[x][y];

        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= n || ny >= n || nx < 0 || ny < 0)
                continue;

            if(graph[nx][ny].equals(color) && !visited[nx][ny])
                dfs(nx, ny);
        }

        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        graph = new String[n][n];
        visited = new boolean[n][n];

        sc.nextLine();

        for(int i = 0; i < n; i++) {
            String[] data = sc.nextLine().split("");
            graph[i] = data;
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(!visited[i][j]) {
                    dfs(i, j);
                    normalCnt++;
                }
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(graph[i][j].equals("G"))
                    graph[i][j] = "R";
            }
        }

        visited = new boolean[n][n];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(!visited[i][j]) {
                    dfs(i, j);
                    notNormalCnt++;
                }
            }
        }

        System.out.println(normalCnt + " " + notNormalCnt);
    }
}
