import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] solArr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for(int i = 0; i < n; i++) {
            int sol = Integer.parseInt(st.nextToken());
            solArr[i] = sol;
        }

        Arrays.sort(solArr);

        int start = 0;
        int end = solArr.length - 1;
        int min = Integer.MAX_VALUE;
        int sum = 0;
        int absValue = 0;
        int firstNum = 0;
        int secondNum = 0;

        while (start < end) {
            sum = solArr[start] + solArr[end];
            absValue = Math.abs(sum);

            if(absValue < min) {
                min = absValue;
                firstNum = solArr[start];
                secondNum = solArr[end];
            }

            if(sum > 0)
                end--;

            else
                start++;
        }

        System.out.println(firstNum + " " + secondNum);
    }
}
