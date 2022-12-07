def solution():
    import sys
    import heapq

    num_input = int(input())
    heap = []

    for _ in range(num_input):
        command = int(sys.stdin.readline().strip())
        if command == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap)*(-1))

        else:
            heapq.heappush(heap, command*(-1))


if __name__ == '__main__':
    solution()
