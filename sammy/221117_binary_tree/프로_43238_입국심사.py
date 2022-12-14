def binary_search(start,end,arr,n):
    result=0
    while start<=end:
        mid=(start+end)//2
        total=0
        
        for divide in arr:
            # print((divide,mid))
            total+=(mid//divide)
        # print(total)

        if total<n:
            
            start=mid+1 
           
        else:
            result=mid
            
            end=mid-1
             
    
    return result
        


def solution(n, times):
    
    answer=binary_search(1,n*max(times),times,n)
    return answer

# print(solution(6,[7,10]))