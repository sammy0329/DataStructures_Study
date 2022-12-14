from collections import deque
from heapq import heappop,heappush

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 a에서 b로 이동
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = []  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            heappush(q,i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now =heappop(q)
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                heappush(q,i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

"""
5 3
4 1
3 1
5 3
-> 5 3 4 1 2

5 4
5 4
4 3
3 2 
2 1
5 4 3 2 1


4 2
4 2
3 1
3 1 4 2

5 4
4 1
5 1
2 5 
3 5
2 3 4 5 1

6 7
5 6
5 2
2 4
4 3
2 1
6 1
1 3
4 3 5 2 6 1

6 7
5 6
5 2
2 4
4 3
2 1
6 1
1 3

4 3 5 2 6 1
"""