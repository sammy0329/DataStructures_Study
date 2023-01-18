class Solution {
    public int solution(String s) {
        int answer = s.length();
    
        for(int i = 1; i <= s.length() / 2; i++) {
            String target = s.substring(0, i);
            String text = ""; 
            int cnt = 1; 
            StringBuilder sb = new StringBuilder();
            
            for(int start = i; start <= s.length(); start += i) {
                if(start + i >= s.length()) {
                    text = s.substring(start, s.length());
                }
                
                else {
                    text = s.substring(start, start + i);
                }
            
                if(text.equals(target)) {
                    cnt++;
                }
                
                else if(cnt == 1){
                    sb.append(target);
                    target = text;
                }
                
                else {
                    sb.append(cnt).append(target);
                    target = text;
                    cnt = 1;
                }
            }
            
            if(i != target.length()) 
                sb.append(target);
        
            answer = Math.min(answer, sb.toString().length());
        }
    
        return answer;
    }
}
