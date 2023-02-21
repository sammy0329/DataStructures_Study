def solution(N, stages):
    stage_access = [0 for _ in range(N)]
    stage_not_clear = [0 for _ in range(N)]
    result = []

    for stage_now in stages:
        if stage_now <= N:
            stage_not_clear[stage_now-1] += 1

        for idx in range(0, min(stage_now, N)):
            stage_access[idx] += 1

    for idx in range(N):
        if stage_access[idx] == 0: result.append([0, (idx+1)*(-1)])
        else: result.append([stage_not_clear[idx] / stage_access[idx], (idx + 1) * (-1)])


    result.sort(reverse=True)
    result = [(-1)*stage for _, stage in result]

    return result
