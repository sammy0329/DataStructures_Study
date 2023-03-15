def solution(nums):
    answer = 0
    dataset={}

    for i in nums:
        if i not in dataset:
            dataset[i]=1
        else:
            dataset[i]+=1
    
    key=dataset.keys()

    if len(key)>=len(nums)//2:
        answer=len(nums)//2
    else:
        answer=len(key)
    return answer