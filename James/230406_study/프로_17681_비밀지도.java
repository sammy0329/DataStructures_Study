import java.util.*;

class Solution {
    public String[] addZero(String binary, int n) {
        if(binary.length() != n) {
            String zero = "";
            
            for(int i = 0; i < n - binary.length(); i++) {
                zero += "0";    
            }
            
            binary = zero + binary;
        }
        
        return binary.split("");
    }
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String one = "1";
        
        for(int i = 0; i < n; i++) {
            String text = "";
            
            String binary1 = Integer.toBinaryString(arr1[i]);
            String binary2 = Integer.toBinaryString(arr2[i]);
            
            String[] binaryArr1 = addZero(binary1, n);
            String[] binaryArr2 = addZero(binary2, n);
            
            // System.out.println(Arrays.toString(binaryArr1));
            // System.out.println(Arrays.toString(binaryArr2));
            
            for(int j = 0; j < n; j++) {
                if(one.equals(binaryArr1[j]) || one.equals(binaryArr2[j])) {
                    text += "#";
                }
                
                else {
                    text += " ";
                }
            }
            
            answer[i] = text;
        }

        return answer;
    }
}
