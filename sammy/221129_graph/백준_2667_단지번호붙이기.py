from heapq import heappop,heappush
n=int(input())
cnt=0
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))
heap=[]

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:      
        return False    
    
    if graph[x][y]==1:
        graph[x][y]=0
        cnt+=1
        
        # 상하좌우
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1) 
              
        return True
    return False

result=0
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result+=1
            heappush(heap,cnt)
            cnt=0
print(result)
for i in range(result):
    print(heappop(heap))
