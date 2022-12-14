from heapq import heappop,heappush
import math

def solution(jobs):
    answer = 0
    current=0
    length=len(jobs)
    heap=[]
    for i in range(length):
        heappush(heap,(jobs[i][1]+jobs[i][0],jobs[i][0],jobs[i][1]))

    while heap:
        data=heappop(heap)
        
        if current>=data[1]:
            current+=data[2]
            # print(current)
            print(current-data[1])
            answer+=current-data[1]
            
        else:
            answer+=data[1]
            current+=data[1]+data[2]
            # print(current)
            
            print(current-data[1])
            answer+=current-data[1]

        # print(answer)

    return math.trunc(answer/length)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[101, 2], [100, 1]]))