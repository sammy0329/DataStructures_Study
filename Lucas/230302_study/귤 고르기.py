def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in tangerine:
        if(i not in dic):
            dic[i] = 1
            continue
        dic[i] += 1
        
    dic = dict(sorted(dic.items(),key = lambda x:x[1],reverse = True))

    for i in dic:
        if(k == 0):
            break
            
        if(dic[i]>=k):

            answer += 1
            break
        else:

            k = k-dic[i]
            answer += 1
    
    return answer

# %%
