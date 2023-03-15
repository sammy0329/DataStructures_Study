def checking(board):
    pang=[]

    # 오른쪽, 아래, 대각선 탐색
    dx=[1,0,1] 
    dy=[0,1,1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(3): # 범위를 벗어나거나, 오른쪽, 아래, 대각선 값이 다르거나, '_' 즉 비어있다면 break
                if not(0<=i+dx[k]<len(board)) or not(0<=j+dy[k]<len(board[0])): break
                if board[i+dx[k]][j+dy[k]] != board[i][j] or board[i+dx[k]][j+dy[k]]=='_': break
            else: # 같다면 값들 append
                pang.append((i,j))
                for k in range(3):
                    pang.append((i+dx[k],j+dy[k]))

    if not pang: return None # 리스트가 비었다면 None 반환

    return list(set(pang)) # 중복 제거 후 반환

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    while True:
        pang_list=checking(board)
        
        if pang_list == None: return answer # while문 종료조건

        pang_list.sort() # 윗단 부터 떨어지는거 진행해야 하므로 sort 진행

        for x,y in pang_list:
            answer+=1
            for check_x in range(x,-1,-1):
                if check_x==0 or board[check_x][y]=='_': # check_x가 맨 꼭대기 값이거나, '_'를 만나면 break
                    board[check_x][y]='_'
                    break
                board[check_x][y]=board[check_x-1][y] # 위의 값을 하나씩 땡겨옴

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]),14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]),15)