def solution(N, stages):
    stage_list = []
    # stages 내림차순으로 정렬
    stages.sort(reverse=True)
    
    for stage in range(1,N+1):
        cnt=0
        stages_length=len(stages)
        
        if stages_length!=0:
            # 역순으로 idx 값을 통해 stage와 비교해서 같으면 cnt 증가
            for idx in range(stages_length-1,-1,-1):
                if stage>=stages[idx]:  
                    cnt+=1
                else: break

            # 해당 cnt 만큼 pop 진행
            for _ in range(cnt):
                stages.pop()
                
            stage_list.append((stage,cnt/stages_length))

        else:
            stage_list.append((stage,0))

    stage_list.sort(key=lambda x : (-x[1],x[0]))
    
    answer=[x[0] for x in stage_list] 
                
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))

print(solution(5, [2, 1, 3, 5, 6, 6, 6]), [5, 3, 2, 1, 4])
print(solution(5, [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4]),[4, 3, 2, 1, 5])