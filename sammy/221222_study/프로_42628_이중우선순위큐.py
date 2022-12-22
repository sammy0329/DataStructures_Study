from heapq import heapify, heappop,heappush
# nlargest, nsmallest 생각해보기

# map 함수 이용
def multiple_minus(n):
    return n * (-1)

def solution(operations):
    answer = []
    result=[]

    for check in operations:       
        command,data=check.split() # 명령어랑 데이터 값 분리
        
        if command == 'I': # 명령어가 I이면, heapq에 값을 넣음
            heappush(answer,int(data))
            

        elif command == 'D' and answer: # 명령어가 D이고, answer에 값이 있다면 -1,1에 따라 최댓값, 최솟값 pop
            if data == '-1': # 최솟값 pop
                heappop(answer)
                

            elif data == '1': # 최댓값 pop 하기 위해 heapq에 각각 -1을 곱해주고 heapify 작업
                answer=list(map(multiple_minus,answer))
                heapify(answer)

                heappop(answer) # 최댓값 pop
                answer=list(map(multiple_minus,answer)) # 명령어 처리 이후 heapq 원상복귀 시키고 heapify 작업
                heapify(answer)
        # print(command + ': ',end='')
        # print(answer)
    if answer: # answer에 값이 있다면, result에 [max,min] 저장 
        result.append(max(answer))
        result.append(min(answer))

    else: # answer에 값이 없다면, result에 [0,0] 저장
        result.append(0)
        result.append(0)
        
    return result

# print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))