# 할인율은 10, 20, 30 , 40 중 하나 따라서 상품개수가 3개라면 4*4*4 총 64가지
from itertools import product 

def solution(users, emoticons):
    answer=[]
    all_cases=[]
    talk=0
    money=0
    
    for i in product([10,20,30,40], repeat=len(emoticons)):
        all_cases.append(i)
    
    for user in users:    
        total=0
        
        for check in all_cases:
            for idx,sale in enumerate(check):
                if sale>=user[0]:
                    total+=(100-sale)*0.01*emoticons[idx]

        if total >= user[1]:
            talk+=1
        else:
            money+=total
    
    print(talk,money)
                               
    return answer

print(solution([[40, 10000], [25, 10000]],[7000, 9000]))