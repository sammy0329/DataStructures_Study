# %%
from itertools import product

def solution(users, emoticons):
    sets = [40,30,20,10]
    percent = list(product(sets, repeat = len(emoticons)))
    result = []

    
    def output(users,emoticons,percent):
        price = []
        user_result = [0 for i in range(len(users))]
        result = [0,0]
        for i in range(len(emoticons)):
            now = emoticons[i] - (emoticons[i] * (percent[i]/100))
            price.append(now)
            
        for i in range(len(users)):
            for j in range(len(percent)):
            
                if users[i][0] <= percent[j] :
                    user_result[i] += price[j]
            if user_result[i] >= users[i][1] :
                result[0] += 1
            else:
                result[1] += user_result[i]
                
        return result
    
    for i in percent:
        result.append(output(users,emoticons,i))
    result.sort(reverse = True)
    
    return result[0]