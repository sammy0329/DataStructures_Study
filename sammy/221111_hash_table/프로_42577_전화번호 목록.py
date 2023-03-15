# 파이썬의 딕셔너리가 해시 테이블로 구현되어있음.
def solution(phone_book):
    answer = True
    dic=dict()

    for phone in phone_book:
        dic[phone]=len(phone)  
          
    for phone in phone_book:
        
        check=''
        for word in phone:
            check+=word
            # in 연산시 hash를 통해서 자료들을 저장하므로 O(1) 충돌이 많은 경우 O(n)
            # list,tuple은 하나하나 순회하기 때문에 데이터의 크기만큼 시간 복잡도를 갖음 O(n)
            if check in dic and check!=phone: # 같은 크기 전화번호는 없다.
                answer=False
    return answer

print(solution(["1195524421","119", "97674223"]))