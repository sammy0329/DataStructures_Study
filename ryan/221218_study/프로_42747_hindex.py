"""
citations	return
[3, 0, 6, 1, 5]	3
"""


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


# citations = [3, 0, 6, 1, 5]
citations = [6,6,5,3,1,0]
# citations = [4, 4, 4]
# citations = [10, 10, 10, 10, 10]

print(solution(citations))
