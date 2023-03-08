import java.util.*;

class Solution {
    public int[] solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        s = s.substring(2, s.length());
        s = s.substring(0, s.length() - 2).replace("},{", "-");
        
        String[] arr = s.split("-");
        
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.length() - o2.length();
            }
        }); 
        
        for(int i = 0; i < arr.length; i++) {
            String[] tmp = arr[i].split(",");
            
            for(int j = 0; j < tmp.length; j++) {
                int num = Integer.parseInt(tmp[j]);
                
                if(!answer.contains(num))
                    answer.add(num);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
