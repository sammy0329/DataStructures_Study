import sys
import heapq

front = []
mid = 0
back = []

num_input = int(input())

mid = int(sys.stdin.readline().strip())
print(mid)

for idx in range(1, num_input):
    value = int(sys.stdin.readline().strip())

    if mid > value:
        heapq.heappush(front, value * (-1))
    else:
        heapq.heappush(back, value)

    if len(back) - len(front) > 1:
        heapq.heappush(front, mid * (-1))
        mid = heapq.heappop(back)

    elif len(back) - len(front) < 0:
        heapq.heappush(back, mid)
        mid = heapq.heappop(front) * (-1)

    print(mid)
