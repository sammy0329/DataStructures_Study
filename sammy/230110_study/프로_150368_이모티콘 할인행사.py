# 할인율은 10, 20, 30 , 40 중 하나 따라서 상품개수가 3개라면 4*4*4 총 64가지
from itertools import product 

def solution(users, emoticons):
    answer=[]
    all_cases=[] # 모든 경우의 수 넣을 리스트
    
    # 이모티콘 개수만큼 중복순열을 통해 모든 경우의 수 구해서 all_cases에 append
    for i in product([10,20,30,40], repeat=len(emoticons)):
        all_cases.append(i)
        
    
    for case in all_cases:      
        emoticonPlus=0 # 이모티콘 플러스 서비스 가입 수
        emoticonRevenue=0 # 이모티콘 구매 수익
        
        for user in users: 
            costs=0 # 한 유저가 특정 할인율 이상 할인하는 이모티콘 구매 비용 값
            
            for idx,sale in enumerate(case):
                if sale>=user[0]: 
                    costs+=int((100-sale)*0.01*emoticons[idx])

            # 한 명 유저의 이모티콘 총 구매 비용이 유저가 정한 가격 이상이면 플러스 서비스 가입
            if costs >= user[1]: 
                emoticonPlus+=1
                
            # 한 명 유저의 이모티콘 총 구매 비용이 유저가 정한 가격 이하이면 플러스 서비스 가입하지 않고, 이모티콘 구매 수익에 더해주기
            else:
                emoticonRevenue+=costs
    
        answer.append([emoticonPlus,emoticonRevenue]) # 각 케이스 별 emoticonPlus,emoticonPlus 리스트에 저장
    
    answer.sort() # 최대값을 뽑기 위해 sort 후 마지막 값 반환
                           
    return answer[-1]

# print(solution([[40, 10000], [25, 10000]],[7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))