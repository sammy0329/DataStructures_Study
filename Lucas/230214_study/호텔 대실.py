# %%
def solution(book_time):
    answer = 0
    visited = [0 for i in range(len(book_time))]
    queue = []
    
    for i in book_time:
        
        a = list(map(int,i[0].split(":")))
        b = list(map(int,i[1].split(":")))
        a = a[0] * 60 + a[1]
        b = b[0] * 60 + b[1]
        queue.append([a,b])       
    queue = sorted(queue,key=lambda x : x[0])
    last = 0
    check = []
    while True:
        if(0 not in visited):
            break
        for i in range(len(queue)):
            if(visited[i] == 1):
                continue
                
            if check == []:
                check.append(queue[i])
                visited[i] = 1
                last = queue[i][1]+10
                continue
            
            if(queue[i][0]>=last):
                check.append(queue[i])
                visited[i] = 1
                last = queue[i][1] + 10

        check = []
        answer += 1
    return answer

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
# %%
