from collections import deque

# 상하좌우 확인
drow=[1,-1,0,0]
dcol=[0,0,1,-1]

def solution(places):
    answer = []
    
    for i in range(5):
        check_place=places[i]
        person=deque() # 사람 좌표(row,col) 리스트
        desk=deque() # 책상 좌표(row,col) 리스트
        check=True # 거리두기를 지켰는지 check하는 변수
        
        for row_idx,row_value in enumerate(check_place): # 사람, 책상 좌표를 각각의 리스트에 append
            for col_idx,col_value in enumerate(row_value):
                if col_value=="P": person.append((row_idx,col_idx))
                elif col_value=="O": desk.append((row_idx,col_idx))
                
        # 해당 좌표를 하나씩 뽑아 row,col 변수에 저장하고 상하좌우에 P가 있으면 
        # 맨해튼 거리 조건에 맞지 않기 때문에 check를 False로 바꿔주고 answer에 0을 append 해주기
        while person and check:
            row,col=person.popleft()
            
            for i in range(4): 
                nrow=row+drow[i]
                ncol=col+dcol[i]
                
                # 위치 벗어나면 안됨
                if nrow<0 or nrow>=5 or ncol<0 or ncol>=5:
                    continue
                
                if check_place[nrow][ncol]=="P":
                    check=False
                    answer.append(0)
                    break
                
        # 해당 좌표를 하나씩 뽑아 row,col 변수에 저장하고 상하좌우에 P가 2개 이상 있으면 
        # 맨해튼 거리 조건에 맞지 않기 때문에 check를 False로 바꿔주고 answer에 0을 append 해주기
        while desk and check:
            person_count=0
            
            row,col=desk.popleft() 
            
            for i in range(4):
                nrow=row+drow[i]
                ncol=col+dcol[i]
                
                # 위치 벗어나면 안됨
                if nrow<0 or nrow>=5 or ncol<0 or ncol>=5:
                    continue
                
                if check_place[nrow][ncol]=="P":
                    person_count+=1
                
                if person_count>=2:
                    check=False
                    answer.append(0)
                    break
        
        if check: answer.append(1) # check가 True일 경우에만 1을 append
            
    return answer

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))