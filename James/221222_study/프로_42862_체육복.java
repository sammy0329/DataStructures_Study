package Day03;

import java.util.*;
import java.util.stream.Collectors;

public class 프로_42862_체육복 {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        Set<Integer> newLost, newReserve, set;

        newLost = Arrays.stream(lost).boxed().collect(Collectors.toSet());
        newReserve = Arrays.stream(reserve).boxed().collect(Collectors.toSet());

        set = new HashSet<>(newReserve);
        set.retainAll(newLost);

        newLost.removeAll(set); 
        newReserve.removeAll(set);

        List<Integer> newLost2 = new ArrayList<>(newLost);
        List<Integer> newReserve2 = new ArrayList<>(newReserve);

        for(int i : newReserve2) {
            if(newLost2.contains(i - 1))
                newLost2.remove(i - 1);

            else if (newLost2.contains(i + 1)) {
                newLost2.remove(i + 1);
            }
        }

        answer = n - newLost2.size();

        return answer;
    }
}
