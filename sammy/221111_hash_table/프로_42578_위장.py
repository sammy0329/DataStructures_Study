def solution(clothes):
    answer = 1
    all = {} # 각 원소의 등장 횟수를 카운팅할 딕셔너리

    for i in clothes:

        if i[1] in all:
            all[i[1]]+=1

        else:
            all[i[1]] = 2


    data=list(all.keys())

   
    for check in data:
        answer*=all[check]
        

    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))