from collections import Counter

def solution(weights):
    answer = 0
    countList=Counter(weights)

    for key,value in countList.items():
        if  value>=2: # 해당 무게를 가진 사람이 두명 이상이면 짝꿍 만들기 가능.
            answer += value*(value-1)//2
        weights=set(weights) # 중복 없애면 빨라짐.
        if key*2/3 in weights: # 2:3 비율을 가진 값 찾기
            answer += countList[key*2/3] * countList[key]

        if key*2/4 in weights: # 2:4 비율을 가진 값 찾기
            answer += countList[key*2/4] * countList[key]
        
        if key*3/4 in weights: # 3:4 비율을 가진 값 찾기
            answer += countList[key*3/4] * countList[key]

    return answer

print(solution([100,180,360,100,270]),4)