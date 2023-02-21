import sys

input=sys.stdin.readline().rstrip
expression=input().split('-')

minus_dataset=[] # 마이너스 작업 할 데이터셋

for data in expression: 
    plus=0
    check=data.split('+') # '+' 수식 있는 경우 더하기 작업 진행
    
    for plus_data in check:
        plus += int(plus_data)
        
    minus_dataset.append(plus)
 
result=minus_dataset[0] # minus_dataset 리스트에서 첫번째 값 저장

# 첫번째 값을 제외하고 모든 값들 마이너스 작업 진행
for idx in range(1,len(minus_dataset)):
    result -= minus_dataset[idx]

print(result)