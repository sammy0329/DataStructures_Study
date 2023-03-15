import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int turnNum;
        int turnCnt;
        List<String> wordList = new LinkedList<>();
        answer[0] = 0;
        answer[1] = 0;
        
        for(int i = 0; i < words.length; i++) {
            turnNum = i % n;
            turnCnt = i / n;
            if(i > 0 && words[i - 1].charAt(words[i - 1].length() - 1) != words[i].charAt(0)) {
                answer[0] = turnNum + 1;
                answer[1] = turnCnt + 1;
                break;
            }
            
            if(wordList.contains(words[i])) {
                answer[0] = turnNum + 1;
                answer[1] = turnCnt + 1;
                break;
            }
            
            wordList.add(words[i]);
        }
        
        return answer;
    }
}
