import java.util.*;

class Solution {
    static char[][] map;
    static boolean[][] visited;
    
    public int checkBlock(int i, int j) {
        char target = map[i][j];
        
        if(target != '0' && target == map[i][j] && target == map[i + 1][j] && target == map[i][j + 1] && target == map[i + 1][j + 1]) {
            visited[i][j] = true;
            visited[i + 1][j] = true;
            visited[i][j + 1] = true;
            visited[i + 1][j + 1] = true;
            
            return 1;
        }
        
        return 0;
    }
    
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        int flag = 0;
        map = new char[m][n];
        
        for(int i = 0; i < m; i++) {
            map[i] = board[i].toCharArray();
        }
        
        //System.out.println(Arrays.deepToString(map));
        
        while(true) {
            flag = 0;
            visited = new boolean[m][n];
            
            for(int i = 0; i < m - 1; i++) {
                for(int j = 0; j < n - 1; j++) {
                    flag += checkBlock(i, j);
                }
            }
            
            if(flag == 0)
                break;
            
            for(int j = 0; j < n; j++) {
                ArrayList<Character> list = new ArrayList<>();
                
                for(int i = m - 1; i >= 0; i--) {
                    if(!visited[i][j]) {
                        list.add(map[i][j]);
                    }
                    
                    else {
                        answer++;
                    }
                }
                
                for(int i = m - 1, index = 0; i >= 0; i--, index++) {
                    if(index < list.size()) {
                        map[i][j] = list.get(index);
                    }
                    
                    else {
                        map[i][j] = '0';
                    }
                }
                
                // System.out.println(list.toString());
            }
        }
        
        return answer;
    }
}
