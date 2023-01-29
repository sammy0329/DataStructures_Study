from itertools import permutations

def solution(expression):
    answer = 0
   
    cal=[]  # permutation 하기 위해 사용된 연산자 저장 리스트
    dataset=[] # 해당 수식 split해서 저장하는 리스트
    test=[] # dataset 복사해서 우선순위 처리해나갈 리스트
    
    check=''
    
    # dataset에 split 해서 넣는 과정
    for i in expression:
        if i=='+' or i == '-' or i == '*':
            dataset.append(int(check))
            dataset.append(i)
            check=''  
            
            # cal 리스트에 연산자 저장
            if i not in cal:
                cal.append(i)                        
        else:
            check+=i
    
    # 마지막 남은 숫자 dataset에 넣어주기
    dataset.append(int(check))
    
    # cal에 저장된 연산자로 permutation 진행 
    cases=list(permutations(cal,len(cal)))
    
    for case in cases:
        test=dataset[:]
        
        # 연산자 우선순위 별로 진행
        for i in case: 
            idx=0
            
            # test에 수식이 있다면 슬라이싱을 통해 처리 후 idx를 0으로 바꿔주기
            while i in test:         
                if test[idx] == i and i=='*':
                    before=test[:idx-1]
                    after=test[idx+2:]
                    data=[test[idx-1]*test[idx+1]]
                    
                    test=before+data+after
                    idx=0        
                    
                elif test[idx] == i and i=='+':
                    before=test[:idx-1]
                    after=test[idx+2:]
                    data=[test[idx-1]+test[idx+1]]   
                    
                    test=before+data+after
                    idx=0
                    
                elif test[idx]== i and i=='-':
                    before=test[:idx-1]
                    after=test[idx+2:]
                    data=[test[idx-1]-test[idx+1]]
                    
                    test=before+data+after
                    idx=0
                
                # 연산자가 아닌경우 idx + 1 처리    
                idx+=1      
        
        # answer 값을 최댓값으로 최신화         
        answer=max(abs(test[0]),answer)
          
    return answer

# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))
# print(solution("2-990-5+2"))
# print(solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))