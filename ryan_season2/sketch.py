def solution(jobs):
    import heapq

    heapq.heapify(jobs)
    sub_heap = []
    num_jobs = len(jobs)
    now = 0
    response_sum = 0

    while len(jobs) != 0 or len(sub_heap) != 0:
        if len(sub_heap) == 0:
            req, eta = heapq.heappop(jobs)
            now = req
        else:
            eta, req = heapq.heappop(sub_heap)

        now += eta
        response_sum += now - req

        while True:
            if len(jobs) == 0:
                break

            if jobs[0][0] <= now:
                req, eta = heapq.heappop(jobs)
                heapq.heappush(sub_heap, (eta, req))

            else:
                break

    answer = response_sum // num_jobs

    return answer
