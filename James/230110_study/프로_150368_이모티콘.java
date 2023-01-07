import java.util.*;

class Solution {
    static int[][] userArray;
    static int[] emoticonsArray;
    static int finalTotalPrice = -1;
    static int serviceJoinMemberCount = -1;
    
    //10 10 10 10      // 2 12323
    // 2 12323
    
    //10 10 10 20      // 2 12323
    // 1 24234
    
    //10 10 10 30      // 2 12323
    // 0 222222
    
    //10 10 10 40      // 4 22222
    // 4 22222
    
    //10 10 20 10      // 4 222223
    // 4 222223
    public static void dfs(int[] saleRateArray, int idx, int[] emoticonsDiscount) {
        if(idx == emoticonsDiscount.length) {
            int totalPrice = 0;
            int memberCount = 0;
            
            for(int i = 0; i < userArray.length; i++) {
                int userRate = userArray[i][0];
                int userPrice = userArray[i][1];
                //한 유저 구매 비용
                int userTotalPrice = 0; 
                
                for(int j = 0; j < emoticonsDiscount.length; j++) {
                    // 구매 비용
                    int salePrice = emoticonsArray[j] - emoticonsArray[j] * emoticonsDiscount[j] / 100;
                    
                    if(userRate <= emoticonsDiscount[j]) {
                        // userRate보다 이모티콘 할인율이 크거나 같은 경우 
                        userTotalPrice += salePrice;      
                    }
                }
                // userPrice가 userTotalPrice가 더 크거나 같은 경우
                if(userPrice <= userTotalPrice)
                    memberCount++; // 서비스 가입
                
                // userPrice가 userTotalPrice보다 작은 경우
                else
                    totalPrice += userTotalPrice;
                
                // 초기 값인 경우
                if(finalTotalPrice == -1) {
                    finalTotalPrice = totalPrice;
                    serviceJoinMemberCount = memberCount;
                } else {
                    // 기존의 전체 가입 수보다 새로운 가입 수가 더 크다면 갱신 
                    if(serviceJoinMemberCount < memberCount){
                        finalTotalPrice = totalPrice;
                        serviceJoinMemberCount = memberCount;
                        // 기존의 전체 가입수와 새로운 가입 수가 같다면 totalPrice끼리 비교
                    } else if(serviceJoinMemberCount == memberCount){
                        // 기존의 이모티콘 판매액보다 새로운 이모티콘 판매액이 더 높다면 갱신
                        if(finalTotalPrice < totalPrice){
                            finalTotalPrice = totalPrice;
                            serviceJoinMemberCount = memberCount;
                        }
                        
                    }
                    
                }
                
            }
            return;
        } //if문 끝
            
        for(int i = 0; i < saleRateArray.length; i++) {
            emoticonsDiscount[idx] = saleRateArray[i];
            dfs(saleRateArray, idx + 1, emoticonsDiscount);   
        }
    }
    
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[2];
        int[] saleRateArray = {10, 20, 30, 40};
        int[] emoticonsDiscount = new int[emoticons.length];
        userArray = users;
        emoticonsArray = emoticons;
        
        dfs(saleRateArray, 0, emoticonsDiscount);

        //System.out.println(finalTotalPrice + " " + serviceJoinMemberCount);
        answer[0] = serviceJoinMemberCount;
        answer[1] = finalTotalPrice;
        
        return answer;
    }

}
