# 정확도만 해결, 효율성 시간초과
# def solution(board, skill):
#     answer = []
#     total = len(board)*len(board[0])
#     for type,r1,c1,r2,c2,degree in skill:
        
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 if type == 1:
#                     board[i][j]-=degree
#                     if board[i][j]<=0 and (i,j) not in answer: answer.append((i,j))
#                 else:
#                     board[i][j]+=degree
#                     if board[i][j]>0 and (i,j) in answer:
#                         answer.remove((i,j))
                    

#     return total-len(answer)


def solution(board, skill):
    answer = 0
    row = len(board) #행
    col = len(board[0]) #열
    sum_board = [[0]*(col+1) for _ in range(row+1)] #누적합 저장하는 배열
    
            
    for ty_pe, r1, c1, r2, c2, degree in skill:
        if ty_pe == 1:
            sum_board[r1][c1] -= degree
            sum_board[r1][c2+1] += degree
            sum_board[r2+1][c1] += degree
            sum_board[r2+1][c2+1] -= degree
        else:
            sum_board[r1][c1] += degree
            sum_board[r1][c2+1] -= degree
            sum_board[r2+1][c1] -= degree
            sum_board[r2+1][c2+1] += degree
                    
    for i in range(row):# 수평방향 누적합 구하기
        for j in range(1, col):
            sum_board[i][j] += sum_board[i][j-1]
            
    for i in range(1, col): # 수직방향 누적합 구하기
        for j in range(row):     
            sum_board[i][j] += sum_board[i-1][j]
    
    for i in range(row): 
        for j in range(col): # 무너지지 않은 건물 판별
            board[i][j] += sum_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]),10)
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]),6)

# type : 1.공격 2.회복
# r1,c1 ~ r2,c2까지 모양 범위 안에 내용을 degree만큼 처리