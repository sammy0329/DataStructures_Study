from collections import deque

def solution(priorities, location):
    
    answer = 0
    new=deque()
    
    for idx,num in enumerate(priorities): # 인덱스와 데이터 값을 튜플 형태로 재저장
        new.append((idx,num))  

    max_prior=max(new, key = lambda x : x[1])[1] # 최대값 저장
    
    while new:
        
        data=new.popleft()
        
        
        if data[1] < max_prior: # 최대값과 비교해서 작으면 뒤에 다시 넣음
            new.append((data[0],data[1]))
            
        else: # 최대값 보다 크거나 같으면 answer+1 해주고, 만약 인덱스와 원하는 location 값이 같으면 break
            answer += 1
            if data[0]==location: break
            max_prior=max(new, key = lambda x : x[1])[1]
            
    return answer

# print(solution([2, 1, 3, 2],2))
# print(solution([1, 1, 9, 1, 1, 1],0))

