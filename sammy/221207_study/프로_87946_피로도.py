from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)): # 순열의 경우의 수 생성
        cnt=0
        current_k=k
        
        for j in i:
            if current_k>=j[0]: # 최소 필요 보다 피로도가 큰지 파악
                current_k-=j[1] # 소모 피로도 빼주기 
                cnt+=1 # 던전 수 업데이트
                
        if cnt>answer: # 파악된 던전 수가 제일 큰 경우 찾기
            answer=cnt
            
    return answer

solution(80,[[80,20],[50,40],[30,10]])