import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i = 0; i < priorities.length; i++) {
            pq.offer(priorities[i]);
        }
        
        //System.out.println(pq.toString());
        
        while(!pq.isEmpty()) {
            for(int i = 0; i < priorities.length; i++) {
                if(priorities[i] == pq.peek()) {
                    if(i == location) {
                        answer++;
                        return answer;
                    }
                    
                    //System.out.println("뽑은 데이터 : " + pq.poll());
                    answer++;
                    //System.out.println("answer : " + answer);
                }
            }
            //System.out.println("---------");
        }
        return -1;
    }
}
