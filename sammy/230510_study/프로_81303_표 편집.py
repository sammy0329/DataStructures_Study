import heapq

def solution(n, k, cmd): # 현재 위치는 right heap의 첫 번째 원소
    left, right, stack = [], [], []
    # 현재 위치의 바로 위가 left 마지막 원소이므로 최대힙, 현재 위치의 바로 아래가 right의 첫번째 원소이므로 최소힙 사용.
    for i in range(n):
        heapq.heappush(right, i)
    for i in range(k): # 현재 위치 k이므로 k만큼 pop 진행 후 push
        heapq.heappush(left, -heapq.heappop(right))

    for command in cmd:
        if len(command) > 1:
            cnt, check= command.split()
            if check == "D":
                for _ in range(cnt): # right heap에서 left heap으로 값 이동. 부호가 반대여야 하므로 - 붙여준다.
                    if right:
                        heapq.heappush(left, -heapq.heappop(right))

            elif check == "U":
                for _ in range(cnt):
                    heapq.heappush(right, -heapq.heappop(left)) # left heap에서 right heap으로 값을 이동. 마찬가지로 부호 반대여야 하므로 - 붙여준다.

        elif command == "C":
            # 값을 삭제할 때는 복구 할 수도 있으므로 stack을 사용한다.
            stack.append(heapq.heappop(right))

            # 삭제된 행이 가장 마지막 행일 때 바로 위에 있는 행을 선택한다.
            if not right:
                heapq.heappush(right, -heapq.heappop(left))

        elif command == "Z":
            # 삭제한 값 복구하기
            recover = stack.pop()

            # 현재 위치보다 값이 작을 경우 left heap에 넣는다
            if recover < right[0]:
                heapq.heappush(left, -recover)
            else:
                heapq.heappush(right, recover)

    result = []

    while left:
        result.append(-heapq.heappop(left))

    while right:
        result.append(heapq.heappop(right))


    answer = ["O" if i in result else "X" for i in range(n)]

    return "".join(answer)

print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]),"OOOOXOOO")
print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]),"OOXOXOOO")