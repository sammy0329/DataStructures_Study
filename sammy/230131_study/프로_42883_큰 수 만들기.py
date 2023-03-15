# 첫번째 풀이 (시간초과 실패)

# from itertools import combinations
 
# def solution(number, k):
#     answer=0
    
#     combi=list(combinations(number,len(number)-k))
    
#     for check in combi:
#         num=int(''.join(check))

#         if num > answer: answer=num
   
#     return str(answer)


def solution(number, k):
    answer=[] # stack 개념 활용
    
    for check in number: # number를 하나씩 불러옴
            
         # k가 0보다 크고 answer의 마지막 수가 check보다 크거나 같을때까지 반복해서 pop
        while k>0 and answer and answer[-1]<check:
            answer.pop()
            k-=1
            
        answer.append(check) # check를 answer 스택에 append
     
    return ''.join(answer[:len(number)-k])


# print(solution("1924",2))
# print(solution("1231234",3))


