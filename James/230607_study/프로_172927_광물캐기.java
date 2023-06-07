/*틀린 풀이*/

// import java.util.*;

// class Solution {
//     public int solution(int[] picks, String[] minerals) {
//         int answer = 0;
//         int index = 0;
        
//         for(int i = 0; i < picks.length; i++) {
//             int limit = 0;
            
//             if(index == minerals.length - 1)
//                 break;
                       
//             for(int j = index; j < minerals.length; j++) {
//                 if(picks[i] == 0)
//                     break;
                
//                 if(i == 0) {
//                     if(minerals[j].equals("diamond")) {
//                         answer += 1;
//                         limit++;
//                     } else if(minerals[j].equals("iron")) {
//                         answer += 1;
//                         limit++;
//                     } else if(minerals[j].equals("stone")) {
//                         answer += 1;
//                         limit++;
//                     }
//                 } else if(i == 1) {
//                     if(minerals[j].equals("diamond")) {
//                         answer += 5;
//                         limit++;
//                     } else if(minerals[j].equals("iron")) {
//                         answer += 1;
//                         limit++;
//                     } else if(minerals[j].equals("stone")) {
//                         answer += 1;
//                         limit++;
//                     }
//                 } else if(i == 2) {
//                     if(minerals[j].equals("diamond")) {
//                         answer += 25;
//                         limit++;
//                     } else if(minerals[j].equals("iron")) {
//                         answer += 5;
//                         limit++;
//                     } else if(minerals[j].equals("stone")) {
//                         answer += 1;
//                         limit++;
//                     }
//                 }
                
//                 index = j;
                
//                 if(limit == 5) {
//                     index++;
//                     break;
//                 }
                    
//             }
//         }
        
//         return answer;
//     }
// }

