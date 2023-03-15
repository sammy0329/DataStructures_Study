import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[] array;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    
    public static void dfs(int n, int m, int cnt) {
        if(cnt == m) {
            for(int i : array) {
                sb.append(i + " ");
            }

            sb.append("\n");
            return;
        }

        for (int i = 0; i < n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                array[cnt] = i + 1;
                dfs(n, m, cnt + 1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        array = new int[m];
        visited = new boolean[n];

        dfs(n, m, 0);

        System.out.println(sb.toString());
    }
}
