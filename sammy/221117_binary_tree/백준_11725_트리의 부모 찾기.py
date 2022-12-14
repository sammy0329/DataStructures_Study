import sys
from collections import deque

def solution(graph, n):
    parent = [0] * (n+1)
    q = deque([1])

    while q:
        current_node = q.pop()

        for i in graph[current_node]:
            if parent[i]==0 and i!=1:
                parent[i]=current_node
                q.append(i)
        
    for i in range(2,n+1):
        print(parent[i])


n=int(sys.stdin.readline().rstrip())
data={}
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    
    if a not in data:
        data[a]=[b]
    else:
        data[a].append(b)
        
    if b not in data:
        data[b]=[a]
    else:
        data[b].append(a)

        

solution(data,n)

        
