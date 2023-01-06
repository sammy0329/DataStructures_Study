from collections import deque
import math
def solution(fees, records):
    answer = []
    inStatus={} # 입차 데이터 관리 딕셔너리
    outStatus={} # 출차 데이터 관리 딕셔너리
    
    for record in records:
        time,number,status=record.split() # 시간/ 차량번호/ 입출차 상태 변수로 split
        
        if status=="IN": # 입차시 차량번호를 key로 inStatus 딕셔너리에 deque로 저장          
            if number in inStatus:
                inStatus[number].append(time)
            else:
                inStatus[number] = deque([time])
                outStatus[number] = deque([])
                
        else: # 출차시 차량번호를 key로 outStatus 딕셔너리에 deque로 저장    
            if number in outStatus:
                outStatus[number].append(time)
          
       
    allCarNumbers=list(inStatus.keys()) # 입차된 모든 차량 번호 저장 리스트
    allCarNumbers.sort()
        
    
    for check in allCarNumbers:
        check_time=0
        
        while inStatus[check]: # 입출차 하나씩 pop해서 계산식에 계산 후 check_time에 저장
            if not outStatus[check]: break
            
            in_data=inStatus[check].popleft()
            out_data=outStatus[check].popleft()  
            
            check_time+=(int(out_data[:2])-int(in_data[:2]))*60 + (int(out_data[3:])-int(in_data[3:]))    
            
            
        for _ in range(len(inStatus[check])): # 입차는 했지만, 출차는 안했을 경우 남은 값들 pop 후 계산 처리
            in_data=inStatus[check].popleft()
            check_time+=(23-int(in_data[:2]))*60 + (59-int(in_data[3:]))   
     
        if check_time>fees[0]: 
            answer.append(fees[1]+(int(math.ceil((check_time-fees[0])/fees[2])))*fees[3])
        else:
            answer.append(fees[1])
        
            
    return answer

# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# print(solution([1, 461, 1, 10],["00:00 1234 IN"]))