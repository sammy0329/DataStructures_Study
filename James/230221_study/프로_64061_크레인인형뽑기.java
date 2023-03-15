import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack[] stackArr = new Stack[board[0].length];
        Stack<Integer> stack = new Stack<>();
        
        for(int i = 0; i < board[0].length; i++) {
            stackArr[i] = new Stack<>();   
        }

        for(int i = board.length - 1; i >= 0; i--){
            for(int j = 0; j < board[0].length; j++)
                if(board[i][j] != 0)
                    stackArr[j].push(board[i][j]);
        }
        
        // System.out.println(Arrays.toString(stackArr));

        for(int i = 0; i < moves.length; i++) {
            int index = moves[i] - 1;
            
            if(stackArr[index].empty())
                continue;
            
            int data = (int)stackArr[index].pop();
            
            if(stack.isEmpty())
                stack.push(data);
            
            else{
                if(data == stack.peek()) {
                    answer += 2;
                    stack.pop();
                }
                
                else
                    stack.push(data);
            }
        }
        return answer;
    }
}
