from collections import deque # 데큐는 sort가 안되는구나..

def solution(people, limit):
    answer = 0
    total=0 # 배에 태울 총 kg
    check=False
    people.sort()
    people_queue=deque(people)
    
    while people_queue:
        
        if check: break
        total=people_queue.pop() # 가장 큰값을 꺼내 total에 넣어준다.
        
        while True:
            if people_queue:
                
                if total+people_queue[0]<=limit:
                    total+=people_queue.popleft() #                     
                
                else:
                    total=0 # total과 남은 최소값의 합이 limit 보다 크면 total 0으로 초기화 후 answer+1
                    answer+=1
                    break
            else:
                check=True
                break       
    return answer+1

print(solution([70, 50, 80, 50],100))
print(solution([70, 50, 40, 20],100))
print(solution([70, 80, 50],100))