import java.util.*;

class Solution {
    static int n, m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    static class Result {
        boolean win;
        int moveCnt;
        
        public Result(boolean win, int moveCnt) {
            this.win = win;
            this.moveCnt = moveCnt;
        }
    }
    
    public Result dfs(int[][] board, int ax, int ay, int bx, int by, int aDepth, int bDepth) {
        boolean win = false;
        int winCnt = 5 * 5;
        int loseCnt = aDepth + bDepth;
        
        // A 움직임
        if(aDepth == bDepth && board[ax][ay] == 1) {
            for(int i = 0; i < 4; i++) {
                int nx = ax + dx[i];
                int ny = ay + dy[i];
                
                if(!isMovePossible(board, nx, ny))
                    continue;
                
                board[ax][ay] = 0;
                Result r = dfs(board, nx, ny, bx, by, aDepth + 1, bDepth);
                win |= !r.win;
                
                if(r.win)
                    loseCnt = Math.max(loseCnt, r.moveCnt);
                
                else
                    winCnt = Math.min(winCnt, r.moveCnt);
                
                board[ax][ay] = 1;
            }
        }
        
        // B 움직임
        else if(aDepth > bDepth && board[bx][by] == 1) {
            for(int i = 0; i < 4; i++) {
                int nx = bx + dx[i];
                int ny = by + dy[i];
                
                if(!isMovePossible(board, nx, ny))
                    continue;
                
                board[bx][by] = 0;
                Result r = dfs(board, ax, ay, nx, ny, aDepth, bDepth + 1);
                win |= !r.win;
                
                if(r.win)
                    loseCnt = Math.max(loseCnt, r.moveCnt);
                
                else
                    winCnt = Math.min(winCnt, r.moveCnt);
                
                board[bx][by] = 1;
            }
        }
        
        return new Result(win, win ? winCnt : loseCnt);
    }
    
    public boolean isMovePossible(int[][] board, int nx, int ny) {
        if(nx < 0 || ny < 0 || nx >= n || ny >= m || board[nx][ny] == 0) {
            return false;
        } else {
            return true;
        }
    }
    
    public int solution(int[][] board, int[] aloc, int[] bloc) {
        n = board.length;
        m = board[0].length;
        
        return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1], 0, 0).moveCnt;        
    }
}
