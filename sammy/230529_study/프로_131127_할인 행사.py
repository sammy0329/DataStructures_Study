from collections import Counter

def solution(want, number, discount):
    answer = 0
    wantBasket={}
    for idx,data in enumerate(want): # 원하는 제품의 수량을 딕셔너리에 저장
        wantBasket[data]=number[idx]
    
    # 인덱싱한 discount에 Counter를 활용해 제품당 개수가 몇 개인지 파악 후 wantBasket과 같은지 판단
    for i in range(len(discount)-9):
        discoutCheck=Counter(discount[i:i+10])
        if discoutCheck==wantBasket:
            answer+=1
            
    return answer

print(solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]),3)
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]),0)