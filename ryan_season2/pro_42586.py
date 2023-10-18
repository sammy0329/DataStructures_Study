"""
기능개발

작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
"""


def solution(progresses, speeds):
    answer = []
    isDone = [False for _ in progresses]

    for idx, (progress, speed) in enumerate(zip(progresses, speeds)):
        if isDone[idx]:
            continue

        eta = (100 - progress)
        eta = (eta // speed) + 1 if eta % speed != 0 else eta // speed

        isDone[idx] = True
        cnt = 1

        isPossible = True
        for each in range(idx + 1, len(progresses)):
            progresses[each] += speeds[each] * eta

            if progresses[each] >= 100 and isPossible:
                isDone[each] = True
                cnt += 1

            else:
                isPossible = False

        answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
