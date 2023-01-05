import java.util.*;

public class Main {
    static int[] numArray;
    static int[] operArray;
    static ArrayList<Integer> resultAl;
    
    public static void dfs(int cnt, int number) {
        if(cnt >= numArray.length) {
            resultAl.add(number);
            return;
        }

        for(int i = 0; i < operArray.length; i++) {
            if(operArray[i] > 0) {
                operArray[i]--;

                switch (i) {
                    // 덧셈
                    case 0 :
                        dfs(cnt + 1, number + numArray[cnt]);
                        break;
                    // 뺄셈
                    case 1 :
                        dfs(cnt + 1, number - numArray[cnt]);
                        break;
                    // 곱셈
                    case 2 :
                        dfs(cnt + 1, number * numArray[cnt]);
                        break;
                    // 나눗셈
                    case 3 :
                        dfs(cnt + 1, number / numArray[cnt]);
                        break;
                }
                operArray[i]++;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        numArray = new int[n];
        operArray = new int[4];
        resultAl = new ArrayList<>();

        for(int i = 0; i < n; i++) {
            numArray[i] = scanner.nextInt();
        }

        for(int i = 0; i < 4; i++) {
            int oper = scanner.nextInt();
            operArray[i] = oper;
        }

        dfs(1, numArray[0]);
//        System.out.println(resultAl.toString());
        System.out.println(Collections.max(resultAl));
        System.out.println(Collections.min(resultAl));
    }
}
