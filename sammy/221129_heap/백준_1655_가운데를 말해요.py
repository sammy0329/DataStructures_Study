from heapq import heappop,heappush
import sys

leftheap=[]
rightheap=[]

for i in range(int(sys.stdin.readline())):

    data=int(sys.stdin.readline())
    
    if len(leftheap) == len(rightheap):
        heappush(leftheap, (-data,data))
    else:
        heappush(rightheap,data)

    if rightheap and leftheap[0][1]>rightheap[0]:
        left=heappop(leftheap)
        right=heappop(rightheap)
        heappush(rightheap,left[1])
        heappush(leftheap,(-right,right))
    
    print(leftheap[0][1])
