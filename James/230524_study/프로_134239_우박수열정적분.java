import java.util.*;

class Solution {
    public double calcArea(int y1, int y2) {
        double area = (double)(y1 + y2) * 1 / 2;
        
        return area;
    }
    
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        List<Integer> al = new ArrayList<>();
        List<Double> areaAl = new ArrayList<>();
        int num = k;
        
        while(num > 1) {
            al.add(num);
            
            if(num % 2 == 0) {
                num /= 2;
            } else {
                num = num * 3 + 1;   
            }
        }
        
        al.add(1);
                
        for(int i = 1; i < al.size(); i++) {
            double area = calcArea(al.get(i - 1), al.get(i));
            areaAl.add(area);
        }
                
        for(int i = 0; i < ranges.length; i++) {
            int x1 = ranges[i][0];
            int x2 = ranges[i][1] + areaAl.size();
            double sum = 0.0;
            
            if(x1 == x2) {
                sum = 0.0;
                answer[i] = sum;
            }
            
            else if(x1 > x2) {
                sum = -1.0;
                answer[i] = sum;
            }
            
            for(int j = x1; j < x2; j++) {
                sum += areaAl.get(j);
            }
            
            answer[i] = sum;    
            
        }
        
        return answer;
    }
}
