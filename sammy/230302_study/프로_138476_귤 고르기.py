from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt=0 # 종류에 따라 귤의 개수 파악해서 더해나가기
    data=Counter(tangerine).most_common()
   
    while cnt<k:
        cnt+=data.pop(0)[1] # 가장 빈도수가 많은 값부터 pop하고 cnt에 더해나가기
        answer+=1 # 종류의 개수 +1

    return answer


# print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]), 3)
# print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]), 2)
# print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]), 1)
