#%%
from collections import deque
import math

def solution(n, k):
    
    answer = 0
    result = deque([])
    
    def jinsoo(n,k):
        
        while n//k != 0:
            
            result.appendleft(n%k)
            n = n//k
        result.appendleft(n%k)
        return result
    
    def is_prime_number(x):
        if(x <= 1):
            return False
        for i in range(2, int(x**(0.5))+1):

            if x % i == 0:
                return False 
        return True 

    result = jinsoo(n,k)
    print(result)
    p = -1
    
    for i in result:

        if(i == 0):
            
            if(p == -1):
                p = -1
                continue
            print(p)
            if(is_prime_number(int(p))):
                if(answer == 0):
                    answer = 1
                else:
                    answer += 1
            p = -1
            
        else:
            if(p == -1):
                p = str(i)
            else:
                p += str(i)
                
    if(p == -1):
        return answer
    else:
        if(is_prime_number(int(p))):
            if(answer == 0):
                answer = 1
            else:
                answer += 1
    
    return answer
#%%
solution(112,10)
# %%
