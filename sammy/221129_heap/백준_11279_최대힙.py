from heapq import heappop,heappush
import sys

heap=[]
for i in range(int(sys.stdin.readline())):
    data=int(sys.stdin.readline())
    if data:
        heappush(heap,(-data,data))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)