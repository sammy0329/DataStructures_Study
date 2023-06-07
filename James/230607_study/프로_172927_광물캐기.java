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
import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        int picksNumber = picks[0] + picks[1] + picks[2];
        int[][] sliceMinerals = new int[minerals.length / 5 + 1][3];
        
        for(int i = 0; i < minerals.length && picksNumber > 0; i++) {
            if(minerals[i].equals("diamond")) {
                sliceMinerals[i / 5][0] += 1;
                sliceMinerals[i / 5][1] += 5;
                sliceMinerals[i / 5][2] += 25;
            } else if(minerals[i].equals("iron")) {
                sliceMinerals[i / 5][0] += 1;
                sliceMinerals[i / 5][1] += 1;
                sliceMinerals[i / 5][2] += 5;
            } else if(minerals[i].equals("stone")) {
                sliceMinerals[i / 5][0] += 1;
                sliceMinerals[i / 5][1] += 1;
                sliceMinerals[i / 5][2] += 1;
            }
            
            if(i % 5 == 4) {
                picksNumber--;
            }
        }
        
        Arrays.sort(sliceMinerals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] < o2[2] ? 1 : -1;
            }
        });
        
        for(int i = 0, pick = 0; i < sliceMinerals.length; i++) {
            while(pick < 3 && picks[pick] == 0) {
                pick++;
            }
            
            if(pick == 3)
                break;
            
            picks[pick]--;
            answer += sliceMinerals[i][pick];
        }
        
        return answer;
    }
}
