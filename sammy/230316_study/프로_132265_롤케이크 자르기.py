from collections import defaultdict,Counter

def solution(topping):
    result = 0
    young=defaultdict(int) # 동생 딕셔너리 - 형의 토핑을 하나씩 뺏어오기
    older=Counter(topping) # 형 딕셔너리 - 형이 모든 토핑을 가져갔다는 가정하에 Counter함수 진행
    
    for i in range(len(topping)):
        # 형의 토핑을 하나씩 가져옴
        young[topping[i]]+=1 
        older[topping[i]]-=1
        
        # 형의 토핑 중 특정 토핑의 값이 0이 되었을 경우 딕셔너리에서 삭제
        if older[topping[i]]==0: del older[topping[i]]

        # 형의 딕셔너리 길이와 동생의 딕셔너리 길이가 같으면 result+=1
        if len(older) == len(young): result+=1
    return result

print(solution([1, 2, 1, 3, 1, 4, 1, 2]),2)
print(solution([1, 2, 3, 1, 4]),0)