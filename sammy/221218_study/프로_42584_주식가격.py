from collections import deque

def solution(prices):
    answer = []
    q=deque(prices)

    while q:
        data=q.popleft() # 데이터를 왼쪽에서 꺼냄    
        cnt=0
        
        for check_data in q: # q에서 하나씩 꺼내 data보다 작은 값이 있는지 확인
            cnt+=1
            
            if check_data<data: # 작은 값이 있다면 가격이 떨어진 것이므로 break
                break
        
        answer.append(cnt) 
        
    return answer

# print(solution([1, 2, 3, 2, 3]))