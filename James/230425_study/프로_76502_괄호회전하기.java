import java.util.*;

class Solution {
    public boolean isCorrect(String newS) {
        Stack<Character> stack = new Stack<>();
        
        try {
            for(int i = 0; i < newS.length(); i++) {
                char bracket = newS.charAt(i);
            
                switch(bracket) {
                    case '(' :
                        stack.add(bracket);
                        break;
                    
                    case ')' :
                        if(stack.peek() != '(')
                            return false;
                    
                        stack.pop();
                        break;
                    
                    case '{' :
                        stack.add(bracket);
                        break;
                    
                    case '}' :
                        if(stack.peek() != '{')
                            return false;
                    
                        stack.pop();
                        break;
                    
                    case '[' :
                        stack.add(bracket);
                        break;
                    
                    case ']' :
                        if(stack.peek() != '[')
                            return false;
                    
                        stack.pop();
                        break;
                    }
                }    
        } catch(Exception e) {
            return false;
        }
        
        return stack.isEmpty() ? true : false;
    }

    public int solution(String s) {
        int answer = 0;
        String newS;
        
        for(int i = 0; i < s.length(); i++) {
            String firstS = s.substring(0, i);
            String secondS = s.substring(i, s.length());
            
            newS = secondS + firstS;
            
            if(isCorrect(newS))
                answer++;            
        }
            
        return answer;
    }
}
