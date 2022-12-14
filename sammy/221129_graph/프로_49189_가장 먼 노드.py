from collections import deque

def solution(n, edge):
    answer = 0
    route=[-1]*(n+1) # 노드 1부터 각 노드까지의 거리
    queue=deque()
    graph = [[] for _ in range(n + 1)]

    for i in edge: # 양방향으로 각 노드에 연결된 노드 정보 저장
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    queue.append(1)
    route[1]=0
        
    while queue:
        now=queue.popleft()
        for i in graph[now]:
            if route[i]==-1:
                queue.append(i)
                route[i]=route[now]+1
    
    # 1번 노드로부터 가장 멀리 떨어져 있는 노드의 개수 계산
    max_route=max(route)
    answer=route.count(max_route)
    
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))