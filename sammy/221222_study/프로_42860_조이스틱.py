def solution(name):
	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수
    min_move = len(name) - 1
    
    for idx, char in enumerate(name):
        
    	# char 알파벳 변경 최솟값 answer에 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 다음 변경해야하는 알파벳 찾기
        next_char_idx = idx + 1
        
        while next_char_idx < len(name) and name[next_char_idx] == 'A':
            next_char_idx += 1
            
        # 기존 방식, 왼쪽시작 방식, 오른쪽 시작 방식 비교 후 변경
        min_move = min([min_move, 2 *idx + len(name) - next_char_idx, idx + 2 * (len(name) -next_char_idx)])
        
    # answer에 최소 좌우이동 횟수 추가
    answer += min_move
    
    return answer


# print(solution("JEROEN"))
# print(solution("JAN"))
# print(solution("BBBAAAAACC"))

