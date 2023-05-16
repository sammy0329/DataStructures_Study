import java.util.*;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        List<String> al = new ArrayList<>();
        
        for(char i = 'A'; i <= 'Z'; i++) {
            al.add(String.valueOf(i));
        }
                
        for(int i = 0; i < msg.length(); i++) {
            String w = String.valueOf(msg.charAt(i));
            
            if(i == msg.length() - 1) {
                answer.add(al.indexOf(String.valueOf(msg.charAt(i))) + 1);
                break;
            }
            
            String c = String.valueOf(msg.charAt(i + 1));
            
            while(al.contains(w + c)) {
                w += c;
                i++;
                
                if(i == msg.length() - 1 || c.equals("")) {
                    c = "";
                    break;
                }
                
                c = String.valueOf(msg.charAt(i + 1));
            }
            
            if(!al.contains(w + c))
                al.add(w + c);
            
            int index = al.indexOf(w);
            
            if(index != -1)
                answer.add(index + 1);
            
            if(index == msg.length() - 1 && !c.equals("")) {
                answer.add(al.indexOf(c) + 1);
            }
        }
                
        return answer.stream().mapToInt(Integer :: intValue).toArray();
    }
}
