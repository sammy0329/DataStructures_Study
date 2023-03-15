def solution(scores):
    target = scores[0]
    target_score = sum(target)

    scores.sort(key=lambda x:(x[0], (-1)*x[1]))

    answer = 1
    threshold = 0

    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1

        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1

            threshold = score[1]

    return answer


scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
print(solution(scores))
