# heapify()를 활용하면 힙을 만들 수 있음.
from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heappop(heap)[1])
  
  
# n번째 최소값/ 최대값 구하기

def solution(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(heap)

    return nth_min

print(solution([4, 1, 7, 3, 8, 5], 3))

# 힙 정렬
def heap_sort(nums):
    heap = []
    for num in nums:
        heappush(heap, num)

    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
    return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))