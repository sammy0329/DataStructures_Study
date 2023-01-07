# 할인율은 10, 20, 30 , 40 중 하나 따라서 상품개수가 3개라면 4*4*4 총 64가지
from itertools import product 

def solution(users, emoticons):
    answer = []
    all_cases=[]
    
    for i in product([10,20,30,40], repeat=len(emoticons)):
        all_cases.append(i)
        
    print(all_cases)
        
    return answer

solution([[40, 10000], [25, 10000]],[7000, 9000])