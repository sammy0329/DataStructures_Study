from collections import deque

def BFS(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        
        if n not in visited:
            visited.append(n)
            queue += set(graph[n]) - set(visited)

    return visited


def solution(n, wires):
    answer = 9999

    for j in wires:
        graph=dict()
        cnt=0
        root=1 # bfs 돌릴 기준이 되는 root 노드 default 1
        
        for i in wires: # graph 딕셔너리로 생성
            if i==j: continue # 간선 하나씩 제거해보며 완전 탐색
            
            if i[0] not in graph:
                graph[i[0]]=[i[1]]
                
            else:
                graph[i[0]].append(i[1])
            
            if i[1] not in graph:
                graph[i[1]]=[i[0]]
                
            else:
                graph[i[1]].append(i[0])

        
        for k in range(1,n+1):
            if k!=j[0] and k!=j[1]: # root가 될 수 있는 후보군 아무거나 설정
                root=k
                break
            
        cnt=abs(n-2*len(BFS(graph,root))) # 간선 제거했을때 송전탑 개수의 차 구하기
        
        if cnt<answer: # 송전탑 개수 차가 최소가 될때 answer 변수에 저장
            answer=cnt    
            
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))