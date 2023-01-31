import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = Integer.MAX_VALUE;
        String[] initArray = sc.nextLine().split("-");
//        System.out.println(Arrays.toString(initArray));

        for(int i = 0; i < initArray.length; i++) {
            int tmp = 0;

            String[] array = initArray[i].split("\\+");
//            System.out.println(Arrays.toString(array));

            for(int j = 0; j < array.length; j++) {
                tmp += Integer.parseInt(array[j]);
            }

            if(answer == Integer.MAX_VALUE) {
                answer = tmp;
            }

            else {
                answer -= tmp;
            }
        }

        System.out.println(answer);
    }
}
