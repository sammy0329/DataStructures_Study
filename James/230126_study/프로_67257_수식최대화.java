import java.util.*;

class Solution {
    static char[] operArr = {'+', '-', '*'};
    static ArrayList<Long> numberAl = new ArrayList<>();
    static ArrayList<Character> charAl = new ArrayList<>();
    static long answer = 0;
    static boolean[] visited = new boolean[3];
    
    public static void dfs(int cnt, char[] oper) {
        if(cnt == 3) {
            ArrayList<Long> numberList = new ArrayList<>(numberAl);
            ArrayList<Character> operList = new ArrayList<>(charAl);
            
            for(int i = 0; i < 3; i++) {
                for(int j = 0; j < operList.size(); j++) {
                    if(oper[i] == operList.get(j)) {
                        long result = calculate(numberList.remove(j), numberList.remove(j), oper[i]); 
                        numberList.add(j, result);
                        operList.remove(j);
                        j--;
                    }
                }
            }
            //System.out.println(numberList.toString());
            
            answer = Math.max(answer, Math.abs(numberList.get(0)));
            
            return;
        }
        
        for(int i = 0; i < 3; i++) {
            if(!visited[i]) {
                visited[i] = true;
                oper[cnt] = operArr[i];
                dfs(cnt + 1, oper);
                visited[i] = false;   
            }
        }
    }
    
    public static long calculate(long firstNum, long secondNum, char oper) {
        if(oper == '+') {
            return firstNum + secondNum;
        }
        
        else if(oper == '-') {
            return firstNum - secondNum;
        }
        
        else {
            return firstNum * secondNum;
        }
    }
    
    public long solution(String expression) {
        answer = 0;
        
        char[] oper = new char[3];
        String number = "";
        
        for(int i = 0; i < expression.length(); i++) {
            if(expression.charAt(i) >= '0'&& expression.charAt(i) <= '9') {
                number += expression.charAt(i);
            }
            
            else {
                numberAl.add(Long.parseLong(number));
                charAl.add(expression.charAt(i));
                number = "";
            }
        }
        numberAl.add(Long.parseLong(number));
        
        //System.out.println(numberAl.toString());
        
        dfs(0, oper);
        
        return answer;
    }
}
