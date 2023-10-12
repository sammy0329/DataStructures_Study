"""
더 맵게

scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
"""
import heapq


def solution(scoville, K):
    heap = scoville
    heapq.heapify(heap)

    answer = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1

        answer += 1
        lower_1st = heapq.heappop(heap)
        lower_2nd = heapq.heappop(heap)

        new = lower_1st + 2*lower_2nd

        heapq.heappush(heap, new)

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
