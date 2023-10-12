"""
디스크 컨트롤러

평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return

jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.

하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

jobs	return
[[0, 3], [1, 9], [2, 6]]	9
"""
# import heapq
# from collections import defaultdict
#
#
# def solution(jobs):
#     job_cnt = 0
#     time_now = 0
#     total_consume = 0
#
#     info = defaultdict(list)
#
#     for req_time, consume_time in jobs:
#         info[req_time].append(consume_time)
#
#     heap = []
#     blockTill = -1
#
#     while job_cnt < len(jobs):
#         for each in info[time_now]:
#             heapq.heappush(heap, (each, time_now))
#
#         if blockTill <= time_now and heap:
#             consume_time, added_time = heapq.heappop(heap)
#             job_cnt += 1
#             total_consume += time_now + consume_time - added_time
#             blockTill = time_now + consume_time
#
#             # print(time_now, (added_time, consume_time), 'execute', total_consume)
#
#         time_now += 1
#
#     return total_consume // len(jobs)


import heapq


def solution(jobs):
    num_jobs = len(jobs)
    time_now = 0
    total_consume = 0

    heapq.heapify(jobs)
    accessable_jobs = []

    while jobs or accessable_jobs:
        if len(accessable_jobs) == 0:
            time_added, time_consume = heapq.heappop(jobs)
            time_now = time_added

        else:
            time_consume, time_added = heapq.heappop(accessable_jobs)

        time_now += time_consume
        total_consume += time_now - time_added

        while jobs:
            if jobs[0][0] <= time_now:
                time_added, time_consume = heapq.heappop(jobs)
                heapq.heappush(accessable_jobs, (time_consume, time_added))

            else:
                break

    return total_consume // num_jobs


print(solution([[0, 3], [1, 9], [2, 6]]))
