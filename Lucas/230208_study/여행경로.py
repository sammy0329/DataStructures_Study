#%%
from copy import deepcopy
def solution(tickets):

    answer = []
    
    def dfs(tickets,start,ans):

        if(len(tickets) == 0):
            answer.append(ans)
            return 0 
        
        for i in range(len(tickets)):
            if(tickets[i][0] == start):

                a = tickets[0:i]
                an = deepcopy(ans)
                an.append(tickets[i][1])

                if(i!=len(tickets)-1):
                    a+=tickets[i+1:len(tickets)]

                dfs(a,tickets[i][1],an)
    dfs(tickets,"ICN",["ICN"])
    print(answer)
    answer.sort()
    return answer[0]
#%%
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])

# %%
