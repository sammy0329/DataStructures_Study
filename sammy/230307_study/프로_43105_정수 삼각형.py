def solution(triangle):
    # 꼭대기를 제외한 높이에서 가장 왼쪽 값은 (h-1,w)인덱스를 가장 오른쪽 값은 (h-1,w-1) 인덱스 값을 더해나가고
    # 사잇값들은 (h-1,w-1)과 (h-1,w) 인덱스 값중에 최댓값을 더해나간다.
    for h in range(1,len(triangle)):
        for w in range(len(triangle[h])):
            if w==0:
                triangle[h][w] += triangle[h-1][w]
            elif  w==len(triangle[h])-1:
                triangle[h][w] += triangle[h-1][w-1]
            else:
                triangle[h][w] += max(triangle[h-1][w-1],triangle[h-1][w])
    
    # 가장 아랫층의 리스트 중 최댓값 추출
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]),30)