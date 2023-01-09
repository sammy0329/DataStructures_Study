import sys
from itertools import permutations 

input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().rstrip().split()))
operatorsCount=list(map(int,input().rstrip().split()))

operater=[]
operators=['+','-','*','//']
dataset=[]


for idx,oper in enumerate(operatorsCount): # 쓸 수 있는 연산식 operater에 넣기
    for i in range(oper):
        operater.append(operators[idx])
        
# 순열을 구하고 set을 통해 중복을 없애고 다시 list로 변환.
allCases=set(permutations(operater,n-1))
allCases=list(allCases)


for check in allCases: # 모든 경우의 수 하나씩 판단
    total=nums[0]
    
    for idx in range(1,len(nums)): # 해당 연산 진행
        
        if check[idx-1]=='+':
            total+=nums[idx]
            
        elif check[idx-1]=='-':
            total-=nums[idx]
            
        elif check[idx-1]=='*':
            total*=nums[idx]
            
        elif check[idx-1]=='//': # total이 음수인 경우 양수로 변환 후 계산하고 음수로 다시 변환 ***
            if total<=0:
                total*=-1 
                total//=nums[idx]
                total*=-1
                
            else: total//=nums[idx]
            
    dataset.append(total)

# 최대 최솟값 찾기
print(max(dataset))
print(min(dataset))