import java.util.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        String answer = "(None)";
        m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
            .replace("A#", "a");
        int maxTime = 0;
        
        for(int i = 0; i < musicinfos.length; i++) {
            String[] info = musicinfos[i].split(",");
            String[] firstTimeArr = info[0].split(":");
            int firstTimeHour = Integer.parseInt(firstTimeArr[0]);
            int firstTimeMinute = Integer.parseInt(firstTimeArr[1]);
            int firstTime = firstTimeHour * 60 + firstTimeMinute;
            
            String[] endTimeArr = info[1].split(":");
            int endTimeHour = Integer.parseInt(endTimeArr[0]);
            int endTimeMinute = Integer.parseInt(endTimeArr[1]);
            int endTime = endTimeHour * 60 + endTimeMinute;
            
            int time = endTime - firstTime;
            
            String musicTitle = info[2];
            String sheet = info[3];
            sheet = sheet.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
            .replace("A#", "a");
            
            int sheetLength = sheet.length();
            
            String text = "";
                            
            if(time > sheetLength) {
                int cnt = time / sheetLength;
                
                for(int j = 0; j < cnt; j++) {
                    text += sheet;
                }
                
                text += sheet.substring(0, time % sheetLength);
            } else {
                text = sheet.substring(0, time);   
            }
            
            if(text.contains(m) && maxTime < time) {
                answer = musicTitle;
                maxTime = time;
            }
        }
                
        return answer;
    }
}
