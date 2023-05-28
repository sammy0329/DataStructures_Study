# 플로이드 워셜 알고리즘

def solution(n, s, a, b, fares):
    
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)] # 정점 개수 +1 X 정점 개수 +1 만큼의 graph를 INF로 초기화

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    for check in fares: # 간선 양방향으로 대입
        graph[check[0]][check[1]]=graph[check[1]][check[0]]=check[2]
    
    
    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    for k in range(1,n+1): # 시작점에서 k까지 간 값과 k에서 a,b로 간 값들을 모두 더해 현재 answer 갱신
        answer=min(answer,graph[s][k]+graph[k][a]+graph[k][b])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]),82)
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]),14)
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]),18)