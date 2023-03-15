package Day03;

import java.util.*;

public class 프로_42628_이중우선순위큐 {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        int length = operations.length;
        TreeMap<Integer, Integer> tm = new TreeMap<>();

        for(int i = 0; i < length; i++) {
            String[] operArray = operations[i].split(" ");
            String oper = operArray[0];
            int operNum = Integer.parseInt(operArray[1]);

            if(oper.equals("I")) {
                tm.put(operNum, 1);
            }

            else if(oper.equals("D")) {
                if(operNum == 1) {
                    if(!tm.isEmpty()) {
                        int lastData = tm.lastKey();
                        tm.remove(lastData);
                        //System.out.println(lastData);
                    }
                }
                else if(operNum == -1) {
                    if(!tm.isEmpty()) {
                        int firstData = tm.firstKey();
                        tm.remove(firstData);
                        //System.out.println(firstData);
                    }
                }
            }
        }

        if(!tm.isEmpty()) {
            answer[0] = tm.lastKey();
            answer[1] = tm.firstKey();
            return answer;
        }

        else {
            answer[0] = 0;
            answer[1] = 0;
            return answer;
        }
    }

    public static void main(String[] args) {
        프로_42628_이중우선순위큐 ex = new 프로_42628_이중우선순위큐();
        String[] operations1 = {"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
        String[] operations2 = {"I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"};
        System.out.println(Arrays.toString(ex.solution(operations1)));
        System.out.println(Arrays.toString(ex.solution(operations2)));
    }
}
