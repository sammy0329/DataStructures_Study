import java.util.*;

class Solution {
    public boolean game(String target, String[][] graph) {
        for(int i = 0; i < 3; i++) {
            if(graph[i][0].equals(target) && graph[i][1].equals(target) && graph[i][2].equals(target)) {
                return true;
            }
        }
        
        for(int i = 0; i < 3; i++) {
            if(graph[0][i].equals(target) && graph[1][i].equals(target) && graph[2][i].equals(target)) {
                return true;
            }
        }
        
        if(graph[0][0].equals(target) && graph[1][1].equals(target) && graph[2][2].equals(target))
            return true;
        
        if(graph[0][2].equals(target) && graph[1][1].equals(target) && graph[2][0].equals(target))
            return true;
        
        return false;
    }
    
    public int solution(String[] board) {
        String[][] graph = new String[3][3];
        int xCnt = 0;
        int oCnt = 0;
        
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board.length; j++) {
                graph[i][j] = String.valueOf(board[i].charAt(j));
                
                if(graph[i][j].equals("O"))
                    oCnt++;
                
                if(graph[i][j].equals("X"))
                    xCnt++;
            }
        }
        
        System.out.println(oCnt + " " + xCnt);
        
        if(oCnt < xCnt || oCnt - xCnt > 1)
            return 0;
        
        boolean oWin = game("O", graph);
        boolean xWin = game("X", graph);
        
        if(oWin && oCnt != xCnt + 1) {
            return 0;
        }
        
        if(xWin && oCnt != xCnt) {
            return 0;
        }
        
        return 1;
    }
}
