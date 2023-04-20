import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        for(int i = 0; i < numbers.length; i++) {
            int number = numbers[i];
            
            while(!pq.isEmpty() && pq.peek()[1] < number) {
                answer[pq.poll()[0]] = number;
            }
            
            pq.add(new int[] {i, number});
        }
        
        while(!pq.isEmpty()) {
            answer[pq.poll()[0]] = -1;   
        }
        
        return answer;
    }
}
