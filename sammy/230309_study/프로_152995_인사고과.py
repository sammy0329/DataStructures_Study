def solution(scores):
    answer = 1
    wanho_score=scores[0] # 완호의 x,y 점수
    wanho_score_sum=sum(wanho_score) # 완호 점수 합

    # (x,y)로 가정할 때, x는 내림차순 y는 오름차순으로 정리
    scores.sort(key=lambda x: (-x[0],x[1]))
    
    check=0
    
    for val in scores:
        # 완호 점수 x,y가 val의 x,y 값 보다 모두 작으면 -1 반환
        if wanho_score[0]<val[0] and wanho_score[1]<val[1]: return -1 

        if check<=val[1]: # val[1] 값 중 최댓값 찾아감.
            if sum(val)>wanho_score_sum:
                answer+=1
            check=val[1]

    return answer

print(solution([[2,2],[1,4],[3,1],[3,2],[3,2],[2,1]]), 4)
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]]), 3)