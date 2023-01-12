import sys

def backTracking(n,x,y):
    
    global count,queen_count
    
    if queen_count == n:
        count+=1
        return
    if x<0 or x>n or y<0 or y>n: return
    
    if visited[x][y]==True: return
    
    if visited[x][y]==False:
        visited[x][y]=True
        queen_count+=1
            
    for i in range(1,n):
        x+=i
        for j in range(1,n):  
            y+=i
            backTracking(n,x,y)
            
            y-=i
        x-=i
            
        
        
    # if total>n: return # total 값이 n보다 클 경우 종료 조건
    
    # if total==n: # total 값이 n일 경우 count+1을 해주고 종료
    #     count+=1
    #     return
    
    # for i in range(1,4): # 1부터 3까지의 수들로 합을 만들기
    #     total+=i
    #     backTracking(n,total)
    #     total-=i
    
input = sys.stdin.readline
n=int(input())
visited=[[False]*n for _ in range(n)]
count=0
queen_count=0
backTracking(n,0,0)
print(count)

