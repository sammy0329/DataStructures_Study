import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = -2;
        Queue<Integer> firstQueue = new LinkedList<>();
        Queue<Integer> secondQueue = new LinkedList<>();
        long firstQueueSum = 0, secondQueueSum = 0;
        long halfTotal;
        int maxCount = queue1.length * 3;
        int count = 0;
        
        for(int i = 0; i < queue1.length; i++) {
            firstQueue.add(queue1[i]);
            secondQueue.add(queue2[i]);
            firstQueueSum += queue1[i];
            secondQueueSum += queue2[i];
        }
        
        halfTotal = (firstQueueSum + secondQueueSum) / 2;
        
        while(firstQueueSum != halfTotal) {
             if(maxCount < 0) {
                break;
            }
            
            if(firstQueueSum > halfTotal) {
                int firstQueueData = firstQueue.poll();
                secondQueue.add(firstQueueData);
                firstQueueSum -= firstQueueData;
            }
            
            else if(firstQueueSum < halfTotal) {
                int secondQueueData = secondQueue.poll();
                firstQueue.add(secondQueueData);
                firstQueueSum += secondQueueData;
            }
            
            count++;
            maxCount--;
        }
        
        if(maxCount < 0) {
            return -1;
        }
        
        else {
            answer = count;
            return answer;
        }
    }
}
