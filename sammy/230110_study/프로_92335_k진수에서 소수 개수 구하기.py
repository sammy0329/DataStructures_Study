import math

def is_prime_number(x): # 시간복잡도 O(sqrt(N))
    if x<=1: return False
    # 가운데 약수를 기준으로 곱셈 연산에 대해 대칭이므로 가운데 약수(제곱근)까지만 확인하면 됨. 
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


def solution(n, k):
    answer = 0
    change_n = '' # k진수로 변환시킨 값이 저장될 변수
    data='' # 변환된 change_n을 하나씩 붙이면서 확인할 변수
    
    while n > 0:
        n, mod = divmod(n, k)
        change_n += str(mod)
    change_n=change_n[::-1]
    
    if '0' not in change_n: # change_n에 0이 없다면 바로 1 반환
         if is_prime_number(int(change_n)):
                return 1
            
    for check in change_n: # 하나씩 뺀 값이 0이면 소수인지 확인하고 data를 ''로 다시 비워주기
        if check=='0': 
            if data != '' and is_prime_number(int(data)):
                answer+=1
            data=''
                 
        else: # 0이 아니면 data에 계속 붙여나가기
            data+=check
            
    # 마지막에 0으로 안 끝났을 경우 예외처리        
    if data !='' and is_prime_number(int(data)): answer+=1 
        
    return answer

# print(solution(437674,3))
# print(solution(12021,10))