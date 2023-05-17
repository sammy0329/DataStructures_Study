from collections import defaultdict,Counter

def solution(weights):
    answer = 0
    countList=Counter(weights)

    for key,value in countList.items():
        if  value>=2: # 해당 무게를 가진 사람이 두명 이상이면 짝꿍 만들기 가능.
            answer += value*(value-1)//2
        
        if key*2/3 in weights:
            answer += countList[key*2/3] * countList[key]

        if key*2/4 in weights:
            answer += countList[key*2/4] * countList[key]
        
        if key*3/4 in weights:
            answer += countList[key*3/4] * countList[key]


    
        
    return answer

print(solution([100,180,360,100,270]),4)