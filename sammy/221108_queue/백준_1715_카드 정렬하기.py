# import sys
# n=int(sys.stdin.readline().rstrip())
# resultlist=[]

# data=[]
# for i in range(n):
#     data.append(int(sys.stdin.readline().rstrip()))
# data.sort(reverse=True)

# result=data.pop()
# resultlist.append(result)

# for i in range(len(data)-1):
#     if data:
#         popdata=data.pop()
#         resultlist.append(popdata)
#         result+=popdata
#         resultlist.append(result)
# if n==1:
#     print(0)
# if n>=2:
#     resultlist.append(data.pop())
#     print(sum(resultlist))

from heapq import heappush,heappop
import sys
def solution():
    n=int(sys.stdin.readline().rstrip())
    heap=[]
    result=0
    
    for i in range(n):
        heappush(heap, int(sys.stdin.readline().rstrip()))
        
    if n==1: # 1일경우 0
        return 0
    
# 30 30 40 50

    while len(heap)>1: # 1일경우 0
        min1=heappop(heap)
        min2=heappop(heap)
        result+=min1+min2
        heappush(heap,min1+min2)
    
    return result    


print(solution())