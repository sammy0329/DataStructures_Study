def solution(n):
    triangle = [ [0] * n for _ in range(n) ] # n x n 리스트 만들기
    answer = []
    row, col = -1, 0 # 초반 (0,0) 부터 리스트에 대입되어야 하므로 x,y 값 각각 -1,0로 초기화 
    num = 1 # num은 1부터 순차적으로 증가

    for i in range(n):
        for j in range(i, n):
			
            # 아래로 이동
            if i % 3 == 0:
                row += 1 # 아래쪽으로 이동하므로 row+=1
			
            # 오른쪽으로 이동
            elif i % 3 == 1:
                col += 1 # 오른쪽으로 이동하므로 col+=1
			
            # 대각선 위로 이동
            else:
                # 대각선 위로 이동하기 때문에 row-=1, col-=1
                row -= 1
                col -= 1

            triangle[row][col] = num
            num += 1

    # answer에 값들 append
    for i in range(n):
        for j in range(i+1):
            answer.append(triangle[i][j])

    return answer

print(solution(4),[1, 2, 9, 3, 10, 8, 4, 5, 6, 7])
print(solution(5),[1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9])
print(solution(6),[1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])