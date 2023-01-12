import java.util.*;

// DP 풀이
public class ex01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int[] dpArray = new int[11];

        dpArray[0] = 0;
        dpArray[1] = 1;
        dpArray[2] = 2;
        dpArray[3] = 4;

        for(int i = 0; i < t; i++) {
            int n = sc.nextInt();

            for(int j = 4; j <= n; j++) {
                dpArray[j] = dpArray[j - 1] + dpArray[j - 2] + dpArray[j - 3];
            }
            System.out.println(dpArray[n]);
        }

        //System.out.println(Arrays.toString(dpArray));
    }
}

// dfs 풀이
import java.util.*;

public class ex03 {
    static int result;
    public static void dfs(int n, int value) {
        if(value > n)
            return;

        if(value >= n) {
            result++;
            return;
        }

        for(int i = 1; i <= 3; i++) {
            dfs(n, value + i);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for(int i = 0; i < t; i++) {
            int n = sc.nextInt();
            result = 0;
            dfs(n, 0);
            System.out.println(result);
        }
    }
}
