from collections import deque

def solution(record):
    answer = []
    data={}
    q=deque()
    
    for check in record:
        if check[0] == "E": # 입장시 3개의 변수로 받고 닉네임 최신화 후 (status,userID) q에 삽입
            status,userID,nickName=check.split()
            data[userID]=nickName
            q.append((status,userID))
       
        elif check[0] == "L":  # 떠날시 2개의 변수로 받고 (status,userID) q에 삽입
            status,userID=check.split()
            q.append((status,userID))
            
        else:
            # 닉네임 변경시 3개의 변수로 받고 닉네임 최신화
            status,userID,nickName=check.split()
            data[userID]=nickName

    while q:
        status,userID=q.popleft() # q를 꺼내 작업 진행
        if status == "Enter" : answer.append(data[userID]+"님이 들어왔습니다.")
        elif status == "Leave": answer.append(data[userID]+"님이 나갔습니다.")
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))