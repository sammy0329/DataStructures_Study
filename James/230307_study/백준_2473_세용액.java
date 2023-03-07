import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static long min = 3000000000L;
    static long sum, absValue;
    static long[] answer = new long[3];
    
    public static void binarySearch(long[] arr, int index) {
        int start = index + 1;
        int end = arr.length - 1;

        while(start < end) {
            sum = arr[start] + arr[end]+ arr[index];
            absValue = Math.abs(sum);

            if(absValue < min) {
                min = absValue;
                answer[0] = arr[start];
                answer[1] = arr[end];
                answer[2] = arr[index];
            }

            if(sum > 0)
                end--;

            else
                start++;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i = 0; i < arr.length; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        for(int i = 0; i < n - 2; i++) {
            binarySearch(arr, i);
        }

        Arrays.sort(answer);

        for(int i = 0; i < 3; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}
