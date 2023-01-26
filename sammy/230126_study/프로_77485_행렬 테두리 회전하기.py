def solution(rows, columns, queries):
    answer = []
    
    # 행렬 만들기
    graph =  [[0 for _ in range(columns)] for _ in range(rows)]
    n = 1
    for row in range(rows):
        for column in range(columns):
            graph[row][column] = n
            n += 1
            
    # 왼쪽 세로 -> 아래쪽 가로 -> 오른쪽 세로 -> 위쪽 가로 순으로 처리    
    for x1, y1, x2, y2 in queries:
        tmp=graph[x1-1][y1-1] # 첫값
        mindata=tmp # 가장 작은 값
        
        for i in range(x1-1,x2-1): # 왼쪽 세로
            data = graph[i+1][y1-1]
            graph[i][y1-1] = data
            mindata = min(mindata, data)

        for i in range(y1-1,y2-1): # 아래쪽 가로
            data = graph[x2-1][i+1]
            graph[x2-1][i] = data
            mindata = min(mindata, data)
            
        for i in range(x2-1,x1-1,-1): # 오른쪽 세로
            data = graph[i-1][y2-1]
            graph[i][y2-1] = data
            mindata = min(mindata, data)
        
        for i in range(y2-1,y1-1,-1): # 위쪽 가로
            data = graph[x1-1][i-1]
            graph[x1-1][i] = data
            mindata = min(mindata, data)
        
        # 모든 처리 후 tmp에 저장한 값을 첫 번째 값 옆에 저장
        graph[x1-1][y1] = tmp 
        answer.append(mindata)   
      
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))