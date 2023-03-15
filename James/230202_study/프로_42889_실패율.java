import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[] failPlayerArray = new double[N + 1];
        double player = stages.length;
        ArrayList<Double> failAl = new ArrayList<>();
        
        for(int i = 0; i < stages.length; i++) {
            if(stages[i] == N + 1)
                continue;
            
            failPlayerArray[stages[i]]++;
        }
        
        for(int i = 1; i < failPlayerArray.length; i++) {
            double failPlayer = failPlayerArray[i];
            double failRate = 0.0;
            
            if(player == 0)
                failRate = 0.0;
            
            else {
                failPlayerArray[i] = (double)failPlayer / player;
                player -= failPlayer;
            }
            failAl.add(failPlayerArray[i]);
        }
        
        Collections.sort(failAl, Collections.reverseOrder());
//         System.out.println(failAl.toString()); // 실패율 - 정렬
//         System.out.println(Arrays.toString(failPlayerArray)); // 실패율 - 스테이지순
        
        for(int i = 0; i < failAl.size(); i++) {
            for(int j = 1; j < failPlayerArray.length; j++) {
                if(failAl.get(i) == failPlayerArray[j]) {
                    answer[i] = j;
                    failPlayerArray[j] = -1;
                    break;
                }
            }
        }
        
        return answer;
    }
}
