def solution(info, edges):
    answer = []
    visited=[0]*len(info) # 방문한 노드 관리
    visited[0]=1 # 초기 시작 노드 방문처리

    def dfs(sheep_cnt,wolf_cnt):
        # 종료조건 및 sheep_cnt가 더 클 경우 정답 후보군으로 answer 리스트에 append
        if sheep_cnt>wolf_cnt:
            answer.append(sheep_cnt)
        else:
            return
        
        # parent, child로 분리하여 parent는 방문했고, child는 방문하지 않았을 경우 child 방문처리 해주고, 늑대인지 판단 후 dfs 또 돌리기
        for i in range(len(edges)):
            parent=edges[i][0]
            child=edges[i][1]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child]:
                    dfs(sheep_cnt,wolf_cnt+1)
                else:
                    dfs(sheep_cnt+1,wolf_cnt)
                visited[child] = 0

    dfs(1,0)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]),5)
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]),5)