# %%
def solution(number, k):
    answer = ""
    number = list(map(int,number))
    now = 0
    a = k
    now_1 = 0
    while k > 0:
        if(len(answer)==(len(number)-a)):
            return answer
        max_value = 0
        
        for i in range(now,now+k+1):
            if(max_value < number[i]):
                max_value = number[i]
                now_1 = i
                if(max_value == 9):
                    break
                
        answer+=str(max_value)

        k = k- (now_1 - now) 
        
        now = now_1+1

    for i in range(now,len(number)):
        answer += str(number[i])
    
    return answer
#%%
solution("4321", 1)
# %%
