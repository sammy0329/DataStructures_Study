def solution(str1, str2):
    answer=0
    
    # 대문자와 소문자 무시하는 조건
    str1=str1.lower()
    str2=str2.lower()
    
    # str1, str2 다중 집합 만들 리스트
    str1List=[]
    str2List=[]
    
    for i in range(len(str1)-1):
        # 알파벳으로 된 글자 쌍만 유효하고 나머지는 버리는 조건
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1List.append(str1[i]+str1[i+1])
    
    for j in range(len(str2)-1):
        # 알파벳으로 된 글자 쌍만 유효하고 나머지는 버리는 조건
        if str2[j].isalpha() and str2[j+1].isalpha():
            str2List.append(str2[j]+str2[j+1])
    
    # str1과 str2 각각의 다중집합 사이의 교집합 구하기
    strIntersection = set(str1List).intersection(set(str2List))
    # str1과 str2 각각의 다중집합 사이의 합집합 구하기
    strUnion=set(str1List).union(set(str2List))
    
    # str1과 str2 각각의 다중집합 사이의 합집합이 공집합일 경우 1로 정의하므로 1*65536 값 리턴
    if len(strUnion) == 0:
        return 65536
    
    # 두 집합의 교집합 크기와 합집합 크기 구하기
    strInter_size=0
    strUnion_size=0
    
    for i in strIntersection:
        # 다중집합 속 중복되는 원소가 있으면 min으로 처리
        strInter_size+=min(str1List.count(i),str2List.count(i))
        
    for j in strUnion:
        # 다중집합 속 중복되는 원소가 있으면 max로 처리
        strUnion_size+=max(str1List.count(j),str2List.count(j))
        
    # (교집합 크기 / 합집합 크기) * 65536 값의 내림 값 반환        
    answer=int((strInter_size/strUnion_size)*65536)
    
    return answer

# print(solution('FRANCE','french'),16384)
# print(solution('handshake','shake hands'),65536)
# print(solution('aa1+aa2','AAAA12'),43690)
# print(solution('E=M*C^2','e=m*c^2'),65536)