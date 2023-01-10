from collections import deque

# 상하좌우 움직임 처리
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def solution(places):
    answer = []

    
    for i in range(5):
        check_place=places[i]
        person=deque()
        desk=deque()
        check=True
        
        for row_idx,row_value in enumerate(check_place):
            for col_idx,col_value in enumerate(row_value):
                if col_value=="P": person.append((row_idx,col_idx))
                elif col_value=="O": desk.append((row_idx,col_idx))
        
        while person and check:
            
            row,col=person.popleft() 
            
            for i in range(4):
                nrow=row+dx[i]
                ncol=col+dy[i]
                
                # 위치 벗어나면 안됨
                if nrow<0 or nrow>=5 or ncol<0 or ncol>=5:
                    continue
                
                if check_place[nrow][ncol]=="P":
                    check=False
                    answer.append(0)
                    break
                
        
        while desk and check:
            person_count=0
            
            row,col=desk.popleft() 
            
            for i in range(4):
                nrow=row+dx[i]
                ncol=col+dy[i]
                
                # 위치 벗어나면 안됨
                if nrow<0 or nrow>=5 or ncol<0 or ncol>=5:
                    continue
                
                if check_place[nrow][ncol]=="P":
                    person_count+=1
                
                if person_count==2:
                    check=False
                    answer.append(0)
                    break
        
        if check: answer.append(1)
        
        
        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))