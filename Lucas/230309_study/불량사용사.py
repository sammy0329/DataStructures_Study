#%%
import numpy as np
from itertools import combinations,product
def solution(user_id, banned_id):# 벤 아이디에 가능한 목록을 만들고 거기서 목록별로 길이를 각각 곱해주면 된다.
    answer = []


    suspect = [[]for i in range(len(banned_id))]
    
    for i in range(len(banned_id)):
        
         for user in user_id: #벤 아이디에 해당하는 usr id 확인
                a = np.array(list(user))
                b = np.array(list(banned_id[i]))
                check = np.array([],dtype=bool)

                if(len(a) != len(b)):
                     continue
                result = (a==b)

                for j in range(len(b)):
                    
                    if(b[j] == "*"):
                        check = np.append(check,False)
                    else:
                        check = np.append(check,True)

                if((result == check).all()):
                    
                    suspect[i].append(user)
   #(frodo fradi),(abc123)

    # 중복되는 경우 제거
    print(*suspect)
    k = list(product(*suspect))
    print(k)

    for i in k:
         if len(i) == len(set(i)):
              answer.append(i)
    for i in range(len(answer)):
         answer[i] = sorted(answer[i])      
         
    return len(set(map(tuple,answer)))


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])
# %%
