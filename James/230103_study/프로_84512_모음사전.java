import java.util.*;

class Solution {
    public static void dfs(String text, int index, ArrayList<String> array, String[] chList) {
        if(index >= 5)
            return;
            
        for(String word : chList) {
            String newText = text + word;
            array.add(newText);
            dfs(newText, index + 1, array, chList);
        }
    }
    
    public int solution(String word) {
        int answer = 0;
        String[] chList = {"A", "E", "I", "O", "U"};
        String text = "";
        ArrayList<String> array = new ArrayList<>();
        
        dfs(text, 0, array, chList);
        
        //System.out.println(array.toString());
        Collections.sort(array);
        answer = array.indexOf(word) + 1;
        
        return answer;
    }
}
