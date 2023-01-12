package Day03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class 백준_1261_알고스팟 {

    static int n, m;
    static int[][] distance;
    public static void bfs(int[][] graph) {
        PriorityQueue<Node> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.weight));
        int[] dy = {1, -1, 0, 0};
        int[] dx = {0, 0, 1, -1};
        distance[0][0] = 0;
        pq.offer(new Node(0, 0, 0));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int y = node.y;
            int x = node.x;
            //int dist = node.weight;

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                int dist = node.weight;

                if (nx < 0 || ny < 0 || nx >= m || ny >= n)
                    continue;

                if (graph[ny][nx] == 1)
                    dist++;

                if (distance[ny][nx] > dist) {
                    distance[ny][nx] = dist;
                    pq.offer(new Node(ny, nx, dist));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        m = Integer.parseInt(input[0]); // 가로
        n = Integer.parseInt(input[1]); // 세로
        int[][] graph = new int[n][m];
        distance = new int[n][m];
        int result = 0;

        for (int i = 0; i < n; i++) {
            String[] data = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.valueOf(data[j]);
                Arrays.fill(distance[i], Integer.MAX_VALUE);
            }
        }

        bfs(graph);
        System.out.println(Arrays.deepToString(distance));
        System.out.println(distance[n - 1][m - 1]);
    }

    static class Node {
        int x, y, weight;
        Node(int y, int x, int weight) {
            this.y = y;
            this.x = x;
            this.weight = weight;
        }
    }
}
