import sys
from collections import deque

T=int(sys.stdin.readline().rstrip()) # testcase 갯수

for tc in range(1,T+1): 
    cmd=sys.stdin.readline().rstrip() # 명령어 입력
    n=int(sys.stdin.readline().rstrip()) # 배열에 들어있는 수
    
    arr=deque() 
    error_check=False # error가 있는지 판단하는 변수 
    cnt=0 # reverse 횟수
    
    for check in sys.stdin.readline().rstrip()[1:-1].split(","): 
        if check=='': continue # 원소가 하나 이상 있을때 양 끝 [] 빼고 원소들만 배열에 넣기
        arr.append(check)
         
    for comand in cmd:          
        try:
            if comand=='R': # 명령어가 'R'이라면 cnt+1
                cnt+=1
                
            elif comand=='D': # reverse 횟수에 따라 홀수면 오른쪽, 짝수면 왼쪽에서 pop
                if cnt%2==1: arr.pop()
                else: arr.popleft()
             
        except IndexError:
            error_check=True # error 발견시 error_check True 저장 후 반복문 탈출
            break

    if error_check: # error 처리
        print('error')
        
    else: # error 아닐시 처리
        if cnt%2==0:
            print('[' + ','.join(arr) + ']')
        else:
            arr.reverse()
            print('[' + ','.join(arr) + ']')



# 1
# R
# 0
# []
# answer : [] 

# 1
# D
# 0
# []

# answer : error