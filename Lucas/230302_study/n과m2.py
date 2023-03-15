N,M = map(int,input().split())
num_list = [i + 1 for i in range(N)]
arr= []
check_list = [False] * N
def aaa(cnt):
    if(cnt == M):
        print(*arr)
        return
    for i in range(N):
        if(check_list[i]):
            continue
        
        arr.append(num_list[i])
        check_list[i]=True
        aaa(cnt + 1)
        arr.pop()
        
        check_list[i]=False
    


    
aaa(0)