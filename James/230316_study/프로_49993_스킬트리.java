import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for(int i = 0; i < skill_trees.length; i++) {
            String tempSkill = skill_trees[i];
            
            for(int j = 0; j < skill_trees[i].length(); j++) {
                String tmpValue = skill_trees[i].substring(j, j + 1);
                
                if(!skill.contains(tmpValue)) {
                    tempSkill = tempSkill.replace(tmpValue, "");   
                }
            }
                        
            if(skill.indexOf(tempSkill) == 0)
                answer++;
        }
        
        return answer;
    }
}
