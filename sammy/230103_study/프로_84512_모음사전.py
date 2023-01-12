# 순열 조합 노트정리
from itertools import product

def solution(word):
    answer = 0
    items=["A","E","I","O","U"]
    all_data=[]

    for i in range(1,6): # 모든 중복 순열 경우의수 따지기
        all_data.extend(list(product(items,repeat=i)))

    all_data.sort() # 오름차순 정렬

    # 해당 word와 같은 인덱스 찾아 +1
    answer=all_data.index(tuple(word))+1 

    return answer

# print(solution("AAAAE"))