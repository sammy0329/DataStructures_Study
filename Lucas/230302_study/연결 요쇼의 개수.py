#%%
from collections import deque

n,m= map(int,input().split(" "))

graph = {}
visited = [0 for i in range(n)]

for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    a,b = input().split(" ")
    
    graph[int(a)].append(int(b))
    graph[int(b)].append(int(a))


def bfs(graph,visited,start):
    queue = deque([])
    queue.append(start)
    ans = 0
    while True:

        if(0 not in visited):
            break
        
        ans +=1
        while queue:
            now = queue.popleft()
            if(visited[now-1] == 1):
                continue

            visited[now-1] = 1
            for i in graph[now]:
                queue.append(i)
        
        for i in range(len(visited)):
            if(visited[i] == 0):
                queue.append(i+1)
                break

    return ans

print(bfs(graph,visited,1))
            