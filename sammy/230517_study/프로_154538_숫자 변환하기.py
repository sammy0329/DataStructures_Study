from collections import deque

def solution(x, y, n):
    q=deque()
    q.append((y,0))
    
    while q:
        data=q.popleft()

        if data[0]==x: # data[0] 값 즉, 변경된 y값이 x로 변경되었으면 return
            return data[1]
        
        if data[0]>x: 
            if data[0]%3==0: # 3으로 나눠지면 나누기 진행, 2번째 값에는 count를 1 올려주기
                q.append((data[0]/3,data[1]+1))

            if data[0]%2==0: # 2로 나눠지면 나누기 진행, 2번째 값에는 count를 1 올려주기
                q.append((data[0]/2,data[1]+1))

            q.append((data[0]-n,data[1]+1)) # n을 빼주기

    return -1
 

print(solution(10, 40, 5),2)
print(solution(	10, 40, 30),1)

