import sys
import itertools

input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().rstrip().split()))
operatorsCount=list(map(int,input().rstrip().split()))

li=[]
operators=['+','-','*','//']
data=[]

for idx,oper in enumerate(operatorsCount):
    for i in range(oper):
        li.append(operators[idx])
li_set=set(itertools.permutations(li,n-1))
li_set=list(li_set)


for check in li_set:
    total=nums[0]
    for idx in range(1,len(nums)):
        if check[idx-1]=='+':
            total+=nums[idx]
            
        elif check[idx-1]=='-':
            total-=nums[idx]
            
        elif check[idx-1]=='*':
            total*=nums[idx]
            
        elif check[idx-1]=='//':
            if total<=0:
                total*=-1 # 음수 // 양수는 0
                total//=nums[idx]
                total*=-1
                
            else: total//=nums[idx]
            
    data.append(total)
    
print(max(data))
