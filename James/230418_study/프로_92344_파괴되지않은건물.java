import java.util.*;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        int n = board.length;
        int m = board[0].length;
        int preSum[][] = new int[n + 1][m + 1]; 
        
        for(int i = 0; i < skill.length; i++){
            int type = skill[i][0];
            int r1 = skill[i][1], c1 = skill[i][2];
            int r2 = skill[i][3], c2 = skill[i][4];
            int degree = skill[i][5];
            
            if(type == 1){  //파괴
                preSum[r1][c1] += -degree;
                preSum[r2 + 1][c1] += degree;
                preSum[r1][c2 + 1] += degree;
                preSum[r2 + 1][c2 + 1] += -degree;
            } else{  //복구
                preSum[r1][c1] += degree;
                preSum[r2 + 1][c1] += -degree;
                preSum[r1][c2 + 1] += -degree;
                preSum[r2 + 1][c2 + 1] += degree;
            }
        }
        
        // 가로 누적합 계산
        for(int i = 0; i < n + 1; i++){
            int sum = 0;
            
            for(int j = 0; j < m + 1; j++){
                sum += preSum[i][j];
                preSum[i][j] = sum;
            }
        }
        
        // 세로 누적합 계산        
        for(int i = 0; i < m; i++){
            int sum = 0;
            
            for(int j = 0; j < n; j++){
                sum += preSum[j][i];
                preSum[j][i] = sum;
            }
        }
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(preSum[i][j] + board[i][j] > 0 ) 
                    answer++;
            }
        }                   
        
        return answer;
    }
    
}
