import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] arr = new int[number];
        
        for(int i = 1; i <= number; i++) {
            int cnt = 0;
            for(int j = 1; j * j <= i; j++) {
                if(j * j == i)
                    cnt++;
                
                else if(i % j == 0)
                    cnt += 2;
            }
            
            arr[i - 1] = cnt;
        }
        
        // System.out.println(Arrays.toString(arr));
        
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] > limit)
                arr[i] = power;
        }
        
        // System.out.println(Arrays.toString(arr));
        
        for(int i : arr)
            answer += i;
        
        return answer;
    }
}
