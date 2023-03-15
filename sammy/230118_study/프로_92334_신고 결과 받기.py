def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    data=dict() # 자신이 신고한 사람들 저장
    reported_count=dict() # 자신이 몇번 신고되었는지 저장

    for id in id_list: # data, reported_count 딕셔너리 id 마다 [],0으로 초기화
        data[id]=[]
        reported_count[id]=0

    for check in report:
      checkdata=check.split()

      if checkdata[1] not in data[checkdata[0]]:
        data[checkdata[0]].append(checkdata[1])
        reported_count[checkdata[1]]+=1
    
    for report in id_list: # 자신이 k번 이상 신고됐을 경우 자신을 신고한 사람들의 answer 값을 1씩 증가 
        if reported_count[report] >= k:
            for idx,check_report in enumerate(id_list):
              if report in data[check_report]:
                  answer[idx]+=1

    return answer

# print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))