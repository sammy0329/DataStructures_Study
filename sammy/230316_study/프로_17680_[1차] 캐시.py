from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q=deque()
    
    if cacheSize==0: # 캐시 사이즈가 0이면 cities 리스트 길이 * 5 반환
        return len(cities)*5
    
    for i in cities:
        i=i.upper() # 대소문자 구분하지 않으므로 대문자로 변환시키기

        if i in q:
            q.remove(i) # 값이 q 안에 있는 경우 그 값을 remove 해준 후 다시 append하기
            q.append(i)
            answer+=1

        else: 
            if len(q)==cacheSize: # 캐시가 꽉차면 LRU를 따르기 때문에 가장 나중에 들어온 값을 pop하기 위해 popleft 진행
                q.popleft()
            
            q.append(i) # q에 값 append
            answer+=5
        
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]),50)
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]),21)
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]),60)
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]),52)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]),16)

