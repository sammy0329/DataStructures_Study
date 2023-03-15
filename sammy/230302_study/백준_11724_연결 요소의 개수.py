import sys
from collections import defaultdict

input = sys.stdin.readline

n,m=map(int,input().split())

visited=[False]*(n+1) # 방문여부 판단하기 위한 리스트
data=defaultdict(list) # 각각 어떤 간선끼리 연결되어 있는지 딕셔너리로 저장

cnt=0

def dfs(v): # 방문처리 해주고, 해당 간선과 연결된 값들 재귀를 통해 방문처리
    visited[v]=True
    for i in data[v]:
        if not visited[i]:
            dfs(i)
    
for _ in range(m): # 딕셔너리에 넣어주는 작업
    u,v=map(int,input().split())
    data[u].append(v)
    data[v].append(u)
    
for i in range(1,n+1): # 노드가 방문처리가 안됐으면 dfs호출
    if not visited[i]:
        dfs(i)
        cnt+=1
        
print(cnt)
