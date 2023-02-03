import java.util.*;

public class Main {

    static int cnt = -1;
    static int x;
    static int y;

    public static void binarySearch(int start, int end, int target) {
        while(start <= end) {
            int mid = (start + end) / 2;

            int z = getPercent(x + mid, y + mid);

            if(z != target) {
                cnt = mid;
                end = mid - 1;
            }

            else {
                start = mid + 1;
            }
        }
    }

    public static int getPercent(int x, int y) {
        return (int)((long) y * 100 / x);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        x = sc.nextInt();
        y = sc.nextInt();

        int start = 0;
        int end = (int)1e9;

        binarySearch(start, end, getPercent(x, y));
        System.out.println(cnt);
    }
}
