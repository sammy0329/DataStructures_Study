import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int length = survey.length;
        int score_RT = 0, score_CF = 0, score_JM = 0, score_AN = 0;
        String string_RT = "R", string_CF = "C", string_JM = "J", string_AN = "A";
        int score = 0;
        
        for(int i = 0; i < length; i++) {
            switch(choices[i]) {
                case 1 : score = -3; break;
        
                case 2 : score = -2; break;
                    
                case 3 : score = -1; break;
                    
                case 4 : score = 0; break;
                    
                case 5 : score = 1; break;
                    
                case 6 : score = 2; break;
                    
                case 7 : score = 3; break;
            }
            
            switch(survey[i]) {
                case "RT" : score_RT += score; break;
                    
                case "TR" : score_RT -= score; break;
                    
                case "CF" : score_CF += score; break;
                    
                case "FC" : score_CF -= score; break;
                    
                case "JM" : score_JM += score; break;
                    
                case "MJ" : score_JM -= score; break;
                    
                case "AN" : score_AN += score; break;
                    
                case "NA" : score_AN -= score; break;
            }
        }
        
        if(score_RT > 0) string_RT = "T";
        if(score_CF > 0) string_CF = "F";
        if(score_JM > 0) string_JM = "M";
        if(score_AN > 0) string_AN = "N";
        
        answer = string_RT + string_CF + string_JM + string_AN;
        
        return answer;
    }
}
