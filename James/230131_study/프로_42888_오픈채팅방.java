import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> hashMap = new HashMap<>();
        int cnt = 0;
        
        for(int i = 0; i < record.length; i++) {
            String[] userLog = record[i].split(" ");
            String log = userLog[0];
            String uid = userLog[1];
            
            if(log.equals("Enter")) {
                String name = userLog[2];
                hashMap.put(uid, name);
            }
            
            else if(log.equals("Leave")) {
                continue;
            }
            
            else {
                String name = userLog[2];
                hashMap.put(uid, name);
                cnt++;
            }
        }
        
        // System.out.println(hashMap.toString());
        
        String[] answer = new String[record.length - cnt];
        int index = 0;
        
        for(int i = 0; i < record.length; i++) {
            String[] userLog = record[i].split(" ");
            String log = userLog[0];
            String uid = userLog[1];
            String name = hashMap.get(uid);
            
            if(log.equals("Enter")) {
                answer[index++] = name + "님이 들어왔습니다.";
            }
            
            else if(log.equals("Leave")) {
                answer[index++] = name + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}
