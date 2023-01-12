"""
n	info	                result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
"""
def solution(n, info):
    from itertools import combinations_with_replacement

    max_score_sub = -1
    min_score = 0

    result_list = []

    for sample in combinations_with_replacement([i for i in range(11)], n):
        info_ryan = [0 for _ in range(11)]

        min_sample = max(sample)

        score_apeach = 0
        score_ryan = 0

        for idx in sample:
            info_ryan[idx] += 1

        for idx in range(11):
            if info[idx] == 0 and info_ryan[idx] == 0:
                continue

            if info[idx] >= info_ryan[idx]:
                score_apeach += (10-idx)

            else:
                score_ryan += (10-idx)

        if score_ryan > score_apeach:
            if max_score_sub < (score_ryan - score_apeach):
                max_score_sub = score_ryan - score_apeach
                min_score = min_sample
                result_list = [info_ryan]

            elif max_score_sub == (score_ryan - score_apeach) and min_score <= min_sample:
                max_score_sub = score_ryan - score_apeach
                if min_score == min_sample:
                    result_list.append(info_ryan)
                else:
                    result_list = [info_ryan]
                    min_score = min_sample

    if max_score_sub > 0:
        return result_list[-1]

    else:
        return [-1]


print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
