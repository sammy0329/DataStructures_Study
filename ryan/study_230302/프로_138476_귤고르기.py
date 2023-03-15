def solution(k, tangerine):
    info = {}

    for each in tangerine:
        if info.get(each) is None: info[each] = 1
        else: info[each] += 1

    info_count = list(info.values())
    info_count.sort(reverse=True)

    accumul = 0
    for i, each in enumerate(info_count):
        accumul += each
        if accumul >= k:
            return i + 1


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
