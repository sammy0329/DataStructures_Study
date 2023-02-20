import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        str1 = str1.toUpperCase();
        str2 = str2.toUpperCase();
        ArrayList<String> str1Al = new ArrayList<>();
        ArrayList<String> str2Al = new ArrayList<>();
        ArrayList<String> interAl = new ArrayList<>();
        ArrayList<String> sumAl = new ArrayList<>();
        
        for(int i = 0; i < str1.length() - 1; i++) {
            char first = str1.charAt(i);
            char second = str1.charAt(i + 1);
            
            if(first >= 'A' && first <= 'Z' && second >= 'A' && second <= 'Z')
                str1Al.add(first + "" + second);
        }
        
        for(int i = 0; i < str2.length() - 1; i++) {
            char first = str2.charAt(i);
            char second = str2.charAt(i + 1);
            
            if(first >= 'A' && first <= 'Z' && second >= 'A' && second <= 'Z')
                str2Al.add(first + "" + second);
        }
        
        for(String s : str1Al) {
            if(str2Al.remove(s)) {
                interAl.add(s);
            }
            
            sumAl.add(s);
        }
        
        for(String s : str2Al) {
            sumAl.add(s);
        }
                
        if(interAl.size() == sumAl.size())
            return 65536;
        
        else {
            return interAl.size() * 65536 / sumAl.size();
        }
    }
}
