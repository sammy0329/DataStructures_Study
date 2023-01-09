#DFS
def dfs(graph, start):
    result, visit = [], []
    visit.append(start)
    
    while visit:
        node = visit.pop()
        if node not in result:
            result.append(node)
            visit.extend(graph[node])
    
    return result     
 
def solution(n, computers):
    answer = 0

    # 딕셔너리로 그래프 생성
    graph={i:[] for i in range(1,n+1)}
    
    # 딕셔너리에 자기 자신을 제외하고 연결된 값들 리스트로 저장
    for i in range(n): 
        for j in range(n):
            if computers[i][j]==1 and i!=j:
                graph[i+1].append(j+1)

    # n_arr 리스트에 1부터 n까지 값 저장
    n_arr=[i for i in range(1,n+1)]

    while n_arr:
        answer+=1
        # dfs 함수를 통해 연결된 그래프 리스트로 반환 받음
        check=dfs(graph,(n_arr[0]))

        # 차집합을 통해 dfs를 통해 확인해야하는 정점 파악
        n_arr=list(set(n_arr)-set(check))

    return answer

# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))