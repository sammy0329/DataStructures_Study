def solution(n, info):
    answer = [-1]
    
    scoreDifference= -1
    lion_info=[0 for _ in range(11)]

    def backTracking(current_n,index):
        nonlocal scoreDifference,answer, lion_info
        
        if current_n>n: return 
        
        if current_n==n:
            ap_cost=0
            li_cost=0
            
            for i in range(11):
                if info[i] < lion_info[i]:
                    li_cost += 10 - i

                elif info[i] != 0 and lion_info[i] <= info[i] :
                    ap_cost += 10 - i
            
            if li_cost>ap_cost:
                if li_cost - ap_cost > scoreDifference :
                    answer =lion_info[:]
                    scoreDifference=li_cost-ap_cost
                    #print(lion_info,scoreDifference)

                elif li_cost - ap_cost == scoreDifference :
                    for i in range(10, -1, -1) :
                        if lion_info[i] < answer[i] :
                            break

                        if lion_info[i] > answer[i] :
                            answer = lion_info[:]
                            break
            return
        
        for i in range(index, 11):
            lion_info[i]+=1
            backTracking(current_n+1, i)
            lion_info[i]-=1

    backTracking(0,0)
    
    return answer

# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0])) 
# print(solution(9,[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))

