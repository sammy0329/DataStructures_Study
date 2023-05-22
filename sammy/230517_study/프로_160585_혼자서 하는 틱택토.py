def isWin(board, x, y):
    x1, x2 = (x - 1) % 3, (x + 1) % 3
    if board[x][y] == board[x1][y] == board[x2][y]: # 열 파악
        return True
    
    y1, y2 = (y - 1) % 3, (y + 1) % 3
    if board[x][y] == board[x][y1] == board[x][y2]: # 행 파악
        return True

    if (board[x][y] == board[x1][y1] == board[x2][y2]) or (board[x][y] == board[x1][y2] == board[x2][y1]): # 대각선 파악
        return True

    return False

def solution(board):
    O_list=[]
    X_list=[]

    for x,datas in enumerate(board):
        for y,data in enumerate(datas):
            if data == "O":
                O_list.append((x,y))
            elif data == "X":
                X_list.append((x,y))

    # X 선택한 수가 O 선택한 수보다 많을때, 혹은 X 선택한 수 +1 보다 O 선택한 수가 많을 때 0 반환
    if len(X_list)>len(O_list) or len(O_list) > (len(X_list)+1): return 0 

    for x,y in O_list: # X가 O의 한턴 전이 아니면서 O가 이겼을 때
        if isWin(board,x,y) and len(X_list) != (len(O_list)-1): return 0
    
    for x,y in X_list: # O와 X의 턴수가 같지 않으면서 X가 이겼을 때
        if isWin(board,x,y) and len(X_list) != len(O_list): return 0


    return 1

print(solution(	["O.X", ".O.", "..X"]),1)
print(solution(["OOO", "...", "XXX"]),0)
print(solution(["...", ".X.", "..."]),0)
print(solution(["...", "...", "..."]),1)