def solution(n, t, m, timetable):
    answer = 0
    crewTimeTable=[int(t[:2])*60 + int(t[3:]) for t in timetable] # 크루원들 TimeTable 리스트
    crewTimeTable.sort(reverse=True) # 내림차순으로 정렬

    busTimeTable = [9*60 + t*i for i in range(n)] # 버스 TimeTable 리스트

    lastData=9*60 # 마지막 pop한 값 저장할 변수

    for busTime in busTimeTable: # 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도차 시간 출력이므로 busTimeTable 만큼 반복
        cnt=0 # 탑승한 크루원들 카운팅할 변수

        # timeTable 마지막 값이 현재 버스시간보다 작거나 같거나 cnt가 m보다 작으면 반복문 진행
        while crewTimeTable and cnt<m  and crewTimeTable[-1]<=busTime: 
            lastData=crewTimeTable.pop()
            cnt+=1
        
        if cnt<m: answer=busTime # 버스에 자리가 남은경우 버스 도착시간에 도착하면 됨.
        else: answer=lastData-1 # 버스에 자리가 없을경우 맨마지막 버스에 탑승한 크루보다 1분 일찍 도착하면 됨.


    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)

print(solution(	1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]),"09:00")
print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]),"09:09")
print(solution(	2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]),"08:59")
print(solution(	1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]),"00:00")
print(solution(1, 1, 1, ["23:59"]),"09:00")
print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]),"18:00")