# 첫번째 풀이
# from itertools import combinations
 
# def solution(number, k):
#     answer=0
    
#     combi=list(combinations(number,len(number)-k))
    
#     for check in combi:
#         num=int(''.join(check))

#         if num > answer: answer=num
   
#     return str(answer)

def solution(number, k):
    answer=''
    max_index=len(number)-1
    for idx,data in enumerate(number):
        if max_index-idx>=k and 
        
    
    
   
    return answer



print(solution("1924",2))
print(solution("1231234",3))