n=int(input())
result=[i for i in range(1,n+1)]
rule=list(map(int,input().split()))

cursor=0
print(result.pop(cursor),end=' ')
while result:
        
    plus=rule.pop(cursor)
    #왼쪽으로 갈때는 자기 포함x 오른쪽갈때는 자기포함.
    if plus<0:
        cursor=(cursor+plus)%len(rule) -9 %2 
    else:
        cursor=(cursor+plus-1)%len(rule) 

    print(result.pop(cursor),end=' ')
  


    #  1 2 3 4 5
    #  2 3 4 5
    
    # 탐색 빠를땐 리스트 앞뒤 연산할때는 dequeue