"""
H

[3, 0, 6, 1, 5]	3
"""
# CHECK


def solution(citations):
    citations.sort()

    i = 0
    j = 1000

    while i < j:
        num_cites = (i + j) // 2

        num_papers = sum([True if each >= num_cites else False for each in citations])


        if num_cites > num_papers:
            j = num_cites

        elif num_cites < num_papers:
            i = num_cites

        else:
            return num_cites


def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for idx in range(1, len(citations)):
        if citations[idx - 1] >= idx >= citations[idx]:
            answer = idx

    else:
        if citations[-1] >= len(citations):
            answer = len(citations)

    return answer


print(solution([3, 0, 6, 1, 5]))
