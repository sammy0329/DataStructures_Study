import java.util.*;

class Solution {
    static class Node {
        int b, cost;
        
        Node(int b, int cost) {
            this.b = b;
            this.cost = cost;
        }
    }
    
    static ArrayList<ArrayList<Node>> graph = new ArrayList<>();
    static int[] distance;
    
    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.cost, b.cost)); 
        distance[start] = 0;
        pq.add(new Node(start, 0));
        
        while(!pq.isEmpty()) {
            Node data = pq.poll();
            int now = data.b;
            int dist = data.cost;
            
            if(distance[now] < dist)
                continue;
            
            for(Node n : graph.get(now)) {
                int node = n.b;
                int weight = n.cost;
                int cost = dist + weight;
                
                if(distance[node] > cost) {
                    distance[node] = cost;
                    pq.add(new Node(node, cost));
                }
            }
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        distance = new int[N + 1];
        
        for(int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
            distance[i] = Integer.MAX_VALUE;
        }
        
        for(int i = 0; i < road.length; i++) {
            int a = road[i][0];
            int b = road[i][1];
            int c = road[i][2];
            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }
        
        dijkstra(1);
        
        for(int i = 0; i < distance.length; i++) {
            if(distance[i] <= K)
                answer++;
        }
        
        return answer;
    }
}
