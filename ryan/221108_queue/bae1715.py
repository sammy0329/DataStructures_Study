import sys
import heapq

heap = []
num_input = int(input())

for _ in range(num_input):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

count = 0

for idx in range(num_input-1):
    item_1 = heapq.heappop(heap)
    item_2 = heapq.heappop(heap)

    new_item = item_1 + item_2

    heapq.heappush(heap, new_item)
    count += new_item

print(count)
