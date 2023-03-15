import java.util.*;

public class ex02 {
    // index -> 열,  value -> 행
    // (value, index) -> (3, 0) -> 3행 0열
    static int count = 0; // 경우의 수
    static int[] chessArray;
    public static void dfs(int column, int n) {
        if(column == n) {
            count++;
            return;
        }

        for(int i = 0; i < n; i++) {
            // column -> 열, i -> 행
            chessArray[column] = i;

            // column 열에 세울 수 있는지 확인
            if(isPossible(column)) {
                dfs(column + 1, n);
            }
        }
    }

    public static boolean isPossible(int column) {
        for(int i = 0; i < column; i++) {
            // i열의 행과 column열의 행과 같다면 같은 행에 있는 것이므로 false
            if(chessArray[column] == chessArray[i])
                return false;
            // value(행)와 value(행)을 뺀 것과 열과 열을 뺀 것이 같으면 대각선
            else if(Math.abs(column - i) == Math.abs(chessArray[column] - chessArray[i]))
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        chessArray = new int[n];

        dfs(0, n);
        //System.out.println(Arrays.toString(chessArray));
        System.out.println(count);
    }
}
