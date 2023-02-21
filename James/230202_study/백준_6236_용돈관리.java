import java.util.*;

public class Main {
    static int n, m;
    static int k = 0;
    static int[] priceArray;
  
    public static void binarySearch(int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;

            if(m >= isWithdraw(mid)) {
                k = mid;
                end = mid - 1;
            }

            else {
                start = mid + 1;
            }
        }
    }

    public static int isWithdraw(int withdrawMoney) {
        int count = 1;
        int myMoney = withdrawMoney;

        for (int price : priceArray) {
           myMoney -= price;

           if(myMoney < 0) {
               count++;
               myMoney = withdrawMoney - price;
           }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        priceArray = new int[n];
        int maxPrice = 0;

        for (int i = 0; i < n; i++) {
            int price = sc.nextInt();
            priceArray[i] = price;
            maxPrice = Math.max(maxPrice, priceArray[i]);
        }

        int start = maxPrice;
        int end = (int)1e9;

        binarySearch(start, end);
        System.out.println(k);
    }
}
