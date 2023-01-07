import java.util.*;

class Solution {
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[2];
        int[] saleRate = {10, 20, 30, 40};
        int[][] emoticonsCombination = new int[emoticons.length][4];
        int userCount = users.length;
        int serviceJoinCount = 0;
        
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < emoticons.length; j++) {
                emoticonsCombination[j][i] = emoticons[j] - emoticons[j] * saleRate[i] / 100;
            }
        }
        
        System.out.println(Arrays.deepToString(emoticonsCombination));
        
        for(int i = 0; i < users.length; i++) {
            int serviceJoinSaleRate = users[i][0]; // 해당 할인 비율 넘는 이모티콘 모두 구입
            int serviceJoinCost = users[i][1]; // 위의 조건과 해당 비용 넘으면 이모티콘 플러스 가입
            
            for(int j = 0; j < emoticonsCombination.length; j++) {
                for(int k = 0; k < 4; k++) {
                    int emoticonsSaleRate = (k + 1) * 10;
                    int emoticonsSalePrice = emoticonsCombination[j][k];
                    
                    if(serviceJoinSaleRate >= emoticonsSaleRate && )
                }
            }   
        }
        
        return answer;
    }
}
