def solution(tickets):
    answer = []
    dataset={}
    
    for i in tickets: # 딕셔너리에 해당 값 저장     
        if i[0] not in dataset:
            dataset[i[0]]=[i[1]]
        else:
            dataset[i[0]].append(i[1])
    
    for i in dataset.keys(): # 알파벳 내림차순으로 정렬
        dataset[i].sort(reverse=True)
    
    # 첫번째 요소 값 queue에 넣어주기
    q=["ICN"]
  
    while q:
        # queue를 하나씩 꺼내고 answer에 append 해주고, dataset 딕셔너리에서 해당 value 하나씩 pop
        top = q[-1]
        # 시작지를 top으로 하는 티켓이 없을 경우 즉, 제일 마지막 방문 공항
        if top not in dataset or not dataset[top]:
            answer.append(q.pop())
        # stack 개념으로 queue에 하나씩 쌓기
        else:
            q.append(dataset[top].pop())
    # answer에는 공항 방문 순서가 거꾸로 저장되어 있기 때문에 뒤집어 주기
    return answer[::-1]

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# # 추가 반례
# print(solution([["ICN","A"],['ICN',"B"],["B","ICN"]])) # [ICN, B, ICN, A]