"""
이중 우선순위 큐

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.

operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

operations	return
["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	[0,0]
["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	[333, -45]
예외 발생 구간
len(heap) == 0 or == 1
"""
import heapq


def solution(operations):
    heap = []

    for operation in operations:
        ops, value = operation.split(' ')

        if ops == 'I':
            heapq.heappush(heap, int(value))

        elif ops == 'D' and heap:
            if value == '1':
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)

            elif value == '-1':
                heapq.heappop(heap)

    if not heap:
        answer = [0, 0]

    else:
        answer = [max(heap), heap[0]]

    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333", "D -1", "D -1"]))
print(solution(["D 1","D 1","D 1","D 1","D 1","D -1"]))
