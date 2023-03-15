from collections import defaultdict

def solution(n, results):
    answer = 0
    win=defaultdict(set)
    lose=defaultdict(set)
    

    for check in results:
        win[check[0]].add(check[1])
        lose[check[1]].add(check[0])
        
    for i in range(1,n+1):         
        for winner in win[i]:          
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])
    
    for i in range(1,n+1):
        if len(win[i])+len(lose[i])==n-1:
            answer+=1
        
    return answer
    
print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))