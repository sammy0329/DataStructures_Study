from collections import deque
import math
def solution(fees, records):
    answer = []
    inStatus={}
    outStatus={}
    
    for record in records:
        time,number,status=record.split()
        
        if status=="IN":          
            if number in inStatus:
                inStatus[number].append(time)
            else:
                inStatus[number] = deque([time])
                outStatus[number] = deque([])
                
        else:
            if number in outStatus:
                outStatus[number].append(time)
          
       
    data=list(inStatus.keys())
    data.sort()
        
    
    for check in data:
        check_time=0
        
        
        while inStatus[check]:
            if not outStatus[check]: break
            
            in_data=inStatus[check].popleft()
            out_data=outStatus[check].popleft()  
            
            check_time+=(int(out_data[:2])-int(in_data[:2]))*60 + (int(out_data[3:])-int(in_data[3:]))    
            
            
        for _ in range(len(inStatus[check])):
            in_data=inStatus[check].popleft()
            check_time+=(23-int(in_data[:2]))*60 + (59-int(in_data[3:]))   
     
        if check_time>fees[0]:
            
            answer.append(fees[1]+(int(math.ceil((check_time-fees[0])/fees[2])))*fees[3])
        else:
            answer.append(fees[1])
        
            
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))