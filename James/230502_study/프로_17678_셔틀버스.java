import java.util.*;

class Solution {
    public int returnMinute(String time) {
        String[] timeArr = time.split(":");
        int hour = Integer.parseInt(timeArr[0]);
        int minute = Integer.parseInt(timeArr[1]);
        
        int result = hour * 60 + minute;
        return result;
    }
    
    public String returnTime(int result) {
        int hour = (int)(result / 60);
        int minute = result % 60;
        String strMinute = "";
        String strHour = "";
        
        strHour = String.valueOf(hour);
        strMinute = String.valueOf(minute);
        
        if(String.valueOf(hour).length() == 1)
            strHour = "0" + String.valueOf(hour);
        
        if(String.valueOf(minute).length() == 1)
            strMinute = "0" + String.valueOf(minute);
        
        String time = strHour + ":" + strMinute;
        return time;
    }
    
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        
        Arrays.sort(timetable);
        Queue<String> queue = new LinkedList<>(Arrays.asList(timetable));
        int firstTime = returnMinute("09:00");
        int cnt = 0;
        int konTime = 0;
        
        for(int i = 0; i < n; i++) {
            cnt = 0;
            
            while(!queue.isEmpty()) {
                int currentTime = returnMinute(queue.peek());
                
                if(currentTime <= firstTime && cnt < m) {
                    queue.poll();
                    cnt++;
                } else {
                    break;
                }
                
                konTime = currentTime - 1;
            }
            
            firstTime += t;
        }
        
        if(cnt < m)
            konTime = firstTime - t;
        
//         System.out.println(konTime);
        return returnTime(konTime);
    }
}
