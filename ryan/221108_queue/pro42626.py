def solution(scoville, K):
    import heapq

    answer = 0

    heap = scoville
    heapq.heapify(heap)

    for _ in range(len(scoville) - 1):
        item_1 = heapq.heappop(heap)
        item_2 = heapq.heappop(heap)

        if item_1 >= K:
            break

        else:
            item_new = item_1 + (item_2 * 2)
            heapq.heappush(heap, item_new)

            answer += 1
    else:
        if heapq.heappop(heap) < K:
            answer = -1

    return answer


if __name__ == '__main__':
    solution([1, 2, 3, 9, 10, 12], 7)
