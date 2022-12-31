from collections import deque

def solution(priorities, location):
    
    answer = 0
    new=deque()
    
    
    for idx,num in enumerate(priorities):
        new.append((idx,num))  

    max_prior=max(new, key = lambda x : x[1])[1]
    while new:
        
        
        data=new.popleft()
        print(data,max_prior)
        
        
        if data[1] < max_prior:
            new.append((data[0],data[1]))
            
        else:
            answer += 1
            if data[0]==location: break
            max_prior=max(new, key = lambda x : x[1])[1]
            
    return answer

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))

